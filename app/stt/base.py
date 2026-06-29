"""Общий интерфейс STT-провайдера.

Любой провайдер (облачный Google STT или локальный whisper.cpp) принимает
аудио/видео-файл и возвращает единый объект `Transcript`. Дальше по пайплайну
(выравнивание, суммаризация, метрики Э2) код не знает, какой именно провайдер
сгенерировал транскрипт — он работает только с этой моделью данных.
"""

from __future__ import annotations

import json
from abc import ABC, abstractmethod
from dataclasses import asdict, dataclass, field
from pathlib import Path


def _fmt_ts(seconds: float | int | None) -> str | None:
    """Секунды -> «MM:SS» или «H:MM:SS» для читаемого markdown."""
    if seconds is None:
        return None
    seconds = int(round(float(seconds)))
    h, rem = divmod(seconds, 3600)
    m, s = divmod(rem, 60)
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m:02d}:{s:02d}"


@dataclass
class Word:
    """Одно слово с таймкодами (если провайдер их отдаёт)."""

    text: str
    start: float | None = None  # секунды от начала
    end: float | None = None
    confidence: float | None = None


@dataclass
class Segment:
    """Фраза/реплика — непрерывный кусок речи между паузами."""

    text: str
    start: float | None = None
    end: float | None = None
    words: list[Word] = field(default_factory=list)


@dataclass
class Transcript:
    """Результат распознавания речи, общий для всех провайдеров.

    `provider` и `meta` нужны эксперименту Э2 (бенчмарк STT): по ним считается
    latency / стоимость / WER-TER в разрезе провайдеров.
    """

    text: str
    segments: list[Segment] = field(default_factory=list)
    language: str | None = None
    provider: str | None = None
    audio_duration: float | None = None  # секунды
    meta: dict = field(default_factory=dict)

    # --- сериализация ---------------------------------------------------

    def to_dict(self) -> dict:
        return asdict(self)

    def to_json(self, indent: int = 2) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=indent)

    def save(self, path: str | Path) -> Path:
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(self.to_json(), encoding="utf-8")
        return path

    # --- человекочитаемый markdown (та же информация, что в JSON) --------

    def to_markdown(self) -> str:
        lines: list[str] = [f"# Транскрипт — {self.provider or 'unknown'}", ""]
        meta_rows = [
            ("Провайдер", self.provider),
            ("Язык", self.language),
            ("Длительность аудио", _fmt_ts(self.audio_duration)),
            ("Сегментов", len(self.segments)),
        ]
        for key, val in self.meta.items():
            meta_rows.append((key, val))
        for key, val in meta_rows:
            if val is not None:
                lines.append(f"- **{key}:** {val}")
        lines += ["", "## Сегменты", ""]
        for seg in self.segments:
            text = (seg.text or "").strip()
            if not text:
                continue
            if seg.start is not None:
                stamp = f"[{_fmt_ts(seg.start)} – {_fmt_ts(seg.end)}]"
                lines.append(f"**{stamp}** {text}")
            else:
                lines.append(text)
            lines.append("")
        lines += ["## Полный текст", "", self.text or ""]
        return "\n".join(lines).rstrip() + "\n"

    def save_markdown(self, path: str | Path) -> Path:
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(self.to_markdown(), encoding="utf-8")
        return path

    @classmethod
    def from_dict(cls, data: dict) -> "Transcript":
        segments = [
            Segment(
                text=s["text"],
                start=s.get("start"),
                end=s.get("end"),
                words=[Word(**w) for w in s.get("words", [])],
            )
            for s in data.get("segments", [])
        ]
        return cls(
            text=data["text"],
            segments=segments,
            language=data.get("language"),
            provider=data.get("provider"),
            audio_duration=data.get("audio_duration"),
            meta=data.get("meta", {}),
        )

    @classmethod
    def load(cls, path: str | Path) -> "Transcript":
        return cls.from_dict(json.loads(Path(path).read_text(encoding="utf-8")))


class STTProvider(ABC):
    """Базовый класс адаптера распознавания речи.

    Контракт прост: на вход путь к медиа (видео/аудио), на выход `Transcript`.
    Подготовку аудио (извлечение дорожки, ресемплинг в 16 кГц моно) провайдеры
    делают через общий модуль `app.stt.audio`, чтобы не дублировать логику.
    """

    #: человекочитаемое имя провайдера, попадает в Transcript.provider и метрики
    name: str = "base"

    @abstractmethod
    def transcribe(self, media_path: str | Path) -> Transcript:
        """Распознать речь из файла и вернуть единый Transcript."""
        raise NotImplementedError

    def __repr__(self) -> str:  # pragma: no cover - удобство отладки
        return f"<STTProvider {self.name!r}>"
