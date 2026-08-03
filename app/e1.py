"""Claim-level summary evaluation (experiment E1): coverage / faithfulness / F1.

For each lecture directory this evaluates the final conspect against its two
sources, at the level of atomic facts. All artifacts are cached under
``<lecture-dir>/e1/`` so interrupted or repeated runs skip finished stages.

1. **Decompose** three texts into atomic, self-contained claims via LLM, each
   labelled with a salience (``core`` / ``supporting`` / ``aside``)
   (→ ``e1/claims.json``):

   * slides — ``slides_extracted/slides_reconstructed.md``, the same LLM-cleaned
     source the conspect was built from (the raw ``slides.md`` duplicates beamer
     overlay frames and mangles math, which would corrupt the claim sets);
   * transcript — ``<stt-provider>/transcription_reconstructed.md``, the
     LLM-cleaned transcript the conspect was built from (falls back to the raw
     ``transcription.md`` with a warning; see ``app.reconstruct_transcript``);
   * summary — ``conspect.md``.

2. **entails(claim, premise_set)** — top-k retrieval over the premise claims
   (sentence-transformers embeddings when installed, otherwise a built-in
   TF-IDF retriever) followed by a batched LLM-judge confirmation. Three
   directions are judged (→ ``e1/judgments_<direction>.json``):

   * source claim ⊑ summary claims → **coverage** (recall);
   * summary claim ⊑ source claims → **faithfulness** (precision);
   * transcript claim ⊑ slide claims → the **transcript-only** mask.

3. **Metrics** (→ ``e1/e1.json`` + console report): coverage (overall and per
   source), faithfulness, their harmonic-mean **F1**, and
   ``transcript_only_coverage`` — the share of spoken facts absent from the
   slides that survived into the summary. That last number is the project's
   thesis ("site > deck") in a single figure.

    python -m app.e1 data/deep-learning-and-computer-vision/lecture-06
    python -m app.e1 <lecture-dir> --stt google_stt --model claude-opus-4-8
    python -m app.e1 <lecture-dir> --sample-labels 12   # template for manual judge calibration
    python -m app.e1 <lecture-dir> --agreement          # judge vs filled-in manual labels
"""

from __future__ import annotations

import argparse
import json
import random
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, Field

from app import config
from app.quiz import QuizGenerator

SOURCE_KEYS = ("slides", "transcript", "summary")

DEFAULT_TOP_K = 16
DEFAULT_JUDGE_BATCH = 8
# ~2k words decompose into ~100 claims ≈ 10k output tokens with the salience
# labels; 3k-word chunks overflowed the 32k completion cap (thinking included)
# on dense texts and came back as truncated JSON.
DEFAULT_CHUNK_WORDS = 2_000
DEFAULT_WORKERS = 4
DEFAULT_SEED = 13
# Reasoning models (deepseek-v4-pro) spend most of the completion budget on
# thinking before the JSON comes out; 8k (the quiz default) hits the cap with
# an empty response on decomposition-sized inputs.
DEFAULT_MAX_TOKENS = 32_000

# --- schemas -----------------------------------------------------------------


class ExtractedClaim(BaseModel):
    text: str = Field(description="An atomic, self-contained factual claim extracted from the text.")
    salience: Literal["core", "supporting", "aside"] = Field(
        description=(
            "core = a main teaching point of the lecture; supporting = a detail elaborating a core point; "
            "aside = tangential to the taught material."
        )
    )


class ExtractedClaims(BaseModel):
    """LLM output of the decomposition stage: one chunk → a list of atomic claims."""

    claims: list[ExtractedClaim] = Field(description="Atomic, self-contained factual claims extracted from the text.")


class BaselineClaim(BaseModel):
    text: str = Field(description="An atomic, self-contained factual claim extracted from the text.")


class BaselineClaims(BaseModel):
    """Baseline decomposition output: atomic claims without salience labels."""

    claims: list[BaselineClaim] = Field(description="Atomic, self-contained factual claims extracted from the text.")


class JudgeVerdict(BaseModel):
    id: int = Field(description="The item id this verdict is for, copied verbatim.")
    entailed: bool = Field(description="Whether the claim is fully supported by the item's premises.")
    evidence: int | None = Field(
        default=None,
        description="1-based number of the single premise that best supports the claim; null when not entailed.",
    )


class JudgeVerdicts(BaseModel):
    """LLM output of the judge stage: a verdict for every item in the batch."""

    verdicts: list[JudgeVerdict]


# --- prompts -------------------------------------------------------------------

