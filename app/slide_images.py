"""Render slides.pdf pages to PNGs for embedding in the conspect.

Every page of ``<lecture-dir>/slides.pdf`` is rendered with ``pdftoppm``
(poppler, same dependency as ``app.align_video``) into
``<lecture-dir>/slides_images/slide-NN.png``. ``app.conspect`` points the LLM
at these files so it can inline figure-heavy slides as Markdown images, and the
web app serves them next to the rendered conspect.

    python -m app.slide_images data/<course>/<lecture>

Idempotent: skips rendering when slides_images/ already holds one PNG per page.
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

IMAGES_DIRNAME = "slides_images"
RENDER_WIDTH = 1600  # px; readable in the conspect without bloating the repo

SLIDE_HEADING_RE = re.compile(r"^## Slide (\d+)\s*$", re.MULTILINE)


def render_slide_images(lecture_dir: Path, *, force: bool = False) -> Path | None:
    """Render slides.pdf → slides_images/slide-NN.png. Returns the images dir, or None without a PDF."""
    pdf = lecture_dir / "slides.pdf"
    if not pdf.exists():
        return None

    pdftoppm = shutil.which("pdftoppm")
    if pdftoppm is None:
        raise RuntimeError("pdftoppm not found in PATH — install poppler (brew install poppler).")

    out_dir = lecture_dir / IMAGES_DIRNAME
    if not force and out_dir.is_dir() and list(out_dir.glob("slide-*.png")):
        return out_dir
    out_dir.mkdir(exist_ok=True)
    for stale in out_dir.glob("slide-*.png"):
        stale.unlink()

    cmd = [pdftoppm, "-png", "-scale-to-x", str(RENDER_WIDTH), "-scale-to-y", "-1", str(pdf), str(out_dir / "page")]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        raise RuntimeError(f"pdftoppm failed:\n{proc.stderr[-2000:]}")

    # pdftoppm pads page numbers to the page-count width (page-1.png / page-001.png);
    # normalize to slide-NN.png (2+ digits) so conspect references are predictable.
    for rendered in sorted(out_dir.glob("page-*.png")):
        n = int(rendered.stem.split("-")[1])
        rendered.rename(out_dir / f"slide-{n:02d}.png")
    return out_dir


def build_slide_index(lecture_dir: Path) -> str | None:
    """One line per slide for the conspect prompt: image path, first text line, word count.

    Reads the raw ``slides_extracted/slides.md`` (the only artifact that keeps
    physical slide boundaries) and lists only slides that actually got rendered.
    """
    raw = lecture_dir / "slides_extracted" / "slides.md"
    images_dir = lecture_dir / IMAGES_DIRNAME
    if not raw.exists() or not images_dir.is_dir():
        return None
    rendered = {p.name for p in images_dir.glob("slide-*.png")}
    if not rendered:
        return None

    text = raw.read_text(encoding="utf-8")
    matches = list(SLIDE_HEADING_RE.finditer(text))
    lines: list[str] = []
    for i, m in enumerate(matches):
        n = int(m.group(1))
        name = f"slide-{n:02d}.png"
        if name not in rendered:
            continue
        body = text[m.end() : matches[i + 1].start() if i + 1 < len(matches) else len(text)].strip()
        words = len(body.split())
        first = next((ln.strip() for ln in body.splitlines() if ln.strip()), "")
        if len(first) > 80:
            first = first[:77] + "..."
        lines.append(f"{IMAGES_DIRNAME}/{name} — slide {n}, {words} words: {first or '(no extracted text)'}")
    return "\n".join(lines) or None


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Render slides.pdf pages to slides_images/slide-NN.png")
    parser.add_argument("lectures", nargs="+", help="Lecture directories containing slides.pdf")
    parser.add_argument("--force", action="store_true", help="Re-render even if images already exist")
    args = parser.parse_args(argv)

    for lec in args.lectures:
        lecture_dir = Path(lec).resolve()
        out = render_slide_images(lecture_dir, force=args.force)
        if out is None:
            print(f"[{lecture_dir.name}] no slides.pdf — skipped")
        else:
            print(f"[{lecture_dir.name}] {len(list(out.glob('slide-*.png')))} pages -> {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
