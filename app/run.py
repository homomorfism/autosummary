"""End-to-end run: video + slides → transcript → summary.

    python -m app.run --video lecture.mp4 --slides slides.pdf --provider whisper_cpp

The alignment / question generation / webapp stages will plug into this same
pipeline as they become ready (see TODO.md). For now STT and summarization are
covered — enough to produce a grounded summary and save the artifacts.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Autosummary: video+slides → summary")
    parser.add_argument("--video", required=True, help="Path to lecture video/audio")
    parser.add_argument("--slides", help="Path to slides PDF (optional)")
    parser.add_argument(
        "--provider",
        default=None,
        help="STT provider: whisper_cpp | google_stt (default from config)",
    )
    parser.add_argument(
        "--out",
        default=None,
        help="Directory for artifacts (default: next to the video)",
    )
    parser.add_argument(
        "--transcript",
        help="Existing transcript.json — skip STT and use it",
    )
    parser.add_argument(
        "--no-summary",
        action="store_true",
        help="Only recognize speech, without calling the LLM summarizer",
    )
    args = parser.parse_args(argv)

    video = Path(args.video)
    out_dir = Path(args.out) if args.out else video.parent
    out_dir.mkdir(parents=True, exist_ok=True)

    from app.stt import Transcript, get_stt_provider

    # --- 1. STT -----------------------------------------------------------
    if args.transcript:
        print(f"[1/3] Using existing transcript: {args.transcript}")
        transcript = Transcript.load(args.transcript)
    else:
        provider = get_stt_provider(args.provider)
        print(f"[1/3] Recognizing speech with provider {provider.name} …")
        transcript = provider.transcribe(video)
        tpath = transcript.save(out_dir / "transcript.json")
        print(f"      transcript saved: {tpath} ({len(transcript.segments)} seg.)")

    # --- 2. Slides --------------------------------------------------------
    slide_deck = None
    if args.slides:
        from app.slides import extract_slides

        print(f"[2/3] Extracting slide text: {args.slides}")
        slide_deck = extract_slides(args.slides)
        print(f"      slides: {len(slide_deck)}")
    else:
        print("[2/3] No slides provided — summarizing speech only")

    if args.no_summary:
        print("Done (summarization stage skipped via --no-summary).")
        return 0

    # --- 3. Summarization -------------------------------------------------
    from app.summarize import summarize

    print("[3/3] Building a structured summary (LLM) …")
    concept = summarize(transcript, slide_deck if slide_deck else "")
    spath = out_dir / "summary.json"
    spath.write_text(
        concept.model_dump_json(indent=2),
        encoding="utf-8",
    )
    print(f"      summary saved: {spath}")
    print(
        f"      sections: {len(concept.sections)}, "
        f"terms: {len(concept.key_terms)}, "
        f"spoken remarks: {len(concept.transcript_only_notes)}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
