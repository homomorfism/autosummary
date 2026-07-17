"""STT providers: a common interface + a factory for selecting an adapter.

from app.stt import get_stt_provider
provider = get_stt_provider("whisper_cpp")   # or "google_stt"
transcript = provider.transcribe("lecture.mp4")
"""

from __future__ import annotations

from app.stt.base import Segment, STTProvider, Transcript, Word

__all__ = [
    "STTProvider",
    "Transcript",
    "Segment",
    "Word",
    "get_stt_provider",
    "available_providers",
]


def available_providers() -> list[str]:
    return ["whisper_cpp", "google_stt"]


def get_stt_provider(name: str | None = None, **overrides) -> STTProvider:
    """Return an STT adapter by name.

    `name=None` -> `STT_PROVIDER` is taken from the configuration. Any adapter
    constructor parameter can be overridden via `overrides`.
    """
    from app import config

    name = (name or config.STT_PROVIDER or "whisper_cpp").lower()

    if name in ("whisper_cpp", "whisper", "local"):
        from app.stt.whisper_cpp import WhisperCppProvider

        kwargs = dict(
            cli_path=config.WHISPER_CLI,
            model_path=config.WHISPER_MODEL,
            vad_model_path=config.WHISPER_VAD_MODEL,
            language=config.WHISPER_LANGUAGE,
        )
        kwargs.update(overrides)
        return WhisperCppProvider(**kwargs)

    if name in ("google_stt", "google", "cloud"):
        from app.stt.google_stt import GoogleSTTProvider

        kwargs = dict(
            bucket=config.GOOGLE_STT_BUCKET,
            project=config.GOOGLE_CLOUD_PROJECT,
            language_code=config.GOOGLE_STT_LANGUAGE,
            model=config.GOOGLE_STT_MODEL,
        )
        kwargs.update(overrides)
        return GoogleSTTProvider(**kwargs)

    raise ValueError(f"Unknown STT provider: {name!r}. Available: {', '.join(available_providers())}.")
