# Lecture Autosummary

> Upload a lecture video and slides — get an interactive web summary and check whether you actually understood the material.

An AI service that turns a lecture recording and slides into a structured summary (HTML served by URL) and checks comprehension with a set of adaptive questions. Built for [Junior ML Contest 2026](https://ai.itmo.ru/junior_ml_contest) (AI Talent Hub, ITMO), graduation thesis track.

---

## What it does

- **Recognizes the lecturer's speech** with swappable STT providers (Google STT in the cloud or whisper.cpp locally).
- **Aligns** slides and transcript by timecodes.
- **Generates a summary** from two sources at once — slides and spoken speech — grounding every statement on its source.
- **Checks comprehension**: a set of "tricky questions" that are automatically discarded and regenerated based on psychometrics.

The core idea: a lecturer's spoken speech contains things that aren't on the slides (examples, caveats, emphasis). The web summary preserves this information — and the project proves it numerically.

## Architecture

```
video ──► STT (Google / whisper.cpp) ──► transcript
                                              │
PDF slides ──► slide text ─────────────┐      │
                                       ▼      ▼
                            slide ↔ transcript alignment
                                       │
                                       ▼
                        multi-source summarization (LLM)
                                       │
                          ┌────────────┴────────────┐
                          ▼                          ▼
                    web summary (HTML)        question generation
                                                     │
                                          adaptive selection (psychometrics)
```

## Quality metrics

The project doesn't just generate text — it measures its quality:

| Metric | What it shows |
|---|---|
| **Coverage** (recall) | what share of facts from the slides and speech made it into the summary |
| **Faithfulness** (precision) | what share of summary statements are grounded on a source (no hallucinations) |
| **transcript-only retained** | share of spoken facts (absent from the slides) preserved in the summary |
| **WER / TER** | speech and technical-term recognition quality across providers |
| **Difficulty / Discrimination** | question psychometrics: difficulty and ability to separate those who understood from those who didn't |

> Coverage and faithfulness are computed by the same `entails(claim, set)` engine — the "source of truth" and the "text under check" simply swap places.

## Stack

Python · Google Cloud STT / whisper.cpp · LLM (summarization and judge) · sentence embeddings · NLI model · HTML/JS · Docker · CI

## Installation

```bash
git clone https://github.com/homomorfism/autosummary.git
cd [repo]

# dependencies
pip install -r requirements.txt

# (optional) local STT
# build whisper.cpp following the instructions in their repository

# configuration
cp .env.example .env
# fill in the keys: GOOGLE_STT_KEY, LLM_API_KEY, choose the STT provider STT_PROVIDER=...
```

Or via Docker:

```bash
docker compose up --build
```

## Usage

```bash
# build a summary from video and slides
python -m app.run --video lecture.mp4 --slides slides.pdf --provider whisper_cpp

# launch the web app
python -m app.web   # the summary will be available at http://localhost:8000/[id]
```

## Reproducing the experiments

```bash
python -m experiments.e1_claim_eval   --lecture data/lectures/L01   # coverage / faithfulness / F1
python -m experiments.e2_stt_bench    --golden data/golden_10min     # WER / TER / latency / cost
python -m experiments.e3_psychometrics --responses data/responses.csv # difficulty / discrimination
```

## Repository structure

```
app/            pipeline and web app
  stt/          STT providers (shared interface + adapters)
  align/        slide ↔ transcript alignment
  summarize/    multi-source summarization
  questions/    question generation and selection
  web/          HTML summary
experiments/    E1 / E2 / E3 — scripts and metrics
eval/           entails() engine and metrics
data/           lectures, golden set, student responses (don't commit private data)
```

## Status and further work

For the current status, see [`TODO.md`](./TODO.md). The full contest write-up is in [`project_description.md`](./docs/project_description.md).

Planned: an agentic tutor with an adaptive review schedule; self-supervised alignment scoring (DTW + monotonicity); cross-university course clustering by embeddings.
