# Project Description

## Autosummary for lectures — an AI summary with comprehension checks

**Junior ML Contest 2026 · AI Talent Hub, ITMO**

| | |
|---|---|
| **Author** | [Full name] |
| **Track** | Graduation thesis |
| **Program** | "Artificial Intelligence" / "AI Product Management" |
| **Repository** | https://github.com/homomorfism/autosummary |
| **Demo** | [URL of the live web summary] |

> Italics in square brackets are placeholders: fill in your own data and final numbers after running the experiments.

---

## 1. Problem and target audience

A student watches a lecture but cannot tell whether they truly understood it. Slides lose the lecturer's spoken explanations (examples, caveats, the "this will be on the exam" emphasis), while a full video recording is too long to review. The target audience is students in technical fields preparing for exams and retakes.

**Product mission — democratize education:** students from all over the world upload and share their course materials and can study lectures from other universities.

## 2. What the system does

The input is a lecture video recording and a presentation. The output is a web summary (HTML at a URL) that combines recognized speech with slides and then checks comprehension with a set of adaptive "tricky questions." The pipeline solves several subtasks:

- speech recognition (STT) with support for swappable providers;
- alignment of slides and transcript by timecodes;
- multi-source summary generation (slides + speech) grounded in the sources;
- generation and adaptive selection of questions by difficulty level.

## 3. Data

Real lectures from our own course (15 students in the group — a source of responses for psychometrics). For each lecture: video, PDF presentation, and a generated summary.

**Golden set:** 10 minutes of audio manually annotated into a reference transcript — for evaluating STT and calibrating the automatic judge. The annotation effort is minimal and requires no external dataset; the slides and transcript themselves serve as weak references for most metrics.

## 4. Architecture and methods

**Pipeline:** `video → STT (swappable provider) → slide↔transcript alignment by embeddings → multi-source summarization (LLM) → question generation → web app`.

**The STT provider abstraction** allows switching between Google STT (cloud) and whisper.cpp (local, private, free) — the "quality / cost / privacy" trade-off is chosen per scenario. The service is containerized (Docker), with automated builds and checks (CI).

## 5. Experiments and metrics (Data Science)

The core of the work is three measurable experiments. All metrics are computed automatically; manual annotation is limited to the 10-minute golden set.

| Experiment | What we measure | Metrics |
|---|---|---|
| **E1. Claim-level summary evaluation** | A single `entails(claim, set)` engine: decomposition of slides / transcript / summary into atomic facts, then retrieve (embeddings, top-k) + confirm (NLI / LLM judge). | Coverage (recall), Faithfulness (precision), F1 |
| **E2. STT provider benchmark** | Comparison of Google STT vs whisper.cpp. TER is computed without annotation — terms are taken from the slides and matched against the transcript via fuzzy matching; WER is measured on the golden set. | WER ↓, TER ↓, latency, $/hour |
| **E3. Question psychometrics** | Responses from 15 students are turned into test-theory data; bad questions are automatically retired and regenerated to hit a target difficulty. | Difficulty (p-value), Discrimination (point-biserial) |

**Key idea of E1:** coverage and faithfulness are the same entailment engine, with the "source of truth" and the "text under test" swapped. This way a single function yields both axes of summary quality and lets us numerically prove that the web summary is richer than the presentation: we measure the share of *transcript-only* facts (spoken but absent from the slides) that the web summary preserves. By definition, the slides cover them 0%.

**STT benchmark results template** (fill in after the run):

| Provider | WER ↓ | TER ↓ | Cost | Local |
|---|---|---|---|---|
| Google STT | [—] | [—] | [$/hour] | no |
| whisper.cpp (large) | [—] | [—] | 0 (local) | yes |

## 6. Results (to be filled in)

- Summary quality: coverage = *[—]*%, faithfulness = *[—]*%; share of preserved transcript-only facts = *[—]*%.
- Agreement of the LLM judge with manual annotation on the golden set = *[—]*%.
- STT: best provider by WER/TER — *[—]*; the quality/cost trade-off is described in the table above.
- Psychometrics: out of *[N]* generated questions, *[—]* were rejected by difficulty/discrimination and *[—]* were regenerated.
- Product feedback: *[N]* students tested the web summary; key takeaways — *[briefly]*.

## 7. Alignment with the contest criteria

| Criterion | How the project addresses it |
|---|---|
| **Development and engineering** | A video→STT→alignment→summarization→questions pipeline delivered as a service; abstraction over swappable STT providers; Docker, CI, a structured codebase. |
| **Data Science** | Three experiments with metrics and validation: claim-level evaluation (coverage/faithfulness), STT benchmark (WER/TER), question psychometrics (difficulty/discrimination) with a closed regeneration loop. |
| **Applying AI** | STT, multi-source LLM summarization, NLI / LLM-as-judge for grounding, question generation; optionally an agentic tutor layer. |
| **Product thinking** | A clear problem and target audience, a working MVP (web summary at a URL), the democratize-education mission with material sharing, and feedback from a real group. |
| **Motivation** | The project is my own ML graduation thesis; goals in AI/ML and EdTech align with the AI Talent Hub project-based master's program (detailed in the motivation letter). |

## 8. Stack and future work

**Stack:** Python, Google STT / whisper.cpp, LLM (summarization and judge), sentence embeddings, an NLI model, an HTML/JS web app, Docker, CI.

**Future work:** an agentic tutor with an adaptive review plan; self-supervised evaluation of slide↔transcript alignment (DTW + monotonicity); cross-university clustering of courses by embeddings.
