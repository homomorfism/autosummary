# Локальный whisper.cpp: CLI и сервер

В проекте локальный STT работает через адаптер `WhisperCppProvider`, который
вызывает **`whisper-cli`** как подпроцесс (см. `app/stt/whisper_cpp.py`). Ниже —
команды и для CLI, и для HTTP-сервера `whisper-server` (если хочется крутить
распознавание как сервис).

Пути на этой машине (уже собрано и скачано):

```
WHISPER_CLI    = /Users/shamilarslanov/whisper.cpp/build/bin/whisper-cli
WHISPER_SERVER = /Users/shamilarslanov/whisper.cpp/build/bin/whisper-server
MODEL          = /Users/shamilarslanov/whisper-models/ggml-large-v3-turbo.bin
VAD_MODEL      = /Users/shamilarslanov/whisper-models/ggml-silero-v6.2.0.bin
```

---

## 0. Подготовка аудио (16 кГц моно WAV)

И CLI, и сервер ждут 16 кГц моно PCM WAV. Из видео лекции:

```bash
ffmpeg -y -i lecture.mp4 -vn -ac 1 -ar 16000 -c:a pcm_s16le lecture.16k.wav
```

(В пайплайне это делает `app/stt/audio.py` автоматически.)

---

## 1. CLI — разовое распознавание

Команда с anti-hallucination флагами (как в адаптере):

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

Создаст `lecture_out.srt`, `lecture_out.txt`, `lecture_out.json`. Адаптер
использует JSON (`-oj`) и парсит таймкоды/вероятности токенов.

Флаги:
- `-bs 5` beam size, `-bo 5` best-of
- `-tpi 0.1` temperature increment (ниже дефолта 0.2 / whisper 0.4)
- `-et 2.8` entropy threshold (выше дефолта 2.4 — быстрее режет вырожденный вывод)
- `-mc 64` max context (короткое окно — меньше циклов повторов)
- `--vad` + `--vad-model` — выкидывает тишину до декодирования

---

## 2. HTTP-сервер `whisper-server`

Поднять сервер с моделью в памяти (распознаёт по HTTP, удобно для сервиса):

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

- `--host` / `--port` — адрес сервера
- `--convert` — сервер сам конвертирует вход в 16 кГц WAV через ffmpeg (можно
  слать mp3/mp4/исходный wav)
- `-t N` — число потоков (по умолчанию по числу ядер)

Сервер слушает на `http://127.0.0.1:8080`. Веб-морда — открой этот адрес в
браузере.

### Распознать файл (HTTP)

```bash
curl http://127.0.0.1:8080/inference \
  -H "Content-Type: multipart/form-data" \
  -F file=@lecture.16k.wav \
  -F temperature=0.0 \
  -F response_format=json
```

`response_format` принимает `json`, `text`, `srt`, `verbose_json`, `vtt`.
Эндпоинт совместим с форматом OpenAI Whisper (`/inference` ≈ `/v1/audio/transcriptions`).

### Сменить модель на лету

```bash
curl http://127.0.0.1:8080/load \
  -H "Content-Type: multipart/form-data" \
  -F model="/Users/shamilarslanov/whisper-models/ggml-large-v3-turbo.bin"
```

---

## 3. Полезное

- Список всех флагов: `whisper-cli --help` и `whisper-server --help`.
- Скачать другую модель: `bash /Users/shamilarslanov/whisper-models/download-ggml-model.sh large-v3-turbo`.
- Если меняешь пути/модель — пропиши их в `.env` (`WHISPER_CLI`, `WHISPER_MODEL`,
  `WHISPER_VAD_MODEL`); адаптер подхватит из конфига.

> Сейчас адаптер ходит в `whisper-cli` (проще и без поднятого сервиса). Если
> нужен именно сетевой режим через `whisper-server`, адаптер легко расширить
> HTTP-вызовом `/inference` — структура `Transcript` от этого не меняется.
