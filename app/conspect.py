"""Final lecture conspect: transcript + reconstructed slides → one Markdown document.

For each lecture directory this takes the two sources produced by the earlier
pipeline stages:

* ``<lecture-dir>/<stt-provider>/transcription_reconstructed.md`` — the
  LLM-cleaned timestamped transcript (see ``app.reconstruct_transcript``; falls
  back to the raw ``transcription.md`` from ``app.transcribe``);
* ``<lecture-dir>/slides_extracted/slides_reconstructed.md`` — the LLM-cleaned
  slide conspect (see ``app.extract_slides``; falls back to the raw
  ``slides.md`` if the reconstruction is missing);

and merges them with a single LLM call into ``<lecture-dir>/conspect.md`` — the
final study conspect. The slides give the backbone structure; the transcript
contributes everything the lecturer said that is *not* on the slides (intuitions,
examples, caveats, exam emphases) — preserving that spoken-only value is the
project's thesis. Spoken material is woven into the text in the conspect's own
voice (no lecturer quotes), section headings carry ``*[HH:MM]*`` timestamps, and
math from both sources is reconstructed as proper LaTeX.

    python -m app.conspect data/deep-learning-and-computer-vision/lecture-01
    python -m app.conspect <lecture-dir> ... --stt google_stt --model claude-opus-4-8

Programmatic use: ``write_conspect(transcript_md, slides_md)`` → Markdown string.
"""

from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

from app.slide_images import build_slide_index, render_slide_images

# --- prompts ---------------------------------------------------------------

