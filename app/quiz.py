"""Lecture quiz: conspect.md → quiz.json with single-choice questions.

For each lecture directory this takes the final study conspect produced by
``app.conspect`` (``<lecture-dir>/conspect.md``) and generates a self-check
quiz with one LLM call: 5 single-choice questions, each with 4 options and a
per-option explanation of why it is correct or incorrect. Every question is
grounded strictly in the conspect — no outside facts. The result is validated
against a pydantic schema (exactly one correct option per question) and saved
to ``<lecture-dir>/quiz.json``.

    python -m app.quiz data/deep-learning-and-computer-vision/lecture-01
    python -m app.quiz <lecture-dir> ... --model claude-opus-4-8 --questions 5

Programmatic use: ``generate_quiz(conspect_md)`` → ``Quiz``.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

from pydantic import BaseModel, Field, model_validator

from app.summarize.prompts import JSON_FORMAT_INSTRUCTION

DEFAULT_NUM_QUESTIONS = 5
NUM_OPTIONS = 4

# Anti length-leak guard: without it the LLM writes correct options ~1.6x longer
# than distractors, so "pick the longest option" scored ~78% on generated quizzes.
LENGTH_LEAK_MARGIN = 1.30  # correct option may exceed the longest distractor by at most 30%
MAX_LONGEST_CORRECT_SHARE = 0.5  # at most half the questions may have the correct option strictly longest
MAX_LLM_ATTEMPTS = 5

# --- schema ------------------------------------------------------------------


class QuizOption(BaseModel):
    text: str = Field(description="The answer option as shown to the student.")
    is_correct: bool = Field(description="Whether this option is the single correct answer.")
    explanation: str = Field(
        description=(
            "Why this option is correct or incorrect, grounded in the conspect. "
            "For incorrect options, name the specific misconception or mix-up."
        )
    )


class QuizQuestion(BaseModel):
    question: str = Field(description="The question stem. Self-contained, answerable from the conspect alone.")
    options: list[QuizOption] = Field(description=f"Exactly {NUM_OPTIONS} answer options, exactly one correct.")

    @model_validator(mode="after")
    def _exactly_one_correct(self) -> QuizQuestion:
        correct = sum(1 for o in self.options if o.is_correct)
        if correct != 1:
            raise ValueError(f"a single-choice question must have exactly 1 correct option, got {correct}")
        return self

    @model_validator(mode="after")
    def _no_length_leak(self) -> QuizQuestion:
        wrong_lens = [len(o.text) for o in self.options if not o.is_correct]
        correct_len = next(len(o.text) for o in self.options if o.is_correct)
        if wrong_lens and correct_len > LENGTH_LEAK_MARGIN * max(wrong_lens):
            raise ValueError(
                f"length leak in question {self.question!r}: the correct option is {correct_len} chars, "
                f"the longest distractor only {max(wrong_lens)} — shorten the correct option or make the "
                f"distractors equally detailed (all options within roughly ±20% of each other)"
            )
        return self

    def correct_is_strictly_longest(self) -> bool:
        wrong_lens = [len(o.text) for o in self.options if not o.is_correct]
        correct_len = next(len(o.text) for o in self.options if o.is_correct)
        return bool(wrong_lens) and correct_len > max(wrong_lens)


class Quiz(BaseModel):
    """Self-check quiz for one lecture conspect."""

    title: str = Field(description="Title of the lecture the quiz is based on.")
    questions: list[QuizQuestion] = Field(description="The quiz questions in conspect order.")

    @model_validator(mode="after")
    def _no_systematic_length_leak(self) -> Quiz:
        offenders = [q.question for q in self.questions if q.correct_is_strictly_longest()]
        if len(offenders) > len(self.questions) * MAX_LONGEST_CORRECT_SHARE:
            raise ValueError(
                f"length leak: the correct option is the longest one in {len(offenders)} of "
                f"{len(self.questions)} questions ({'; '.join(repr(q) for q in offenders)}) — "
                f"a student picking the longest option would beat chance; rebalance option lengths"
            )
        return self


# --- prompts -----------------------------------------------------------------

SYSTEM_PROMPT = """\
You are an expert university instructor writing a self-check quiz for a lecture.
Your only source is the lecture conspect the student has just studied.

## Question design