DECOMPOSE_SYSTEM_PROMPT = """\
You are an expert annotator preparing texts for claim-level evaluation of
lecture materials. Decompose the given text into ATOMIC FACTUAL CLAIMS.

## Rules

- **Atomic**: exactly one verifiable statement per claim. Split sentences that
  join several independent facts.
- **Self-contained**: resolve pronouns and references so each claim is
  understandable with no surrounding context ("this method" → its name,
  "he" → the person's name, "the previous formula" → the formula itself).
- **Faithful**: state only what the text states — no outside knowledge, no
  corrections of substance. Keep mathematics as LaTeX, as written.
- **Substantive content only**: definitions, theorems, formulas, properties,
  mechanisms, reasons, worked examples, numbers, comparisons, historical
  facts, practical advice, warnings, and points the text marks as important.
- **Skip**: greetings and small talk, course administration, technical
  difficulties, audience interaction, navigation ("let's move on"),
  rhetorical questions, filler, and facts you have already extracted.
- **Salience**: label every claim —
  * `core` — a main teaching point: a definition, theorem, key formula,
    mechanism, central result, or conclusion a good summary must keep;
  * `supporting` — elaboration of a core point: a derivation step, worked
    example, concrete number, comparison, or practical advice;
  * `aside` — tangential to the taught material: historical anecdotes,
    speaker opinions, meta-commentary.
- Write claims in the language of the source text; keep established English
  technical terms as-is.

The text is {source_desc}."""

SOURCE_DESCRIPTIONS = {
    "slides": "a cleaned-up Markdown reconstruction of the lecture slides",
    "transcript": (
        "an LLM-cleaned reconstruction of a lecture's speech transcript; residual "
        "recognition errors are possible — extract only what it clearly says"
    ),
    "summary": "the final study conspect (summary) built from a lecture",
}

# The baseline (run 1 in docs/experiments/e1.md) decomposed with neither
# salience labels nor the off-topic filtering rules; both were added later.
BASELINE_DECOMPOSE_SYSTEM_PROMPT = """\
You are an expert annotator preparing texts for claim-level evaluation of
lecture materials. Decompose the given text into ATOMIC FACTUAL CLAIMS.

## Rules

- **Atomic**: exactly one verifiable statement per claim. Split sentences that
  join several independent facts.
- **Self-contained**: resolve pronouns and references so each claim is
  understandable with no surrounding context ("this method" → its name,
  "he" → the person's name, "the previous formula" → the formula itself).
- **Faithful**: state only what the text states — no outside knowledge, no
  corrections of substance. Keep mathematics as LaTeX, as written.
- Write claims in the language of the source text; keep established English
  technical terms as-is.

The text is {source_desc}."""

BASELINE_SOURCE_DESCRIPTIONS = {
    "slides": "the text extracted from the lecture slides (PDF)",
    "transcript": (
        "a raw speech-recognition transcript of a lecture; recognition errors "
        "are possible — extract only what it clearly says"
    ),
    "summary": "the final study conspect (summary) built from a lecture",
}

DECOMPOSE_USER_TEMPLATE = """\
Decompose the following text into atomic factual claims.{part_note}

=== TEXT ===
{text}"""

JUDGE_SYSTEM_PROMPT = """\
You are a strict entailment judge (NLI) for claim-level evaluation of lecture
summaries. You receive several ITEMs; each has a CLAIM and a numbered list of
PREMISES retrieved from a source document. For every item decide whether the
claim is fully supported by its premises taken together.

- `entailed = true` — the claim's full content follows from the premises: a
  paraphrase, a direct consequence, or a combination of several premises.
- `entailed = false` — anything less: the premises merely mention the topic,
  support only part of the claim, are more general than the claim (the claim
  adds specifics the premises do not state), or contradict it.
- Judge ONLY against the premises. Ignore your own knowledge of the subject: a
  claim that is true in the real world but not stated by the premises is NOT
  entailed.
- Do not let surface differences block entailment when the meaning is
  unambiguous: wording, notation, or an obvious speech-recognition misspelling
  of a technical term.
- When entailed, set `evidence` to the 1-based number of the single premise
  that contributes most; when not entailed, leave it null.

Return exactly one verdict for EVERY item id you were given."""

JUDGE_USER_TEMPLATE = """\
Judge the following items.

{items}"""


# --- input loading -------------------------------------------------------------

_SEGMENT_LINE = re.compile(r"^\s*\*\*\[[^\]]+\]\*\*\s*(.*\S)\s*$")