SYSTEM_PROMPT = """\
You are an expert academic editor. You produce the FINAL study conspect of a
university lecture from two sources:

1. **Slide conspect** — a clean, hierarchical Markdown document reconstructed
   from the lecture slides. Treat it as the backbone: its structure, formulas,
   definitions, and terminology are authoritative.
2. **Speech transcript** — automatic speech recognition of the lecturer, split
   into timestamped segments. It is noisy (recognition errors, filler words,
   digressions) but contains material that is NOT on the slides.

Your output is ONE coherent Markdown document a student can study from instead
of watching the lecture and reading the slides.

## How to merge the sources

- Follow the logical order of the lecture. Use the slide conspect's section
  structure as the starting skeleton and adjust it where the lecturer's actual
  narrative ordered things differently.
- For every section, enrich the slide material with what the lecturer SAID
  about it: explanations of *why*, intuitions, worked examples, analogies,
  caveats, common mistakes, answers to student questions, practical advice.
  This spoken-only material is the most valuable part of the conspect — never
  drop it to save space.
- Weave spoken-only material into the body text as regular statements, lightly
  reformulated into the conspect's own voice. Do NOT quote or attribute the
  lecturer ("the lecturer says…", "Lecturer's note:") — state the point
  directly, as if it were always part of the written material. When the
  lecturer flags importance ("this is important", "this will be on the exam",
  "people always get this wrong"), keep that emphasis in the text itself.
- Where a section corresponds to a clear stretch of the lecture, append the
  starting timestamp to its heading as ` *[HH:MM]*` so the student can jump to
  the recording.
- When the transcript and the slides conflict on a formula, symbol, or precise
  value, trust the slides (ASR mangles math); when they conflict on emphasis or
  interpretation, trust the transcript (it is what the lecturer actually meant).

## Grounding rules

- Do NOT invent facts, examples, or explanations absent from both sources.
- Do NOT summarise away substantive content — compress wording, not ideas.
- Repair obvious ASR errors from context (misheard terms, broken names of
  methods/theorems); if a passage is unintelligible, omit it rather than guess.
- Reconstruct mathematics as proper LaTeX. Both sources corrupt formulas in
  predictable ways: PDF extraction loses braces, sub/superscripts, Greek
  letters, and fraction structure; ASR renders spoken math as words ("p of x
  given theta" → $p(x \\mid \\theta)$). Rebuild the intended formula from
  context; when a symbol is ambiguous, prefer the standard convention for the
  topic and the notation used elsewhere in the slides.
- Keep the language of the lecture; keep established English technical terms
  as-is.

## What to drop from the transcript

Greetings and small talk, technical difficulties ("can you see my screen"),
course administration (grading, schedules, homework logistics), personal
identifiable information, verbatim repetitions, and filler.

## Markdown conventions

- `# Title` (one, first line) → `## Section` → `### Subsection`; `#### Detail`
  sparingly.
- **Bold** for terms on first introduction; bulleted lists for enumerations;
  numbered lists only for ordered procedures.
- `> Blockquote` for definitions, theorems, and key takeaways.
- Fenced code blocks with language tags for code. Tables for tabular data.

## Math formatting

- Use ONLY dollar delimiters: `$...$` for inline math, `$$...$$` for display
  math. NEVER use `\\(...\\)` or `\\[...\\]` — they break the downstream renderer.
- Display math goes on its own lines: opening `$$` and closing `$$` each on a
  separate line with the formula between them, and a blank line before and
  after the block. Inside a list item, indent the whole `$$...$$` block to the
  item's text level instead of adding blank lines.
- Keep a formula inline (`$...$`) when it is part of a sentence; use a display
  block only for standalone equations worth visual emphasis.
- Do not wrap math in backticks or code blocks, and do not emit unicode
  math symbols (×, ², θ) inside prose when the expression belongs in LaTeX —
  write `$\theta^2$`, not θ².

## Slide images (only when a SLIDE IMAGE INDEX is provided)

Rendered PNGs of the original slides may be available. The index lists, for
every slide: its image path, its number, and how much text was extracted from
it (a low word count usually means the slide is a figure — a diagram, plot,
architecture scheme, or photo).

- Embed a slide image where the visual genuinely helps understanding — the
  text discusses a figure, architecture, plot, or geometric intuition that
  words alone convey poorly. Prefer low-word-count slides; text-only slides
  are already covered by the conspect and must NOT be embedded.
- Insert as a standalone paragraph right after the text it illustrates:
  `![<short caption>](<path from the index>)` — use the path EXACTLY as given
  in the index, and write a caption describing the figure, not "slide N".
- Be selective: at most one image per section, none where nothing visual is
  discussed. An image is an illustration, never a substitute for text.

## Output contract

Return ONLY the finished Markdown document — no preamble, no meta-commentary.
The first line must be the `# Title`. Do not append any closing line (no
"End of conspect", no trailing horizontal rule) — the document simply ends
with its last content section.
"""

USER_TEMPLATE = """\
Build the final lecture conspect from the two sources below.

=== SLIDE CONSPECT (reconstructed from the slides) ===
{slides}

=== SPEECH TRANSCRIPT (ASR, with timestamps) ===
{transcript}"""

SLIDE_INDEX_TEMPLATE = """

=== SLIDE IMAGE INDEX (rendered PNGs available for embedding) ===
{slide_index}"""


# --- LLM call ---------------------------------------------------------------


def _infer_provider(model: str) -> str:
    """Infer the provider from the model name; default is deepseek."""
    m = (model or "").lower()
    if m.startswith("claude") or "anthropic" in m:
        return "anthropic"
    return "deepseek"


