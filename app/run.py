"""Сквозной запуск: видео + слайды → транскрипт → конспект.

    python -m app.run --video lecture.mp4 --slides slides.pdf --provider whisper_cpp

Этапы выравнивания / генерации вопросов / webapp подключатся в этот же пайплайн
по мере готовности (см. TODO.md). Сейчас покрыты STT и суммаризация — этого
достаточно, чтобы получить заземлённый конспект и сохранить артефакты.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Autosummary: видео+слайды → конспект")
    parser.add_argument("--video", required=True, help="Путь к видео/аудио лекции")
    parser.add_argument("--slides", help="Путь к PDF слайдов (опционально)")
    parser.add_argument(
        "--provider",
        default=None,
        help="STT-провайдер: whisper_cpp | google_stt (по умолчанию из конфига)",
    )
    parser.add_argument(
        "--out",
        default=None,
        help="Каталог для артефактов (по умолчанию рядом с видео)",
    )
    parser.add_argument(
        "--transcript",
        help="Готовый transcript.json — пропустить STT и взять его",
    )
    parser.add_argument(
        "--no-summary",
        action="store_true",
        help="Только распознать речь, без вызова LLM-суммаризатора",
    )
    args = parser.parse_args(argv)

    video = Path(args.video)
    out_dir = Path(args.out) if args.out else video.parent
    out_dir.mkdir(parents=True, exist_ok=True)

    from .stt import Transcript, get_stt_provider

    # --- 1. STT -----------------------------------------------------------
    if args.transcript:
        print(f"[1/3] Беру готовый транскрипт: {args.transcript}")
        transcript = Transcript.load(args.transcript)
    else:
        provider = get_stt_provider(args.provider)
        print(f"[1/3] Распознаю речь провайдером {provider.name} …")
        transcript = provider.transcribe(video)
        tpath = transcript.save(out_dir / "transcript.json")
        print(f"      транскрипт сохранён: {tpath} ({len(transcript.segments)} сегм.)")

    # --- 2. Слайды --------------------------------------------------------
    slide_deck = None
    if args.slides:
        from .slides import extract_slides

        print(f"[2/3] Извлекаю текст слайдов: {args.slides}")
        slide_deck = extract_slides(args.slides)
        print(f"      слайдов: {len(slide_deck)}")
    else:
        print("[2/3] Слайды не переданы — суммаризация только по речи")

    if args.no_summary:
        print("Готово (этап суммаризации пропущен по --no-summary).")
        return 0

    # --- 3. Суммаризация --------------------------------------------------
    from .summarize import summarize

    print("[3/3] Собираю структурированный конспект (LLM) …")
    concept = summarize(transcript, slide_deck if slide_deck else "")
    spath = out_dir / "summary.json"
    spath.write_text(
        concept.model_dump_json(indent=2),
        encoding="utf-8",
    )
    print(f"      конспект сохранён: {spath}")
    print(
        f"      разделов: {len(concept.sections)}, "
        f"терминов: {len(concept.key_terms)}, "
        f"устных ремарок: {len(concept.transcript_only_notes)}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
