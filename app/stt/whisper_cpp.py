"""whisper.cpp adapter — local speech recognition.

Runs the `whisper-cli` binary as a subprocess with anti-hallucination flags
(tuned for lectures: long monotonous speech tends to make the decoder loop) and
parses the JSON output into the common `Transcript`.

Anti-hallucination flags:
- `-tpi 0.1`  — temperature increment (below the default 0.2 / whisper 0.4)
- `-bs 5`     — beam size
- `-et 2.8`   — entropy threshold (above the default 2.4: cuts degenerate output faster)
- `-mc 64`    — a short context window reduces repetition loops
- `--vad`     — the VAD prefilter drops silence before decoding
- the large-v3-turbo model
"""

from __future__ import annotations

import json
import subprocess
import tempfile
import time
from pathlib import Path

from app.stt.audio import ensure_wav16k, probe_duration
from app.stt.base import Segment, STTProvider, Transcript, Word

# --- default paths and parameters (overridden via config/constructor) ---

DEFAULT_WHISPER_CLI = Path("/Users/shamilarslanov/whisper.cpp/build/bin/whisper-cli")
DEFAULT_WHISPER_MODEL = Path("/Users/shamilarslanov/whisper-models/ggml-large-v3-turbo.bin")
DEFAULT_VAD_MODEL = Path("/Users/shamilarslanov/whisper-models/ggml-silero-v6.2.0.bin")

# anti-hallucination defaults
BEAM_SIZE = 5
BEST_OF = 5
TEMP_INC = 0.1
ENTROPY_THOLD = 2.8
MAX_CONTEXT = 64

# steers the language and topic — reduces hallucinations on technical terms
DEFAULT_INITIAL_PROMPT = (
    "The following is a university lecture on machine learning, deep learning "
    "and computer vision. It uses technical terms such as gradient descent, "
    "backpropagation, convolution, transformer, attention, embedding, tensor."
)


class WhisperCppProvider(STTProvider):
    """Local STT via whisper.cpp (private, free, no cloud)."""

    name = "whisper_cpp"

    def __init__(
        self,
        *,
        cli_path: str | Path = DEFAULT_WHISPER_CLI,
        model_path: str | Path = DEFAULT_WHISPER_MODEL,
        vad_model_path: str | Path | None = DEFAULT_VAD_MODEL,
        language: str = "en",
        initial_prompt: str = DEFAULT_INITIAL_PROMPT,
        beam_size: int = BEAM_SIZE,
        best_of: int = BEST_OF,
        temperature_inc: float = TEMP_INC,
        entropy_thold: float = ENTROPY_THOLD,
        max_context: int = MAX_CONTEXT,
        threads: int | None = None,
    ) -> None:
        self.cli_path = Path(cli_path)
        self.model_path = Path(model_path)
        self.vad_model_path = Path(vad_model_path) if vad_model_path else None
        self.language = language
        self.initial_prompt = initial_prompt
        self.beam_size = beam_size
        self.best_of = best_of
        self.temperature_inc = temperature_inc
        self.entropy_thold = entropy_thold
        self.max_context = max_context
        self.threads = threads

    # ------------------------------------------------------------------

    def _check_paths(self) -> None:
        if not self.cli_path.exists():
            raise FileNotFoundError(
                f"whisper-cli not found: {self.cli_path}. Build whisper.cpp and/or specify the path via WHISPER_CLI."
            )
        if not self.model_path.exists():
            raise FileNotFoundError(
                f"whisper model not found: {self.model_path}. Download "
                "ggml-large-v3-turbo.bin or specify the path via WHISPER_MODEL."
            )
        if self.vad_model_path and not self.vad_model_path.exists():
            raise FileNotFoundError(
                f"VAD model not found: {self.vad_model_path}. "
                "Download ggml-silero-*.bin or disable VAD (vad_model_path=None)."
            )

    def transcribe(self, media_path: str | Path) -> Transcript:
        self._check_paths()
        media_path = Path(media_path)
        duration = probe_duration(media_path)

        with tempfile.TemporaryDirectory() as tmp:
            wav = ensure_wav16k(media_path, out_dir=tmp)
            stem = Path(tmp) / "out"

            cmd: list[str] = [
                str(self.cli_path),
                "-m",
                str(self.model_path),
                "-f",
                str(wav),
                "-l",
                self.language,
                # anti-hallucination
                "-bs",
                str(self.beam_size),
                "-bo",
                str(self.best_of),
                "-tpi",
                str(self.temperature_inc),
                "-et",
                str(self.entropy_thold),
                "-mc",
                str(self.max_context),
                # initial prompt
                "--prompt",
                self.initial_prompt,
                # output
                "-of",
                str(stem),
                "-oj",  # JSON with timestamps and token probabilities
            ]
            if self.vad_model_path:
                cmd += ["--vad", "--vad-model", str(self.vad_model_path)]
            if self.threads:
                cmd += ["-t", str(self.threads)]

            t0 = time.monotonic()
            proc = subprocess.run(cmd, capture_output=True, text=True)
            elapsed = time.monotonic() - t0
            if proc.returncode != 0:
                raise RuntimeError(f"whisper-cli failed with an error:\n{proc.stderr[-2000:]}")

            json_path = Path(f"{stem}.json")
            if not json_path.exists():
                raise RuntimeError("whisper-cli did not produce JSON output; check the binary version.")
            data = json.loads(json_path.read_text(encoding="utf-8"))

        return self._parse(data, duration=duration, elapsed=elapsed)

    # ------------------------------------------------------------------

    @staticmethod
    def _ts(value) -> float | None:
        """whisper.cpp JSON returns offsets in milliseconds -> seconds."""
        if value is None:
            return None
        try:
            return float(value) / 1000.0
        except (TypeError, ValueError):
            return None

    def _parse(self, data: dict, *, duration, elapsed: float) -> Transcript:
        segments: list[Segment] = []
        for seg in data.get("transcription", []):
            offsets = seg.get("offsets", {})
            text = (seg.get("text") or "").strip()
            words: list[Word] = []
            for tok in seg.get("tokens", []):
                tok_text = (tok.get("text") or "").strip()
                # skip whisper special-marker tokens like [_BEG_]
                if not tok_text or tok_text.startswith("[_"):
                    continue
                t_off = tok.get("offsets", {})
                words.append(
                    Word(
                        text=tok_text,
                        start=self._ts(t_off.get("from")),
                        end=self._ts(t_off.get("to")),
                        confidence=tok.get("p"),
                    )
                )
            segments.append(
                Segment(
                    text=text,
                    start=self._ts(offsets.get("from")),
                    end=self._ts(offsets.get("to")),
                    words=words,
                )
            )

        full_text = " ".join(s.text for s in segments if s.text).strip()
        result = data.get("result", {})
        return Transcript(
            text=full_text,
            segments=segments,
            language=result.get("language") or self.language,
            provider=self.name,
            audio_duration=duration,
            meta={
                "model": self.model_path.name,
                "vad": bool(self.vad_model_path),
                "beam_size": self.beam_size,
                "entropy_thold": self.entropy_thold,
                "latency_sec": round(elapsed, 2),
                "system": data.get("system_info"),
            },
        )
