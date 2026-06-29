"""Multi-source summarization: transcript + slides -> a structured summary.

from app.summarize import summarize
concept = summarize(transcript, slide_deck)
"""

from __future__ import annotations

from app.summarize.schema import KeyTerm, Point, Section, Source, SummaryConcept
from app.summarize.summarizer import Summarizer, summarize

__all__ = [
    "summarize",
    "Summarizer",
    "SummaryConcept",
    "Section",
    "Point",
    "KeyTerm",
    "Source",
]
