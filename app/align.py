"""Slide ↔ transcript alignment (P2 experiment): embeddings + optional DTW.

For each lecture directory this aligns the slide deck to the spoken lecture,
assigning every transcript time window to one slide, and scores the result
without any human labels.

1. **Slide units** — per-page text from ``slides_extracted/slides.md``
   (the raw pypdf extraction; unlike ``slides_reconstructed.md`` it keeps
   page boundaries). Consecutive beamer overlay frames (page N+1's text
   extends page N's) are collapsed into a single unit spanning the page range,
   and page-number footer lines are dropped.

2. **Transcript windows** — fixed-duration windows (default 60 s, stride 60 s)
   over ``<stt-provider>/transcription.json`` segments; a segment belongs to
   the window containing its midpoint. Silent windows are skipped.

3. **Alignment** — both texts are embedded (sentence-transformers per
   ``E1_EMBED_MODEL``, TF-IDF fallback if not installed) and every window is
   assigned a slide unit two ways:

   * **plain** — argmax cosine similarity, each window independently;
   * **dtw** — the monotonic path (slide index non-decreasing in time) that
     maximizes total similarity, via dynamic programming. Slides may be
     skipped or dwelt on, but the lecturer never goes backwards.

4. **Label-free proxy metrics** (→ ``align/alignment.json`` + console report),
   computed for plain, dtw, and a *uniform* baseline (slides spread evenly
   over the lecture's duration):

   * **keyword hit rate** — each slide unit gets its most distinctive terms
     (TF-IDF within the deck); the score is the mean fraction of a unit's
     keywords that appear in the transcript windows assigned to it;
   * **timecode monotonicity** — share of consecutive window pairs whose
     slide index does not decrease, plus Kendall tau-b between window order
     and slide order (dtw is monotone by construction);
   * **slide coverage** — fraction of units that received at least one window.

    python -m app.align data/deep-learning-and-computer-vision/lecture-01
    python -m app.align data/<course>/lecture-0{1..9}          # batch + aggregate
    python -m app.align <lecture-dir> --stt google_stt --window 90 --stride 45
    python -m app.align <lecture-dir> --backend tfidf           # no torch needed
"""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

import numpy as np

from app import config

DEFAULT_WINDOW_S = 60.0
DEFAULT_STRIDE_S = 60.0
DEFAULT_KEYWORDS_PER_SLIDE = 10

SLIDE_HEADER_RE = re.compile(r"^## Slide (\d+)\s*$", re.MULTILINE)

# Compact English stopword list — only used to pick distinctive slide keywords.
STOPWORDS = frozenset(
    """a about above after again all also an and any are as at be because been
    before being below between both but by can did do does doing down during
    each few for from further had has have having he her here hers him his how
    i if in into is it its itself just let me more most my no nor not now of
    off on once only or other our out over own same she should so some such
    than that the their them then there these they this those through to too
    under until up very was we were what when where which while who whom why
    will with would you your yours""".split()
)


# --- inputs ---------------------------------------------------------------------


@dataclass
class SlideUnit:
    """One alignment target: a slide, or a run of overlay frames of one slide."""

    first_page: int
    last_page: int
    text: str

    @property
    def label(self) -> str:
        if self.first_page == self.last_page:
            return f"slide {self.first_page}"
        return f"slides {self.first_page}-{self.last_page}"


@dataclass
class Window:
    start: float
    end: float
    text: str


def _clean_slide_body(body: str) -> str:
    """Drop page-number footer lines (a line that is just digits)."""
    lines = [line for line in body.splitlines() if not re.fullmatch(r"\s*\d+\s*", line)]
    return "\n".join(lines).strip()


def _norm(text: str) -> str:
    return " ".join(text.split()).lower()


