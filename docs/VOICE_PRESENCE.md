# Voice Presence (Phase 7)

Local STT/TTS behind an OpenAI-compatible HTTP API so Eve and the Workbench composer
can hear and speak without cloud LLMs.

## Prefer

- **Speaches** (or Voicebox) on `http://127.0.0.1:8000`
- **Kokoro ONNX** TTS (`speaches-ai/Kokoro-82M-v1.0-ONNX`, voice `af_heart`)
- **faster-whisper base** STT (`Systran/faster-whisper-base`) so chat VRAM stays free

## Start

```powershell
.\scripts\start-voice.ps1
```

That script:

1. Creates/starts Docker container `empire-speaches` (`ghcr.io/speaches-ai/speaches:latest-cpu` by default)
2. Binds `127.0.0.1:8000` only (no LAN expose)
3. Ensures the default STT + TTS models are downloaded into volume `empire-speaches-hf`

Or run your chosen speech container/server and set:

```text
EMPIRE_VOICE_BASE_URL=http://127.0.0.1:8000
EMPIRE_VOICE_STT_MODEL=Systran/faster-whisper-base
EMPIRE_VOICE_TTS_MODEL=speaches-ai/Kokoro-82M-v1.0-ONNX
EMPIRE_VOICE_TTS_VOICE=af_heart
```

Optional: `EMPIRE_SPEACHES_IMAGE=ghcr.io/speaches-ai/speaches:latest-cuda` if you deliberately want GPU speech (will contend with Ollama).

## Workbench

1. Enable Toolbelt **Voice Presence**.
2. **Hold the mic** to talk, **release** to transcribe and auto-send (no arrow click).
3. Eve’s reply is spoken **sentence-by-sentence** as text streams in. **Stop** (or **Esc**) cuts speech anytime — even after text finished. Holding the mic also barges in (stops her voice).
4. Eve tools: `voice_transcribe`, `voice_speak` (optional; Workbench covers normal chat).

## Mechanic smoke

```powershell
$env:PYTHONPATH="C:\EMPIRE"
.\venv\Scripts\python.exe -m pipeline.voice_presence health
.\venv\Scripts\python.exe -m pipeline.voice_presence speak "Hello from Eve." -o tmp\voice-out.mp3
.\venv\Scripts\python.exe -m pipeline.voice_presence transcribe tmp\voice-out.mp3
```

API:

```powershell
# Requires Voice Presence limb on
Invoke-RestMethod http://127.0.0.1:8080/api/voice/health
# POST text → audio/mpeg
```

If unreachable, chat still works — voice is opt-in.

## Architect smoke

1. `.\scripts\start-voice.ps1`
2. Hard-refresh http://127.0.0.1:8080/eve.html → Toolbelt **Voice Presence** on
3. **Hold mic → speak → release** — transcript should send itself; Eve answers in text + voice
4. Ask for a multi-sentence reply — first sentence should speak before streaming finishes

Later: hands-free continuous listen / barge-in (not built yet).