class ConspectWriter:
    """Merge transcript + slide conspect into a final Markdown conspect (Claude / DeepSeek)."""

    def __init__(
        self,
        *,
        model: str | None = None,
        provider: str | None = None,
        api_key: str | None = None,
        base_url: str | None = None,
        max_tokens: int = 16_000,
        thinking: bool = True,
    ) -> None:
        from app import config

        self.model = model or config.LLM_MODEL
        self.provider = (provider or config.LLM_PROVIDER or _infer_provider(self.model)).lower()
        self.api_key = api_key
        self.base_url = base_url
        self.max_tokens = max_tokens
        self.thinking = thinking
        self._client = None

    # --- provider clients ----------------------------------------------------

    def _anthropic_client(self):
        if self._client is None:
            from app import config

            try:
                import anthropic
            except ImportError as e:  # pragma: no cover
                raise ImportError("The anthropic SDK is not installed. Install it: pip install anthropic") from e
            self._client = anthropic.Anthropic(api_key=self.api_key or config.ANTHROPIC_API_KEY)
        return self._client

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

    # --- public API ----------------------------------------------------------

    def write(self, transcript_md: str, slides_md: str, slide_index: str | None = None) -> str:
        """Return the final conspect as a Markdown string."""
        user_msg = USER_TEMPLATE.format(
            slides=slides_md.strip() or "(no slides provided)",
            transcript=transcript_md.strip() or "(transcript is empty)",
        )
        if slide_index:
            user_msg += SLIDE_INDEX_TEMPLATE.format(slide_index=slide_index)
        if self.provider == "anthropic":
            content = self._call_anthropic(user_msg)
        elif self.provider == "deepseek":
            content = self._call_deepseek(user_msg)
        else:
            raise ValueError(f"Unknown LLM provider: {self.provider!r} (expected anthropic | deepseek).")
        if not content.strip():
            raise RuntimeError("The model returned an empty conspect.")
        return content.strip() + "\n"

    # --- backends ------------------------------------------------------------

    def _call_anthropic(self, user_msg: str) -> str:
        client = self._anthropic_client()
        kwargs = dict(
            model=self.model,
            max_tokens=self.max_tokens,
            system=SYSTEM_PROMPT,
            messages=[{"role": "user", "content": user_msg}],
        )
        if self.thinking:
            kwargs["thinking"] = {"type": "adaptive"}
        response = client.messages.create(**kwargs)
        text = "".join(block.text for block in response.content if getattr(block, "type", None) == "text")
        if response.stop_reason == "max_tokens":
            print(
                f"           WARNING: conspect hit the {self.max_tokens}-token limit and may be "
                "truncated — raise max_tokens for this lecture."
            )
        return text

    def _call_deepseek(self, user_msg: str) -> str:
        client = self._deepseek_client()
        response = client.chat.completions.create(
            model=self.model,
            max_tokens=self.max_tokens,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_msg},
            ],
        )
        choice = response.choices[0]
        if choice.finish_reason == "length":
            print(
                f"           WARNING: conspect hit the {self.max_tokens}-token limit and may be "
                "truncated — raise max_tokens for this lecture."
            )
        return choice.message.content or ""


def write_conspect(transcript_md: str, slides_md: str, slide_index: str | None = None, **kwargs) -> str:
    """Convenience wrapper: a single call without explicitly creating a ConspectWriter."""
    return ConspectWriter(**kwargs).write(transcript_md, slides_md, slide_index)


# --- pipeline --------------------------------------------------------------


def _read_sources(lecture_dir: Path, stt_provider: str, *, baseline: bool = False) -> tuple[str, str]:
    """Load (transcript_md, slides_md) for a lecture directory.

    Prefers the LLM-cleaned ``transcription_reconstructed.md`` (see
    ``app.reconstruct_transcript``) over the raw ASR output.

    ``baseline=True`` forces the baseline sources: the raw ASR
    ``transcription.md`` and the raw extracted ``slides.md``.
    """
    if baseline:
        transcript_path = lecture_dir / stt_provider / "transcription.md"
        if not transcript_path.exists():
            raise FileNotFoundError(
                f"No transcript at {transcript_path} — run `python -m app.transcribe {lecture_dir}` first."
            )
        slides_path = lecture_dir / "slides_extracted" / "slides.md"
        if not slides_path.exists():
            raise FileNotFoundError(f"No raw slides at {slides_path} — run `python -m app.extract_slides` first.")
        return transcript_path.read_text(encoding="utf-8"), slides_path.read_text(encoding="utf-8")

    transcript_path = lecture_dir / stt_provider / "transcription_reconstructed.md"
    if not transcript_path.exists():
        transcript_path = lecture_dir / stt_provider / "transcription.md"
        if transcript_path.exists():
            print(
                "           NOTE: no transcription_reconstructed.md — using the raw transcript "
                f"(run `python -m app.reconstruct_transcript {lecture_dir}` for a cleaned one)"
            )
        else:
            raise FileNotFoundError(
                f"No transcript at {transcript_path} — run `python -m app.transcribe {lecture_dir}` first."
            )

    slides_dir = lecture_dir / "slides_extracted"
    slides_path = slides_dir / "slides_reconstructed.md"
    if not slides_path.exists():
        fallback = slides_dir / "slides.md"
        if fallback.exists():
            print(f"           WARNING: no slides_reconstructed.md, falling back to raw {fallback.name}")
            slides_path = fallback
        else:
            raise FileNotFoundError(
                f"No slides in {slides_dir} — run `python -m app.extract_slides {lecture_dir}` first."
            )

    return transcript_path.read_text(encoding="utf-8"), slides_path.read_text(encoding="utf-8")


