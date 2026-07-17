"""Google Cloud Speech-to-Text adapter — cloud speech recognition.

Lectures last tens of minutes, so the synchronous `recognize` (~1 min limit) is
not suitable. We use the asynchronous `long_running_recognize`, which requires
the audio to reside in Google Cloud Storage. Hence the pipeline is:

    video ──ffmpeg──► 16k WAV ──upload──► gs://bucket/... ──► long_running_recognize

Requires ADC authentication (`gcloud auth application-default login`) and the
APIs enabled: speech.googleapis.com, storage.googleapis.com.
"""

from __future__ import annotations

import time
import uuid
from pathlib import Path

from app.stt.audio import ensure_wav16k, probe_duration
from app.stt.base import Segment, STTProvider, Transcript, Word

# google imports are placed inside the methods so the package imports even
# without the cloud SDKs installed (needed for the local whisper-only scenario)


class GoogleSTTProvider(STTProvider):
    """Cloud STT via Google Cloud Speech-to-Text v1 (long running)."""

    name = "google_stt"

    def __init__(
        self,
        *,
        bucket: str,
        project: str | None = None,
        language_code: str = "en-US",
        model: str = "latest_long",
        enable_punctuation: bool = True,
        enable_word_time_offsets: bool = True,
        location_prefix: str = "autosummary-stt",
        timeout: int = 3600,
    ) -> None:
        if not bucket:
            raise ValueError(
                "No GCS bucket set. Specify GOOGLE_STT_BUCKET in .env or "
                "pass bucket=... — long_running_recognize reads audio from GCS."
            )
        self.bucket = bucket
        self.project = project
        self.language_code = language_code
        self.model = model
        self.enable_punctuation = enable_punctuation
        self.enable_word_time_offsets = enable_word_time_offsets
        self.location_prefix = location_prefix.strip("/")
        self.timeout = timeout

    # ------------------------------------------------------------------

    def _upload(self, wav_path: Path) -> tuple[str, object]:
        """Upload the WAV to GCS, return (gs_uri, blob) for later cleanup."""
        from google.cloud import storage

        client = storage.Client(project=self.project)
        bucket = client.bucket(self.bucket)
        blob_name = f"{self.location_prefix}/{uuid.uuid4().hex}/{wav_path.name}"
        blob = bucket.blob(blob_name)
        blob.upload_from_filename(str(wav_path), content_type="audio/wav")
        return f"gs://{self.bucket}/{blob_name}", blob

    def transcribe(self, media_path: str | Path) -> Transcript:
        from google.cloud import speech

        media_path = Path(media_path)
        duration = probe_duration(media_path)

        wav = ensure_wav16k(media_path)
        gs_uri, blob = self._upload(wav)
        try:
            client = speech.SpeechClient()
            config = speech.RecognitionConfig(
                encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
                sample_rate_hertz=16_000,
                audio_channel_count=1,
                language_code=self.language_code,
                model=self.model,
                use_enhanced=True,
                enable_automatic_punctuation=self.enable_punctuation,
                enable_word_time_offsets=self.enable_word_time_offsets,
            )
            audio = speech.RecognitionAudio(uri=gs_uri)

            t0 = time.monotonic()
            operation = client.long_running_recognize(config=config, audio=audio)
            response = operation.result(timeout=self.timeout)
            elapsed = time.monotonic() - t0
        finally:
            # the GCS object is no longer needed — avoid accumulating junk and storage costs
            try:
                blob.delete()
            except Exception:
                pass

        return self._parse(response, duration=duration, elapsed=elapsed)

    # ------------------------------------------------------------------

    @staticmethod
    def _ts(duration_obj) -> float | None:
        """google.protobuf.Duration -> seconds (float)."""
        if duration_obj is None:
            return None
        try:
            return duration_obj.total_seconds()
        except AttributeError:
            return None

    def _parse(self, response, *, duration, elapsed: float) -> Transcript:
        segments: list[Segment] = []
        for result in response.results:
            if not result.alternatives:
                continue
            alt = result.alternatives[0]
            words = [
                Word(
                    text=w.word,
                    start=self._ts(getattr(w, "start_time", None)),
                    end=self._ts(getattr(w, "end_time", None)),
                    confidence=getattr(w, "confidence", None) or None,
                )
                for w in getattr(alt, "words", [])
            ]
            start = words[0].start if words else None
            end = words[-1].end if words else None
            segments.append(
                Segment(
                    text=alt.transcript.strip(),
                    start=start,
                    end=end,
                    words=words,
                )
            )

        full_text = " ".join(s.text for s in segments if s.text).strip()
        return Transcript(
            text=full_text,
            segments=segments,
            language=self.language_code,
            provider=self.name,
            audio_duration=duration,
            meta={
                "model": self.model,
                "use_enhanced": True,
                "latency_sec": round(elapsed, 2),
            },
        )
