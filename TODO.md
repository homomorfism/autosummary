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

- [~] `[P0]` End-to-end pipeline: `video → STT → alignment → summarization → questions → webapp` — partial: `video → STT → summarization` works (`python -m app.run`); alignment / questions / webapp not yet
- [x] `[P0]` STT provider abstraction (shared interface for Google STT and whisper.cpp) — `app/stt/base.py` (`STTProvider`, unified `Transcript`)
- [x] `[P0]` Google STT adapter (cloud) — `app/stt/google_stt.py` (long_running_recognize + upload to GCS), verified on the 10-min set
- [x] `[P0]` whisper.cpp adapter (local run) — `app/stt/whisper_cpp.py` (anti-hallucination flags + VAD), `build-nocoreml` build
- [x] `[P0]` Summarization module: input — transcript + slide text, output — structured summary — `app/summarize/` (Claude + structured outputs, grounded on the source)
- [ ] `[P0]` Web app: render the summary by URL + question block
- [ ] `[P1]` Dockerfile + docker-compose for the whole service
- [ ] `[P1]` CI (lint, run tests, build image)
- [x] `[P1]` Configuration via .env / config (API keys, provider choice) — `app/config.py` + `.env.example`
- [ ] `[P2]` Upload and share materials between users (democratize education)

---

## 2. Data and golden set

- [x] `[P0]` Collect 3–5 lectures from your own course: video + PDF slides — 9 lectures in `data/deep-learning-and-computer-vision/`
- [x] `[P0]` Extract text and bullets from the PDF slides — `app/slides.py` (text per slide, `SlideDeck`)
- [~] `[P0]` Golden set: manually transcribe 10 minutes of audio into a reference transcript — 10-min set of lecture-01 + transcripts from both providers ready (`data/gcloud/_test_course/lecture-01/`, GCS); the manual reference annotation remains
- [ ] `[P1]` On the golden set, manually label ~10 "fact ↔ present in summary" pairs to calibrate the judge
- [ ] `[P2]` Deduplication script for near-duplicate facts (clustering by embeddings)

---

## 3. Experiment E1 — Claim-level summary evaluation `[P0]`

- [ ] `[P0]` Decompose text into atomic facts (slides / transcript / summary) via LLM
- [ ] `[P0]` Unified `entails(claim, claim_set)` function: retrieve (top-k embeddings) + confirm (NLI / LLM judge)
- [ ] `[P0]` **Coverage** metric (recall): share of source facts that made it into the summary
- [ ] `[P0]` **Faithfulness** metric (precision): share of summary facts grounded on the source
- [ ] `[P0]` Combine into the summary **F1**
- [ ] `[P0]` transcript-only metric: share of spoken facts (not on the slides) preserved in the web summary → proof that "site > slides"
- [ ] `[P1]` Check the LLM judge's agreement with the manual labels on the golden set
- [ ] `[P2]` Deduplicate facts before counting so repeats don't inflate the denominator

---

## 4. Experiment E2 — STT provider benchmark `[P1]`

- [ ] `[P1]` **TER** without labels: extract terms from the slides → fuzzy search in the transcript → share recognized
- [ ] `[P1]` **WER** on the golden set for each provider
- [ ] `[P1]` Measure latency and cost ($/hour) for each provider
- [ ] `[P1]` Final table: Provider × {WER, TER, latency, $/hour, locality}
- [ ] `[P2]` Term post-processing (dictionary from the slides) and measure the quality gain

---

## 5. Experiment E3 — Question psychometrics `[P0]`

- [ ] `[P0]` Generate questions from the summary (with options / reference answer)
- [ ] `[P0]` Collect responses from 15 students in the group (who answered which question correctly)
- [ ] `[P0]` **Difficulty** (p-value) for each question
- [ ] `[P0]` **Discrimination** (point-biserial correlation) for each question
- [ ] `[P0]` Rejection rule: questions outside the target difficulty range → retire
- [ ] `[P1]` Adaptive regeneration: replace bad questions to hit the target difficulty (closed loop)
- [ ] `[P1]` Explicit caveat about sample size (n=15): methodology matters more than statistical significance

---

## 6. Slide ↔ transcript alignment `[P2]`

- [ ] `[P2]` Embeddings of slide text and transcript windows → alignment by cosine similarity
- [ ] `[P2]` Proxy metric without labels: slide keywords landing in the window + timecode monotonicity
- [ ] `[P2]` Compare plain embeddings vs embeddings + DTW (monotonicity constraint)

---

## 7. Documents and slides

- [ ] `[P0]` Project description (PDF, ≤3 pages) — fill in with numbers after E1/E3
- [ ] `[P0]` Repository README with run instructions
- [ ] `[P1]` CV (PDF)
- [ ] `[P1]` Motivation letter (why AI/ML, why AI Talent Hub)
- [ ] `[P1]` Defense slides
- [ ] `[P1]` Record a short demo video of the web summary in action

---

## Minimum scope for the deadline (if time is tight)

For a convincing submission it's enough to have: **a working pipeline (section 1)** + **E1 (coverage/faithfulness)** + **E3 (psychometrics)**. E2 and alignment can be flagged in the description as "partially done / further work".
