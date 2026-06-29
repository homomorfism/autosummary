"""Извлечение текста из PDF-слайдов.

Второй источник для суммаризации (помимо транскрипта). Каждый слайд — отдельный
элемент `Slide` с номером и текстом, чтобы суммаризатор мог ссылаться на
конкретный слайд, а Э1 — раскладывать слайды на атомарные факты.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass
class Slide:
    number: int          # 1-based
    text: str


@dataclass
class SlideDeck:
    slides: list[Slide]
    source: str | None = None

    @property
    def full_text(self) -> str:
        return "\n\n".join(
            f"[Слайд {s.number}]\n{s.text}" for s in self.slides if s.text.strip()
        )

    def __len__(self) -> int:
        return len(self.slides)


def extract_slides(pdf_path: str | Path) -> SlideDeck:
    """Достать текст по страницам PDF. Использует pypdf.

    Заметка: PDF со сканами/растровыми слайдами текст не отдадут — для них
    нужен OCR (вне задачи этого модуля).
    """
    pdf_path = Path(pdf_path)
    if not pdf_path.exists():
        raise FileNotFoundError(pdf_path)

    try:
        from pypdf import PdfReader
    except ImportError as e:  # pragma: no cover
        raise ImportError(
            "Не установлен pypdf. Установите: pip install pypdf"
        ) from e

    reader = PdfReader(str(pdf_path))
    slides: list[Slide] = []
    for i, page in enumerate(reader.pages, start=1):
        text = (page.extract_text() or "").strip()
        slides.append(Slide(number=i, text=text))
    return SlideDeck(slides=slides, source=str(pdf_path))
