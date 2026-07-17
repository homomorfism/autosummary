# Slide ↔ transcript alignment — embeddings vs embeddings + DTW

**Code:** `app/align.py` (alignment + proxy metrics), `app/align_video.py`
(video-frame ground truth + evaluation) · **Artifacts:**
`<lecture-dir>/align/alignment.json`, `align/video_labels.json` ·
**Run:** `uv run python -m app.align <lecture-dir>…` then
`uv run python -m app.align_video <lecture-dir>…`

## Goal

Assign every transcript time window to the slide being discussed, with no human
labels — the P2 experiment from `TODO.md` §6. Two questions:

1. Does embedding similarity actually align windows to the right slides
   (vs a trivial "slides spread evenly over time" baseline)?
2. What does adding a **monotonicity constraint** (DTW-style dynamic
   programming: the lecturer never goes back to an earlier slide) buy, and
   what does it cost?

## Pipeline

```
slides_extracted/slides.md ──► slide units (overlay frames collapsed)
<stt>/transcription.json ───► 60 s text windows          ─► embed both ─► cosine sim matrix
                                                              ├─► plain: argmax per window
                                                              └─► dtw:   max-similarity monotonic path
```

- **Slide units** come from the raw per-page `slides.md` (unlike
  `slides_reconstructed.md` it keeps page boundaries). Consecutive beamer
  overlay frames — page *N+1*'s text extends page *N*'s — collapse into one
  unit spanning the page range; page-number footers are dropped. Across the 9
  lectures this turns 619 pages into 567 units.
- **Windows** are fixed 60 s slices (configurable `--window/--stride`); a
  segment belongs to the window containing its midpoint; silent windows are
  skipped.
- **Embeddings** — `E1_EMBED_MODEL` (default `BAAI/bge-small-en-v1.5`),
  normalized, cosine = dot product; dependency-free TF-IDF fallback
  (`--backend tfidf`).
- **plain** assigns each window independently to its most-similar unit.
  **dtw** finds the highest-total-similarity path with non-decreasing slide
  index (`best[w][s] = sim[w][s] + max_{s'≤s} best[w-1][s']`, prefix-max DP,
  backtracked). Slides may be skipped or dwelt on, never revisited.

## Proxy metrics (no labels)

| metric | what it measures |
|---|---|
| **keyword hit rate** | each unit gets its 10 most distinctive terms (TF-IDF within the deck, stopwords out); score = mean fraction of a unit's keywords found in the windows assigned to it. Content grounding. |
| **monotonicity** | share of consecutive window pairs whose slide index does not decrease (dtw = 1.0 by construction). |
| **Kendall τ-b** | rank correlation between window order and slide order — an order measure that, unlike the step share, punishes big backward jumps more than small ones. |
| **slide coverage** | fraction of units that received ≥ 1 window. |

The **uniform** baseline (slides spread evenly over the lecture duration, in
order) is perfectly monotone by construction, so it calibrates the keyword
metric: any real alignment must beat its keyword hit rate to be doing anything.

## Results — 9 lectures (deep-learning-and-computer-vision), 2026-07-16

whisper_cpp transcripts, `BAAI/bge-small-en-v1.5`, 60 s windows. Aggregate
(mean over lectures):

| method | keyword hit | monotone steps | Kendall τ-b | slide coverage |
|---|---|---|---|---|
| uniform baseline | 0.152 | 1.000 | 0.994 | 1.000 |
| plain (argmax cosine) | **0.379** | 0.661 | 0.416 | **0.533** |
| embeddings + DTW | 0.377 | **1.000** | **0.901** | 0.348 |

Per-lecture keyword hit rate (uniform / plain / dtw):

| lecture | pages→units | windows | uniform | plain | dtw |
|---|---|---|---|---|---|
| 01 | 66→62 | 190 | 0.203 | 0.388 | **0.423** |
| 02 | 67→61 | 181 | 0.161 | 0.383 | **0.430** |
| 03 | 69→68 | 176 | 0.121 | 0.359 | **0.364** |
| 04 | 21→19 | 89 | 0.325 | **0.388** | 0.369 |
| 05 | 83→79 | 96 | 0.073 | **0.396** | 0.281 |
| 06 | 82→80 | 176 | 0.177 | 0.441 | **0.473** |
| 07 | 62→60 | 101 | 0.142 | **0.402** | 0.367 |
| 08 | 87→67 | 96 | 0.078 | **0.308** | 0.297 |
| 09 | 82→71 | 96 | 0.090 | 0.346 | **0.386** |

## Reading the numbers

- **Embedding alignment works.** Both methods hit ~2.5× the uniform baseline's
  keyword rate (0.38 vs 0.15). The windows land on slides whose distinctive
  vocabulary the lecturer is actually using.
- **The monotonicity constraint is free on grounding.** DTW matches plain's
  keyword hit rate (0.377 vs 0.379 aggregate; wins 5/9 lectures) while fixing
  plain's ordering completely: plain violates order at a third of all steps
  (0.661 monotone, τ-b 0.416), DTW is monotone by construction. Plain's jumps
  are real errors, not real revisits — when forced onto a monotone path the
  content grounding does not degrade. **DTW is the method to build on.**
- **DTW trades coverage for dwelling.** It assigns windows to fewer distinct
  slides (0.348 vs 0.533 coverage) — the path dwells on content-heavy slides
  and skips thin ones (section dividers, picture-only pages, which pypdf
  extracts as a bare title). Low coverage is partly honest: lectures 05/08
  have ~80 slide pages but only ~96 spoken minutes, so much of the deck was
  never discussed.
