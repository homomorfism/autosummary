"""Question psychometrics (experiment E3): item analysis + closed-loop repair.

For every quiz question, computed from the attempts stored in the results DB
(see ``app.db``, filled by the ``web/`` Next.js quiz app):

* **difficulty (p-value)** — the share of respondents who answered correctly;
* **discrimination (point-biserial)** — the correlation between getting the
  item right and the *rest score* (attempt score excluding the item itself,
  so the item does not correlate with its own contribution).

The **rejection rule** flags questions with enough data (``--min-attempts``)
whose difficulty falls outside the target range (``--p-range``, default
0.30–0.85) or whose discrimination is below ``--min-rpb`` (default 0.15).
``--retire`` removes flagged questions from ``quiz.json`` and archives them
(with their statistics) in the DB. ``--regenerate`` additionally asks the LLM
for replacements: the prompt carries the retired questions, their measured
statistics and the miss direction ("too easy → make it harder"), closing the
generate → measure → retire → regenerate loop.

    python -m app.quality data/<course>/<lecture>                # report only
    python -m app.quality data/<course>/<lecture> --retire       # apply rejection rule
    python -m app.quality data/<course>/<lecture> --regenerate   # retire + replace via LLM

Caveat (per TODO): with n≈15 respondents these statistics are noisy — the
methodology matters more than significance; thresholds are deliberately soft.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from dataclasses import dataclass
from pathlib import Path

from pydantic import BaseModel, Field

from app import db
from app.quiz import NUM_OPTIONS, Quiz, QuizGenerator, QuizQuestion

# Rejection-rule defaults. The p-value window is the classic "informative item"
# range: below it the item is frustration, above it everyone gets it for free.
TARGET_P_RANGE = (0.30, 0.85)
MIN_POINT_BISERIAL = 0.15
MIN_ATTEMPTS = 5

# --- item statistics ---------------------------------------------------------


@dataclass
class ItemStats:
    """Psychometric statistics of one quiz question."""

    question_id: str
    question: str
    n: int  # number of respondents who saw the item
    p_value: float | None  # difficulty: share of correct answers
    point_biserial: float | None  # discrimination vs the rest score
    status: str = "ok"  # ok | too_easy | too_hard | low_discrimination | insufficient_data
    reason: str = ""


def _point_biserial(item_correct: list[int], rest_scores: list[float]) -> float | None:
    """Point-biserial correlation between item correctness (0/1) and the rest score.

    Returns None when undefined: no variance in the item (p=0 or p=1) or in the
    rest scores.
    """
    n = len(item_correct)
    p = sum(item_correct) / n
    if p in (0.0, 1.0):
        return None
    mean_rest = sum(rest_scores) / n
    var_rest = sum((s - mean_rest) ** 2 for s in rest_scores) / n
    if var_rest == 0:
        return None
    m1 = sum(s for s, c in zip(rest_scores, item_correct, strict=True) if c) / sum(item_correct)
    m0 = sum(s for s, c in zip(rest_scores, item_correct, strict=True) if not c) / (n - sum(item_correct))
    return (m1 - m0) / math.sqrt(var_rest) * math.sqrt(p * (1 - p))


def compute_item_stats(course: str, lecture: str, *, db_path: Path | None = None) -> list[ItemStats]:
    """Difficulty and discrimination for every question with recorded answers."""
    responses = db.load_responses(course, lecture, db_path=db_path)
    by_question: dict[str, list[dict]] = {}
    for r in responses:
        by_question.setdefault(r["question_id"], []).append(r)

    stats: list[ItemStats] = []
    for qid, rows in by_question.items():
        correct = [int(r["is_correct"]) for r in rows]
        # rest score = attempt score minus this item's own contribution
        rest = [float(r["score"] - r["is_correct"]) for r in rows]
        n = len(rows)
        stats.append(
            ItemStats(
                question_id=qid,
                question=rows[0]["question"],
                n=n,
                p_value=sum(correct) / n,
                point_biserial=_point_biserial(correct, rest),
            )
        )
    return stats


def apply_rejection_rule(
    stats: list[ItemStats],
    *,
    p_range: tuple[float, float] = TARGET_P_RANGE,
    min_rpb: float = MIN_POINT_BISERIAL,
    min_attempts: int = MIN_ATTEMPTS,
) -> list[ItemStats]:
    """Set status/reason on every item; returns the same list for chaining."""
    p_lo, p_hi = p_range
    for s in stats:
        if s.n < min_attempts:
            s.status = "insufficient_data"
            s.reason = f"only {s.n} attempts (< {min_attempts}) — keep collecting"
        elif s.p_value < p_lo:
            s.status = "too_hard"
            s.reason = f"p={s.p_value:.2f} < {p_lo:.2f} — almost nobody answers correctly"
        elif s.p_value > p_hi:
            s.status = "too_easy"
            s.reason = f"p={s.p_value:.2f} > {p_hi:.2f} — almost everybody answers correctly"
        elif s.point_biserial is not None and s.point_biserial < min_rpb:
            s.status = "low_discrimination"
            s.reason = f"r_pb={s.point_biserial:.2f} < {min_rpb:.2f} — does not separate strong from weak"
        else:
            s.status = "ok"
            s.reason = ""
    return stats


def flagged_items(stats: list[ItemStats]) -> list[ItemStats]:
    """Items the rejection rule condemns (insufficient data is NOT a flag)."""
    return [s for s in stats if s.status in ("too_easy", "too_hard", "low_discrimination")]


# --- adaptive regeneration (closed loop) --------------------------------------


class ReplacementQuestions(BaseModel):
    """LLM output schema for the regeneration call."""

    questions: list[QuizQuestion] = Field(description="Replacement quiz questions.")


REGENERATE_SYSTEM = """\
You are an expert university instructor maintaining a self-check quiz for a
lecture. The quiz has been given to students; item analysis flagged some
questions as psychometrically bad, and they were removed. Your job is to write
REPLACEMENT questions grounded ONLY in the lecture conspect provided.

