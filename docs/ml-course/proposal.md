# Lecture Autosummary: From Lecture Recordings to Verified Understanding

**Final Project Proposal**
Author: [Your Name] · Course: [Course Name] · Date: July 2026
Repository: https://github.com/homomorfism/autosummary

---

## Part 1. Problem Formulation

### 1.1 Project Description

University lectures carry two parallel information streams: the slides and the lecturer's spoken speech. Slides are compact and persistent; speech contains what slides omit — worked examples, caveats, intuitions, and emphasis. Today, when students revise, they usually have only the slides (or a raw, unwatchable 90-minute recording), so the spoken layer of the course is effectively lost.

**Lecture Autosummary** is an AI service that takes a lecture recording and its slide deck and produces:

1. an **interactive web summary** (HTML, served by URL) that fuses both sources and grounds every statement on where it came from — slide or speech;
2. an **adaptive comprehension check** — a set of automatically generated questions that are filtered and regenerated based on psychometric quality (difficulty, discrimination), so the student learns whether they actually understood the material, not just skimmed it.

The core hypothesis, which the project verifies numerically, is that **a meaningful share of lecture content exists only in speech** and can be preserved by multi-source summarization.

### 1.2 Machine Learning Problem Statement

The system decomposes into four ML sub-problems:

1. **Speech-to-text (STT).** Transcribe the lecture audio. Formally: given audio $A$, produce transcript $T$ minimizing word error rate (WER) and, critically for lectures, technical-term error rate (TER). Swappable providers: Google Cloud STT (cloud) vs whisper.cpp (local).
2. **Slide–transcript alignment.** Given slide texts $S = \{s_1, …, s_n\}$ and time-stamped transcript segments, assign each transcript span to the slide being discussed (a monotone sequence-alignment problem over timecodes and semantic similarity).
3. **Multi-source grounded summarization.** Given the aligned pair $(S, T)$, generate summary $Y$ that maximizes coverage of source facts while every claim in $Y$ is entailed by at least one source (faithfulness constraint).
4. **Question generation with psychometric selection.** Generate candidate questions from $Y$; estimate each question's **difficulty** and **discrimination** from student responses (item response theory-style analysis); discard and regenerate questions that fail psychometric thresholds.

### 1.3 Validation

Validation is built into the pipeline, not bolted on:

| Component | Metric | How it is measured |
|---|---|---|
| Summary completeness | **Coverage (recall)** | share of atomic claims from slides + speech present in the summary |
| Summary reliability | **Faithfulness (precision)** | share of summary claims entailed by a source (hallucination control) |
| Core hypothesis | **Transcript-only retained** | share of spoken facts absent from slides that survive into the summary |
| STT quality | **WER / TER**, latency, cost | benchmarked on a golden 10-minute annotated set, per provider |
| Question quality | **Difficulty / Discrimination** | psychometric analysis of real student responses |

Coverage and faithfulness are computed by a single `entails(claim, set)` engine (NLI model + sentence embeddings) in which the "source of truth" and the "text under check" swap places — one evaluation harness, two directions. Experiments E1–E3 in the repository reproduce all metrics from raw data.

**Success criteria (targets):** faithfulness ≥ 0.9 (few hallucinations is non-negotiable for a study aid), coverage ≥ 0.7, transcript-only retained ≥ 0.5, question discrimination ≥ 0.3 for retained items. *(Adjust to your current measured numbers.)*

### 1.4 Business Goal

**Reduce the cost and time of producing revision materials and formative assessments for recorded courses, while improving their completeness.**

Formalized: for a university department or EdTech platform, cut the per-lecture human effort of producing a summary + quiz from ~1 hour of instructor/TA work to ~15 minutes of review, at a marginal compute cost of a few dollars per lecture — without losing the speech-only content that manual slide-based notes typically drop.

Secondary goal (outcome-side): improve student self-assessment and retention by giving every lecture a verified comprehension check, which correlates with course completion — a revenue-relevant metric for paid online programs.

### 1.5 Model Usage Scenario