def process_lecture(
    lecture_dir: Path,
    *,
    stt_provider: str = "whisper_cpp",
    model: str | None = None,
    provider: str | None = None,
    max_tokens: int = 16_000,
    baseline: bool = False,
) -> Path:
    """``baseline=True`` rebuilds the low-effort baseline conspect: raw ASR
    transcript + raw extracted slide text, no slide images, written to
    ``conspect_baseline.md`` (the main ``conspect.md`` is left untouched)."""
    transcript_md, slides_md = _read_sources(lecture_dir, stt_provider, baseline=baseline)

    # Render slide PNGs (pdftoppm) so the conspect can embed figure-heavy slides.
    slide_index = None
    if not baseline:
        try:
            if render_slide_images(lecture_dir) is not None:
                slide_index = build_slide_index(lecture_dir)
        except RuntimeError as e:
            print(f"           WARNING: slide images skipped ({e})")

    writer = ConspectWriter(model=model, provider=provider, max_tokens=max_tokens)
    print(
        f"[{lecture_dir.name}] writing {'baseline ' if baseline else ''}conspect "
        f"({writer.provider}:{writer.model}, stt={stt_provider}, images={'yes' if slide_index else 'no'}) …"
    )
    t0 = time.monotonic()
    conspect = writer.write(transcript_md, slides_md, slide_index)
    dt = time.monotonic() - t0

    out_path = lecture_dir / ("conspect_baseline.md" if baseline else "conspect.md")
    out_path.write_text(conspect, encoding="utf-8")
    print(f"           {dt:.0f}s wall -> {out_path}")
    return out_path


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Transcript + reconstructed slides → final Markdown conspect")
    parser.add_argument(
        "lectures",
        nargs="+",
        help="One or more lecture directories (each must contain <stt>/transcription.md and slides_extracted/)",
    )
    parser.add_argument(
        "--stt",
        default="whisper_cpp",
        choices=["whisper_cpp", "google_stt"],
        help="Which STT provider's transcript to use (default: whisper_cpp)",
    )
    parser.add_argument(
        "--model",
        default=None,
        help="LLM model (default from config, e.g. deepseek-v4-pro or claude-opus-4-8)",
    )
    parser.add_argument(
        "--provider",
        default=None,
        choices=["anthropic", "deepseek"],
        help="LLM provider (default: from config / inferred from the model name)",
    )
    parser.add_argument(
        "--max-tokens",
        type=int,
        default=16_000,
        help="Output token limit for the conspect (default: 16000)",
    )
    parser.add_argument(
        "--baseline",
        action="store_true",
        help="Baseline conspect: raw transcription.md + raw slides.md, no images, -> conspect_baseline.md",
    )
    args = parser.parse_args(argv)

    for lec in args.lectures:
        lecture_dir = Path(lec).resolve()
        process_lecture(
            lecture_dir,
            stt_provider=args.stt,
            model=args.model,
            provider=args.provider,
            max_tokens=args.max_tokens,
            baseline=args.baseline,
        )

    print("Done.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
