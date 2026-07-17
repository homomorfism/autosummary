"""Slide → Markdown extraction and LLM reconstruction.

For each lecture directory (containing ``slides.pdf``) this produces two files
under ``<lecture-dir>/slides_extracted/``:

* ``slides.md`` — raw text extracted page by page with **PyMuPDF** (``fitz``).
  Faithful but messy: PDF extraction mangles math, drops layout, splits words.
* ``slides_reconstructed.md`` — the raw extraction passed through an LLM
  (DeepSeek), rewritten into ONE coherent, ready-to-read lecture conspect:
  logical ``#/##/###`` hierarchy (not slide boundaries), bullet points, LaTeX
  math (``$…$`` / ``$$…$$``), definitions/theorems as blockquotes. It repairs
  extraction noise and reconstructs math without inventing new information, and
  strips PII / course-admin chrome.

    python -m app.extract_slides data/deep-learning-and-computer-vision/lecture-01
    python -m app.extract_slides <lecture-dir> ... --no-reconstruct
    python -m app.extract_slides <lecture-dir> --model deepseek-v4-pro

The reconstructed conspect is a cleaner second source for the summarizer than
the raw ``slides.py`` extraction — math survives, so E1 facts stay grounded.
"""

from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

# --- prompts ---------------------------------------------------------------

RECONSTRUCT_SYSTEM_PROMPT = """\
You are an expert academic editor. Your job is to transform raw, noisy Markdown
extracted from lecture-slide PDFs (via PyMuPDF) into a clean, faithful,
hierarchically-structured lecture conspect in Markdown.

The input is a *full lecture*: many slides concatenated, often with broken
formulas, split paragraphs, repeated headers/footers, page numbers, and
out-of-order fragments. Your output is ONE coherent document that a student
could read top-to-bottom instead of the slides.

## Output structure (strict hierarchy)

Use Markdown headings to reflect the logical structure of the lecture, not the
physical slide boundaries:

- `# Title` — one, inferred from the lecture's overall topic
- `## Section` — each major thematic block (typically corresponds to a group of slides)
- `### Subsection` — distinct subtopics, theorems, algorithms, or case studies inside a section
- `#### Detail` (use sparingly) — only when a subsection genuinely splits into named parts

Within sections, use:
- **Bold** for technical terms on first introduction
- *Italics* for emphasis the lecturer clearly intended
- Bulleted lists for enumerations, properties, assumptions, steps, criteria
- Numbered lists ONLY for ordered procedures (algorithms, proofs, derivations)
- `> Blockquote` for definitions, theorems, lemmas, key takeaways, and named results
- Fenced code blocks with language tags for code (```python, ```sql, etc.)
- LaTeX math: inline `$...$` for short expressions, display `$$...$$` for standalone formulas and derivations.
  Use ONLY these dollar delimiters — NEVER `\\(...\\)` or `\\[...\\]`, they break the downstream renderer.
  Put display `$$` fences on their own lines; inside a list item, indent the block to the item's text level.
- Tables when the source presents tabular data

## Reconstruction rules (PyMuPDF cleanup)

The raw input is corrupted in predictable ways. Repair these:

- **Broken formulas**: PyMuPDF often mangles math (missing braces, misplaced
  sub/superscripts, lost Greek letters, split fractions). Reconstruct the intended
  LaTeX from context. If a symbol is ambiguous, prefer the standard convention for the topic.
- **Hyphenated line-breaks**: join `compu-\\ntation` -> `computation`.
- **Split paragraphs**: merge sentences broken across slide lines into flowing prose.
- **Repeated chrome**: drop page numbers, slide numbers, recurring lecturer name /
  course code / date headers and footers.
- **Out-of-order fragments**: if related content is scattered across slides (e.g. a
  definition on slide 4 and its example on slide 7), merge them into one coherent section.
- **Duplicate content**: if the same definition or formula appears on multiple slides
  (e.g. recap slides), keep it once in the most logical place.
- **Bullet noise**: replace stray glyphs with proper Markdown list syntax.
- **Figure references**: if the slide says "see figure" but the figure is not in the
  text, preserve the reference as plain text (e.g. *(figure: gradient descent
  trajectory)*) — do not invent the figure.

## Faithfulness rules (do NOT alter content)

- Do NOT summarise, compress, or omit substantive content — preserve the full arc
  and every concept the lecturer covered.
- Do NOT add explanations, intuitions, examples, or commentary not present in the source.
- Do NOT translate between languages — keep the original language of the lecture.
- Do NOT invent section titles that don't reflect actual content; derive every heading from the material itself.
- Do NOT rephrase definitions, theorem statements, or formulas — copy them verbatim (modulo formatting/LaTeX repair).
- Preserve numerical values, variable names, and notation exactly as given.

## Rules

- Remove any personal identifiable information from the lecture slides (instructor
  names, phones, email, links to linkedin, etc).
- Remove any organization information about the course (grading, course structure, etc).

## Output contract

Return ONLY the cleaned Markdown document. No preamble, no meta-commentary,
no explanation of what you did. The first line must be the `# Title`.
"""

