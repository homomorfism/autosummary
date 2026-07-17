# Capstone Midterm Speech — Lecture Autosummary

~1,380 words ≈ 10 minutes at a calm presentation pace (135–140 wpm).
Time markers assume you start the clock on slide 1.

---

## Slide 1 · Title (0:00–0:40)

Good afternoon. My name is Shamil Arslanov, and my capstone is called Lecture Autosummary — grounded multi-source lecture summaries with adaptive comprehension checks.

In one sentence: I built a pipeline that turns a lecture recording plus its slide deck into a summary you can actually trust, and a quiz that measures whether you understood the lecture — and then I built the evaluation to prove, with numbers, that the summary is worth trusting. The measurement is really the heart of this thesis, and that's what I'll spend most of these ten minutes on.

## Slide 2 · Problem (0:40–1:40)

Let me start with the problem. After a lecture ends, a student is left with exactly two artifacts, and both of them fail.

The recording is complete, but it's two to three and a half hours long. Nobody re-watches that before an exam — and certainly not nine of them.

The slides are compact, but they lose everything the lecturer only *said*: the worked examples, the caveats, the intuition, the "this will be on the exam" moments. And this loss is not small. In the course I use as my dataset, I measured it: a single lecture contains 334 atomic facts that were spoken out loud but appear nowhere on the slides.

So the goal of this project is to keep what was said, not just what was shown — and, crucially, to prove with numbers that we kept it.

## Slide 3 · Solution (1:40–2:40)

The solution takes both inputs — the video and the PDF deck — and produces two things.

First, a conspect: a structured summary that merges the spoken lecture with the slides, where every single statement is tagged with its source — slide, transcript, or both. That grounding tag is not decoration; it's what makes the summary auditable and what makes the evaluation possible.

Second, a quiz: five questions per lecture that check comprehension — and the quiz improves itself over time, which I'll come back to.

The central research question is evaluative, not just generative: can we numerically show that a multi-source summary is richer than the slide deck alone, and faithful to its sources? My thesis metric is *transcript-only coverage* — of the facts the lecturer spoke that are absent from the slides, what share survives into the summary? For any slides-only summary, that number is zero by definition. Everything above zero is value that existing tools throw away.

## Slide 4 · Pipeline (2:40–3:40)

Here's the architecture, briefly, in two lanes.

The audio lane: ffmpeg extracts sixteen-kilohertz mono audio from the video, speech-to-text turns it into a raw transcript — about 46,000 words for a three-hour lecture, full of filler, student questions, and recognition errors — and then an LLM reconstruction stage cleans that into about 8,600 words of proper lecture text, with spoken math rendered as LaTeX.

The slide lane: text is extracted from the PDF per page, and a similar reconstruction collapses beamer overlay duplicates and repairs the math.

The two lanes merge in a structured-output LLM call that writes the source-tagged conspect. From the conspect we generate the quiz, students take it in a web app, attempts land in a database, and psychometric analysis closes the loop on question quality.

One design decision worth noting: there are exactly two swappable seams — the speech-to-text provider and the LLM. Everything downstream is provider-independent, which is what makes the benchmarking in experiment two clean.

## Slide 5 · Data (3:40–4:30)

The dataset is a real course: "Deep Learning and Computer Vision," taught at Harbour Space this year by Sergey Nikolenko. I collected it end to end: nine lectures, twenty-one hours of video, 619 slide pages.

On top of the raw course I built three annotation sets by hand: a 19-and-a-half-minute golden transcript for measuring speech recognition error rates; forty hand-labelled entailment pairs for calibrating my LLM judge; and quiz attempts from roughly fifteen students in the course group, which are still being collected.

This data is deliberately hard: dense mathematics, heavy terminology, accented English. It stresses both the speech recognition and the summarization — which is exactly what you want from an evaluation dataset.

## Slide 6 · E1 method (4:30–5:45)

Now the core experiment, E1: how do you measure summary quality?

The classical answer — ROUGE, n-gram overlap — cannot tell you whether a *fact* survived summarization. So instead, following the FActScore line of work, I evaluate at the level of atomic facts. An LLM decomposes each of the three texts — reconstructed slides, reconstructed transcript, and the conspect — into atomic, self-contained claims. For lecture six that's 157 claims from the slides, 526 from the transcript, 208 from the conspect. Each claim also gets a salience label — core, supporting, or aside — so that deliberately dropping an aside doesn't count against the summary.