1. An instructor (or platform pipeline) uploads `lecture.mp4` and `slides.pdf`.
2. The service transcribes, aligns, summarizes, and generates questions; the instructor optionally spends ~15 minutes reviewing flagged low-confidence claims.
3. The student receives a URL: an interactive summary where each statement links to its source (slide N or timestamp T), followed by an adaptive quiz.
4. Student responses feed back into psychometric filtering: weak questions are discarded and regenerated, so question quality improves with usage.
5. Aggregated quiz analytics show the instructor which topics the cohort failed to understand — actionable before the exam, not after.

---

## Part 2. Domain Research

### 2.1 Sources Used

*(Replace/extend with the exact papers and materials you actually used.)*

- **Lecture and meeting summarization:** literature on long-document and multimodal summarization; work on abstractive summarization faithfulness (e.g., FactCC, SummaC-style NLI evaluation).
- **STT benchmarking:** Whisper paper (Radford et al.), whisper.cpp documentation, Google Cloud STT documentation; studies on domain-specific term recognition in ASR.
- **Grounded generation / hallucination measurement:** NLI-based entailment evaluation of generated text; claim decomposition approaches (atomic fact extraction).
- **Psychometrics:** classical test theory and item response theory basics — item difficulty and discrimination indices; literature on automatic question generation quality.
- **Market/context:** reports on EdTech and corporate L&D content production costs; MOOC completion-rate studies.

### 2.2 Key Insights

1. **Speech ≠ slides.** Prior work and our own measurements confirm lecturers verbalize substantial content never written down — the "transcript-only retained" metric exists precisely because standard slide-based notes silently lose it.
2. **Faithfulness must be measured, not assumed.** LLM summarizers hallucinate; NLI-based entailment checking of decomposed claims is the current practical standard for catching this, and the same machinery yields coverage when run in reverse.
3. **STT provider choice is a real trade-off**, not a detail: local whisper.cpp removes per-minute cloud costs and privacy concerns but changes WER/TER and latency — hence a swappable-provider design and an explicit E2 benchmark.
4. **Most auto-generated questions are bad.** Without psychometric filtering, generated quizzes are dominated by trivially easy or ambiguous items; difficulty/discrimination filtering on real responses is what separates a toy from a usable assessment.

---

## Part 3. Dataset

### 3.1 Data Sources

| Dataset | Origin | Used for |
|---|---|---|
| Lecture set (`data/lectures/`) | [Recorded lectures from AI Talent Hub / ITMO courses — specify; or openly licensed university lectures, e.g., OCW-style recordings] | End-to-end pipeline, E1 coverage/faithfulness evaluation |
| Golden STT set (`data/golden_10min`) | 10 minutes of lecture audio with manually verified transcript, including technical terms | E2: WER / TER / latency / cost benchmark across STT providers |
| Student responses (`data/responses.csv`) | Anonymized quiz responses from [pilot group / classmates] | E3: psychometric estimation of question difficulty and discrimination |

### 3.2 Why It Is Suitable

- **Real, not synthetic, for the core task.** Actual lecture recordings contain exactly the phenomena the project targets: disfluent speech, domain terminology, and speech-only content — none of which a synthetic dataset reproduces well.
- **A golden set enables provider-fair comparison.** Manual transcript annotation makes WER/TER numbers trustworthy and lets cost/latency/quality trade-offs be stated per provider.
- **Response data makes psychometrics possible.** Difficulty and discrimination are undefined without real answers from real students; even a small pilot cohort is sufficient to demonstrate the filtering loop.
- **Privacy handled explicitly:** student responses are anonymized; private lecture data is excluded from the repository.

*(If the graders expect scale: the pipeline extends to openly licensed lecture corpora, so the dataset can grow without licensing risk.)*

---

## Part 4. Business Impact

### 4.1 Target Customer and Model

Primary segment for the estimate: a **university department or online-degree provider** running recorded courses. (Corporate L&D is a secondary segment with a similar cost structure.)

### 4.2 Key Assumptions

*(All numbers are stated assumptions — adjust to your local context; the estimation approach is the point.)*

