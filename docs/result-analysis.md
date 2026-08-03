# Course-wide E1 results — analysis and conclusions

**Data:** all 9 lectures of `data/deep-learning-and-computer-vision/` ·
**Method:** `app/e1.py` (see `docs/experiments/e1.md`) · **Artifacts:**
`<lecture-dir>/e1/e1.json` + `judgments_*.json` per lecture ·
**Models:** conspect generation *and* judging both `deepseek-v4-pro`,
embeddings `BAAI/bge-small-en-v1.5`, top-k 16, whisper_cpp transcripts.

## Results

| lecture | coverage | coverage (core) | faithfulness | F1 | transcript-only preserved | t-only (core) | unsupported claims |
|---|---|---|---|---|---|---|---|
| 01 | 0.592 | 0.708 | 0.811 | 0.684 | 46.1% | 56.1% | 35/185 |
| 02 | 0.625 | 0.714 | 0.828 | 0.713 | 49.3% | 60.6% | 35/204 |
| 03 | 0.504 | 0.557 | 0.800 | 0.618 | 36.3% | 40.5% | 29/145 |
| 04 | 0.701 | 0.738 | 0.788 | 0.742 | 71.7% | 75.7% | 42/198 |
| 05 | 0.751 | 0.794 | 0.888 | 0.814 | 65.6% | 58.3% | 32/285 |
| 06 | 0.625 | 0.686 | 0.865 | 0.726 | 48.5% | 52.4% | 28/208 |
| 07 | 0.593 | 0.599 | 0.751 | 0.663 | 38.0% | 36.5% | 50/201 |
| 08 | 0.603 | 0.675 | 0.774 | 0.678 | 41.8% | 54.8% | 43/190 |
| 09 | 0.688 | 0.762 | 0.844 | 0.758 | 42.9% | 59.0% | 19/122 |
| **mean** | **0.631** | **0.693** | **0.817** | **0.711** | **48.9%** | **54.9%** | ~17% |

"Unsupported claims" = conspect claims the judge did **not** find entailed by
slides ∪ transcript (the faithfulness direction). Full per-claim records:
`<lecture-dir>/e1/judgments_faithfulness.json` (`entailed: false`).

Baseline-pipeline reference numbers over the same 9 lectures (raw-transcript
conspect, salience-free decomposition, `all-MiniLM-L6-v2`, top-k 8):
`docs/result-analysis-baseline.md`. Means: coverage 0.453, faithfulness 0.674,
F1 0.539, transcript-only 37.8% — the main pipeline above wins every metric on
every lecture.

Per-lecture spread is real: lecture 05 is best across the board, lecture 03 is
the coverage low point (0.504, and only 36% of spoken-only facts kept),
lecture 07 is the faithfulness low point (0.751, 50 unsupported claims).
Lectures 03 and 07 are the first candidates for manual inspection and conspect
regeneration.

## The "site > deck" thesis in numbers

On average **~49% of the facts the lecturer said but the slides don't show**
(core facts: ~55%) survive into the conspect — a slides-only summarizer scores
~0 here by construction. Lecture 04 is the best case at 72–76%. This is the
project's headline number.

## Faithfulness is a lower bound, not a hallucination rate

A manual audit of lecture 01 checked the 9 most suspicious unsupported claims
(named entities, dates, historical assertions — the classic hallucination
profile) against the raw transcripts and slides. **All of them were actually
grounded**:

