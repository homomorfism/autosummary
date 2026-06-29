"""Мультиисточниковая суммаризация: транскрипт + слайды → структурированный конспект.

    from app.summarize import summarize
    concept = summarize(transcript, slide_deck)
"""

from __future__ import annotations

from .schema import KeyTerm, Point, Section, Source, SummaryConcept
from .summarizer import Summarizer, summarize

__all__ = [
    "summarize",
    "Summarizer",
    "SummaryConcept",
    "Section",
    "Point",
    "KeyTerm",
    "Source",
]
