"""Schema of the structured summary (the summarizer's output).

The key project requirement is grounding: every statement is tagged with a
source (`slide` / `transcript` / `both`). This is needed for experiment E1
(coverage / faithfulness) and to prove "site > deck": the share of statements
with source `transcript` = facts that were not on the slides.
"""

from __future__ import annotations

from enum import StrEnum

from pydantic import BaseModel, Field


class Source(StrEnum):
    """Where the statement comes from."""

    slide = "slide"  # present on a slide
    transcript = "transcript"  # said aloud, not on a slide
    both = "both"  # both on a slide and in speech


class Point(BaseModel):
    claim: str = Field(description="A single atomic statement of the summary.")
    source: Source = Field(description="Source of the statement.")
    slide_number: int | None = Field(default=None, description="Slide number, if the statement relies on a slide.")
    timestamp: float | None = Field(
        default=None,
        description="Timestamp (seconds from the start) in the transcript, if applicable.",
    )


class Section(BaseModel):
    heading: str = Field(description="Heading of a thematic section of the lecture.")
    points: list[Point] = Field(description="Statements of the section.")


class KeyTerm(BaseModel):
    term: str = Field(description="Technical term.")
    definition: str = Field(description="Short definition based on the lecture material.")
    source: Source = Field(description="Source of the definition.")


class SummaryConcept(BaseModel):
    """Full structured summary of the lecture."""

    title: str = Field(description="Title of the lecture/topic.")
    overview: str = Field(description="A 2-4 sentence summary.")
    sections: list[Section] = Field(description="Summary sections in lecture order.")
    key_terms: list[KeyTerm] = Field(description="Key terms with definitions.")
    transcript_only_notes: list[str] = Field(
        default_factory=list,
        description=(
            "Important spoken remarks by the lecturer that are NOT on the slides "
            '(examples, caveats, emphases like "this will be on the exam").'
        ),
    )
