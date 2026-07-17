"""STT provider benchmark (experiment E2): latency / cost per provider.

Compares the STT providers (``whisper_cpp`` vs ``google_stt``) on every lecture
that has their transcripts. Quality (WER against the hand-labelled golden set)
lives in ``notebooks/wer_ter.ipynb``; this module covers the operational axes:

1. **Latency** — read back from ``<provider>/transcription.json`` (``meta.
   latency_sec``, recorded by ``app.transcribe`` at transcription time), and
   reported as RTF (real-time factor = processing seconds per audio second).

2. **Cost per audio-hour** —
   * google_stt: the API price per billed minute (``--google-usd-min``;
     default is the Speech-to-Text V1 rate for standard models — which include
     ``latest_long`` — without data logging, $0.024/min as of 2026-07). GCS
     staging adds ~115 MB/h of short-lived storage, far below a cent.
   * whisper_cpp: measured RTF x a rented-GPU hourly rate (``--gpu-usd-hr``;
     default $0.35/h, the typical on-demand RTX 4090 price on vast.ai as of
     2026-07). On owned hardware the marginal cost is ~0.

    python -m app.e2 data/deep-learning-and-computer-vision            # all lectures
    python -m app.e2 data/<course>/<lecture> [<lecture> ...]           # a subset
    python -m app.e2 data/<course> --json docs/experiments/e2.json     # save raw numbers
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

PROVIDERS = ("whisper_cpp", "google_stt")

DEFAULT_GOOGLE_USD_PER_MIN = 0.024  # STT V1, standard models (incl. latest_long), no data logging, 2026-07
DEFAULT_GPU_USD_PER_HR = 0.35  # vast.ai RTX 4090 on-demand, typical, 2026-07


# --- per-lecture measurement -------------------------------------------------


def _load_transcript_meta(lecture_dir: Path, provider: str) -> dict | None:
    path = lecture_dir / provider / "transcription.json"
    if not path.exists():
        return None
    data = json.loads(path.read_text(encoding="utf-8"))
    return {
        "audio_duration": data.get("audio_duration"),
        "latency_sec": (data.get("meta") or {}).get("latency_sec"),
        "model": (data.get("meta") or {}).get("model"),
    }


def evaluate_lecture(lecture_dir: Path, args: argparse.Namespace) -> dict | None:
    row: dict = {"lecture": lecture_dir.name, "providers": {}}
    for provider in args.providers:
        meta = _load_transcript_meta(lecture_dir, provider)
        if meta is None:
            continue
        duration, latency = meta["audio_duration"], meta["latency_sec"]
        row["providers"][provider] = {
            "model": meta["model"],
            "audio_duration_sec": duration,
            "latency_sec": latency,
            "rtf": (latency / duration) if latency and duration else None,
        }
    return row if row["providers"] else None


# --- aggregation & report ----------------------------------------------------


def aggregate(rows: list[dict], args: argparse.Namespace) -> dict:
    """Pooled per-provider totals: latency-weighted RTF and $/audio-hour."""
    agg: dict[str, dict] = {}
    for provider in args.providers:
        stats = [r["providers"][provider] for r in rows if provider in r["providers"]]
        if not stats:
            continue
        total_audio = sum(s["audio_duration_sec"] or 0 for s in stats)
        total_latency = sum(s["latency_sec"] or 0 for s in stats)
        rtf = total_latency / total_audio if total_audio else None
        if provider == "google_stt":
            usd_per_audio_hr = args.google_usd_min * 60
            cost_basis = f"API @ ${args.google_usd_min}/min"
        else:
            usd_per_audio_hr = (rtf or 0) * args.gpu_usd_hr
            cost_basis = f"RTF x ${args.gpu_usd_hr}/GPU-h (vast.ai)"
        agg[provider] = {
            "lectures": len(stats),
            "audio_hours": total_audio / 3600,
            "rtf": rtf,
            "usd_per_audio_hour": usd_per_audio_hr,
            "cost_basis": cost_basis,
            "local": provider == "whisper_cpp",
        }
    return agg


def print_report(rows: list[dict], agg: dict) -> None:
    print(f"\n{'lecture':<12} {'provider':<12} {'audio':>8} {'latency':>8} {'RTF':>6}")
    for row in rows:
        for provider, s in row["providers"].items():
            audio = f"{(s['audio_duration_sec'] or 0) / 60:.0f} min"
            latency = f"{(s['latency_sec'] or 0) / 60:.0f} min"
            rtf = f"{s['rtf']:.3f}" if s["rtf"] else "—"
            print(f"{row['lecture']:<12} {provider:<12} {audio:>8} {latency:>8} {rtf:>6}")
    print(f"\n{'provider':<12} {'lect':>4} {'audio-h':>8} {'RTF':>6} {'$/audio-h':>10}  cost basis")
    for provider, a in agg.items():
        print(
            f"{provider:<12} {a['lectures']:>4} {a['audio_hours']:>8.1f} {a['rtf']:>6.3f}"
            f" {a['usd_per_audio_hour']:>10.3f}  {a['cost_basis']}"
        )


def _expand_lecture_dirs(paths: list[Path]) -> list[Path]:
    """A course dir expands to its lecture subdirs; a lecture dir is taken as-is."""
    lectures: list[Path] = []
    for path in paths:
        if any((path / p / "transcription.json").exists() for p in PROVIDERS):
            lectures.append(path)
        else:
            lectures.extend(
                sorted(
                    d
                    for d in path.iterdir()
                    if d.is_dir() and any((d / p / "transcription.json").exists() for p in PROVIDERS)
                )
            )
    return lectures


def main() -> None:
    parser = argparse.ArgumentParser(description="E2 STT benchmark: latency / cost per provider.")
    parser.add_argument("paths", nargs="+", type=Path, help="course dir or lecture dir(s)")
    parser.add_argument("--providers", nargs="+", default=list(PROVIDERS))
    parser.add_argument("--google-usd-min", type=float, default=DEFAULT_GOOGLE_USD_PER_MIN)
    parser.add_argument("--gpu-usd-hr", type=float, default=DEFAULT_GPU_USD_PER_HR)
    parser.add_argument("--json", type=Path, help="also dump per-lecture and aggregate numbers to this file")
    args = parser.parse_args()

    rows = [r for d in _expand_lecture_dirs(args.paths) if (r := evaluate_lecture(d, args))]
    if not rows:
        sys.exit("[e2] nothing to evaluate: no lecture dir had a provider transcription.json")
    agg = aggregate(rows, args)
    print_report(rows, agg)

    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        payload = {
            "settings": {
                "google_usd_min": args.google_usd_min,
                "gpu_usd_hr": args.gpu_usd_hr,
            },
            "lectures": rows,
            "aggregate": agg,
        }
        args.json.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"\n[e2] wrote {args.json}")


if __name__ == "__main__":
    main()