RECONSTRUCT_USER_TEMPLATE = """\
Here is the raw extracted Markdown for the full lecture. Produce the cleaned \
conspect per your instructions.

{slides}"""


# --- extraction (PyMuPDF) --------------------------------------------------


def extract_markdown(pdf_path: str | Path) -> str:
    """Extract slide text page by page with PyMuPDF and render it as Markdown.

    Each page becomes a ``## Slide N`` section. This is the raw, faithful
    extraction — math and layout are not reconstructed (see ``reconstruct``).
    """
    pdf_path = Path(pdf_path)
    if not pdf_path.exists():
        raise FileNotFoundError(pdf_path)

    try:
        import fitz  # PyMuPDF
    except ImportError as e:  # pragma: no cover
        raise ImportError("PyMuPDF is not installed. Install it: pip install pymupdf") from e

    parts: list[str] = [f"# Slides (extracted) — {pdf_path.name}", ""]
    with fitz.open(str(pdf_path)) as doc:
        for i in range(1, doc.page_count + 1):
            text = doc[i - 1].get_text("text").strip()
            parts.append(f"## Slide {i}")
            parts.append("")
            parts.append(text if text else "*(no extractable text)*")
            parts.append("")
    return "\n".join(parts).rstrip() + "\n"


# --- reconstruction (DeepSeek) ---------------------------------------------


class SlideReconstructor:
    """Clean up extracted slide text and reconstruct math via an LLM (DeepSeek)."""

    def __init__(
        self,
        *,
        model: str | None = None,
        api_key: str | None = None,
        base_url: str | None = None,
        max_tokens: int = 16_000,
    ) -> None:
        from app import config

        self.model = model or config.LLM_MODEL or "deepseek-v4-pro"
        self.api_key = api_key
        self.base_url = base_url
        self.max_tokens = max_tokens
        self._client = None

    def _deepseek_client(self):
        if self._client is None:
            from app import config

            try:
                from openai import OpenAI
            except ImportError as e:  # pragma: no cover
                raise ImportError(
                    "The openai SDK is not installed (needed for DeepSeek). Install it: pip install openai"
                ) from e
            self._client = OpenAI(
                api_key=self.api_key or config.DEEPSEEK_API_KEY,
                base_url=self.base_url or config.DEEPSEEK_BASE_URL,
            )
        return self._client

    def reconstruct(self, extracted_markdown: str) -> str:
        """Return reconstructed Markdown (LaTeX math, cleaned text)."""
        client = self._deepseek_client()
        user_msg = RECONSTRUCT_USER_TEMPLATE.format(slides=extracted_markdown)
        response = client.chat.completions.create(
            model=self.model,
            max_tokens=self.max_tokens,
            messages=[
                {"role": "system", "content": RECONSTRUCT_SYSTEM_PROMPT},
                {"role": "user", "content": user_msg},
            ],
        )
        choice = response.choices[0]
        content = (choice.message.content or "").strip()
        if not content:
            raise RuntimeError("DeepSeek returned an empty reconstruction.")
        if choice.finish_reason == "length":
            print(
                f"           WARNING: reconstruction hit the {self.max_tokens}-token limit and may be "
                "truncated — raise max_tokens for this deck."
            )
        return content.rstrip() + "\n"


# --- pipeline --------------------------------------------------------------


def process_lecture(
    lecture_dir: Path,
    *,
    reconstruct: bool = True,
    model: str | None = None,
) -> None:
    pdf = lecture_dir / "slides.pdf"
    if not pdf.exists():
        raise FileNotFoundError(f"No slides.pdf in {lecture_dir}")

    out_dir = lecture_dir / "slides_extracted"
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"[{lecture_dir.name}] extracting slides with PyMuPDF …")
    extracted = extract_markdown(pdf)
    n_slides = extracted.count("\n## Slide ")
    extracted_path = out_dir / "slides.md"
    extracted_path.write_text(extracted, encoding="utf-8")
    print(f"           {n_slides} slides -> {extracted_path}")

    if not reconstruct:
        return

    print(f"[{lecture_dir.name}] reconstructing text + math (DeepSeek) …")
    t0 = time.monotonic()
    reconstructed = SlideReconstructor(model=model).reconstruct(extracted)
    dt = time.monotonic() - t0
    recon_path = out_dir / "slides_reconstructed.md"
    recon_path.write_text(reconstructed, encoding="utf-8")
    print(f"           {dt:.0f}s wall -> {recon_path}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Slides → Markdown extraction and LLM reconstruction")
    parser.add_argument(
        "lectures",
        nargs="+",
        help="One or more lecture directories (each must contain slides.pdf)",
    )
    parser.add_argument(
        "--no-reconstruct",
        action="store_true",
        help="Only extract with PyMuPDF; skip the LLM reconstruction step",
    )
    parser.add_argument(
        "--model",
        default=None,
        help="LLM model for reconstruction (default from config, e.g. deepseek-v4-pro)",
    )
    args = parser.parse_args(argv)

    for lec in args.lectures:
        lecture_dir = Path(lec).resolve()
        process_lecture(lecture_dir, reconstruct=not args.no_reconstruct, model=args.model)

    print("Done.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