def load_slide_units(lecture_dir: Path) -> tuple[int, list[SlideUnit]]:
    """Parse slides.md into per-page texts and collapse overlay builds.

    Returns (raw page count, collapsed units). Pages whose normalized text
    extends the previous page's (beamer \\pause overlays re-extract the whole
    frame) merge into one unit keeping the fullest text.
    """
    path = lecture_dir / "slides_extracted" / "slides.md"
    parts = SLIDE_HEADER_RE.split(path.read_text(encoding="utf-8"))
    pages: list[tuple[int, str]] = []
    for i in range(1, len(parts) - 1, 2):
        body = _clean_slide_body(parts[i + 1])
        if body:
            pages.append((int(parts[i]), body))

    units: list[SlideUnit] = []
    for page, text in pages:
        if units and units[-1].last_page == page - 1:
            prev, cur = _norm(units[-1].text), _norm(text)
            if cur.startswith(prev) or prev.startswith(cur):
                units[-1].last_page = page
                if len(text) > len(units[-1].text):
                    units[-1].text = text
                continue
        units.append(SlideUnit(page, page, text))
    return len(pages), units


def load_windows(lecture_dir: Path, stt_provider: str, window_s: float, stride_s: float) -> list[Window]:
    """Cut the timestamped transcript into fixed-duration text windows."""
    path = lecture_dir / stt_provider / "transcription.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    segments = [s for s in data["segments"] if s["text"].strip()]
    if not segments:
        return []
    duration = float(data.get("audio_duration") or segments[-1]["end"])

    windows: list[Window] = []
    t = 0.0
    while t < duration:
        w_end = min(t + window_s, duration)
        texts = [s["text"].strip() for s in segments if t <= (s["start"] + s["end"]) / 2 < w_end]
        if texts:
            windows.append(Window(t, w_end, " ".join(texts)))
        t += stride_s
    return windows


# --- embedding ------------------------------------------------------------------


def embed_texts(texts: list[str], backend: str) -> tuple[np.ndarray, str]:
    """L2-normalized vectors for `texts`; returns (matrix, resolved backend)."""
    if backend == "auto":
        try:
            import sentence_transformers  # noqa: F401

            backend = "embeddings"
        except ImportError:
            print("  NOTE: sentence-transformers not installed — using the TF-IDF backend")
            backend = "tfidf"
    if backend == "embeddings":
        import torch
        from sentence_transformers import SentenceTransformer

        if torch.cuda.is_available():
            device = "cuda"
        elif torch.mps.is_available():
            device = "mps"
        else:
            device = "cpu"
        model = SentenceTransformer(config.E1_EMBED_MODEL, device=device)
        return model.encode(texts, normalize_embeddings=True, show_progress_bar=False), backend
    if backend == "tfidf":
        docs = [Counter(_tokenize(t)) for t in texts]
        vocab = {term: i for i, term in enumerate(sorted({t for d in docs for t in d}))}
        df = Counter(term for doc in docs for term in doc)
        n = len(docs)
        idf = {term: math.log((1 + n) / (1 + count)) + 1 for term, count in df.items()}
        mat = np.zeros((n, len(vocab)), dtype=np.float32)
        for row, doc in enumerate(docs):
            for term, tf in doc.items():
                mat[row, vocab[term]] = tf * idf[term]
        norms = np.linalg.norm(mat, axis=1, keepdims=True)
        return mat / np.maximum(norms, 1e-9), backend
    raise ValueError(f"Unknown embedding backend: {backend!r} (expected auto | embeddings | tfidf).")


# --- alignment ------------------------------------------------------------------


def align_plain(sims: np.ndarray) -> list[int]:
    """Each window independently takes its most similar slide unit."""
    return sims.argmax(axis=1).tolist()


def align_dtw(sims: np.ndarray) -> list[int]:
    """Maximum-similarity monotonic path: slide index never decreases in time.

    best[w][s] = sims[w][s] + max_{s' <= s} best[w-1][s'], solved with a
    running prefix max, then backtracked. O(windows x slides).
    """
    n_win, n_slides = sims.shape
    best = sims[0].copy()
    ptr = np.zeros((n_win, n_slides), dtype=np.int32)
    for w in range(1, n_win):
        prefix_max = np.empty(n_slides)
        prefix_arg = np.empty(n_slides, dtype=np.int32)
        run_max, run_arg = -np.inf, 0
        for s in range(n_slides):
            if best[s] > run_max:
                run_max, run_arg = best[s], s
            prefix_max[s], prefix_arg[s] = run_max, run_arg
        best = sims[w] + prefix_max
        ptr[w] = prefix_arg

    path = [int(best.argmax())]
    for w in range(n_win - 1, 0, -1):
        path.append(int(ptr[w][path[-1]]))
    path.reverse()
    return path