Then there is a single entailment engine: for a given claim, retrieve the top sixteen most similar claims from the other side by embeddings, and ask a strict LLM judge whether they entail it.

The elegant part is that one engine, run in three directions, produces every metric I need. Source claims against the summary gives coverage — recall. Summary claims against the sources gives faithfulness — precision, one minus the hallucination rate. And transcript claims against slide claims identifies exactly which facts are transcript-only, which is the mask for my thesis metric.

## Slide 7 · E1 results (5:45–7:00)

So what happened? The baseline was the first honest end-to-end version: a conspect generated straight from the raw ASR transcript. It scored 54 percent coverage, 69 percent faithfulness, F1 of 61 — and it preserved only 37 percent of transcript-only facts.

The diagnosis was that ASR noise was contaminating both the summary and the measurement itself. The main pipeline adds the LLM reconstruction stage on both inputs, adds salience labels, and upgrades the retriever.

The result: every metric moved. Coverage went from 54 to 62 and a half percent. Faithfulness from 69 to 86 and a half. F1 from 61 to 72.6. And the thesis metric — transcript-only facts preserved — went from 37 to 48 and a half percent.

One detail I want to highlight, because it's counterintuitive: reconstruction compresses 46,000 words down to 8,600 — yet the number of extractable atomic facts *increased*, from 449 to 526. That's the evidence that this stage is cleaning noise, not doing hidden summarization.

## Slide 8 · Judge calibration (7:00–7:50)

Of course, there's an obvious objection: your judge is itself an LLM — why should anyone believe its verdicts?

That's why I calibrated it before trusting a single number. I hand-labelled forty claim–premise pairs, stratified across all three judgment directions, and compared. The judge agreed with me on thirty-nine out of forty — Cohen's kappa of 0.95 — with zero false positives and one false negative.

Those two error directions matter differently. Zero false positives means the judge never credits a fact that isn't actually supported — so the faithfulness score is not inflated by a lenient judge. The one miss means coverage numbers are, if anything, slightly conservative. And this calibration is repeated whenever the judge prompt or model changes.

## Slide 9 · E2, speech-to-text (7:50–8:30)

Experiment two benchmarks the transcription seam, because everything downstream depends on it. On the golden segment — identical audio for both providers — local whisper.cpp achieved a word error rate of 2.3 percent, against 16.3 percent for Google Cloud Speech-to-Text. Seven times lower, on accented, terminology-heavy speech — while also being free, local, and private. So whisper.cpp is the pipeline default, and the cloud provider becomes the paid reference point in the latency-and-cost table I'm completing now.

## Slide 10 · E3, the quiz loop (8:30–9:20)

Experiment three closes the loop on the quiz. A known weakness of LLM-generated questions is that many are trivially easy, or fail to separate students who understood the lecture from those who didn't. So I apply classical test theory to real attempts collected through the web app: for each question, difficulty — the share of correct answers — and discrimination — the point-biserial correlation with the rest of the score.

A question is retired if it's too easy, too hard, or doesn't discriminate; it's archived, and the LLM regenerates a replacement conditioned on the measured statistics and the direction in which students missed. The quiz literally improves as more students use it. With roughly fifteen respondents the estimates are noisy — I state that openly — so the midterm deliverable here is the working methodology and the closed loop, validated live as attempts accumulate.

## Slide 11 · Status and next steps (9:20–10:00)

To sum up where the project stands. Done: the full end-to-end pipeline; the E1 evaluation engine with strong results on the development lecture; a judge calibrated at kappa 0.95; the speech-to-text benchmark; and the psychometric retire-and-regenerate loop.

Next: freeze the pipeline and run it unchanged on the eight held-out lectures — the development lecture tuned it, the other eight will test it; finish the latency-and-cost side of E2; collect enough student attempts to run the quiz loop on live data; and run an ablation to separate the three improvements that are currently confounded.

Everything — code, data, golden sets, labels — is in the open repository. Thank you; I'm happy to take questions.
