"""Extracting text from PDF slides.

A second source for summarization (besides the transcript). Each slide is a
separate `Slide` element with a number and text, so the summarizer can reference
a specific slide, and E1 can break slides down into atomic facts.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass
class Slide:
    number: int  # 1-based
    text: str


@dataclass
class SlideDeck:
    slides: list[Slide]
    source: str | None = None

    @property
    def full_text(self) -> str:
        return "\n\n".join(f"[Slide {s.number}]\n{s.text}" for s in self.slides if s.text.strip())

    def __len__(self) -> int:
        return len(self.slides)


def extract_slides(pdf_path: str | Path) -> SlideDeck:
    """Extract text page by page from a PDF. Uses pypdf.

    Note: PDFs with scanned/raster slides will not yield text — those require
    OCR (outside the scope of this module).
    """
    pdf_path = Path(pdf_path)
    if not pdf_path.exists():
        raise FileNotFoundError(pdf_path)

    try:
        from pypdf import PdfReader
    except ImportError as e:  # pragma: no cover
        raise ImportError("pypdf is not installed. Install it: pip install pypdf") from e

    reader = PdfReader(str(pdf_path))
    slides: list[Slide] = []
    for i, page in enumerate(reader.pages, start=1):
        text = (page.extract_text() or "").strip()
        slides.append(Slide(number=i, text=text))
    return SlideDeck(slides=slides, source=str(pdf_path))
