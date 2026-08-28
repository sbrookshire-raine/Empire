# 10 — Models and Ollama

EMPIRE uses **Ollama** for all runtime LLM and embedding inference. The Workbench **Models** tab and Eve tools share one **suite planner** in `frontend/ollama_inventory.py`.

## Roles

| Role | Configured via | Examples |
|------|----------------|----------|
| **Eve chat** | `ollama-active-model.json` | `llama3.1:8b`, `deepseek-r1:8b` |
| **Cognee embed** | `config/cognee.env` `EMBEDDING_MODEL` | `nomic-embed-text:latest` |
| **Cognee graph LLM** | `config/cognee.env` `LLM_MODEL` | `llama3.1:latest` |

Chat switching does **not** automatically update Cognee env.

## Target suite (16 GB VRAM reference)

| Skill slot | Target model | Purpose |
|------------|--------------|---------|
| `dailyChat` | `llama3.1:8b` | Fast default, tools, PocketBase |
| `coding` | `qwen2.5-coder:14b` | Repo work (equivalents: abliterate 14b, etc.) |
| `reasoning` | `deepseek-r1:8b` | Planning, multi-step (`deepseek-r1:latest` OK) |
| `deepQuality` | `qwen3:8b` | One strong model; avoid many 27B duplicates |
| `embedding` | `nomic-embed-text:latest` | Cognee only |

Slot status per install:

- **Covered** — ideal or exact target installed
- **Workable** — equivalent installed
- **Gap** — pull recommended

## Workbench Models tab

Shows per skill:

- Target model + why + `ollama pull` command if gap
- Installed match + **Use in Chat**
- **Pull to fill gaps** — only missing skills
- **Remove duplicates & overlap** — `ollama rm` with reasons
- **Eve routing briefing** — copyable text for Eve memory

## API

| Endpoint | Returns |
|----------|---------|
| `GET /api/ollama/inventory` | Full `build_inventory()` payload |
| `GET /api/ollama/models` | Chat list + active + embedded inventory |
| `PUT /api/ollama/model` | Set active model |

## Eve integration

| Tool | Action |
|------|--------|
| `get_model_suite` | Read suite, `eveGuidance`, pull/remove lists |
| `list_models` | Installed chat models |
| `switch_chat_model` | Write active model for next steps |
| `ollama_health` | Connectivity check |

Skill: `route-local-models` — when to switch before coding/reasoning work.

### Routing map (Eve)

| Task | Model |
|------|-------|
| Greetings, quick chat | Keep current / `llama3.1:8b` |
| Coding | Coder 14B |
| Reasoning | `deepseek-r1` |
| Hardest analysis | One 27B or `qwen3:8b` |

## Fit levels

Inventory tags each model:

| Fit | Meaning (16 GB VRAM) |
|-----|----------------------|
| `excellent` | ≤ ~45% VRAM |
| `good` | ≤ ~62% |
| `tight` | ≤ ~95% |
| `heavy` | RAM offload likely |
| `embed` | Embedding only |

## CLI (for Eve subprocess)

```powershell
.\venv\Scripts\python.exe -m frontend.ollama_cli inventory
.\venv\Scripts\python.exe -m frontend.ollama_cli models
.\venv\Scripts\python.exe -m frontend.ollama_cli set-active llama3.1:8b
```

## Customizing the suite

Edit `SUITE_SLOTS` and `PREFERRED_BY_SKILL` in `frontend/ollama_inventory.py` for different hardware or model preferences.

## Next

- [06-eve-agent](06-eve-agent.md)
- [14-configuration](14-configuration.md)