- Write single-choice questions: exactly {num_options} options each, exactly ONE correct.
- Cover the conspect broadly: different sections, not several questions about
  the same paragraph. Within each section quiz its core ideas, not asides,
  examples, or anecdotes. Order questions to follow the conspect.
- Test understanding of the FUNDAMENTALS: definitions, mechanisms, why a
  method works, its assumptions, trade-offs, and when to apply it. Prefer
  "why / what follows / which is an example of" over recall; include at most
  one pure recall question.
- Never quiz historical narrative or attribution: who proposed, said, or
  discovered something, in which year or paper, what motivated a researcher,
  or which architecture "introduced" a trick — unless that fact is itself the
  section's central claim. A person's name may appear only as part of a
  method's established name ("Bahdanau attention"), never as the thing being
  tested.
- Distractors must be plausible: real misconceptions, adjacent concepts from
  the same conspect, or common mix-ups — never absurd or joke options, and
  never options a student could eliminate without knowing the material.
- Avoid "all/none of the above" and options that give away the answer by
  length or level of detail.
- Balance option lengths — enforced by an automatic validator with hard
  numeric limits:
  * within a question the correct option must never be more than 30% longer
    (in characters) than the longest distractor;
  * across the quiz the correct option may be the single longest one in at
    most half of the questions.
  Put extra precision, hedges, and caveats into the explanation, not the
  option text. When in doubt, make the correct option one of the SHORTEST
  options and expand the distractors to match. Before returning, compare the
  character lengths of the options in every question and rebalance where the
  correct one stands out.

## Explanations

For EVERY option write an explanation:
- for the correct option — why it is right, referring to the relevant idea of
  the conspect;
- for each incorrect option — why a student might pick it and what exactly
  makes it wrong.

## Grounding

- Every question and every explanation must be answerable from the conspect
  alone. Do NOT use outside knowledge, do NOT invent facts.
- Write the quiz in the same language as the conspect; keep established
  English technical terms as-is.
"""

USER_TEMPLATE = """\
Write a quiz of exactly {num_questions} single-choice questions ({num_options} options each) \
based on the lecture conspect below.

