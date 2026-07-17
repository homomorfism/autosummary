"""Video-frame ground truth for slide ↔ transcript alignment.

The lecture recordings are Zoom screen shares: the slide (or a hand-drawn
whiteboard) fills the left ~75% of the 1920x1080 frame, with the webcam on the
right. The slide shown on screen *is* the ground truth the text-based aligners
in ``app.align`` try to recover — so instead of hand-labelling, this module
reads it off the video:

1. **Sample frames** — one keyframe per ``--every`` seconds (default 15 s),
   decoded with ``-skip_frame nokey`` (keyframes are ~4 s apart, so a 3.5 h
   video takes ~35 s), cropped to the slide region, downscaled to 96x72
   grayscale.
2. **Render the deck** — every ``slides.pdf`` page via ``pdftoppm`` to the
   same 96x72 grayscale.
3. **Match** — zero-mean normalized correlation between each frame and every
   page. The distribution is sharply bimodal: a slide on screen scores > 0.9
   against its page, whiteboard/webcam segments score < 0.35 against
   everything, so ``--threshold`` (default 0.7) cleanly separates
   "page N on screen" from "no slide on screen".
4. **Evaluate** (when ``align/alignment.json`` from ``app.align`` exists) —
   per transcript window, the majority frame label becomes the ground-truth
   slide unit; the uniform / plain / dtw assignments are scored with exact and
   ±1-unit accuracy over the slide-visible windows.

Labels and evaluation go to ``<lecture-dir>/align/video_labels.json``.

    python -m app.align_video data/deep-learning-and-computer-vision/lecture-01
    python -m app.align_video data/<course>/lecture-0{1..9}    # batch + aggregate
    python -m app.align_video <lecture-dir> --every 10 --threshold 0.75

Requires ``ffmpeg`` and ``pdftoppm`` (poppler) in PATH.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
from collections import Counter
from pathlib import Path

import numpy as np

DEFAULT_EVERY_S = 15.0
DEFAULT_THRESHOLD = 0.7
DEFAULT_CROP_FRAC = 0.747  # slide region: left 74.7% of the frame (Zoom layout)
MATCH_W, MATCH_H = 96, 72  # 4:3, same as the slide pages


def _require(binary: str) -> str:
    path = shutil.which(binary)
    if not path:
        raise SystemExit(f"{binary} not found in PATH. Install it (brew install {binary}).")
    return path


# --- pixel sources --------------------------------------------------------------


def extract_frames(video: Path, every_s: float, crop_frac: float) -> np.ndarray:
    """(n, H, W) grayscale frames, one per `every_s` seconds of video.

    Only keyframes are decoded (`-skip_frame nokey`); the fps filter then keeps
    the keyframe nearest each bucket start, so sample i sits at ~i * every_s
    with jitter up to the keyframe interval (~4 s) — negligible against 60 s
    transcript windows.
    """
    cmd = [
        _require("ffmpeg"),
        "-v",
        "error",
        "-skip_frame",
        "nokey",
        "-i",
        str(video),
        "-vf",
        f"fps=1/{every_s},crop=iw*{crop_frac}:ih:0:0,scale={MATCH_W}:{MATCH_H},format=gray",
        "-f",
        "rawvideo",
        "-",
    ]
    proc = subprocess.run(cmd, capture_output=True)
    if proc.returncode != 0:
        raise RuntimeError(f"ffmpeg failed:\n{proc.stderr.decode()[-2000:]}")
    n = len(proc.stdout) // (MATCH_W * MATCH_H)
    return np.frombuffer(proc.stdout[: n * MATCH_W * MATCH_H], dtype=np.uint8).reshape(n, MATCH_H, MATCH_W)


def _read_pgm(path: Path) -> np.ndarray:
    data = path.read_bytes()
    header = re.match(rb"P5\s+(\d+)\s+(\d+)\s+(\d+)\s", data)
    if not header:
        raise ValueError(f"{path}: not a binary PGM")
    w, h = int(header.group(1)), int(header.group(2))
    return np.frombuffer(data, dtype=np.uint8, count=w * h, offset=header.end()).reshape(h, w)


def render_pages(pdf: Path) -> np.ndarray:
    """(n_pages, H, W) grayscale renders of every page of the deck."""
    pdftoppm = _require("pdftoppm")
    with tempfile.TemporaryDirectory() as tmp:
        cmd = [pdftoppm, "-gray", "-scale-to-x", str(MATCH_W), "-scale-to-y", str(MATCH_H), str(pdf), f"{tmp}/page"]
        proc = subprocess.run(cmd, capture_output=True, text=True)
        if proc.returncode != 0:
            raise RuntimeError(f"pdftoppm failed:\n{proc.stderr[-2000:]}")
        return np.stack([_read_pgm(p) for p in sorted(Path(tmp).glob("page-*.pgm"))])


# --- matching -------------------------------------------------------------------


def _normalize(imgs: np.ndarray) -> np.ndarray:
    flat = imgs.reshape(len(imgs), -1).astype(np.float32)
    flat = flat - flat.mean(axis=1, keepdims=True)
    return flat / np.maximum(np.linalg.norm(flat, axis=1, keepdims=True), 1e-6)


def label_frames(frames: np.ndarray, pages: np.ndarray, threshold: float) -> list[dict]:
    """Per frame: best-matching page (1-based) or None when nothing matches."""
    sims = _normalize(frames) @ _normalize(pages).T
    best, arg = sims.max(axis=1), sims.argmax(axis=1)
    return [
        {"page": int(a) + 1 if s >= threshold else None, "score": round(float(s), 4)}
        for s, a in zip(best, arg, strict=True)
    ]


# --- evaluation against app.align assignments ------------------------------------


def evaluate(alignment: dict, samples: list[dict], every_s: float) -> dict | None:
    """Score each stored assignment against the majority frame label per window.

    A window gets a ground-truth unit when at least half its frame samples
    (and at least two) show some slide; whiteboard-dominated windows are
    excluded — the text aligners are only judged where there is a slide to hit.
    """
    page_to_unit: dict[int, int] = {}
    for idx, unit in enumerate(alignment["units"]):
        first, last = unit["pages"]
        for page in range(first, last + 1):
            page_to_unit[page] = idx

    truth: dict[int, int] = {}
    for w, win in enumerate(alignment["windows"]):
        pages = [
            s["page"]
            for i, s in enumerate(samples)
            if win["start"] <= i * every_s < win["end"] and s["page"] is not None
        ]
        n_samples = max(1, round((win["end"] - win["start"]) / every_s))
        if len(pages) >= max(2, n_samples / 2):
            page = Counter(pages).most_common(1)[0][0]
            if page in page_to_unit:  # pages whose text was empty have no unit
                truth[w] = page_to_unit[page]

    if not truth:
        return None
    result: dict = {"n_windows_labelled": len(truth), "n_windows": len(alignment["windows"])}
    for name, assignment in alignment["assignments"].items():
        diffs = [abs(assignment[w] - unit) for w, unit in truth.items()]
        result[name] = {
            "accuracy": round(sum(d == 0 for d in diffs) / len(diffs), 4),
            "accuracy_pm1": round(sum(d <= 1 for d in diffs) / len(diffs), 4),
            "mean_unit_distance": round(float(np.mean(diffs)), 4),
        }
    return result


# --- driver ---------------------------------------------------------------------


def process_lecture(lecture_dir: Path, *, every_s: float, threshold: float, crop_frac: float) -> dict | None:
    print(f"== {lecture_dir.name} ==")
    video = lecture_dir / "video.mp4"
    pdf = lecture_dir / "slides.pdf"
    for path in (video, pdf):
        if not path.exists():
            raise SystemExit(f"{path} not found")

    frames = extract_frames(video, every_s, crop_frac)
    pages = render_pages(pdf)
    samples = label_frames(frames, pages, threshold)
    visible = [s for s in samples if s["page"] is not None]
    print(
        f"   {len(frames)} frames vs {len(pages)} pages: slide on screen {len(visible) / len(samples):.0%} "
        f"of the time, {len({s['page'] for s in visible})} distinct pages seen"
    )

    out = {
        "settings": {
            "every_s": every_s,
            "threshold": threshold,
            "crop_frac": crop_frac,
            "match_size": [MATCH_W, MATCH_H],
        },
        "n_pages": len(pages),
        "slide_visible_share": round(len(visible) / len(samples), 4),
        "samples": [{"t": round(i * every_s, 1), **s} for i, s in enumerate(samples)],
    }

    evaluation = None
    alignment_path = lecture_dir / "align" / "alignment.json"
    if alignment_path.exists():
        alignment = json.loads(alignment_path.read_text(encoding="utf-8"))
        evaluation = evaluate(alignment, samples, every_s)
        if evaluation:
            out["evaluation"] = evaluation
            print(f"   ground truth on {evaluation['n_windows_labelled']}/{evaluation['n_windows']} windows:")
            for name in ("uniform", "plain", "dtw"):
                m = evaluation[name]
                print(
                    f"   {name:>8}: accuracy {m['accuracy']:.3f}  ±1 unit {m['accuracy_pm1']:.3f}  "
                    f"mean distance {m['mean_unit_distance']:.1f}"
                )
        else:
            print("   too few slide-visible windows to evaluate against")
    else:
        print("   no align/alignment.json — run `python -m app.align` first for the evaluation part")

    out_dir = lecture_dir / "align"
    out_dir.mkdir(exist_ok=True)
    (out_dir / "video_labels.json").write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"   -> {out_dir / 'video_labels.json'}")
    return evaluation


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Label slide<->transcript alignment ground truth from video frames")
    parser.add_argument("lectures", nargs="+", help="Lecture directories (each with video.mp4 + slides.pdf)")
    parser.add_argument("--every", type=float, default=DEFAULT_EVERY_S, help="Seconds between samples (default: 15)")
    parser.add_argument(
        "--threshold",
        type=float,
        default=DEFAULT_THRESHOLD,
        help=f"Min frame-page correlation to call a slide visible (default: {DEFAULT_THRESHOLD})",
    )
    parser.add_argument(
        "--crop",
        type=float,
        default=DEFAULT_CROP_FRAC,
        help=f"Fraction of frame width occupied by the slide region (default: {DEFAULT_CROP_FRAC})",
    )
    args = parser.parse_args(argv)

    evaluations = []
    for lec in args.lectures:
        evaluations.append(
            process_lecture(Path(lec).resolve(), every_s=args.every, threshold=args.threshold, crop_frac=args.crop)
        )

    done = [e for e in evaluations if e]
    if len(done) > 1:
        print(f"\n== aggregate over {len(done)} lectures ==")
        for name in ("uniform", "plain", "dtw"):
            means = {k: float(np.mean([e[name][k] for e in done])) for k in done[0][name]}
            print(
                f"   {name:>8}: accuracy {means['accuracy']:.3f}  ±1 unit {means['accuracy_pm1']:.3f}  "
                f"mean distance {means['mean_unit_distance']:.1f}"
            )
    return 0


if __name__ == "__main__":
    sys.exit(main())
