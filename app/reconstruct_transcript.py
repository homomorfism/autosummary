"""Reconstructed transcript: raw ASR → clean timestamped lecture text, no summarizing.

For each lecture directory this takes ``<lecture-dir>/<stt-provider>/transcription.md``
(the timestamped ASR transcript, see ``app.transcribe``) and rewrites it with an
LLM into ``<lecture-dir>/<stt-provider>/transcription_reconstructed.md``: the same
spoken content at full detail, but without the "water" — filler, false starts,
greetings, course administration, off-topic Q&A and anecdotes, stray
foreign-language speech — and with obvious recognition errors repaired from
context and spoken math rendered as LaTeX.

This is a *cleaning* pass, not a summary: every substantive statement must
survive. The output keeps the ``**[HH:MM:SS]**`` paragraph timestamps so both
downstream consumers work unchanged — ``app.conspect`` (section timestamps) and
``app.e1`` (claim decomposition strips the markers).

The transcript is processed in ~2000-word chunks (segment boundaries preserved)
with concurrent LLM calls; a chunk whose output hits the completion cap is
split in half and retried.

    python -m app.reconstruct_transcript data/deep-learning-and-computer-vision/lecture-06
    python -m app.reconstruct_transcript <lecture-dir> --stt google_stt --model claude-opus-4-8
"""

from __future__ import annotations

import argparse
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

DEFAULT_CHUNK_WORDS = 2_000
DEFAULT_MAX_TOKENS = 16_000
DEFAULT_WORKERS = 4

# --- prompts ---------------------------------------------------------------

SYSTEM_PROMPT = """\
You are an expert academic editor. You receive a chunk of a raw automatic
speech recognition (ASR) transcript of a university lecture, split into
timestamped segments. Rewrite it into clean, readable lecture text.

This is a CLEANING pass, NOT a summary: every substantive statement of the
lecturer must survive at full detail. Compress wording, never ideas.

## Keep (verbatim in meaning, lightly cleaned in wording)

Definitions, theorems, formulas, mechanisms and how they work, reasons and
intuitions, worked examples, numbers, comparisons, historical facts about the
material, practical advice, warnings, common mistakes, and anything the
lecturer flags as important — keep that emphasis in the text.

## Remove entirely

- greetings, small talk, course administration (grading, schedules, homework
  logistics), technical difficulties ("can you see my screen");
- audience interaction and question-and-answer exchanges that do not add
  material content (when an answer DOES explain the material, keep the
  explanation as regular text);
- personal stories, jokes, and anecdotes not part of the taught material;
- speech in a language other than the lecture's main language, unless it
  clearly states lecture content;
- filler words, false starts, self-corrections, and verbatim repetitions.

## Repair

- Fix obvious ASR errors from context (misheard technical terms, broken names
  of methods and people); if a passage is unintelligible, drop it rather than
  guess.
- Render spoken mathematics as LaTeX with dollar delimiters ("p of x given
  theta" → $p(x \\mid \\theta)$). Never use \\(...\\) or \\[...\\].

## Format

- Merge the segments into coherent paragraphs following the lecture's flow.
- Start every paragraph with the timestamp of its first source segment in the
  original bold form: `**[HH:MM:SS]** text…` — one paragraph per line, a blank
  line between paragraphs, no headings or lists.
- Keep the language of the lecture; keep established English technical terms
  as-is.

Return ONLY the cleaned transcript text — no preamble, no meta-commentary."""

USER_TEMPLATE = """\
Clean the following transcript chunk.{part_note}

=== TRANSCRIPT CHUNK ===
{text}"""


# --- LLM call ---------------------------------------------------------------


def _infer_provider(model: str) -> str:
    """Infer the provider from the model name; default is deepseek."""
    m = (model or "").lower()
    if m.startswith("claude") or "anthropic" in m:
        return "anthropic"
    return "deepseek"