=== LECTURE CONSPECT ===
{conspect}"""


# --- LLM call ----------------------------------------------------------------


def _infer_provider(model: str) -> str:
    """Infer the provider from the model name; default is deepseek."""
    m = (model or "").lower()
    if m.startswith("claude") or "anthropic" in m:
        return "anthropic"
    return "deepseek"


class QuizGenerator:
    """Generate a single-choice quiz from a lecture conspect (Claude / DeepSeek)."""

    def __init__(
        self,
        *,
        model: str | None = None,
        provider: str | None = None,
        api_key: str | None = None,
        base_url: str | None = None,
        max_tokens: int = 32_000,
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

    # --- public API ------------------------------------------------------------

    def generate(self, conspect_md: str, *, num_questions: int = DEFAULT_NUM_QUESTIONS) -> Quiz:
        """Return a validated quiz built from the conspect Markdown."""
        if not conspect_md.strip():
            raise ValueError("The conspect is empty — nothing to build a quiz from.")
        system = SYSTEM_PROMPT.format(num_options=NUM_OPTIONS)
        user_msg = USER_TEMPLATE.format(
            num_questions=num_questions,
            num_options=NUM_OPTIONS,
            conspect=conspect_md.strip(),
        )

        quiz = self.complete_structured(system, user_msg, Quiz)

        if len(quiz.questions) != num_questions:
            print(f"           WARNING: asked for {num_questions} questions, the model returned {len(quiz.questions)}")
        return quiz

    def complete_structured[T: BaseModel](self, system: str, user_msg: str, schema: type[T]) -> T:
        """Structured-output LLM call: the response must validate against `schema`.

        Shared by quiz generation, the adaptive regeneration loop (app.quality),
        and the E1 claim decomposition / entailment judge (app.e1). A response
        that fails validation (schema mismatch or the anti-length-leak
        validators) is retried up to MAX_LLM_ATTEMPTS times with the validator
        error fed back to the model.
        """
        if self.provider == "anthropic":
            complete = self._complete_anthropic
        elif self.provider == "deepseek":
            complete = self._complete_deepseek
        else:
            raise ValueError(f"Unknown LLM provider: {self.provider!r} (expected anthropic | deepseek).")

        msg = user_msg
        last_err: Exception | None = None
        for attempt in range(1, MAX_LLM_ATTEMPTS + 1):
            try:
                return complete(system, msg, schema)
            except (ValueError, RuntimeError) as e:  # pydantic.ValidationError is a ValueError
                last_err = e
                if attempt < MAX_LLM_ATTEMPTS:
                    print(f"           attempt {attempt}/{MAX_LLM_ATTEMPTS} rejected, retrying: {e}")
                msg = (
                    user_msg
                    + "\n\n=== PREVIOUS ATTEMPT REJECTED ===\n"
                    + f"Your previous response was rejected by the validator:\n{e}\n"
                    + "Return a corrected response that satisfies every constraint."
                )
        raise RuntimeError(f"LLM response failed validation after {MAX_LLM_ATTEMPTS} attempts") from last_err

    # --- backends --------------------------------------------------------------

    def _complete_anthropic[T: BaseModel](self, system: str, user_msg: str, schema: type[T]) -> T:
        client = self._anthropic_client()
        kwargs = dict(
            model=self.model,
            max_tokens=self.max_tokens,
            system=system,
            messages=[{"role": "user", "content": user_msg}],
            output_format=schema,
        )
        if self.thinking:
            kwargs["thinking"] = {"type": "adaptive"}
        response = client.messages.parse(**kwargs)
        if response.parsed_output is None:
            raise RuntimeError(f"The model did not return a valid quiz (stop_reason={response.stop_reason!r}).")
        return response.parsed_output

    def _complete_deepseek[T: BaseModel](self, system: str, user_msg: str, schema: type[T]) -> T:
        client = self._deepseek_client()
        schema_json = json.dumps(schema.model_json_schema(), ensure_ascii=False, indent=2)
        system = system + "\n\n" + JSON_FORMAT_INSTRUCTION.format(schema=schema_json)

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
            return schema.model_validate_json(content)
        except Exception as e:  # noqa: BLE001 — wrap it for a clearer error
            raise RuntimeError(f"DeepSeek returned JSON that does not match the quiz schema: {e}") from e


def generate_quiz(conspect_md: str, *, num_questions: int = DEFAULT_NUM_QUESTIONS, **kwargs) -> Quiz:
    """Convenience wrapper: a single call without explicitly creating a QuizGenerator."""
    return QuizGenerator(**kwargs).generate(conspect_md, num_questions=num_questions)


# --- pipeline ----------------------------------------------------------------


def process_lecture(
    lecture_dir: Path,
    *,
    num_questions: int = DEFAULT_NUM_QUESTIONS,
    model: str | None = None,
    provider: str | None = None,
    max_tokens: int = 32_000,
) -> Path:
    conspect_path = lecture_dir / "conspect.md"
    if not conspect_path.exists():
        raise FileNotFoundError(f"No conspect at {conspect_path} — run `python -m app.conspect {lecture_dir}` first.")
    conspect_md = conspect_path.read_text(encoding="utf-8")

    generator = QuizGenerator(model=model, provider=provider, max_tokens=max_tokens)
    print(f"[{lecture_dir.name}] generating quiz ({generator.provider}:{generator.model}, {num_questions} questions) …")
    t0 = time.monotonic()
    quiz = generator.generate(conspect_md, num_questions=num_questions)
    dt = time.monotonic() - t0

    out_path = lecture_dir / "quiz.json"
    out_path.write_text(
        json.dumps(quiz.model_dump(), ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"           {dt:.0f}s wall -> {out_path}")
    return out_path


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Lecture conspect → single-choice quiz (quiz.json)")
    parser.add_argument(
        "lectures",
        nargs="+",
        help="One or more lecture directories (each must contain conspect.md)",
    )
    parser.add_argument(
        "--questions",
        type=int,
        default=DEFAULT_NUM_QUESTIONS,
        help=f"Number of questions to generate (default: {DEFAULT_NUM_QUESTIONS})",
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
        default=32_000,
        help="Output token limit for the quiz (default: 32000)",
    )
    args = parser.parse_args(argv)

    for lec in args.lectures:
        lecture_dir = Path(lec).resolve()
        process_lecture(
            lecture_dir,
            num_questions=args.questions,
            model=args.model,
            provider=args.provider,
            max_tokens=args.max_tokens,
        )

    print("Done.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
