"""Batch dual-provider transcription for lectures.

For each lecture directory (containing ``video.mp4``) this runs BOTH STT
providers — local whisper.cpp and cloud Google STT — and writes the unified
transcript as JSON + Markdown in place, next to the video:

    <lecture-dir>/<provider>/transcription.{json,md}

Google STT internally extracts 16 kHz mono audio, uploads it to the configured
GCS bucket (long_running_recognize reads from GCS), and removes the object
afterwards. A local ``audio.wav`` (16 kHz mono) is also kept in the lecture
directory so the slice can be reused for the E2 benchmark.

    python -m app.transcribe data/deep-learning-and-computer-vision/lecture-01
    python -m app.transcribe <lecture-dir> --providers whisper_cpp google_stt
"""

from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

from dotenv import load_dotenv

from app.stt import get_stt_provider
from app.stt.audio import ensure_wav16k

assert load_dotenv()


def transcribe_lecture(
    lecture_dir: Path,
    providers: list[str],
) -> None:
    video = lecture_dir / "video.mp4"
    if not video.exists():
        raise FileNotFoundError(f"No video.mp4 in {lecture_dir}")

    out_dir = lecture_dir

    # extract 16 kHz mono audio once and reuse for every provider
    print(f"[{lecture_dir.name}] extracting 16 kHz mono audio …")
    audio = ensure_wav16k(video, out_dir=out_dir)
    # ensure_wav16k names the file "<stem>.16k.wav"; normalize to audio.wav
    final_audio = out_dir / "audio.wav"
    if audio != final_audio:
        audio.replace(final_audio)
    print(f"           audio: {final_audio}")

    for name in providers:
        provider = get_stt_provider(name)
        p_dir = out_dir / provider.name
        p_dir.mkdir(parents=True, exist_ok=True)
        print(f"[{lecture_dir.name}] {provider.name}: transcribing …")
        t0 = time.monotonic()
        transcript = provider.transcribe(final_audio)
        dt = time.monotonic() - t0
        jpath = transcript.save(p_dir / "transcription.json")
        mpath = transcript.save_markdown(p_dir / "transcription.md")
        print(f"           {provider.name}: {len(transcript.segments)} segments, {dt:.0f}s wall")
        print(f"           json: {jpath}")
        print(f"           md:   {mpath}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Dual-provider lecture transcription")
    parser.add_argument(
        "lectures",
        nargs="+",
        help="One or more lecture directories (each must contain video.mp4)",
    )
    parser.add_argument(
        "--providers",
        nargs="+",
        default=["whisper_cpp", "google_stt"],
        help="STT providers to run (default: whisper_cpp google_stt)",
    )
    args = parser.parse_args(argv)

    for lec in args.lectures:
        lecture_dir = Path(lec).resolve()
        transcribe_lecture(lecture_dir, args.providers)

    print("Done.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
