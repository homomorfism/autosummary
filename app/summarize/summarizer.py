"""Summarization module.

Input is a transcript (a `Transcript` object or text) and the slide text
(`SlideDeck` or a string). Output is a structured summary `SummaryConcept`,
where every statement is grounded in a source.

Two LLM providers are supported:

* **anthropic** — Claude. A single `client.messages.parse` call with structured
  outputs: the model must return JSON exactly matching the pydantic schema
  (validation happens on the SDK side). Adaptive thinking is used.
* **deepseek** — DeepSeek via the OpenAI-compatible API. We ask for a JSON object
  strictly matching the JSON Schema (the schema is in the system prompt) and do
  the parsing and validation ourselves via pydantic.

The provider is chosen explicitly (`provider=` / `LLM_PROVIDER`) or inferred from
the model name: `claude-*` -> anthropic, `deepseek-*` -> deepseek. The default is
deepseek with the model `deepseek-v4-pro`.
"""

from __future__ import annotations

import json
from typing import TYPE_CHECKING

from app.summarize.prompts import JSON_FORMAT_INSTRUCTION, SYSTEM_PROMPT, USER_TEMPLATE
from app.summarize.schema import SummaryConcept

if TYPE_CHECKING:  # for type hints without a hard dependency
    from app.slides import SlideDeck
    from app.stt.base import Transcript

# maximum number of seconds to show in a segment timestamp
_MAX_TS = 10  # this many characters is enough


def _format_transcript(transcript: Transcript | str) -> str:
    """Render the transcript as text with per-segment timestamps."""
    if isinstance(transcript, str):
        return transcript
    lines: list[str] = []
    for seg in transcript.segments:
        text = (seg.text or "").strip()
        if not text:
            continue
        if seg.start is not None:
            lines.append(f"[{seg.start:.1f}s] {text}")
        else:
            lines.append(text)
    if not lines and transcript.text:
        return transcript.text
    return "\n".join(lines)


def _format_slides(slides: SlideDeck | str) -> str:
    if isinstance(slides, str):
        return slides
    return slides.full_text


def _infer_provider(model: str) -> str:
    """Infer the provider from the model name; default is deepseek."""
    m = (model or "").lower()
    if m.startswith("claude") or "anthropic" in m:
        return "anthropic"
    if m.startswith("deepseek"):
        return "deepseek"
    return "deepseek"


class Summarizer:
    """Multi-source summarizer (Claude / DeepSeek)."""

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
            # api_key=None -> the SDK reads ANTHROPIC_API_KEY from the environment
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

    def summarize(
        self,
        transcript: Transcript | str,
        slides: SlideDeck | str,
    ) -> SummaryConcept:
        """Build a structured summary from the transcript and slides."""
        transcript_text = _format_transcript(transcript)
        slides_text = _format_slides(slides) or "(no slides provided)"

        user_msg = USER_TEMPLATE.format(
            slides=slides_text,
            transcript=transcript_text or "(transcript is empty)",
        )

        if self.provider == "anthropic":
            return self._summarize_anthropic(user_msg)
        if self.provider == "deepseek":
            return self._summarize_deepseek(user_msg)
        raise ValueError(f"Unknown LLM provider: {self.provider!r} (expected anthropic | deepseek).")

    # --- backends ------------------------------------------------------------

    def _summarize_anthropic(self, user_msg: str) -> SummaryConcept:
        client = self._anthropic_client()
        kwargs = dict(
            model=self.model,
            max_tokens=self.max_tokens,
            system=SYSTEM_PROMPT,
            messages=[{"role": "user", "content": user_msg}],
            output_format=SummaryConcept,
        )
        if self.thinking:
            # adaptive thinking is the recommended mode for opus-4-8
            kwargs["thinking"] = {"type": "adaptive"}

        response = client.messages.parse(**kwargs)
        if response.parsed_output is None:
            raise RuntimeError(f"The model did not return a valid summary (stop_reason={response.stop_reason!r}).")
        return response.parsed_output

    def _summarize_deepseek(self, user_msg: str) -> SummaryConcept:
        client = self._deepseek_client()
        schema_json = json.dumps(SummaryConcept.model_json_schema(), ensure_ascii=False, indent=2)
        system = SYSTEM_PROMPT + "\n\n" + JSON_FORMAT_INSTRUCTION.format(schema=schema_json)

        response = client.chat.completions.create(
            model=self.model,
            max_tokens=self.max_tokens,
            response_format={"type": "json_object"},
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user_msg},
            ],
        )
        content = (response.choices[0].message.content or "").strip()
        if not content:
            raise RuntimeError("DeepSeek returned an empty response.")
        try:
            return SummaryConcept.model_validate_json(content)
        except Exception as e:  # noqa: BLE001 — wrap it for a clearer error
            raise RuntimeError(f"DeepSeek returned JSON that does not match the summary schema: {e}") from e


def summarize(
    transcript: Transcript | str,
    slides: SlideDeck | str,
    **kwargs,
) -> SummaryConcept:
    """Convenience wrapper: a single call without explicitly creating a Summarizer."""
    return Summarizer(**kwargs).summarize(transcript, slides)
