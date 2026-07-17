"""Service configuration via environment variables (.env).

Loaded once at import time. Values are taken from the environment; if
`python-dotenv` is installed, a `.env` file in the repository root is also
picked up.
"""

from __future__ import annotations

import os
from pathlib import Path

# .env is picked up softly: dotenv is optional
try:  # pragma: no cover
    from dotenv import load_dotenv

    # override=True: .env is the single source of truth for these paths, so it
    # must win over any stale value already exported in the shell environment
    # (e.g. a leftover fish universal variable pointing at a non-existent binary).
    load_dotenv(override=True)
except Exception:  # pragma: no cover
    pass


def _get(name: str, default: str | None = None) -> str | None:
    val = os.environ.get(name, default)
    return val if val not in ("", None) else default


# --- STT provider selection -----------------------------------------------
STT_PROVIDER = _get("STT_PROVIDER", "whisper_cpp")

# --- whisper.cpp ----------------------------------------------------------
# default — the build without Core ML (build-nocoreml); the build/ build on this
# machine is compiled with Core ML and crashes without the .mlmodelc encoder.
WHISPER_CLI = _get("WHISPER_CLI", "/Users/shamilarslanov/whisper.cpp/build-nocoreml/bin/whisper-cli")
WHISPER_MODEL = _get("WHISPER_MODEL", "/Users/shamilarslanov/whisper-models/ggml-large-v3-turbo.bin")
WHISPER_VAD_MODEL = _get("WHISPER_VAD_MODEL", "/Users/shamilarslanov/whisper-models/ggml-silero-v6.2.0.bin")
WHISPER_LANGUAGE = _get("WHISPER_LANGUAGE", "en")

# --- Google STT -----------------------------------------------------------
# Accept both the project's "native" names and the familiar names from the
# docker environment (GCP_PROJECT_ID / GCS_STT_BUCKET). Authentication is via
# GOOGLE_APPLICATION_CREDENTIALS (the SDK reads it itself).
GOOGLE_CLOUD_PROJECT = _get("GOOGLE_CLOUD_PROJECT") or _get("GCP_PROJECT_ID")
GOOGLE_STT_BUCKET = _get("GOOGLE_STT_BUCKET") or _get("GCS_STT_BUCKET")
GOOGLE_STT_LANGUAGE = _get("GOOGLE_STT_LANGUAGE", "en-US")
GOOGLE_STT_MODEL = _get("GOOGLE_STT_MODEL", "latest_long")

# --- LLM (summarization) --------------------------------------------------
# LLM provider: anthropic | deepseek. If unset — inferred from the model name
# (claude-* → anthropic, deepseek-* → deepseek), otherwise deepseek.
LLM_PROVIDER = _get("LLM_PROVIDER")
LLM_MODEL = _get("LLM_MODEL", "deepseek-v4-pro")

# Anthropic (Claude). The SDK reads ANTHROPIC_API_KEY itself if the key is not passed.
ANTHROPIC_API_KEY = _get("ANTHROPIC_API_KEY")

# DeepSeek — OpenAI-compatible API.
DEEPSEEK_API_KEY = _get("DEEPSEEK_API_KEY")
DEEPSEEK_BASE_URL = _get("DEEPSEEK_BASE_URL", "https://api.deepseek.com")

# --- paths -----------------------------------------------------------------
REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = Path(_get("DATA_DIR", str(REPO_ROOT / "data")))

# --- E1 claim-level evaluation ----------------------------------------------
# Embedding model for entailment retrieval (sentence-transformers). When the
# package is not installed, app.e1 falls back to a built-in TF-IDF retriever.
E1_EMBED_MODEL = _get("E1_EMBED_MODEL", "BAAI/bge-small-en-v1.5")

# --- quiz web app / psychometrics -------------------------------------------
# SQLite database with quiz attempts and per-question answers (experiment E3).
QUIZ_DB_PATH = Path(_get("QUIZ_DB_PATH", str(DATA_DIR / "quiz_results.db")))
