Use when the user asks about models, which LLM to use, slow vs fast replies, coding vs reasoning,
or when a task clearly needs a different local model than the current chat default.

## Workflow

1. Call `get_model_suite` or `list_models` only when diagnosing install gaps or Ollama health.
2. Tell the user which **Workbench mode** fits the task — never call `switch_chat_model`.
3. The user switches modes manually in the chat header:
   - **Fast Mode (14b)** — default daily driver
   - **Deep Mode (32b)** — complex planning and architecture
   - **Librarian (Command-R 35b)** — massive cross-file synthesis
4. After they switch, continue in the new session they started.

## Routing map (16 GB VRAM laptop)

| Task type | Tell the user to choose |
|-----------|-------------------------|
| Daily chat, tools, tasks | Fast Mode (14b) |
| Deep planning, complex MCP, ARC sessions | Deep Mode (32b) |
| Many flattened files at once, heavy RAG | Librarian (Command-R 35b) |
| Memory embed | `nomic-embed-text:latest` in Cognee only — not a chat mode |

## Rules

- **Never** call `switch_chat_model` — it is disabled. Model hot-swapping causes VRAM thrashing.
- Do not switch models for greetings or one-line answers.
- Sampling is **per Workbench mode** (top_p **0.90** shared):
  - Fast → temperature **0.2** (strict tool JSON)
  - Deep → temperature **0.7** (creative brainstorming)
  - Librarian → temperature **0.4** (balanced retrieval)
- Every mode uses **num_ctx 8192** to protect 16 GB VRAM.
- If `get_model_suite` shows a gap, tell the user the `ollama pull …` command from `pullGaps`.
- Embedding model is configured in Cognee (`config/cognee.env`), not via chat tools.

## If Ollama is down

Call `ollama_health`, report the error, and point to `ollama serve` plus `.\\scripts\\start-stack.ps1`.
