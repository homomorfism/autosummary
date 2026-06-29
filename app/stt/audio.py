"""Подготовка аудио для STT.

И Google STT, и whisper.cpp ждут на вход 16 кГц моно PCM WAV. Видео лекции
(`.mp4`) к этому приводит ffmpeg. Логика вынесена сюда, чтобы оба адаптера
готовили аудио одинаково (иначе WER в Э2 будет несравним).
"""

from __future__ import annotations

import json
import shutil
import subprocess
from pathlib import Path

#: целевые параметры — требование Google STT (LINEAR16) и нативный формат whisper.cpp
TARGET_SAMPLE_RATE = 16_000
TARGET_CHANNELS = 1

_AUDIO_EXTS = {".wav"}


def _require_ffmpeg() -> str:
    ffmpeg = shutil.which("ffmpeg")
    if not ffmpeg:
        raise RuntimeError(
            "ffmpeg не найден в PATH. Установите его (brew install ffmpeg) — "
            "он нужен для извлечения аудиодорожки из видео."
        )
    return ffmpeg


def ensure_wav16k(media_path: str | Path, out_dir: str | Path | None = None) -> Path:
    """Привести любой медиафайл к 16 кГц моно WAV.

    Если на вход уже подан подходящий `.wav`, он конвертируется всё равно —
    так мы гарантируем нужные частоту/каналы независимо от исходного WAV.
    Возвращает путь к готовому WAV.
    """
    media_path = Path(media_path)
    if not media_path.exists():
        raise FileNotFoundError(media_path)

    out_dir = Path(out_dir) if out_dir else media_path.parent
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{media_path.stem}.16k.wav"

    ffmpeg = _require_ffmpeg()
    cmd = [
        ffmpeg,
        "-y",                       # перезаписать
        "-i", str(media_path),
        "-vn",                      # выбросить видео
        "-ac", str(TARGET_CHANNELS),
        "-ar", str(TARGET_SAMPLE_RATE),
        "-c:a", "pcm_s16le",        # LINEAR16
        str(out_path),
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        raise RuntimeError(f"ffmpeg завершился с ошибкой:\n{proc.stderr[-2000:]}")
    return out_path


def probe_duration(media_path: str | Path) -> float | None:
    """Длительность медиа в секундах через ffprobe (для метрик latency/$ в Э2)."""
    ffprobe = shutil.which("ffprobe")
    if not ffprobe:
        return None
    proc = subprocess.run(
        [
            ffprobe,
            "-v", "quiet",
            "-print_format", "json",
            "-show_format",
            str(media_path),
        ],
        capture_output=True,
        text=True,
    )
    if proc.returncode != 0:
        return None
    try:
        return float(json.loads(proc.stdout)["format"]["duration"])
    except (KeyError, ValueError, json.JSONDecodeError):
        return None