def align_uniform(n_windows: int, n_slides: int) -> list[int]:
    """Baseline: slides spread evenly over the lecture, in order."""
    return [min(n_slides - 1, int(w / n_windows * n_slides)) for w in range(n_windows)]


# --- proxy metrics --------------------------------------------------------------


def _tokenize(text: str) -> list[str]:
    return re.findall(r"\w+", text.lower())


def _keyword_tokens(text: str) -> list[str]:
    return [t for t in _tokenize(text) if len(t) >= 3 and t not in STOPWORDS and not t.isdigit()]


def slide_keywords(units: list[SlideUnit], per_slide: int) -> list[list[str]]:
    """Most distinctive terms per unit: TF-IDF scored within the deck."""
    docs = [Counter(_keyword_tokens(u.text)) for u in units]
    df = Counter(term for doc in docs for term in doc)
    n = len(docs)
    idf = {term: math.log((1 + n) / (1 + count)) + 1 for term, count in df.items()}
    return [
        [term for term, _ in sorted(doc.items(), key=lambda kv: kv[1] * idf[kv[0]], reverse=True)[:per_slide]]
        for doc in docs
    ]


def keyword_hit_rate(assignment: list[int], keywords: list[list[str]], windows: list[Window]) -> tuple[float, float]:
    """(mean fraction of a unit's keywords found in its assigned windows,
    fraction of units that received at least one window)."""
    assigned_text: dict[int, list[str]] = {}
    for w, s in enumerate(assignment):
        assigned_text.setdefault(s, []).append(windows[w].text)
    rates = []
    for s, kws in enumerate(keywords):
        if s not in assigned_text or not kws:
            continue
        tokens = set(_tokenize(" ".join(assigned_text[s])))
        rates.append(sum(kw in tokens for kw in kws) / len(kws))
    coverage = len(assigned_text) / len(keywords) if keywords else 0.0
    return (float(np.mean(rates)) if rates else 0.0, coverage)


def monotonicity(assignment: list[int]) -> float:
    """Share of consecutive window pairs with a non-decreasing slide index."""
    if len(assignment) < 2:
        return 1.0
    steps = sum(b >= a for a, b in zip(assignment, assignment[1:], strict=False))
    return steps / (len(assignment) - 1)


def kendall_tau_b(assignment: list[int]) -> float:
    """Kendall tau-b between window order and assigned slide index."""
    n = len(assignment)
    conc = disc = ties_y = 0
    for i in range(n):
        for j in range(i + 1, n):
            d = assignment[j] - assignment[i]
            if d > 0:
                conc += 1
            elif d < 0:
                disc += 1
            else:
                ties_y += 1
    pairs = conc + disc + ties_y
    denom = math.sqrt(pairs * (conc + disc))
    return (conc - disc) / denom if denom else 0.0


def score(assignment: list[int], keywords: list[list[str]], windows: list[Window]) -> dict:
    hit_rate, coverage = keyword_hit_rate(assignment, keywords, windows)
    return {
        "keyword_hit_rate": round(hit_rate, 4),
        "slide_coverage": round(coverage, 4),
        "monotonicity": round(monotonicity(assignment), 4),
        "kendall_tau_b": round(kendall_tau_b(assignment), 4),
    }


# --- driver ---------------------------------------------------------------------