def _load_transcript_text(path: Path) -> str:
    """Spoken text of a timestamped transcript .md, without the metadata header."""
    lines = path.read_text(encoding="utf-8").splitlines()
    spoken = [m.group(1) for line in lines if (m := _SEGMENT_LINE.match(line))]
    if spoken:
        return "\n".join(spoken)
    return "\n".join(lines).strip()


def _read_texts(lecture_dir: Path, stt_provider: str, *, baseline: bool = False) -> dict[str, str]:
    """Load the three texts to decompose: slides, transcript, summary.

    The transcript side prefers the LLM-cleaned ``transcription_reconstructed.md``
    (see ``app.reconstruct_transcript``) — the same source the conspect was
    built from — falling back to the raw ASR output with a warning.

    ``baseline=True`` evaluates the baseline pipeline instead: the raw ASR
    ``transcription.md``, the raw extracted ``slides.md``, and the baseline
    conspect (``conspect_baseline.md``, from ``app.conspect --baseline``).
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
        conspect_path = lecture_dir / "conspect_baseline.md"
        if not conspect_path.exists():
            raise FileNotFoundError(
                f"No baseline conspect at {conspect_path} — run `python -m app.conspect {lecture_dir} --baseline`."
            )
        return {
            "slides": slides_path.read_text(encoding="utf-8"),
            "transcript": _load_transcript_text(transcript_path),
            "summary": conspect_path.read_text(encoding="utf-8"),
        }

    transcript_path = lecture_dir / stt_provider / "transcription_reconstructed.md"
    if not transcript_path.exists():
        fallback_transcript = lecture_dir / stt_provider / "transcription.md"
        if fallback_transcript.exists():
            print(
                "           WARNING: no transcription_reconstructed.md — using the raw transcript "
                f"(run `python -m app.reconstruct_transcript {lecture_dir}` for a cleaned one)"
            )
            transcript_path = fallback_transcript
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

    conspect_path = lecture_dir / "conspect.md"
    if not conspect_path.exists():
        raise FileNotFoundError(f"No conspect at {conspect_path} — run `python -m app.conspect {lecture_dir}` first.")

    return {
        "slides": slides_path.read_text(encoding="utf-8"),
        "transcript": _load_transcript_text(transcript_path),
        "summary": conspect_path.read_text(encoding="utf-8"),
    }


def _chunk_text(text: str, max_words: int) -> list[str]:
    """Split on line boundaries into chunks of roughly `max_words` words."""
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


# --- retrieval -----------------------------------------------------------------


class Retriever:
    """Ranks premise claims for query claims.

    Backend "embeddings" uses sentence-transformers (config.E1_EMBED_MODEL);
    "tfidf" is a dependency-free lexical fallback; "auto" picks embeddings when
    the package is installed. Retrieval only needs good recall@k — the LLM
    judge makes the actual entailment decision.
    """

    def __init__(self, premises: list[str], *, backend: str = "auto") -> None:
        self.premises = premises
        self.backend = backend
        if backend == "auto":
            try:
                import sentence_transformers  # noqa: F401
            except ImportError:
                print("           NOTE: sentence-transformers not installed — using the TF-IDF retriever")
                self.backend = "tfidf"
            else:
                self.backend = "embeddings"
        if self.backend == "embeddings":
            import torch
            from sentence_transformers import SentenceTransformer

            if torch.cuda.is_available():
                device = "cuda"
            elif torch.mps.is_available():
                device = "mps"
            else:
                device = "cpu"
            self._model = SentenceTransformer(config.E1_EMBED_MODEL, device=device)
            self._premise_vecs = self._model.encode(premises, normalize_embeddings=True, show_progress_bar=False)
        elif self.backend == "tfidf":
            self._fit_tfidf(premises)
        else:
            raise ValueError(f"Unknown retriever backend: {self.backend!r} (expected auto | embeddings | tfidf).")

    def rank(self, queries: list[str], k: int) -> list[list[int]]:
        """For each query, indices of the top-k premises, best first."""
        k = min(k, len(self.premises))
        if k == 0:
            return [[] for _ in queries]
        if self.backend == "embeddings":
            query_vecs = self._model.encode(queries, normalize_embeddings=True, show_progress_bar=False)
            sims = query_vecs @ self._premise_vecs.T
            return [row.argsort()[::-1][:k].tolist() for row in sims]
        return [self._tfidf_topk(q, k) for q in queries]

    # --- TF-IDF fallback -------------------------------------------------------

    @staticmethod
    def _tokenize(text: str) -> list[str]:
        return re.findall(r"\w+", text.lower())

    def _fit_tfidf(self, premises: list[str]) -> None:
        import math
        from collections import Counter

        docs = [Counter(self._tokenize(p)) for p in premises]
        df = Counter(term for doc in docs for term in doc)
        n = len(docs)
        self._idf = {term: math.log((1 + n) / (1 + count)) + 1 for term, count in df.items()}
        self._doc_vecs = []
        for doc in docs:
            vec = {term: tf * self._idf[term] for term, tf in doc.items()}
            norm = sum(w * w for w in vec.values()) ** 0.5 or 1.0
            self._doc_vecs.append((vec, norm))

    def _tfidf_topk(self, query: str, k: int) -> list[int]:
        from collections import Counter

        q = {term: tf * self._idf.get(term, 0.0) for term, tf in Counter(self._tokenize(query)).items()}
        q_norm = sum(w * w for w in q.values()) ** 0.5 or 1.0
        scores = [
            (sum(w * vec.get(term, 0.0) for term, w in q.items()) / (q_norm * norm), i)
            for i, (vec, norm) in enumerate(self._doc_vecs)
        ]
        scores.sort(key=lambda pair: (-pair[0], pair[1]))
        return [i for _, i in scores[:k]]


# --- LLM stages ------------------------------------------------------------------


def _ensure_client(gen: QuizGenerator) -> None:
    # The generator builds its SDK client lazily on first use; build it once up
    # front so worker threads don't race the initialization.
    if gen.provider == "anthropic":
        gen._anthropic_client()  # noqa: SLF001
    else:
        gen._deepseek_client()  # noqa: SLF001


def decompose_source(
    gen: QuizGenerator,
    source: str,
    text: str,
    *,
    chunk_words: int = DEFAULT_CHUNK_WORDS,
    max_chunks: int | None = None,
    workers: int = DEFAULT_WORKERS,
    baseline: bool = False,
) -> list[dict]:
    """Decompose one source text into atomic claims (with salience), chunk by chunk.

    ``baseline=True`` uses the run-1 prompt: no salience labels, no off-topic
    filtering rules (claims come back as ``{"text": ...}`` only).
    """
    chunks = _chunk_text(text, chunk_words)
    if max_chunks is not None:
        chunks = chunks[:max_chunks]
    if baseline:
        system = BASELINE_DECOMPOSE_SYSTEM_PROMPT.format(source_desc=BASELINE_SOURCE_DESCRIPTIONS[source])
        schema = BaselineClaims
    else:
        system = DECOMPOSE_SYSTEM_PROMPT.format(source_desc=SOURCE_DESCRIPTIONS[source])
        schema = ExtractedClaims

    def decompose_chunk(chunk: str, part_note: str) -> list[ExtractedClaim | BaselineClaim]:
        user_msg = DECOMPOSE_USER_TEMPLATE.format(part_note=part_note, text=chunk)
        try:
            return gen.complete_structured(system, user_msg, schema).claims
        except RuntimeError:
            # Dense chunks can produce more claims than fit in the completion
            # budget, truncating the JSON — halve the chunk and retry.
            lines = chunk.splitlines()
            if len(lines) >= 2:
                mid = len(lines) // 2
                halves = ["\n".join(lines[:mid]), "\n".join(lines[mid:])]
            else:
                words = chunk.split()
                if len(words) < 2:
                    raise
                halves = [" ".join(words[: len(words) // 2]), " ".join(words[len(words) // 2 :])]
            print(f"           NOTE: a {source} chunk failed to decompose in one call — splitting it in half")
            return [claim for half in halves if half.strip() for claim in decompose_chunk(half, part_note)]

    def one(args: tuple[int, str]) -> list[ExtractedClaim]:
        i, chunk = args
        part_note = f" This is part {i + 1} of {len(chunks)} of the document." if len(chunks) > 1 else ""
        return decompose_chunk(chunk, part_note)

    _ensure_client(gen)
    with ThreadPoolExecutor(max_workers=workers) as pool:
        per_chunk = list(pool.map(one, enumerate(chunks)))
    claims = [
        {"text": claim.text.strip(), **({} if baseline else {"salience": claim.salience})}
        for chunk_claims in per_chunk
        for claim in chunk_claims
        if claim.text.strip()
    ]
    if baseline:
        print(f"           {source}: {len(chunks)} chunk(s) -> {len(claims)} claims")
    else:
        by_salience = {label: sum(c["salience"] == label for c in claims) for label in ("core", "supporting", "aside")}
        print(
            f"           {source}: {len(chunks)} chunk(s) -> {len(claims)} claims "
            f"(core {by_salience['core']} / supporting {by_salience['supporting']} / aside {by_salience['aside']})"
        )
    return claims


def _format_judge_items(batch: list[tuple[int, str, list[str]]]) -> str:
    blocks = []
    for item_id, claim, premises in batch:
        numbered = "\n".join(f"{j + 1}. {p}" for j, p in enumerate(premises))
        blocks.append(f"=== ITEM id={item_id} ===\nCLAIM: {claim}\nPREMISES:\n{numbered}")
    return "\n\n".join(blocks)


def judge_direction(
    gen: QuizGenerator,
    targets: list[tuple[str, str]],
    premises: list[tuple[str, str]],
    *,
    retriever_backend: str = "auto",
    top_k: int = DEFAULT_TOP_K,
    batch_size: int = DEFAULT_JUDGE_BATCH,
    workers: int = DEFAULT_WORKERS,
) -> list[dict]:
    """Judge every target claim against its top-k retrieved premises.

    `targets` and `premises` are lists of (claim_ref, claim_text), where
    claim_ref is a global "<source>:<index>" id. Returns one record per target:
    {"claim": ref, "text": ..., "entailed": bool, "evidence": ref | None,
    "top": [refs]}.
    """
    if not premises:
        return [{"claim": ref, "text": text, "entailed": False, "evidence": None, "top": []} for ref, text in targets]

    retriever = Retriever([text for _, text in premises], backend=retriever_backend)
    ranks = retriever.rank([text for _, text in targets], top_k)

    batches = [
        [(idx, targets[idx][1], [premises[p][1] for p in ranks[idx]]) for idx in range(start, end)]
        for start, end in _batch_bounds(len(targets), batch_size)
    ]

    def one(batch: list[tuple[int, str, list[str]]], retry: bool = True) -> dict[int, JudgeVerdict]:
        try:
            result = gen.complete_structured(
                JUDGE_SYSTEM_PROMPT, JUDGE_USER_TEMPLATE.format(items=_format_judge_items(batch)), JudgeVerdicts
            )
            return {v.id: v for v in result.verdicts}
        except RuntimeError as e:
            # Occasional empty/truncated responses (reasoning models can spend
            # the whole completion budget thinking) — halve the batch and retry
            # instead of losing the direction; a single item that keeps failing
            # is dropped and counted as not entailed by the caller.
            if len(batch) > 1:
                mid = len(batch) // 2
                print(f"           NOTE: a judge batch of {len(batch)} failed ({e}) — splitting it in half")
                return {**one(batch[:mid]), **one(batch[mid:])}
            if retry:
                return one(batch, retry=False)
            print(f"           WARNING: judging one claim failed twice ({e}) — dropping it")
            return {}

    _ensure_client(gen)
    with ThreadPoolExecutor(max_workers=workers) as pool:
        verdict_maps = list(pool.map(one, batches))
    verdicts = {item_id: v for vmap in verdict_maps for item_id, v in vmap.items()}

    records = []
    missing = 0
    for idx, (ref, text) in enumerate(targets):
        verdict = verdicts.get(idx)
        if verdict is None:
            missing += 1
            verdict = JudgeVerdict(id=idx, entailed=False, evidence=None)
        evidence_ref = None
        if verdict.entailed and verdict.evidence is not None and 1 <= verdict.evidence <= len(ranks[idx]):
            evidence_ref = premises[ranks[idx][verdict.evidence - 1]][0]
        records.append(
            {
                "claim": ref,
                "text": text,
                "entailed": verdict.entailed,
                "evidence": evidence_ref,
                "top": [premises[p][0] for p in ranks[idx]],
            }
        )
    if missing:
        print(f"           WARNING: the judge returned no verdict for {missing} claim(s) — counted as not entailed")
    return records


def _batch_bounds(total: int, batch_size: int) -> list[tuple[int, int]]:
    return [(start, min(start + batch_size, total)) for start in range(0, total, batch_size)]


# --- metrics ---------------------------------------------------------------------


def _share(records: list[dict]) -> float | None:
    return round(sum(r["entailed"] for r in records) / len(records), 4) if records else None


def compute_metrics(
    coverage_records: list[dict],
    faithfulness_records: list[dict],
    transcript_vs_slides_records: list[dict],
    salience: dict[str, str],
) -> dict:
    """Aggregate judged records into the E1 metric set.

    `salience` maps a claim ref ("<source>:<index>") to its salience label; the
    `*_core` metrics restrict coverage to core claims — the facts a good summary
    is actually obliged to keep (asides counting against coverage was the main
    distortion of the unweighted numbers).
    """
    slides_cov = [r for r in coverage_records if r["claim"].startswith("slides:")]
    transcript_cov = [r for r in coverage_records if r["claim"].startswith("transcript:")]

    def core(records: list[dict]) -> list[dict]:
        return [r for r in records if salience.get(r["claim"]) == "core"]

    coverage = _share(coverage_records)
    faithfulness = _share(faithfulness_records)
    f1 = None
    if coverage and faithfulness:
        f1 = round(2 * coverage * faithfulness / (coverage + faithfulness), 4)

    # Spoken facts absent from the slides; how many of them the summary kept.
    on_slides = {r["claim"] for r in transcript_vs_slides_records if r["entailed"]}
    transcript_only = [r for r in transcript_cov if r["claim"] not in on_slides]
    transcript_only_core = core(transcript_only)

    return {
        "coverage": coverage,
        "coverage_core": _share(core(coverage_records)),
        "coverage_slides": _share(slides_cov),
        "coverage_transcript": _share(transcript_cov),
        "coverage_transcript_core": _share(core(transcript_cov)),
        "faithfulness": faithfulness,
        "f1": f1,
        "transcript_only_claims": len(transcript_only),
        "transcript_only_coverage": _share(transcript_only),
        "transcript_only_core_claims": len(transcript_only_core),
        "transcript_only_core_coverage": _share(transcript_only_core),
    }


# --- caching ---------------------------------------------------------------------


def _load_cache(path: Path, fingerprint: dict) -> dict | None:
    if not path.exists():
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return None
    if data.get("fingerprint") != fingerprint:
        print(f"           NOTE: {path.name} was built with different settings — recomputing")
        return None
    return data


def _save_cache(path: Path, fingerprint: dict, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps({"fingerprint": fingerprint, **payload}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


# --- manual calibration (P1) --------------------------------------------------------


def write_labels_sample(e1_dir: Path, sample_size: int, seed: int) -> Path:
    """Sample judged pairs into a template for manual labelling (judge calibration)."""
    labels_path = e1_dir / "labels_manual.json"
    if labels_path.exists():
        print(f"           NOTE: {labels_path} already exists — not overwriting; fill it in or delete it")
        return labels_path

    claims = json.loads((e1_dir / "claims.json").read_text(encoding="utf-8"))

    def claim_text(ref: str) -> str:
        source, idx = ref.split(":")
        claim = claims[source][int(idx)]
        return claim["text"] if isinstance(claim, dict) else claim

    pool = []
    for direction in ("coverage", "faithfulness", "transcript_vs_slides"):
        data = json.loads((e1_dir / f"judgments_{direction}.json").read_text(encoding="utf-8"))
        for record in data["records"]:
            pool.append(
                {
                    "direction": direction,
                    "claim": record["claim"],
                    "text": record["text"],
                    "judge_entailed": record["entailed"],
                    "evidence": claim_text(record["evidence"]) if record["evidence"] else None,
                    # everything the judge saw — labelling against fewer premises
                    # would blame the judge for evidence the human wasn't shown
                    "retrieved_premises": [claim_text(ref) for ref in record["top"]],
                    "manual_entailed": None,
                }
            )
    sample = random.Random(seed).sample(pool, min(sample_size, len(pool)))
    labels_path.write_text(json.dumps(sample, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"           {len(sample)} pairs -> {labels_path} (fill in manual_entailed: true/false)")
    return labels_path


def report_agreement(e1_dir: Path) -> None:
    """Compare the judge's verdicts with the filled-in manual labels."""
    labels_path = e1_dir / "labels_manual.json"
    if not labels_path.exists():
        raise FileNotFoundError(f"No manual labels at {labels_path} — create them with --sample-labels first.")
    rows = json.loads(labels_path.read_text(encoding="utf-8"))
    labelled = [r for r in rows if r.get("manual_entailed") is not None]
    if not labelled:
        print(f"           no filled-in labels in {labels_path} yet (set manual_entailed: true/false)")
        return
    agree = sum(r["judge_entailed"] == r["manual_entailed"] for r in labelled)
    false_pos = sum(r["judge_entailed"] and not r["manual_entailed"] for r in labelled)
    false_neg = sum(not r["judge_entailed"] and r["manual_entailed"] for r in labelled)
    print(
        f"           judge vs manual: {agree}/{len(labelled)} agree ({agree / len(labelled):.0%}); "
        f"judge said entailed but human said no: {false_pos}; missed by judge: {false_neg}"
    )


