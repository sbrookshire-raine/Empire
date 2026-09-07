# Voice Presence (Phase 7)

Local STT/TTS behind an OpenAI-compatible HTTP API so Eve and the Workbench composer
can hear and speak without cloud LLMs.

## Prefer

- **Speaches** or **Voicebox** on `http://127.0.0.1:8000`
- **CPU Piper** (or Kokoro ONNX) for TTS
- **faster-whisper base/small** for STT so chat VRAM stays free

## Start

```powershell
.\scripts\start-voice.ps1
```

Or run your chosen speech container/server and set:

```text
EMPIRE_VOICE_BASE_URL=http://127.0.0.1:8000
```

## Workbench

1. Enable Toolbelt **Voice Presence**.
2. Use the **mic** button on the Eve composer (audio blob → `/api/voice/transcribe`).
3. Eve tools: `voice_transcribe`, `voice_speak` (GPU lease tenant `voice`).

## Health

```powershell
$env:PYTHONPATH="C:\EMPIRE"
.\venv\Scripts\python.exe -m pipeline.voice_presence health
```

If unreachable, chat still works — voice is opt-in.