def process_lecture(
    lecture_dir: Path,
    *,
    stt_provider: str,
    backend: str,
    window_s: float,
    stride_s: float,
    keywords_per_slide: int,
) -> dict:
    print(f"== {lecture_dir.name} ==")
    n_pages, units = load_slide_units(lecture_dir)
    windows = load_windows(lecture_dir, stt_provider, window_s, stride_s)
    if not units or not windows:
        raise SystemExit(f"{lecture_dir}: no slide text or no transcript windows — nothing to align")
    print(f"   {n_pages} slide pages -> {len(units)} units after overlay collapse; {len(windows)} windows")

    vecs, backend = embed_texts([u.text for u in units] + [w.text for w in windows], backend)
    slide_vecs, window_vecs = vecs[: len(units)], vecs[len(units) :]
    sims = window_vecs @ slide_vecs.T

    assignments = {
        "uniform": align_uniform(len(windows), len(units)),
        "plain": align_plain(sims),
        "dtw": align_dtw(sims),
    }
    keywords = slide_keywords(units, keywords_per_slide)
    metrics = {name: score(a, keywords, windows) for name, a in assignments.items()}
    disagree = [abs(p - d) for p, d in zip(assignments["plain"], assignments["dtw"], strict=True)]
    metrics["plain_vs_dtw"] = {
        "windows_differing": round(sum(d > 0 for d in disagree) / len(disagree), 4),
        "mean_unit_distance": round(float(np.mean(disagree)), 4),
    }

    out = {
        "settings": {
            "stt_provider": stt_provider,
            "backend": backend,
            "embed_model": config.E1_EMBED_MODEL if backend == "embeddings" else None,
            "window_s": window_s,
            "stride_s": stride_s,
            "keywords_per_slide": keywords_per_slide,
        },
        "n_slide_pages": n_pages,
        "units": [{"pages": [u.first_page, u.last_page], "title": u.text.splitlines()[0][:80]} for u in units],
        "windows": [{"start": round(w.start, 2), "end": round(w.end, 2)} for w in windows],
        "assignments": assignments,
        "keywords": keywords,
        "metrics": metrics,
    }
    out_dir = lecture_dir / "align"
    out_dir.mkdir(exist_ok=True)
    (out_dir / "alignment.json").write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")

    for name in ("uniform", "plain", "dtw"):
        m = metrics[name]
        print(
            f"   {name:>8}: keyword hit {m['keyword_hit_rate']:.3f}  coverage {m['slide_coverage']:.3f}  "
            f"monotone {m['monotonicity']:.3f}  tau_b {m['kendall_tau_b']:.3f}"
        )
    print(
        f"   plain vs dtw: {metrics['plain_vs_dtw']['windows_differing']:.1%} of windows differ, "
        f"mean distance {metrics['plain_vs_dtw']['mean_unit_distance']:.1f} units "
        f"-> {out_dir / 'alignment.json'}"
    )
    return metrics


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Slide <-> transcript alignment: embeddings vs embeddings + DTW")
    parser.add_argument(
        "lectures",
        nargs="+",
        help="One or more lecture directories (each with slides_extracted/slides.md, <stt>/transcription.json)",
    )
    parser.add_argument(
        "--stt",
        default="whisper_cpp",
        choices=["whisper_cpp", "google_stt"],
        help="Which STT provider's timestamped transcript to use (default: whisper_cpp)",
    )
    parser.add_argument(
        "--backend",
        default="auto",
        choices=["auto", "embeddings", "tfidf"],
        help="Text embedding backend (default: sentence-transformers when installed)",
    )
    parser.add_argument("--window", type=float, default=DEFAULT_WINDOW_S, help="Window length, seconds (default: 60)")
    parser.add_argument("--stride", type=float, default=DEFAULT_STRIDE_S, help="Window stride, seconds (default: 60)")
    parser.add_argument(
        "--keywords",
        type=int,
        default=DEFAULT_KEYWORDS_PER_SLIDE,
        help=f"Distinctive keywords per slide for the proxy metric (default: {DEFAULT_KEYWORDS_PER_SLIDE})",
    )
    args = parser.parse_args(argv)

    all_metrics: list[dict] = []
    for lec in args.lectures:
        all_metrics.append(
            process_lecture(
                Path(lec).resolve(),
                stt_provider=args.stt,
                backend=args.backend,
                window_s=args.window,
                stride_s=args.stride,
                keywords_per_slide=args.keywords,
            )
        )

    if len(all_metrics) > 1:
        print(f"\n== aggregate over {len(all_metrics)} lectures ==")
        for name in ("uniform", "plain", "dtw"):
            means = {k: float(np.mean([m[name][k] for m in all_metrics])) for k in all_metrics[0][name]}
            print(
                f"   {name:>8}: keyword hit {means['keyword_hit_rate']:.3f}  "
                f"coverage {means['slide_coverage']:.3f}  monotone {means['monotonicity']:.3f}  "
                f"tau_b {means['kendall_tau_b']:.3f}"
            )
    return 0


if __name__ == "__main__":
    sys.exit(main())