# --- pipeline ------------------------------------------------------------------------


def process_lecture(
    lecture_dir: Path,
    *,
    stt_provider: str = "whisper_cpp",
    model: str | None = None,
    provider: str | None = None,
    retriever_backend: str = "auto",
    top_k: int = DEFAULT_TOP_K,
    batch_size: int = DEFAULT_JUDGE_BATCH,
    chunk_words: int = DEFAULT_CHUNK_WORDS,
    workers: int = DEFAULT_WORKERS,
    max_tokens: int = DEFAULT_MAX_TOKENS,
    limit: int | None = None,
    max_chunks: int | None = None,
    force: bool = False,
    baseline: bool = False,
) -> dict:
    """Run (or resume) the full E1 pipeline for one lecture; returns the metrics.

    ``baseline=True`` evaluates the baseline pipeline (raw transcript, raw
    slides, ``conspect_baseline.md``, salience-free decomposition) and keeps
    its artifacts in ``<lecture-dir>/e1_baseline/`` so the main run's cache
    survives.
    """
    e1_dir = lecture_dir / ("e1_baseline" if baseline else "e1")
    gen = QuizGenerator(model=model, provider=provider, max_tokens=max_tokens)
    fingerprint = {
        # bump when the prompts or the claims.json format change incompatibly
        "version": 3,
        "stt": stt_provider,
        "model": f"{gen.provider}:{gen.model}",
        "embed_model": config.E1_EMBED_MODEL,
        "chunk_words": chunk_words,
        "top_k": top_k,
        "limit": limit,
        "max_chunks": max_chunks,
    }
    if baseline:
        # only added in baseline mode so pre-existing e1/ caches keep matching
        fingerprint["baseline"] = True
    print(
        f"[{lecture_dir.name}] E1{' baseline' if baseline else ''} ({fingerprint['model']}, stt={stt_provider}, "
        f"retriever={retriever_backend}, k={top_k})"
    )
    t0 = time.monotonic()

    # 1. decomposition
    claims_path = e1_dir / "claims.json"
    cached = None if force else _load_cache(claims_path, fingerprint)
    if cached is not None:
        claims = {source: cached[source] for source in SOURCE_KEYS}
        print("           claims.json: cached")
    else:
        texts = _read_texts(lecture_dir, stt_provider, baseline=baseline)
        claims = {
            source: decompose_source(
                gen,
                source,
                texts[source],
                chunk_words=chunk_words,
                max_chunks=max_chunks,
                workers=workers,
                baseline=baseline,
            )
            for source in SOURCE_KEYS
        }
        _save_cache(claims_path, fingerprint, claims)
    if limit is not None:
        claims = {source: source_claims[:limit] for source, source_claims in claims.items()}

    refs = {
        source: [(f"{source}:{i}", claim["text"]) for i, claim in enumerate(claims[source])] for source in SOURCE_KEYS
    }
    salience = {
        f"{source}:{i}": claim.get("salience") for source in SOURCE_KEYS for i, claim in enumerate(claims[source])
    }
    source_refs = refs["slides"] + refs["transcript"]

    # 2. three judged directions
    directions = {
        "coverage": (source_refs, refs["summary"]),
        "faithfulness": (refs["summary"], source_refs),
        "transcript_vs_slides": (refs["transcript"], refs["slides"]),
    }
    judgments: dict[str, list[dict]] = {}
    for name, (targets, premise_pool) in directions.items():
        path = e1_dir / f"judgments_{name}.json"
        cached = None if force else _load_cache(path, fingerprint)
        if cached is not None:
            judgments[name] = cached["records"]
            print(f"           judgments_{name}.json: cached")
            continue
        print(f"           judging {name}: {len(targets)} claims vs {len(premise_pool)} premises …")
        judgments[name] = judge_direction(
            gen,
            targets,
            premise_pool,
            retriever_backend=retriever_backend,
            top_k=top_k,
            batch_size=batch_size,
            workers=workers,
        )
        _save_cache(path, fingerprint, {"records": judgments[name]})

    # 3. metrics
    metrics = compute_metrics(
        judgments["coverage"], judgments["faithfulness"], judgments["transcript_vs_slides"], salience
    )
    counts = {source: len(claims[source]) for source in SOURCE_KEYS}
    _save_cache(e1_dir / "e1.json", fingerprint, {"counts": counts, "metrics": metrics})

    def pct(value: float | None) -> str:
        return f"{value:.1%}" if value is not None else "n/a"

    print(f"           claims: slides={counts['slides']} transcript={counts['transcript']} summary={counts['summary']}")
    print(
        f"           coverage (source -> summary): {pct(metrics['coverage'])} "
        f"(slides {pct(metrics['coverage_slides'])}, transcript {pct(metrics['coverage_transcript'])})"
    )
    print(
        f"           coverage of core claims: {pct(metrics['coverage_core'])} "
        f"(transcript {pct(metrics['coverage_transcript_core'])})"
    )
    print(f"           faithfulness (summary -> source): {pct(metrics['faithfulness'])}")
    print(f"           F1: {pct(metrics['f1'])}")
    print(
        f"           transcript-only: {metrics['transcript_only_claims']} spoken claims absent from the slides, "
        f"{pct(metrics['transcript_only_coverage'])} preserved in the summary"
    )
    print(
        f"           transcript-only core: {metrics['transcript_only_core_claims']} claims, "
        f"{pct(metrics['transcript_only_core_coverage'])} preserved in the summary"
    )
    print(f"           {time.monotonic() - t0:.0f}s wall -> {e1_dir / 'e1.json'}")
    return metrics


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Claim-level summary evaluation (E1): coverage / faithfulness / F1")
    parser.add_argument(
        "lectures",
        nargs="+",
        help="One or more lecture directories (each with conspect.md, slides_extracted/, <stt>/transcription.md)",
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
        help="LLM model for decomposition and the judge (default from config)",
    )
    parser.add_argument(
        "--provider",
        default=None,
        choices=["anthropic", "deepseek"],
        help="LLM provider (default: from config / inferred from the model name)",
    )
    parser.add_argument(
        "--retriever",
        default="auto",
        choices=["auto", "embeddings", "tfidf"],
        help="Premise retrieval backend (default: embeddings when sentence-transformers is installed)",
    )
    parser.add_argument(
        "--top-k", type=int, default=DEFAULT_TOP_K, help=f"Premises per claim (default: {DEFAULT_TOP_K})"
    )
    parser.add_argument(
        "--batch-size",
        type=int,
        default=DEFAULT_JUDGE_BATCH,
        help=f"Claims per judge LLM call (default: {DEFAULT_JUDGE_BATCH})",
    )
    parser.add_argument(
        "--chunk-words",
        type=int,
        default=DEFAULT_CHUNK_WORDS,
        help=f"Words per decomposition chunk (default: {DEFAULT_CHUNK_WORDS})",
    )
    parser.add_argument("--workers", type=int, default=DEFAULT_WORKERS, help="Concurrent LLM calls (default: 4)")
    parser.add_argument(
        "--max-tokens",
        type=int,
        default=DEFAULT_MAX_TOKENS,
        help=f"Output token limit per LLM call, incl. reasoning (default: {DEFAULT_MAX_TOKENS})",
    )
    parser.add_argument("--limit", type=int, default=None, help="Debug: keep only the first N claims per source")
    parser.add_argument(
        "--max-chunks", type=int, default=None, help="Debug: decompose only the first N chunks of each source"
    )
    parser.add_argument("--force", action="store_true", help="Recompute all stages, ignoring caches")
    parser.add_argument(
        "--baseline",
        action="store_true",
        help=(
            "Evaluate the baseline pipeline: raw ASR transcript, raw slides.md, conspect_baseline.md, "
            "salience-free decomposition; artifacts go to <lecture-dir>/e1_baseline/ "
            "(combine with --top-k 8 and E1_EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2)"
        ),
    )
    parser.add_argument(
        "--sample-labels",
        type=int,
        default=None,
        metavar="N",
        help="Sample N judged pairs into e1/labels_manual.json for manual judge calibration",
    )
    parser.add_argument(
        "--agreement", action="store_true", help="Report judge agreement with the filled-in manual labels"
    )
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED, help="Sampling seed for --sample-labels")
    args = parser.parse_args(argv)

    for lec in args.lectures:
        lecture_dir = Path(lec).resolve()
        process_lecture(
            lecture_dir,
            stt_provider=args.stt,
            model=args.model,
            provider=args.provider,
            retriever_backend=args.retriever,
            top_k=args.top_k,
            batch_size=args.batch_size,
            chunk_words=args.chunk_words,
            workers=args.workers,
            max_tokens=args.max_tokens,
            limit=args.limit,
            max_chunks=args.max_chunks,
            force=args.force,
            baseline=args.baseline,
        )
        e1_dir = lecture_dir / ("e1_baseline" if args.baseline else "e1")
        if args.sample_labels:
            write_labels_sample(e1_dir, args.sample_labels, args.seed)
        if args.agreement:
            report_agreement(e1_dir)

    print("Done.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