| conspect claim (flagged as unsupported) | actually found in |
|---|---|
| Talos threw rocks at approaching ships | transcript ("it would take giant rocks and it would throw…" — ASR garbled the sentence) |
| calligrapher automaton: first programmable device, predates Jacquard looms | transcript ("first actually programmable device right before *Shakira's* looms" = Jacquard, garbled) |
| Turing test passed only in 2025 | transcript ("the models passed, but it's very recent news. It's 2025") |
| models made to "stay in character" | transcript (verbatim; only the added "GPT-4" name is the conspect's embellishment) |
| Deep Blue beat Kasparov; chess dismissed as "just tree search" | transcript ("deep blue *bit Casper off*"; "you can just do a search… doesn't count") |
| Hinton/Bengio labs, GPUs with thousands of cores | transcript (verbatim) |
| Dartmouth: "most ambitious grant proposal in history" | transcript (verbatim quote of the lecturer) |
| O.J. Simpson / Sally Clark probability cases | slides (`slides_reconstructed.md`, the probability-fallacy exercise block) |
| Ramon Llull's logical machine | slides ("a notable early attempt is the logical machine by Ramon Llull") |

So the flagged claims are dominated by **judge/retrieval false negatives**, not
model fabrications. Three mechanisms:

1. **ASR noise defeats embedding retrieval.** "Kasparov" → "Casper off",
   "Jacquard" → "Shakira's", "rocks at ships" → "giant frogs to the animation".
   The claim's embedding no longer matches the garbled source passage, the
   right premise never enters the top-k, and the judge — correctly, given what
   it saw — says "not entailed".
2. **The conspect is penalized for good reconstruction.** The generator
   correctly *repairs* garbled speech (Casper off → Kasparov), which moves the
   conspect's surface form further away from the noisy source. The better the
   reconstruction, the worse the string/embedding match — an inverted
   incentive of the metric, worth a paragraph of its own in the write-up.
3. **Strict NLI + hedge dropping.** The judge requires full entailment; the
   lecturer's hedges ("to my knowledge, the first programmable device") are
   dropped by the conspect, making the claim formally stronger than its source.
   Overgeneralizations ("gated cells are the *only* way…") are rejected for the
   same reason — these are the closest thing to real distortions found.

Consequently the true faithfulness is likely **> 0.9**; 0.817 is the metric's
floor. The residual genuine-hallucination profile that did show up across
lectures: injected outside knowledge with named entities and numbers
("Wu et al. 8 encoder + 8 decoder layers", "RoPE is now the default positional
encoding in most LLMs", "attention is ~2% of total parameters") and
editorial overstatements. Formula-heavy unsupported claims are almost always
retrieval misses — the math is on the slides.

## Correcting the metric with the manual labels

Judge-vs-human agreement (Cohen's κ from `--sample-labels` / `--agreement`)
bounds the error: with prevalence ≈ 0.85, κ = 0.95 implies disagreement on
(1 − κ)(1 − p_e) ≈ 1.3% of claims, i.e. |f_judge − f_human| ≤ ~0.013 in the
worst case. But κ is symmetric and hides the error *direction*, and the audit
above shows the errors are almost entirely one-sided (false negatives). The
right correction is Rogan–Gladen from the labeled sample's confusion matrix:

```
f_true = (f_obs + specificity − 1) / (sensitivity + specificity − 1)
```

e.g. sensitivity 0.98, specificity 1.0 → lecture 06 moves 0.865 → ≈ 0.883.
Report `f_obs`, κ, and the corrected estimate with a bootstrap CI over the
labeled sample (resample labels → re-estimate sens/spec → re-correct); on a
30–50-label sample the CI on κ itself is wide (±0.05–0.1) and must be carried
through.

## On using the same model as generator and judge

Both the conspect and the judge are `deepseek-v4-pro`. A stronger judge than
generator is good practice, but the sharper issue is **self-preference bias**:
LLM judges systematically favor their own outputs. Mitigations, in order of
value per effort:

1. **Calibrate against human labels first** (already supported:
   `--sample-labels`, `--agreement`, `labels_manual.json`). If κ is high, the
   deepseek judge is defensible — cite the number.
2. **Cross-family judge:** the structured-output path already supports
   Anthropic (`claude-*`); re-judge with a second family and compare. If both
   judges agree, the result is robust — stronger evidence than simply
   swapping in a bigger model.

For entailment judging specifically, calibration matters more than raw model
size; a reasoning model is already a competent NLI judge.

## Action items

- [ ] Run `--sample-labels` calibration on 2–3 lectures, report corrected
      faithfulness with CI.
- [ ] Manually inspect lectures 03 (coverage) and 07 (faithfulness) —
      worst outliers, likely conspect regeneration candidates.
- [ ] Consider raising top-k (or unioning premises from both STT providers)
      to cut retrieval false negatives on garbled passages.
- [ ] Cross-family judge run (Claude) on one lecture as a robustness check.
