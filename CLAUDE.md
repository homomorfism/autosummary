# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A pipeline that turns a lecture recording + slides into a grounded structured
summary, a study conspect, and an adaptive self-check quiz. What works today:
STT → summarization, per-lecture conspects (`app/conspect.py`), quiz generation
(`app/quiz.py`), a course web app (`web/`, Next.js: conspect → quiz → results →
item stats, attempts stored in SQLite), and E3 question psychometrics
(`app/quality.py`: p-value, point-biserial, rejection rule, adaptive
regeneration), E1 claim-level summary evaluation (`app/e1.py`), E2 STT
benchmark (`app/e2.py`: latency, $/audio-hour; WER lives in
`notebooks/wer_ter.ipynb` — results in `docs/experiments/e2.md`), and
slide↔transcript alignment (`app/align.py`: embeddings + DTW, label-free proxy
metrics — see `docs/experiments/alignment.md`). Note the README's
`experiments/`, `eval/`, `app/align/` (alignment is the single module
`app/align.py`), `app/questions/`, and `requirements.txt` do **not** exist.

## Commands

This project uses **uv**, not pip/requirements.txt (the README's `pip install -r
requirements.txt` is wrong).

```bash
uv sync                                  # install deps (incl. dev group: ruff, ipykernel)
uv run ruff check .                      # lint
uv run ruff check --fix .                # autofix
uv run ruff format .                     # format (line-length 120)
uv run pre-commit install                # one-time: install the gitleaks secret-scan commit hook
uv run pre-commit run --all-files        # secret scan the whole tree (also runs in CI: .github/workflows/secret-scan.yml)

# end-to-end: video + optional slides → transcript.json + summary.json
uv run autosummary --video lecture.mp4 --slides slides.pdf --provider whisper_cpp
uv run autosummary --video lecture.mp4 --no-summary          # STT only, skip LLM
uv run autosummary --video lecture.mp4 --transcript t.json   # reuse a transcript, skip STT

# batch dual-provider transcription (runs BOTH whisper_cpp + google_stt per lecture)
# writes in place to <lecture-dir>/<provider>/transcription.{json,md} (+ audio.wav)
uv run python -m app.transcribe data/<course>/<lecture>   # lecture dir must contain video.mp4
uv run python -m app.transcribe data/<course>/<lecture> --providers whisper_cpp   # single provider

# per-lecture LLM stages (each reads/writes in place inside <lecture-dir>)
uv run python -m app.reconstruct_transcript data/<course>/<lecture>   # raw ASR → transcription_reconstructed.md (no summarizing)
uv run python -m app.conspect data/<course>/<lecture>     # transcript + slides → conspect.md (prefers the reconstructed transcript)
uv run python -m app.quiz data/<course>/<lecture>         # conspect.md → quiz.json (5 single-choice Qs)

# course web app (web/, Next.js): lectures → conspect → quiz → results
# (attempts saved to data/quiz_results.db; uses npm, not uv)
cd web && npm run dev                                     # http://localhost:3000  (DATA_DIR / QUIZ_DB_PATH env override)

# E3 psychometrics over recorded attempts: difficulty (p), discrimination (r_pb)
uv run python -m app.quality data/<course>/<lecture>              # report only
uv run python -m app.quality data/<course>/<lecture> --retire     # rejection rule → archive bad Qs
uv run python -m app.quality data/<course>/<lecture> --regenerate # + LLM replacements (closed loop)

# E1 claim-level evaluation: coverage / faithfulness / F1 + transcript-only coverage
# (LLM decompose → top-k retrieve → LLM judge; stages cached in <lecture-dir>/e1/)
uv run python -m app.e1 data/<course>/<lecture>                   # full run (hundreds of LLM calls)
uv run python -m app.e1 data/<course>/<lecture> --max-chunks 1 --limit 10   # cheap smoke run
uv run python -m app.e1 data/<course>/<lecture> --sample-labels 12          # manual-calibration template

# E2 STT benchmark: latency (RTF from meta.latency_sec) and $/audio-hour
# (Google rate card via --google-usd-min vs vast.ai GPU rates via --gpu-usd-hr)
uv run python -m app.e2 data/<course>                     # course dir → all lectures + pooled aggregate
# (WER on the golden set: notebooks/wer_ter.ipynb; results doc: docs/experiments/e2.md)

# slide ↔ transcript alignment: embeddings + DTW, label-free proxy metrics
# (local only, no LLM calls; writes <lecture-dir>/align/alignment.json)
uv run python -m app.align data/<course>/<lecture>                # accepts several dirs → aggregate row
uv run python -m app.align data/<course>/<lecture> --backend tfidf   # skip torch/model download

# alignment ground truth from the Zoom recording (video frames ↔ pdftoppm page renders)
# needs ffmpeg + poppler; run app.align first to also get the accuracy evaluation
uv run python -m app.align_video data/<course>/<lecture>         # → align/video_labels.json
```

There is **no test suite** yet. `ruff` is the only check.

External binaries required at runtime: `ffmpeg`/`ffprobe` (audio extraction),
and for local STT the `whisper-cli` binary + GGML model files (not vendored).

## Architecture

The pipeline is provider-swappable at two seams — STT and LLM — both selected by
name/config so downstream code never branches on the concrete backend.

- **`app/config.py`** — single source of all env config, loaded once at import
  (`.env` via python-dotenv). Read config here; don't scatter `os.environ`.
- **`app/stt/`** — STT seam. `base.py` defines the `STTProvider` ABC and the
  unified `Transcript`/`Segment`/`Word` dataclasses that everything downstream
  consumes (with JSON + Markdown serialization). `get_stt_provider(name)` in
  `__init__.py` is the factory. Two adapters: `whisper_cpp.py` (local, shells
  out to `whisper-cli` with anti-hallucination flags tuned for long lectures)
  and `google_stt.py` (cloud, `long_running_recognize` — extracts 16 kHz mono
  WAV, uploads to GCS, transcribes, deletes the object). `audio.py` holds the
  shared ffmpeg 16 kHz-mono conversion so WER is comparable across providers.
- **`app/slides.py`** — `extract_slides(pdf)` → `SlideDeck` of per-page `Slide`
  text via pypdf (the second summarization source). No OCR: scanned PDFs yield
  nothing.
- **`app/summarize/`** — LLM seam. `summarize(transcript, slides)` →
  `SummaryConcept`. `schema.py` is the pydantic output contract; `summarizer.py`
  supports two backends: **anthropic** (Claude, `client.messages.parse` with
  `output_format=` structured outputs + adaptive thinking) and **deepseek**
  (OpenAI-compatible, JSON schema in the system prompt, validated locally).
  Provider is explicit (`LLM_PROVIDER`) or inferred from the model name
  (`claude-*`→anthropic, `deepseek-*`→deepseek, default deepseek).
- **`app/run.py`** — wires STT → slides → summarize into the `autosummary` CLI.
- **`app/quiz.py`** — conspect.md → `quiz.json`: pydantic `Quiz` schema
  (validators enforce exactly one correct option per question and the
  anti-length-leak limits: the correct option ≤1.3× the longest distractor,
  strictly-longest-correct in at most half the questions — without them the
  LLM writes correct options ~1.6× longer and "pick the longest" scores ~78%);
  `QuizGenerator.complete_structured()` is the shared structured-output LLM
  call (same anthropic/deepseek split as the summarizer, retries with the
  validator error fed back) also used by `app/quality.py` regeneration.
- **`app/db.py`** — SQLite results store (`data/quiz_results.db`, override via
  `QUIZ_DB_PATH` or `--db`): attempts, per-question answers (keyed by a stable
  content-hash `question_id`), retired-question archive. All functions accept
  `db_path=` so tests use scratch DBs.
- **`app/quality.py`** — E3 item analysis: difficulty p-value, point-biserial
  discrimination vs the *rest score*; rejection rule (defaults: p ∈ [0.30,
  0.85], r_pb ≥ 0.15, from 5 attempts) retires questions out of `quiz.json`
  into the DB archive; `--regenerate` prompts the LLM with the measured stats
  and miss direction to write replacements (closed loop).
- **`web/`** — the course web app (Next.js App Router, better-sqlite3,
  server-rendered KaTeX; replaced the removed Flask `app/web`). Serves the
  `data/` tree (any `<course>/<lecture>/` with a `conspect.md` shows up;
  `quiz.json` enables the quiz; `info.md` course pages: instructor, source,
  lecture/materials table) and the attempts DB with a byte-identical
  `question_id` (`web/src/lib/db.ts` mirrors `app/db.py`;
  `web/src/lib/quality.ts` ports the E3 item analysis), so Python
  `app.quality --retire/--regenerate` closes the loop over attempts recorded by
  the TS app. One attempt per browser (anonymous `quiz_client_id` cookie): a
  submitted quiz freezes — the quiz page redirects to that attempt's results
  and the API rejects resubmission, unless the quiz was fully regenerated since
  (no overlapping `question_id`). Uses npm, not uv.
- **`app/e1.py`** — E1 claim-level evaluation: LLM decomposition of slides
  (`slides_reconstructed.md`) / transcript (`transcription_reconstructed.md`,
  from `app.reconstruct_transcript` — both the same sources the conspect used) /
  conspect into atomic claims (each with a core/supporting/aside salience
  label), then `entails` = top-k retrieval
  (sentence-transformers per `E1_EMBED_MODEL`, TF-IDF fallback if not
  installed) + batched LLM judge. Three judged directions → coverage,
  faithfulness, F1, transcript-only coverage. Stages cache to
  `<lecture-dir>/e1/` keyed on a settings fingerprint; `--sample-labels` /
  `--agreement` support manual judge calibration. Judge/decompose calls need a
  large `max_tokens` (default 32k) — `deepseek-v4-pro` is a reasoning model
  and returns an empty response if the cap is hit while thinking.
- **`app/e2.py`** — E2 STT benchmark, fully local/deterministic (no LLM):
  reads `meta.latency_sec` / `audio_duration` from each provider's
  `transcription.json` → RTF; prices google_stt from the API rate
  (`--google-usd-min`) and whisper_cpp as RTF × rented-GPU rate
  (`--gpu-usd-hr`, vast.ai). WER (golden set) is in `notebooks/wer_ter.ipynb`.
  A label-free slide-term TER was prototyped and dropped (slides are too weak a
  reference — see `docs/experiments/e2.md`). Results: `e2.md` + `e2.json`.
- **`app/align.py`** — slide↔transcript alignment (P2 experiment, no LLM):
  per-page units from `slides_extracted/slides.md` (consecutive beamer overlay
  frames collapsed), 60 s transcript windows from `<stt>/transcription.json`,
  embedded with `E1_EMBED_MODEL` (TF-IDF fallback). Two aligners — per-window
  argmax cosine and a monotonic-path DP (DTW-style: slide index never
  decreases) — scored without labels via per-slide TF-IDF keyword hit rate,
  monotone-step share, Kendall τ-b, against a time-uniform baseline. Results
  and method comparison: `docs/experiments/alignment.md`.
- **`app/align_video.py`** — alignment ground truth from the recording itself
  (Zoom screen share: slide fills the left ~74.7% of the frame). Samples one
  keyframe per 15 s (`ffmpeg -skip_frame nokey`, ~35 s per 3.5 h video),
  matches each against `pdftoppm` renders of the deck by normalized
  correlation; scores are bimodal (slide > 0.9, whiteboard < 0.35 → 0.7
  threshold = "no slide on screen"). Writes `align/video_labels.json` and,
  when `align/alignment.json` exists, evaluates uniform/plain/dtw accuracy on
  slide-visible windows. Needs `ffmpeg` + poppler (`pdftoppm`), no LLM.

### The grounding invariant

The whole project rests on tagging every summary statement with a `Source`
(`slide` / `transcript` / `both`) — see `SummaryConcept` in
`app/summarize/schema.py`. `transcript_only_notes` + points with
`source=transcript` are the facts spoken but absent from slides; preserving them
is the project's thesis ("site > deck") and the basis for the planned E1
coverage/faithfulness metrics. Preserve this tagging when touching the schema or
prompts.

## Gotchas

- **whisper.cpp Core ML build crashes.** The default `WhisperCppProvider` paths
  point at `.../build/bin/whisper-cli`, but on this machine that build was
  compiled with Core ML and fails without an `.mlmodelc` encoder. Use the
  `build-nocoreml` binary — `config.py` and `.env.example` already default
  `WHISPER_CLI` to it, so run via config, not the hardcoded module defaults.
- **Google STT needs a GCS bucket + ADC/service-account auth.** Config accepts
  both native names (`GOOGLE_CLOUD_PROJECT`, `GOOGLE_STT_BUCKET`) and the docker
  names (`GCP_PROJECT_ID`, `GCS_STT_BUCKET`); auth is via
  `GOOGLE_APPLICATION_CREDENTIALS`.
- Cloud SDK imports (`google-cloud-*`, `anthropic`, `openai`) are done lazily
  inside methods so the package imports fine in a whisper-only / no-key setup.
  Keep new optional-backend imports lazy too.