class TranscriptReconstructor:
    """Rewrite raw ASR transcript chunks into clean lecture text (Claude / DeepSeek)."""

    def __init__(
        self,
        *,
        model: str | None = None,
        provider: str | None = None,
        api_key: str | None = None,
        base_url: str | None = None,
        max_tokens: int = DEFAULT_MAX_TOKENS,
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

    def _ensure_client(self) -> None:
        if self.provider == "anthropic":
            self._anthropic_client()
        else:
            self._deepseek_client()

    # --- public API ----------------------------------------------------------

    def reconstruct_chunk(self, chunk: str, part_note: str = "") -> str:
        """Clean one transcript chunk; returns the cleaned Markdown text."""
        user_msg = USER_TEMPLATE.format(part_note=part_note, text=chunk)
        if self.provider == "anthropic":
            text, truncated = self._call_anthropic(user_msg)
        elif self.provider == "deepseek":
            text, truncated = self._call_deepseek(user_msg)
        else:
            raise ValueError(f"Unknown LLM provider: {self.provider!r} (expected anthropic | deepseek).")
        if truncated:
            # Hit the completion cap — either the reasoning model spent the whole
            # budget thinking, or the chunk's clean text alone exceeds the cap.
            # Halve and retry.
            lines = [line for line in chunk.splitlines() if line.strip()]
            if len(lines) < 2:
                raise RuntimeError("A transcript chunk could not be reconstructed even as a single segment.")
            mid = len(lines) // 2
            print("           NOTE: a chunk came back truncated — splitting it in half")
            parts = [self.reconstruct_chunk("\n".join(part), part_note) for part in (lines[:mid], lines[mid:])]
            return "\n\n".join(p for p in parts if p)
        # A non-truncated empty response is legitimate: the whole chunk was
        # removable filler (greetings, sign-off, admin talk).
        return text.strip()

    # --- backends ------------------------------------------------------------

    def _call_anthropic(self, user_msg: str) -> tuple[str, bool]:
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
        return text, response.stop_reason == "max_tokens"

    def _call_deepseek(self, user_msg: str) -> tuple[str, bool]:
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
        return choice.message.content or "", choice.finish_reason == "length"


# --- pipeline --------------------------------------------------------------


def _segments_only(text: str) -> str:
    """Keep only the timestamped `## Segments` body of a transcription.md.

    The file ends with a `## Full text` section that repeats the whole lecture
    without timestamps; feeding it to the LLM produces a hallucinated summary
    with invented timestamps appended to the output.
    """
    start = text.find("## Segments")
    if start != -1:
        text = text[start + len("## Segments") :]
    end = text.find("## Full text")
    if end != -1:
        text = text[:end]
    return text.strip()


def _chunk_lines(text: str, max_words: int) -> list[str]:
    """Split on line (segment) boundaries into chunks of roughly `max_words` words."""
    chunks: list[str] = []
    current: list[str] = []
    count = 0
    for line in text.splitlines():
        words = len(line.split())
        if current and count + words > max_words:
            chunks.append("\n".join(current))
            current, count = [], 0
        current.append(line)
        count += words
    if current:
        chunks.append("\n".join(current))
    return [c for c in chunks if c.strip()]


def process_lecture(
    lecture_dir: Path,
    *,
    stt_provider: str = "whisper_cpp",
    model: str | None = None,
    provider: str | None = None,
    max_tokens: int = DEFAULT_MAX_TOKENS,
    chunk_words: int = DEFAULT_CHUNK_WORDS,
    workers: int = DEFAULT_WORKERS,
) -> Path:
    transcript_path = lecture_dir / stt_provider / "transcription.md"
    if not transcript_path.exists():
        raise FileNotFoundError(
            f"No transcript at {transcript_path} — run `python -m app.transcribe {lecture_dir}` first."
        )

    reconstructor = TranscriptReconstructor(model=model, provider=provider, max_tokens=max_tokens)
    chunks = _chunk_lines(_segments_only(transcript_path.read_text(encoding="utf-8")), chunk_words)
    print(
        f"[{lecture_dir.name}] reconstructing transcript ({reconstructor.provider}:{reconstructor.model}, "
        f"stt={stt_provider}, {len(chunks)} chunk(s), workers={workers}) …"
    )
    t0 = time.monotonic()

    def one(args: tuple[int, str]) -> str:
        i, chunk = args
        part_note = f" This is part {i + 1} of {len(chunks)} of the transcript." if len(chunks) > 1 else ""
        return reconstructor.reconstruct_chunk(chunk, part_note)

    reconstructor._ensure_client()  # noqa: SLF001 — build once so threads don't race
    with ThreadPoolExecutor(max_workers=workers) as pool:
        parts = list(pool.map(one, enumerate(chunks)))

    out_path = lecture_dir / stt_provider / "transcription_reconstructed.md"
    out_path.write_text("\n\n".join(parts) + "\n", encoding="utf-8")
    print(f"           {time.monotonic() - t0:.0f}s wall -> {out_path}")
    return out_path


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Raw ASR transcript → clean timestamped lecture text (no summarizing)")
    parser.add_argument(
        "lectures",
        nargs="+",
        help="One or more lecture directories (each must contain <stt>/transcription.md)",
    )
    parser.add_argument(
        "--stt",
        default="whisper_cpp",
        choices=["whisper_cpp", "google_stt"],
        help="Which STT provider's transcript to reconstruct (default: whisper_cpp)",
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
        default=DEFAULT_MAX_TOKENS,
        help=f"Output token limit per chunk (default: {DEFAULT_MAX_TOKENS})",
    )
    parser.add_argument(
        "--chunk-words",
        type=int,
        default=DEFAULT_CHUNK_WORDS,
        help=f"Words per LLM call (default: {DEFAULT_CHUNK_WORDS})",
    )
    parser.add_argument("--workers", type=int, default=DEFAULT_WORKERS, help="Concurrent LLM calls (default: 4)")
    args = parser.parse_args(argv)

    for lec in args.lectures:
        process_lecture(
            Path(lec).resolve(),
            stt_provider=args.stt,
            model=args.model,
            provider=args.provider,
            max_tokens=args.max_tokens,
            chunk_words=args.chunk_words,
            workers=args.workers,
        )

    print("Done.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
