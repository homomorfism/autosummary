"""Конфигурация сервиса через переменные окружения (.env).

Загружается один раз при импорте. Значения берутся из окружения; если установлен
`python-dotenv`, дополнительно подхватывается файл `.env` в корне репозитория.
"""

from __future__ import annotations

import os
from pathlib import Path

# .env подхватываем мягко: dotenv опционален
try:  # pragma: no cover
    from dotenv import load_dotenv

    load_dotenv()
except Exception:  # pragma: no cover
    pass


def _get(name: str, default: str | None = None) -> str | None:
    val = os.environ.get(name, default)
    return val if val not in ("", None) else default


# --- выбор провайдера STT -------------------------------------------------
STT_PROVIDER = _get("STT_PROVIDER", "whisper_cpp")

# --- whisper.cpp ----------------------------------------------------------
# по умолчанию — сборка без Core ML (build-nocoreml); сборка build/ на этой
# машине собрана с Core ML и падает без .mlmodelc-энкодера.
WHISPER_CLI = _get("WHISPER_CLI", "/Users/shamilarslanov/whisper.cpp/build-nocoreml/bin/whisper-cli")
WHISPER_MODEL = _get("WHISPER_MODEL", "/Users/shamilarslanov/whisper-models/ggml-large-v3-turbo.bin")
WHISPER_VAD_MODEL = _get("WHISPER_VAD_MODEL", "/Users/shamilarslanov/whisper-models/ggml-silero-v6.2.0.bin")
WHISPER_LANGUAGE = _get("WHISPER_LANGUAGE", "en")

# --- Google STT -----------------------------------------------------------
# Принимаем как «родные» имена проекта, так и привычные имена из docker-окружения
# (GCP_PROJECT_ID / GCS_STT_BUCKET). Аутентификация — через
# GOOGLE_APPLICATION_CREDENTIALS (SDK читает его сам).
GOOGLE_CLOUD_PROJECT = _get("GOOGLE_CLOUD_PROJECT") or _get("GCP_PROJECT_ID")
GOOGLE_STT_BUCKET = _get("GOOGLE_STT_BUCKET") or _get("GCS_STT_BUCKET")
GOOGLE_STT_LANGUAGE = _get("GOOGLE_STT_LANGUAGE", "en-US")
GOOGLE_STT_MODEL = _get("GOOGLE_STT_MODEL", "latest_long")

# --- LLM (суммаризация) ---------------------------------------------------
ANTHROPIC_API_KEY = _get("ANTHROPIC_API_KEY")
LLM_MODEL = _get("LLM_MODEL", "claude-opus-4-8")

# --- пути ------------------------------------------------------------------
REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = Path(_get("DATA_DIR", str(REPO_ROOT / "data")))