- **Where plain wins on keywords (04, 05, 07, 08), the margin is small** and
  these are exactly the low-coverage/short lectures where per-window argmax can
  cherry-pick any slide for each window while a monotone path cannot.

## Validation against video ground truth

The recordings are Zoom screen shares — the slide actually shown on screen
**is** the ground truth, no hand-labelling needed. `app/align_video.py` reads
it off the video: one keyframe every 15 s, cropped to the slide region (left
74.7% of the frame; the rest is the webcam), downscaled to 96×72 grayscale and
matched against `pdftoppm` renders of every PDF page by normalized
correlation. The score distribution is sharply bimodal — a slide on screen
scores > 0.9 against its page, the hand-drawn whiteboard the lecturer uses the
rest of the time scores < 0.35 against everything — so a 0.7 threshold cleanly
labels each moment as "page N" or "no slide". A transcript window gets a
ground-truth unit when ≥ half its frame samples show a slide (majority page).

Two facts the video revealed about the data itself:

- **Slides are on screen only 10–54% of the time** (median ~32%); the rest is
  a hand-drawn whiteboard. Text alignment can only be judged where a slide is
  actually up — 431 of 1 201 windows got labels.
- **Revisits are real:** e.g. in lecture-01 the on-screen slide returns to an
  earlier unit at minutes 109 and 199–200 — exactly what the hard monotonicity
  constraint cannot follow.

Accuracy on the slide-visible windows (aggregate over 9 lectures):

| method | exact unit | ±1 unit | mean unit distance |
|---|---|---|---|
| uniform baseline | 0.119 | 0.203 | 13.3 |
| plain (argmax cosine) | 0.194 | 0.319 | 13.6 |
| embeddings + DTW | **0.220** | **0.382** | **10.6** |

Takeaways:

- **The proxy ranking is confirmed by ground truth:** DTW ≥ plain > uniform on
  real accuracy too (DTW wins exact accuracy on 6 of 9 lectures). The
  keyword-hit proxy also tracks true accuracy *across* lectures: Spearman
  ρ = 0.80 (Pearson r = 0.66, n = 9) between per-lecture keyword hit rate and
  exact accuracy for DTW — a lecture where the proxy is low really is aligned
  worse.
- **Absolute accuracy is modest: ~22% exact, ~38% within ±1 unit.** Exact
  slide-level alignment from text alone is hard: the lecturer dwells on one
  slide for 10+ minutes of verbal examples (windows drift to lexically-closer
  neighbours), intro/outro talk matches nothing, and picture-only slides are
  invisible to text embeddings.
- **A caveat in both directions:** ground truth is *what is on screen*, and
  during long dwells the lecturer sometimes talks ahead of (or behind) the
  visible slide, so "text says unit 12, screen shows unit 8" is not always an
  alignment error. The GT itself is also unavailable during whiteboard
  segments, where the text aligners are forced to guess some slide.
- Practical upshot: for a slide↔time UI the **video labels themselves** are the
  better aligner wherever slides are visible (they are near-perfect and cost
  ~35 s of ffmpeg per 3.5 h lecture); the text alignment is the fallback for
  whiteboard/no-video segments — and DTW is the variant to use.

## Commands

```bash
uv run python -m app.align data/<course>/<lecture>              # one lecture
uv run python -m app.align data/<course>/lecture-0{1..9}        # batch + aggregate row
uv run python -m app.align <dir> --stt google_stt               # other transcript
uv run python -m app.align <dir> --window 90 --stride 45        # overlapping windows
uv run python -m app.align <dir> --backend tfidf                # no torch/model download

# video ground truth + accuracy evaluation (needs ffmpeg + poppler's pdftoppm)
uv run python -m app.align_video data/<course>/<lecture>        # after app.align
uv run python -m app.align_video <dir> --every 10 --threshold 0.75
```

`align/alignment.json` stores the settings, the collapsed units (page ranges +
titles), window timestamps, all three assignments, the per-slide keywords, and
the metrics — enough to render a slide↔time UI or seed E2 question timestamps
without recomputing.

## Known limitations / next steps

- ~~Proxy metrics are not ground truth~~ — **validated**: the video-frame
  ground truth (above) confirms the proxy ranking and shows the keyword-hit
  proxy tracks true accuracy across lectures (ρ ≈ 0.8).
- **No repeated-visit support.** The DP allows skips but never a return to an
  earlier slide — and the video labels show real revisits (lecture-01 returns
  to an earlier unit at minutes 109 and 199). A small constant "revisit
  penalty" instead of a hard constraint would cover this.
- **Fuse the two sources.** The obvious next step is a combined aligner:
  video labels pin the slide wherever one is on screen; the text DP fills the
  whiteboard gaps between those anchors (DP with pinned states). Ground truth
  and prediction then need to be kept honestly separate — evaluate on held-out
  anchors.
- **Silence about confidence.** No per-window confidence is exported; the
  margin between the best and second-best similarity would flag the spans
  where the alignment is guessing (e.g. Q&A breaks, administrative talk).
- **Picture-only slides are invisible** — pypdf extracts no text, the unit is
  a bare title, and nothing aligns to it. OCR or vision-model slide
  descriptions would fix both this and the coverage number.