Target difficulty: a good question is answered correctly by 30-85% of students
and separates those who understood the lecture from those who did not.

Rules for each replacement:
- Single-choice: exactly {num_options} options, exactly ONE correct.
- Fix the measured failure of the question it replaces:
  * too easy (p above the target range) → probe a deeper or more subtle aspect
    of the SAME topic, or a nearby topic not yet covered; make distractors
    closer to the truth so surface recall is not enough;
  * too hard (p below the target range) → test the same understanding more
    directly: simpler wording, more distinct options, no trick edge cases;
  * low discrimination → replace guessable or ambiguous wording with a question
    whose answer clearly follows from understanding the conspect.
- Do NOT duplicate or trivially rephrase any of the questions that remain in
  the quiz (they are listed below) or the retired ones.
- Test fundamentals (definitions, mechanisms, why a method works, trade-offs),
  never historical narrative or attribution (who proposed what, years, papers).
- For EVERY option write an explanation: why the correct one is right, and for
  each distractor which misconception makes it wrong.
- Balance option lengths: all options of a question must be of similar length
  and detail (within roughly ±20%); never make the correct option the longest
  or most hedged one — put caveats into its explanation instead. Length-biased
  questions are rejected by an automatic validator.
- Everything must be answerable from the conspect alone; write in the language
  of the conspect, keeping established English technical terms as-is.
"""

REGENERATE_USER = """\
Write exactly {num_replacements} replacement question(s).

=== RETIRED QUESTIONS (with measured statistics — fix these failures) ===
{retired}

=== QUESTIONS STILL IN THE QUIZ (do not duplicate them) ===
{remaining}

