# Course-wide E1 results — baseline pipeline (reference)

**Data:** all 9 lectures of `data/deep-learning-and-computer-vision/` ·
**Method:** the baseline pipeline (run 1 of `docs/experiments/e1.md`), rerun
over all lectures for reference against `docs/result-analysis.md` ·
**Artifacts:** `<lecture-dir>/conspect_baseline.md` +
`<lecture-dir>/e1_baseline/e1.json` + `judgments_*.json` per lecture ·
**Models:** conspect generation *and* judging both `deepseek-v4-pro`,
embeddings `all-MiniLM-L6-v2`, top-k 8, whisper_cpp transcripts.

The baseline is the deliberately low-effort first end-to-end pipeline:

- conspect generated from the **raw ASR transcript** + raw extracted slide
  text (no transcript/slide reconstruction, no slide images);
- claim decomposition **without** salience labels and off-topic filtering;
- retriever `all-MiniLM-L6-v2`, top-k 8.

Reproduce with:

```bash
uv run python -m app.conspect <lecture-dir> --baseline
E1_EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2 \
  uv run python -m app.e1 <lecture-dir> --baseline --top-k 8
```

## Results

| lecture | coverage | cov slides | cov transcript | faithfulness | F1 | transcript-only preserved | unsupported claims | claims s/t/sum |
|---|---|---|---|---|---|---|---|---|
| 01 | 0.403 | 0.392 | 0.405 | 0.774 | 0.530 | 27.4% (of 624) | 53/235 | 199/857/235 |
| 02 | 0.421 | 0.411 | 0.423 | 0.775 | 0.545 | 31.8% (of 647) | 41/182 | 202/851/182 |
| 03 | 0.472 | 0.386 | 0.498 | 0.709 | 0.567 | 41.9% (of 568) | 64/220 | 223/745/220 |
| 04 | 0.506 | 0.391 | 0.525 | 0.679 | 0.580 | 46.9% (of 324) | 44/137 | 64/377/137 |
| 05 | 0.410 | 0.351 | 0.448 | 0.554 | 0.472 | 38.0% (of 313) | 66/148 | 228/364/148 |
| 06 | 0.466 | 0.397 | 0.486 | 0.758 | 0.577 | 40.1% (of 516) | 40/165 | 199/704/165 |
| 07 | 0.527 | 0.435 | 0.567 | 0.610 | 0.566 | 45.4% (of 306) | 69/177 | 184/434/177 |
| 08 | 0.403 | 0.333 | 0.424 | 0.593 | 0.480 | 33.9% (of 449) | 66/162 | 168/547/162 |
| 09 | 0.473 | 0.391 | 0.501 | 0.616 | 0.535 | 34.9% (of 329) | 43/112 | 169/487/112 |
| **mean** | **0.453** | **0.387** | **0.475** | **0.674** | **0.539** | **37.8%** | ~32% | |

Core-claim columns don't exist for the baseline: its decomposition has no
salience labels (that was a later addition).

## Baseline vs the main pipeline

Means over the same 9 lectures (main-pipeline numbers:
`docs/result-analysis.md`):

| metric | baseline | main | Δ |
|---|---|---|---|
| coverage | 0.453 | 0.631 | +0.178 |
| faithfulness | 0.674 | 0.817 | +0.143 |
| F1 | 0.539 | 0.711 | +0.172 |
| transcript-only preserved | 37.8% | 48.9% | +11.1 pp |
| unsupported claims | ~32% | ~17% | −15 pp |

The main pipeline wins on every metric on **every** lecture — no per-lecture
reversal on coverage, faithfulness, or F1.

Note the baseline's much larger transcript-only pools (306–647 claims vs the
main run's smaller cleaned pools): raw-transcript decomposition extracts
claims from filler, Q&A, and off-topic speech too, which deflates its
preserved-share further.

## Caveats on comparability

Two caveats vs the historical lecture-06 baseline numbers in
`docs/experiments/e1.md` (coverage 0.539, faithfulness 0.694): the original
run-1 code predates the repo's squashed history, so the salience-free
decomposition prompt was reconstructed from its description, and the baseline
conspects were regenerated — with LLM nondeterminism on both sides the
per-lecture numbers shift a few points, but the method matches run 1's
definition.
