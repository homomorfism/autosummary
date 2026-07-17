# TODO — Lecture Autosummary

Project tasks, grouped by area. The `[P0]` tag means critical for submission, `[P1]` means important, `[P2]` means an improvement / further work.

Status: `[x]` — done, `[~]` — partial, `[ ]` — not started.

> Contest deadlines: 2nd wave — projects accepted until **July 1**, 3rd wave — until **July 20**. Minimum for submission: pipeline + E1 + E3.

---

## 0. Contest submission (organizational)

- [ ] `[P0]` Submit the application to participate → the upload form will arrive by email
- [ ] `[P0]` Register in the [applicant portal](https://abitlk.itmo.ru/), choose a program
- [ ] `[P0]` Choose a wave (2nd until 07/01 / 3rd until 07/20) and lock in the deadline
- [ ] `[P0]` Prepare the package: CV, motivation letter, repository link, project description (PDF), slides
- [ ] `[P1]` Build slides from the [template](https://docs.google.com/presentation/d/1cH42eNBEUKBulLkOK8Nd6UDPbKQ70JWkZ7yRAJQ2SM8/edit) (5 min pitch + 7 min Q&A)
- [ ] `[P1]` Sign up for the defense, rehearse the pitch on a timer
- [ ] `[P0]` After winning — upload the certificate to section 4 of the portfolio Contest

---

## 1. Pipeline and engineering

- [~] `[P0]` End-to-end pipeline: `video → STT → alignment → summarization → questions → webapp` — partial: `video → STT → summarization` works (`python -m app.run`); alignment exists standalone (`python -m app.align`, not wired into `app.run`); questions / webapp run per-lecture (`app.quiz`, `web/`)
- [x] `[P0]` STT provider abstraction (shared interface for Google STT and whisper.cpp) — `app/stt/base.py` (`STTProvider`, unified `Transcript`)
- [x] `[P0]` Google STT adapter (cloud) — `app/stt/google_stt.py` (long_running_recognize + upload to GCS), verified on the 10-min set
- [x] `[P0]` whisper.cpp adapter (local run) — `app/stt/whisper_cpp.py` (anti-hallucination flags + VAD), `build-nocoreml` build
- [x] `[P0]` Summarization module: input — transcript + slide text, output — structured summary — `app/summarize/` (Claude + structured outputs, grounded on the source)
- [x] `[P0]` Web app: render the summary by URL + question block — `web/` (Next.js, `cd web && npm run dev`; replaced the original Flask `app/web`): lecture list → conspect → quiz → results (saved to SQLite) → item stats
- [ ] `[P1]` Dockerfile + docker-compose for the whole service
- [ ] `[P1]` CI (lint, run tests, build image)
- [x] `[P1]` Configuration via .env / config (API keys, provider choice) — `app/config.py` + `.env.example`
- [ ] `[P2]` Upload and share materials between users (democratize education)

---

## 2. Data and golden set

- [x] `[P0]` Collect 3–5 lectures from your own course: video + PDF slides — 9 lectures in `data/deep-learning-and-computer-vision/`
- [x] `[P0]` Extract text and bullets from the PDF slides — `app/slides.py` (text per slide, `SlideDeck`)
- [x] `[P0]` Golden set: manually transcribe 10 minutes of audio into a reference transcript — done on lecture-06: ~19.5 min manually labelled (`data/golden-label/lecture-06/golden.md`, 2:01:41–2:21:15) + matching `whisper.md` / `google.md` from both providers for the same segment
- [x] `[P1]` On the golden set, manually label ~10 "fact ↔ present in summary" pairs to calibrate the judge — done on lecture-06: 40 pairs labelled in `e1/labels_manual.json` (`--sample-labels 40`)
- [ ] `[P2]` Deduplication script for near-duplicate facts (clustering by embeddings)

---

## 3. Experiment E1 — Claim-level summary evaluation `[P0]`

- [x] `[P0]` Decompose text into atomic facts (slides / transcript / summary) via LLM — `app/e1.py` (chunked, cached to `<lecture>/e1/claims.json`; slides source = `slides_reconstructed.md`, same as the conspect input)
- [x] `[P0]` Unified `entails(claim, claim_set)` function: retrieve (top-k embeddings) + confirm (NLI / LLM judge) — `app/e1.py` (sentence-transformers retrieval, TF-IDF fallback; batched LLM judge)
- [x] `[P0]` **Coverage** metric (recall): share of source facts that made it into the summary — implemented; full-lecture numbers still to be produced
- [x] `[P0]` **Faithfulness** metric (precision): share of summary facts grounded on the source — implemented
- [x] `[P0]` Combine into the summary **F1** — implemented
- [x] `[P0]` transcript-only metric: share of spoken facts (not on the slides) preserved in the web summary → proof that "site > slides" — implemented (`transcript_only_coverage` in `e1/e1.json`)
- [x] `[P1]` Check the LLM judge's agreement with the manual labels on the golden set — lecture-06, 40 pairs: 39/40 agree (97.5%), Cohen's κ = 0.95, 0 FP / 1 FN (`--agreement`; details in `docs/experiments/e1.md`)
- [ ] `[P2]` Deduplicate facts before counting so repeats don't inflate the denominator

---

## 4. Experiment E2 — STT provider benchmark `[P1]`

- [x] `[P1]` ~~**TER** without labels: extract terms from the slides → fuzzy search in the transcript → share recognized~~ — prototyped, then **dropped from the write-up**: the slide deck is too weak a reference (bibliography names / title-slide trivia are never spoken), so the absolute numbers weren't presentable; WER on the golden set is the quality metric of record
- [x] `[P1]` **WER** on the golden set for each provider — `notebooks/wer_ter.ipynb` on `data/golden-label/lecture-06`: whisper_cpp **2.3 %** vs google_stt **16.3 %** WER (TER likewise)
- [x] `[P1]` Measure latency and cost ($/hour) for each provider — `app/e2.py`: latency from `meta.latency_sec` (RTF 0.123 vs 0.141 on 21.3 h); cost: Google API rate card $1.44/audio-h (V1 no-logging $0.024/min) vs whisper priced at vast.ai RTX 4090 rates ≈ $0.04/audio-h ($0 on own HW)
- [x] `[P1]` Final table: Provider × {WER, latency, $/hour, locality} — `docs/experiments/e2.md` (raw numbers in `docs/experiments/e2.json`)
- [ ] `[P2]` Term post-processing (dictionary from the slides) and measure the quality gain

---

## 5. Experiment E3 — Question psychometrics `[P0]`

- [x] `[P0]` Generate questions from the summary (with options / reference answer) — `app/quiz.py` (`python -m app.quiz <lecture-dir>` → `quiz.json`, 5 single-choice questions with per-option explanations)
- [~] `[P0]` Collect responses from 15 students in the group (who answered which question correctly) — collection tooling ready: the web quiz (`web/`, Next.js) stores every attempt/answer in `data/quiz_results.db`; the actual student responses remain
- [x] `[P0]` **Difficulty** (p-value) for each question — `app/quality.py` (`python -m app.quality <lecture-dir>`) + live `/stats` page
- [x] `[P0]` **Discrimination** (point-biserial correlation) for each question — `app/quality.py`, computed against the rest score (item's own contribution excluded)
- [x] `[P0]` Rejection rule: questions outside the target difficulty range → retire — `--retire`: p ∉ [0.30, 0.85] or r_pb < 0.15 (with ≥5 attempts) → removed from `quiz.json`, archived in DB with stats
- [x] `[P1]` Adaptive regeneration: replace bad questions to hit the target difficulty (closed loop) — `--regenerate`: LLM writes replacements conditioned on the retired questions' measured stats and miss direction
- [ ] `[P1]` Explicit caveat about sample size (n=15): methodology matters more than statistical significance

---

## 6. Slide ↔ transcript alignment `[P2]`

- [x] `[P2]` Embeddings of slide text and transcript windows → alignment by cosine similarity — `app/align.py` (`python -m app.align <lecture-dir>`): per-page slide units (beamer overlays collapsed) × 60 s windows, `E1_EMBED_MODEL` cosine, results in `<lecture-dir>/align/alignment.json`
- [x] `[P2]` Proxy metric without labels: slide keywords landing in the window + timecode monotonicity — per-slide TF-IDF keywords → hit rate, monotone-step share + Kendall τ-b, vs a time-uniform baseline (see `docs/experiments/alignment.md`)
- [x] `[P2]` Compare plain embeddings vs embeddings + DTW (monotonicity constraint) — 9 lectures: keyword hit 0.379 vs 0.377 (2.5× the uniform baseline), monotonicity 0.66 vs 1.0 — the constraint is free on grounding, DTW wins (`docs/experiments/alignment.md`)
- [x] `[P2]` Validate the proxies against ground truth — done better than hand-labelling: `app/align_video.py` reads the slide shown on screen off the Zoom recording (frame ↔ `pdftoppm` page render matching, bimodal scores, 0.7 threshold). 9 lectures: DTW ≥ plain > uniform confirmed (exact accuracy 0.22 / 0.19 / 0.12 on slide-visible windows); keyword proxy tracks true accuracy across lectures (ρ≈0.8). Slides are on screen only ~1/3 of the time (rest is a hand-drawn whiteboard)
- [ ] `[P2]` Soft revisit penalty instead of the hard monotonicity constraint — video labels show real revisits (lecture-01 returns to an earlier slide at min 109 and 199)
- [ ] `[P2]` Fused aligner: video labels pin slide-visible spans, text DP fills the whiteboard gaps between anchors (evaluate on held-out anchors)

---

## 7. Documents and slides

- [ ] `[P0]` Project description (PDF, ≤3 pages) — fill in with numbers after E1/E3
- [ ] `[P0]` Repository README with run instructions
- [ ] `[P1]` CV (PDF)
- [ ] `[P1]` Motivation letter (why AI/ML, why AI Talent Hub)
- [ ] `[P1]` Defense slides
- [ ] `[P1]` Record a short demo video of the web summary in action

---

## 8. Security and deployment hardening

From the `/cso` audit on 2026-07-13 (full report: `.gstack/security-reports/2026-07-13-094500.json`, gitignored).
Zero findings cleared the 8/10 confidence gate. Everything below is hardening or hygiene, not an open vulnerability.

- [ ] `[P1]` Production container runs as root — add `USER node` to the runner stage of `web/Dockerfile` and make `/data` writable by that uid. Today `node server.js` runs as uid 0 with a read-write bind mount of `./data`, so any future RCE gets root over the whole host data tree, and SQLite files land on the host owned by root
- [ ] `[P2]` Harden the prod compose service: add `security_opt: [no-new-privileges:true]` and `cap_drop: [ALL]` to the `quiz` service in `docker-compose.prod.yml`
- [ ] `[P1]` Before open-sourcing: rewrite git history to drop the GCP project id / bucket name still present in the old `.env.example` (commit `7dfa269`, blanked in `7e2aac7`). Identifiers, not credentials — gitleaks is clean over all 12 commits and no key material was ever committed — but they should not ship with a public repo
- [ ] `[P2]` Sanity-check attempt counts before acting on `app.quality --retire`: `/api/attempts` is anonymous and unbounded by design, and `MIN_ATTEMPTS = 5` means a handful of forged attempts can move a question's p-value past the rejection threshold. The per-question `n` in the report is the tell (200 attempts for a 15-student cohort = ignore the stats)
- [ ] `[P2]` Defense-in-depth on the markdown pipeline: add `rehype-sanitize` to `web/src/lib/markdown.ts` with a schema allowing KaTeX spans and the timestamp span. Not attacker-reachable today (conspects are operator-authored and rsync-deployed), but it removes the raw-HTML sink if lecture material ever becomes untrusted

---

## Minimum scope for the deadline (if time is tight)

For a convincing submission it's enough to have: **a working pipeline (section 1)** + **E1 (coverage/faithfulness)** + **E3 (psychometrics)**. E2 and alignment can be flagged in the description as "partially done / further work".
