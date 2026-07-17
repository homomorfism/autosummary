# Local whisper.cpp: CLI and server

In this project, local STT runs through the `WhisperCppProvider` adapter, which
calls **`whisper-cli`** as a subprocess (see `app/stt/whisper_cpp.py`). Below are
the commands for both the CLI and the `whisper-server` HTTP server (if you want to
run recognition as a service).

Paths on this machine (already built and downloaded):

```
WHISPER_CLI    = /Users/shamilarslanov/whisper.cpp/build/bin/whisper-cli
WHISPER_SERVER = /Users/shamilarslanov/whisper.cpp/build/bin/whisper-server
MODEL          = /Users/shamilarslanov/whisper-models/ggml-large-v3-turbo.bin
VAD_MODEL      = /Users/shamilarslanov/whisper-models/ggml-silero-v6.2.0.bin
```

---

## 0. Audio preparation (16 kHz mono WAV)

Both the CLI and the server expect 16 kHz mono PCM WAV. From a lecture video:

```bash
ffmpeg -y -i lecture.mp4 -vn -ac 1 -ar 16000 -c:a pcm_s16le lecture.16k.wav
```

(In the pipeline, `app/stt/audio.py` does this automatically.)

---

## 1. CLI — one-off recognition

The command with anti-hallucination flags (as in the adapter):

```bash
/Users/shamilarslanov/whisper.cpp/build/bin/whisper-cli \
  -m /Users/shamilarslanov/whisper-models/ggml-large-v3-turbo.bin \
  -f lecture.16k.wav \
  -l en \
  -bs 5 -bo 5 \
  -tpi 0.1 \
  -et 2.8 \
  -mc 64 \
  --vad --vad-model /Users/shamilarslanov/whisper-models/ggml-silero-v6.2.0.bin \
  --prompt "University lecture on machine learning and computer vision." \
  -of lecture_out \
  -osrt -otxt -oj
```

This creates `lecture_out.srt`, `lecture_out.txt`, and `lecture_out.json`. The adapter
uses the JSON (`-oj`) and parses the timecodes and token probabilities.

Flags:
- `-bs 5` beam size, `-bo 5` best-of
- `-tpi 0.1` temperature increment (below the default 0.2 / whisper 0.4)
- `-et 2.8` entropy threshold (above the default 2.4 — cuts off degenerate output faster)
- `-mc 64` max context (a short window — fewer repetition loops)
- `--vad` + `--vad-model` — drops silence before decoding

---

## 2. The `whisper-server` HTTP server

Start the server with the model held in memory (recognizes over HTTP, convenient for a service):

```bash
/Users/shamilarslanov/whisper.cpp/build/bin/whisper-server \
  -m /Users/shamilarslanov/whisper-models/ggml-large-v3-turbo.bin \
  --host 127.0.0.1 \
  --port 8080 \
  -l en \
  -bs 5 -bo 5 -tpi 0.1 -et 2.8 -mc 64 \
  --vad --vad-model /Users/shamilarslanov/whisper-models/ggml-silero-v6.2.0.bin \
  --convert
```

- `--host` / `--port` — the server address
- `--convert` — the server itself converts the input to 16 kHz WAV via ffmpeg (you can
  send mp3/mp4/raw wav)
- `-t N` — number of threads (defaults to the number of cores)

The server listens on `http://127.0.0.1:8080`. For the web UI, open this address in
a browser.

### Recognize a file (HTTP)

```bash
curl http://127.0.0.1:8080/inference \
  -H "Content-Type: multipart/form-data" \
  -F file=@lecture.16k.wav \
  -F temperature=0.0 \
  -F response_format=json
```

`response_format` accepts `json`, `text`, `srt`, `verbose_json`, `vtt`.
The endpoint is compatible with the OpenAI Whisper format (`/inference` ≈ `/v1/audio/transcriptions`).

### Swap the model on the fly

```bash
curl http://127.0.0.1:8080/load \
  -H "Content-Type: multipart/form-data" \
  -F model="/Users/shamilarslanov/whisper-models/ggml-large-v3-turbo.bin"
```

---

## 3. Useful notes

- List all flags: `whisper-cli --help` and `whisper-server --help`.
- Download a different model: `bash /Users/shamilarslanov/whisper-models/download-ggml-model.sh large-v3-turbo`.
- If you change the paths/model, set them in `.env` (`WHISPER_CLI`, `WHISPER_MODEL`,
  `WHISPER_VAD_MODEL`); the adapter will pick them up from the config.

> Right now the adapter calls `whisper-cli` (simpler, no running service). If you
> specifically need network mode through `whisper-server`, the adapter is easy to extend
> with an HTTP call to `/inference` — the `Transcript` structure does not change because of it.