| # | Assumption | Value |
|---|---|---|
| A1 | Manual production of a quality summary + quiz per 90-min lecture (TA/instructor) | 1 hour |
| A2 | Loaded hourly cost of TA/instructor time | $25/hour |
| A3 | Human review time per lecture with the service | 0.25 hours |
| A4 | Compute cost per lecture (STT + LLM + eval, measured in E2) | ≈ $2 |
| A5 | Lectures per course per semester | 24 |
| A6 | Courses in the department using the service | 20 |
| A7 | Semesters per year | 2 |

### 4.3 Estimation Approach

Bottom-up cost-substitution model. The annual business effect per department is

$$S_{year} = \underbrace{A5 \cdot A6 \cdot A7}_{\text{lectures/year}} \times \big[\,\underbrace{(A1 - A3) \cdot A2}_{\text{labor saved}} - \underbrace{A4}_{\text{compute}}\,\big], \qquad Net = N_{dept} \cdot S_{year} - C_{ops}$$

- **Cost without service** = A1 × A2 = 1 × $25 = **$25 per lecture**
- **Cost with service** = A3 × A2 + A4 = 0.25 × $25 + $2 = **$8.25 per lecture**
- **Saving per lecture** ≈ **$16.75** (≈ 67% reduction)
- **Annual volume** = A5 × A6 × A7 = 24 × 20 × 2 = **960 lectures/year**
- **Annual gross saving** ≈ 960 × $16.75 ≈ **$16,000 per department per year**

Estimated operating costs (hosting, maintenance, ~0.2 FTE engineering ≈ $20–25k/year) are per *deployment*, not per department: a single-department rollout is roughly break-even, break-even sits at ~1.5 departments, and net value scales with each department added (3 departments ≈ $48k gross against the same shared ops).

Sensitivity: the result is dominated by A1 (manual hours), and A1 = 1 hour is a deliberately conservative floor — producing a quality summary *plus* a vetted quiz often takes 2–4 hours, under which per-lecture saving rises to $41.75–$91.75 and annual gross to $40k–88k. The monetary case rests on scale; the completeness upside (§4.4) is not priced in at all.

### 4.4 Expected Business Value Beyond Cost Savings

- **Quality upside:** the summary preserves speech-only content (measured by *transcript-only retained*), i.e., the automated artifact is not just cheaper but more complete than typical manual slide-based notes.
- **Outcome upside (not monetized above, deliberately conservative):** per-lecture comprehension checks and topic-level cohort analytics support retention; for paid online programs, even a 1–2 p.p. improvement in completion translates directly into tuition revenue.
- **Scalability:** marginal cost per lecture is compute-only; value scales linearly with course volume with near-zero incremental headcount.

---

## Part 5. Project Pitch (7-minute outline)

1. **Hook (1 min):** "Half of what your lecturer says never reaches the slides — and it's exactly what exams test." Show one real example of a speech-only fact recovered by the system.
2. **Problem & solution (1.5 min):** two information streams, one is lost; live demo URL of a generated summary with source-grounded claims + adaptive quiz.
3. **ML formulation & validation (1.5 min):** the four-stage pipeline; one slide with the metrics table (coverage / faithfulness / transcript-only retained / WER-TER / psychometrics) and current numbers.
4. **Dataset & experiments (1 min):** lecture set, golden STT set, response data; E1–E3 reproducibility.
5. **Business case (1.5 min):** cost-substitution model — $25 → $8.25 per lecture, ≈ $16k/year gross per department, scaling with adoption; sensitivity in one line.
6. **Roadmap & close (0.5 min):** agentic tutor with adaptive review schedule, self-supervised alignment scoring, cross-university course clustering.

---

## Appendix: Deliverables Checklist

- [ ] This proposal document (Parts 1–4)
- [ ] Slide deck (PDF/PPTX) following the Part 5 outline
- [ ] Live demo URL prepared and tested offline-safe (screenshots as fallback)
- [ ] Current metric values inserted into §1.3 and §5.3
- [ ] Assumptions in §4.2 adjusted to local salary/volume figures