=== LECTURE CONSPECT (the only source of truth) ===
{conspect}"""


def regenerate_questions(
    conspect_md: str,
    remaining: list[QuizQuestion],
    retired: list[ItemStats],
    *,
    model: str | None = None,
    provider: str | None = None,
    max_tokens: int = 32_000,
) -> list[QuizQuestion]:
    """One LLM call: replacements for the retired questions, schema-validated."""
    retired_desc = "\n\n".join(
        f"- question: {s.question}\n"
        f"  measured: p-value={s.p_value:.2f}, point-biserial="
        f"{'n/a' if s.point_biserial is None else f'{s.point_biserial:.2f}'}, n={s.n}\n"
        f"  verdict: {s.status} ({s.reason})"
        for s in retired
    )
    remaining_desc = "\n".join(f"- {q.question}" for q in remaining) or "(none)"

    generator = QuizGenerator(model=model, provider=provider, max_tokens=max_tokens)
    system = REGENERATE_SYSTEM.format(num_options=NUM_OPTIONS)
    user_msg = REGENERATE_USER.format(
        num_replacements=len(retired),
        retired=retired_desc,
        remaining=remaining_desc,
        conspect=conspect_md.strip(),
    )
    batch = generator.complete_structured(system, user_msg, ReplacementQuestions)

    remaining_texts = {q.question.strip().lower() for q in remaining}
    replacements = [q for q in batch.questions if q.question.strip().lower() not in remaining_texts]
    if len(replacements) != len(retired):
        print(f"           WARNING: asked for {len(retired)} replacements, usable: {len(replacements)}")
    return replacements


# --- pipeline ------------------------------------------------------------------


def _course_and_lecture(lecture_dir: Path) -> tuple[str, str]:
    """data/<course>/<lecture> → (course, lecture) — the identifiers used in the DB."""
    return lecture_dir.parent.name, lecture_dir.name


def _print_report(stats: list[ItemStats]) -> None:
    if not stats:
        print("           no recorded attempts yet — run the web quiz first (cd web && npm run dev)")
        return
    for s in sorted(stats, key=lambda s: (s.status == "ok", s.question)):
        rpb = "  n/a" if s.point_biserial is None else f"{s.point_biserial:+.2f}"
        mark = "OK " if s.status == "ok" else "BAD" if s.status != "insufficient_data" else "..."
        print(f"  [{mark}] p={s.p_value:.2f}  r_pb={rpb}  n={s.n:<3d} {s.question[:80]}")
        if s.reason:
            print(f"        -> {s.status}: {s.reason}")


def process_lecture(
    lecture_dir: Path,
    *,
    retire: bool = False,
    regenerate: bool = False,
    p_range: tuple[float, float] = TARGET_P_RANGE,
    min_rpb: float = MIN_POINT_BISERIAL,
    min_attempts: int = MIN_ATTEMPTS,
    model: str | None = None,
    provider: str | None = None,
    db_path: Path | None = None,
) -> list[ItemStats]:
    course, lecture = _course_and_lecture(lecture_dir)
    quiz_path = lecture_dir / "quiz.json"
    if not quiz_path.exists():
        raise FileNotFoundError(f"No quiz at {quiz_path} — run `python -m app.quiz {lecture_dir}` first.")
    quiz = Quiz.model_validate_json(quiz_path.read_text(encoding="utf-8"))

    print(f"[{lecture}] item analysis ({db.attempt_count(course, lecture, db_path=db_path)} attempts)")
    stats = apply_rejection_rule(
        compute_item_stats(course, lecture, db_path=db_path),
        p_range=p_range,
        min_rpb=min_rpb,
        min_attempts=min_attempts,
    )
    _print_report(stats)

    if not (retire or regenerate):
        return stats

    # --- rejection rule: retire flagged questions from quiz.json ---------------
    flagged = flagged_items(stats)
    active_ids = {db.question_id(course, lecture, q.question) for q in quiz.questions}
    flagged = [s for s in flagged if s.question_id in active_ids]  # ignore stats of already-removed items
    if not flagged:
        print("           nothing to retire — quiz unchanged")
        return stats

    flagged_ids = {s.question_id for s in flagged}
    kept = [q for q in quiz.questions if db.question_id(course, lecture, q.question) not in flagged_ids]
    for s in flagged:
        question = next(q for q in quiz.questions if db.question_id(course, lecture, q.question) == s.question_id)
        db.retire_question(
            course,
            lecture,
            question.model_dump(),
            reason=f"{s.status}: {s.reason}",
            n_attempts=s.n,
            p_value=s.p_value,
            point_biserial=s.point_biserial,
            db_path=db_path,
        )
        print(f"           retired ({s.status}): {s.question[:80]}")

    # --- adaptive regeneration: refill the quiz with targeted replacements -----
    if regenerate:
        conspect_path = lecture_dir / "conspect.md"
        if not conspect_path.exists():
            raise FileNotFoundError(f"No conspect at {conspect_path} — needed to regenerate questions.")
        print(f"           regenerating {len(flagged)} question(s) …")
        replacements = regenerate_questions(
            conspect_path.read_text(encoding="utf-8"),
            kept,
            flagged,
            model=model,
            provider=provider,
        )
        kept.extend(replacements)
        for q in replacements:
            print(f"           new: {q.question[:80]}")

    quiz.questions = kept
    quiz_path.write_text(
        json.dumps(quiz.model_dump(), ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"           -> {quiz_path} now has {len(kept)} question(s)")
    return stats


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Quiz item analysis: difficulty, discrimination, rejection rule")
    parser.add_argument("lectures", nargs="+", help="Lecture directories (each must contain quiz.json)")
    parser.add_argument("--retire", action="store_true", help="Remove flagged questions from quiz.json (archive in DB)")
    parser.add_argument("--regenerate", action="store_true", help="Retire AND generate LLM replacements (closed loop)")
    parser.add_argument(
        "--p-range",
        nargs=2,
        type=float,
        default=list(TARGET_P_RANGE),
        metavar=("LO", "HI"),
        help=f"Target difficulty range (default: {TARGET_P_RANGE[0]} {TARGET_P_RANGE[1]})",
    )
    parser.add_argument(
        "--min-rpb",
        type=float,
        default=MIN_POINT_BISERIAL,
        help=f"Minimum point-biserial discrimination (default: {MIN_POINT_BISERIAL})",
    )
    parser.add_argument(
        "--min-attempts",
        type=int,
        default=MIN_ATTEMPTS,
        help=f"Attempts required before the rejection rule applies (default: {MIN_ATTEMPTS})",
    )
    parser.add_argument("--model", default=None, help="LLM model for regeneration (default from config)")
    parser.add_argument("--provider", default=None, choices=["anthropic", "deepseek"], help="LLM provider")
    parser.add_argument("--db", default=None, type=Path, help="Results DB path (default: from config)")
    args = parser.parse_args(argv)

    for lec in args.lectures:
        process_lecture(
            Path(lec).resolve(),
            retire=args.retire or args.regenerate,
            regenerate=args.regenerate,
            p_range=tuple(args.p_range),
            min_rpb=args.min_rpb,
            min_attempts=args.min_attempts,
            model=args.model,
            provider=args.provider,
            db_path=args.db,
        )

    print("Done.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
