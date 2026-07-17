"""Common STT provider interface.

Any provider (cloud Google STT or local whisper.cpp) takes an audio/video file
and returns a unified `Transcript` object. Further down the pipeline (alignment,
summarization, E2 metrics) the code does not know which provider generated the
transcript — it works only with this data model.
"""

from __future__ import annotations

import json
from abc import ABC, abstractmethod
from dataclasses import asdict, dataclass, field
from pathlib import Path


def _fmt_ts(seconds: float | int | None) -> str | None:
    """Seconds -> "MM:SS" or "H:MM:SS" for readable markdown."""
    if seconds is None:
        return None
    seconds = int(round(float(seconds)))
    h, rem = divmod(seconds, 3600)
    m, s = divmod(rem, 60)
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m:02d}:{s:02d}"


@dataclass
class Word:
    """A single word with timestamps (if the provider returns them)."""

    text: str
    start: float | None = None  # seconds from the start
    end: float | None = None
    confidence: float | None = None


@dataclass
class Segment:
    """A phrase/utterance — a continuous chunk of speech between pauses."""

    text: str
    start: float | None = None
    end: float | None = None
    words: list[Word] = field(default_factory=list)


@dataclass
class Transcript:
    """Speech recognition result, shared across all providers.

    `provider` and `meta` are needed by experiment E2 (STT benchmark): they are
    used to compute latency / cost / WER-TER broken down by provider.
    """

    text: str
    segments: list[Segment] = field(default_factory=list)
    language: str | None = None
    provider: str | None = None
    audio_duration: float | None = None  # seconds
    meta: dict = field(default_factory=dict)

    # --- serialization --------------------------------------------------

    def to_dict(self) -> dict:
        return asdict(self)

    def to_json(self, indent: int = 2) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=indent)

    def save(self, path: str | Path) -> Path:
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(self.to_json(), encoding="utf-8")
        return path

    # --- human-readable markdown (same information as in JSON) -----------

    def to_markdown(self) -> str:
        lines: list[str] = [f"# Transcript — {self.provider or 'unknown'}", ""]
        meta_rows = [
            ("Provider", self.provider),
            ("Language", self.language),
            ("Audio duration", _fmt_ts(self.audio_duration)),
            ("Segments", len(self.segments)),
        ]
        for key, val in self.meta.items():
            meta_rows.append((key, val))
        for key, val in meta_rows:
            if val is not None:
                lines.append(f"- **{key}:** {val}")
        lines += ["", "## Segments", ""]
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
        lines += ["## Full text", "", self.text or ""]
        return "\n".join(lines).rstrip() + "\n"

    def save_markdown(self, path: str | Path) -> Path:
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(self.to_markdown(), encoding="utf-8")
        return path

    @classmethod
    def from_dict(cls, data: dict) -> Transcript:
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
    def load(cls, path: str | Path) -> Transcript:
        return cls.from_dict(json.loads(Path(path).read_text(encoding="utf-8")))


class STTProvider(ABC):
    """Base class for a speech recognition adapter.

    The contract is simple: a media path (video/audio) in, a `Transcript` out.
    Providers prepare audio (extracting the track, resampling to 16 kHz mono)
    through the common `app.stt.audio` module to avoid duplicating the logic.
    """

    #: human-readable provider name, ends up in Transcript.provider and metrics
    name: str = "base"

    @abstractmethod
    def transcribe(self, media_path: str | Path) -> Transcript:
        """Recognize speech from a file and return a unified Transcript."""
        raise NotImplementedError

    def __repr__(self) -> str:  # pragma: no cover - debugging convenience
        return f"<STTProvider {self.name!r}>"
