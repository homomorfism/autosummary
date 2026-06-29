"""Audio preparation for STT.

Both Google STT and whisper.cpp expect 16 kHz mono PCM WAV input. ffmpeg
converts the lecture video (`.mp4`) to this. The logic lives here so both
adapters prepare audio identically (otherwise WER in E2 would be incomparable).
"""

from __future__ import annotations

import json
import shutil
import subprocess
from pathlib import Path

#: target parameters — required by Google STT (LINEAR16) and the native whisper.cpp format
TARGET_SAMPLE_RATE = 16_000
TARGET_CHANNELS = 1

_AUDIO_EXTS = {".wav"}


def _require_ffmpeg() -> str:
    ffmpeg = shutil.which("ffmpeg")
    if not ffmpeg:
        raise RuntimeError(
            "ffmpeg not found in PATH. Install it (brew install ffmpeg) — "
            "it is needed to extract the audio track from the video."
        )
    return ffmpeg


def ensure_wav16k(media_path: str | Path, out_dir: str | Path | None = None) -> Path:
    """Convert any media file to 16 kHz mono WAV.

    If a suitable `.wav` is already provided, it is converted anyway — this way
    we guarantee the required sample rate/channels regardless of the source WAV.
    Returns the path to the resulting WAV.
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
        "-y",  # overwrite
        "-i",
        str(media_path),
        "-vn",  # drop video
        "-ac",
        str(TARGET_CHANNELS),
        "-ar",
        str(TARGET_SAMPLE_RATE),
        "-c:a",
        "pcm_s16le",  # LINEAR16
        str(out_path),
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        raise RuntimeError(f"ffmpeg failed with an error:\n{proc.stderr[-2000:]}")
    return out_path


def probe_duration(media_path: str | Path) -> float | None:
    """Media duration in seconds via ffprobe (for latency/$ metrics in E2)."""
    ffprobe = shutil.which("ffprobe")
    if not ffprobe:
        return None
    proc = subprocess.run(
        [
            ffprobe,
            "-v",
            "quiet",
            "-print_format",
            "json",
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
