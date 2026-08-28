---
name: ai-assistant
description: Summarizes text, classifies content, extracts structured data, generates images, and chats with an LLM — backed primarily by local Ollama models, with optional hosted-provider fallback only if the user explicitly asks for one. Activate for "summarize this", "extract structured data", "classify this", "generate an image", or "chat with a model". Touches Build1's Inference layer (Local Ollama) and can be exposed as a tool through FastMCP.
icon: cpu
color: Purple
---

# AI Assistant

## Activate when
- "Summarize this" / "Extract key points from..."
- "Extract structured data from..." / "Give me a JSON of..."
- "Classify this as..." / "Is this positive or negative?"
- "Generate an image of..." / "Draw a..."
- "Chat with [a local model]..."
- "Remember that..." / "What did I say about X?"

## Primary scripts

Keep the deterministic implementation code in a `scripts/` subdirectory alongside this skill (not inlined here). Suggested layout:

| Script | Purpose |
|---|---|
| `scripts/llm_local.py` | Primary chat/complete/summarize/classify interface — calls the local Ollama HTTP API (`http://localhost:11434`) by default |
| `scripts/llm_provider_router.py` | Optional multi-provider routing with Ollama as the default/first entry; hosted providers only added if the user opts in |
| `scripts/structured_llm_extractor.py` | Pydantic-typed extraction with retry, run against the local model |
| `scripts/llm_guardrails.py` | Hallucination, PII, prompt-injection, and toxicity checks on model output |
| `scripts/image_gen.py` | Image generation (local diffusion model if available; hosted API only on explicit request) |
| `scripts/memory_tools.py` | Cross-session key-value memory — prefer routing this through Cognee (see below) rather than a standalone store |
| `scripts/audio_tools.py` | Local transcription (e.g. Whisper) and meeting summaries |

## Quick start
```python
from scripts.llm_local import chat, summarize, extract_json
from scripts.llm_provider_router import fallback_completion, detect_available_providers
from scripts.structured_llm_extractor import extract_structured
from scripts.llm_guardrails import run_all_checks

# Default: talk to local Ollama
reply = chat(model="llama3", prompt="Summarize the attached notes.")
```

## Build1 Integration
- **Inference**: default every call to local Ollama (`ollama run <model>` / `http://localhost:11434/api/generate`); only fall back to a hosted LLM provider if the user explicitly requests one, and say so when you do.
- **Nervous System**: wrap `chat`, `summarize`, `extract_json`, and `classify` as FastMCP tools so other Build1 components (frontend, agents) can call them uniformly.
- **Memory/RAG**: route "remember that / what did I say about X" requests into Cognee's graph memory instead of a separate key-value store, so extracted facts are queryable alongside other project knowledge.
- **Backend**: persist structured extraction results or generated images' metadata in PocketBase collections rather than an external database.
