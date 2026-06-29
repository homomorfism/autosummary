"""Модуль суммаризации.

Вход — транскрипт (объект `Transcript` или текст) и текст слайдов
(`SlideDeck` или строка). Выход — структурированный конспект `SummaryConcept`,
где каждое утверждение заземлено на источник.

Под капотом — один вызов Claude (claude-opus-4-8) со structured outputs: модель
обязана вернуть JSON ровно по pydantic-схеме, парсинг и валидация — на стороне
SDK (`client.messages.parse`).
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from .prompts import SYSTEM_PROMPT, USER_TEMPLATE
from .schema import SummaryConcept

if TYPE_CHECKING:  # для подсказок типов без жёсткой зависимости
    from ..slides import SlideDeck
    from ..stt.base import Transcript

# сколько максимум секунд показывать в таймкоде сегмента
_MAX_TS = 10  # знаков хватает


def _format_transcript(transcript: "Transcript | str") -> str:
    """Привести транскрипт к тексту с таймкодами по сегментам."""
    if isinstance(transcript, str):
        return transcript
    lines: list[str] = []
    for seg in transcript.segments:
        text = (seg.text or "").strip()
        if not text:
            continue
        if seg.start is not None:
            lines.append(f"[{seg.start:.1f}s] {text}")
        else:
            lines.append(text)
    if not lines and transcript.text:
        return transcript.text
    return "\n".join(lines)


def _format_slides(slides: "SlideDeck | str") -> str:
    if isinstance(slides, str):
        return slides
    return slides.full_text


class Summarizer:
    """Мультиисточниковый суммаризатор на Claude."""

    def __init__(
        self,
        *,
        model: str | None = None,
        api_key: str | None = None,
        max_tokens: int = 16_000,
        thinking: bool = True,
    ) -> None:
        from .. import config

        self.model = model or config.LLM_MODEL
        self.api_key = api_key or config.ANTHROPIC_API_KEY
        self.max_tokens = max_tokens
        self.thinking = thinking
        self._client = None

    def _get_client(self):
        if self._client is None:
            try:
                import anthropic
            except ImportError as e:  # pragma: no cover
                raise ImportError(
                    "Не установлен anthropic SDK. Установите: pip install anthropic"
                ) from e
            # api_key=None -> SDK берёт ANTHROPIC_API_KEY из окружения
            self._client = anthropic.Anthropic(api_key=self.api_key)
        return self._client

    def summarize(
        self,
        transcript: "Transcript | str",
        slides: "SlideDeck | str",
    ) -> SummaryConcept:
        """Собрать структурированный конспект из транскрипта и слайдов."""
        transcript_text = _format_transcript(transcript)
        slides_text = _format_slides(slides) or "(слайды не предоставлены)"

        user_msg = USER_TEMPLATE.format(
            slides=slides_text,
            transcript=transcript_text or "(транскрипт пуст)",
        )

        client = self._get_client()
        kwargs = dict(
            model=self.model,
            max_tokens=self.max_tokens,
            system=SYSTEM_PROMPT,
            messages=[{"role": "user", "content": user_msg}],
            output_format=SummaryConcept,
        )
        if self.thinking:
            # адаптивное мышление — рекомендованный режим для opus-4-8
            kwargs["thinking"] = {"type": "adaptive"}

        response = client.messages.parse(**kwargs)
        if response.parsed_output is None:
            raise RuntimeError(
                f"Модель не вернула валидный конспект (stop_reason="
                f"{response.stop_reason!r})."
            )
        return response.parsed_output


def summarize(
    transcript: "Transcript | str",
    slides: "SlideDeck | str",
    **kwargs,
) -> SummaryConcept:
    """Удобная обёртка: один вызов без явного создания Summarizer."""
    return Summarizer(**kwargs).summarize(transcript, slides)
