"""Схема структурированного конспекта (выход суммаризатора).

Ключевое требование проекта — заземление: каждое утверждение помечено
источником (`slide` / `transcript` / `both`). Это нужно эксперименту Э1
(coverage / faithfulness) и доказательству «сайт > преза»: доля утверждений с
источником `transcript` = факты, которых не было на слайдах.
"""

from __future__ import annotations

from enum import Enum

from pydantic import BaseModel, Field


class Source(str, Enum):
    """Откуда взято утверждение."""

    slide = "slide"            # есть на слайде
    transcript = "transcript"  # сказано устно, на слайде нет
    both = "both"              # и на слайде, и в речи


class Point(BaseModel):
    claim: str = Field(description="Одно атомарное утверждение конспекта.")
    source: Source = Field(description="Источник утверждения.")
    slide_number: int | None = Field(
        default=None, description="Номер слайда, если утверждение опирается на слайд."
    )
    timestamp: float | None = Field(
        default=None,
        description="Таймкод (секунды от начала) в транскрипте, если применимо.",
    )


class Section(BaseModel):
    heading: str = Field(description="Заголовок смыслового раздела лекции.")
    points: list[Point] = Field(description="Утверждения раздела.")


class KeyTerm(BaseModel):
    term: str = Field(description="Технический термин.")
    definition: str = Field(description="Краткое определение по материалам лекции.")
    source: Source = Field(description="Источник определения.")


class SummaryConcept(BaseModel):
    """Полный структурированный конспект лекции."""

    title: str = Field(description="Название лекции/темы.")
    overview: str = Field(description="Резюме в 2–4 предложения.")
    sections: list[Section] = Field(description="Разделы конспекта по порядку лекции.")
    key_terms: list[KeyTerm] = Field(
        description="Ключевые термины с определениями."
    )
    transcript_only_notes: list[str] = Field(
        default_factory=list,
        description=(
            "Важные устные ремарки лектора, которых НЕТ на слайдах "
            "(примеры, оговорки, акценты «это будет на экзамене»)."
        ),
    )
