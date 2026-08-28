---
name: meetily
description: Guides installing and operating Meetily, a privacy-first, fully local AI meeting assistant that captures audio, transcribes it in real time with Whisper/Parakeet, and generates AI summaries on-device — using local Ollama as the default LLM provider (hosted providers remain optional, off by default). Use when the user wants to install Meetily, set up its backend transcription server and frontend app, transcribe/summarize a meeting recording or imported audio file, or build the project from source on Linux. Touches Build1's Inference layer (Local Ollama) and, when integrated, Memory/RAG (Cognee) and Backend (PocketBase).
icon: mic
color: Blue
---

# Meetily — Local Meeting Transcription & Summarization

Local-first meeting transcription + summarization app (Zackriya-Solutions/meetily). Repo layout: `backend/` (Python transcription server), `frontend/` (Tauri + Next.js desktop app), `llama-helper/` (local LLM helper), `docs/`.

## End-user installation (prebuilt binaries — Windows/macOS)
- **Windows:** download the latest `x64-setup.exe` from the project's GitHub releases page and run it.
- **macOS:** download the latest `.dmg` from the same releases page, open it, drag Meetily to Applications, launch from Applications.
- Always fetch the actual latest asset name/version from the releases page rather than assuming a fixed version string.

## Building from source (Linux, or contributor workflow)
1. Clone the repo and follow `backend/README` to build the Python transcription server (Whisper/Parakeet models run fully on-device).
2. Build the Tauri + Next.js frontend per `frontend/README`.
3. Configure the LLM provider used for summarization in `llama-helper/` — point it at a local Ollama instance (e.g. `OLLAMA_HOST=http://localhost:11434`) as the default. Hosted providers (Claude/Groq/OpenRouter/OpenAI-compatible) remain available but should only be enabled if the user explicitly opts in.

## Operating
- Start the backend transcription server, then launch the frontend app.
- Record a live meeting or import an existing audio file; transcription streams in real time, and a summary is generated once the model finishes processing.

## Build1 Integration
- **Inference**: configure Meetily's summarization step to call local Ollama by default instead of a hosted LLM.
- **Memory/RAG**: pipe finished transcripts/summaries into Cognee to build a searchable knowledge graph of meeting content (attendees, decisions, action items) for later retrieval.
- **Backend**: store meeting metadata (title, date, participants, summary, storage path of the raw audio/transcript) in PocketBase collections.
- **Nervous System**: expose "transcribe meeting" and "summarize meeting" as FastMCP tools so other Build1 agents can trigger them programmatically.
