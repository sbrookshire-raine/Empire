Use when the user asks about models, which LLM to use, slow vs fast replies, coding vs reasoning,
or when a task clearly needs a different local model than the current chat default.

## Workflow

1. Call `get_model_suite` to read `eveGuidance`, suite status (covered / workable / gap), and pull/remove hints.
2. Call `list_models` if you need the raw installed chat model ids.
3. Before heavy work, call `switch_chat_model` with the best model for the task type.
4. Tell the user which model you switched to and why. Subsequent Eve steps use that model.

## Routing map (16 GB VRAM laptop)

| Task type | Prefer | Examples |
|-----------|--------|----------|
| Daily chat, tools, tasks | `llama3.1:8b` | Greetings, PocketBase CRUD, quick answers |
| Coding / repo work | `qwen2.5-coder:14b` or `huihui_ai/qwen2.5-coder-abliterate:14b` | Edits, refactors, scripts |
| Reasoning / planning | `deepseek-r1:8b` or `deepseek-r1:latest` | Multi-step plans, math, strategy |
| Deep quality | One 27B or `qwen3:8b` | Hardest analysis when user accepts slower replies |
| Memory embed | `nomic-embed-text:latest` | Cognee only — not switched via chat tools |

## Rules

- Do not switch models for greetings or one-line answers.
- Switch before starting coding or reasoning work, not after finishing.
- If `get_model_suite` shows a gap, tell the user the `ollama pull …` command from `pullGaps`.
- If the user mentions duplicates or disk space, summarize `removeSuggestions` with `ollama rm …` commands.
- Embedding model is configured in Cognee (`config/cognee.env`), not via `switch_chat_model`.

## If Ollama is down

Call `ollama_health`, report the error, and point to `ollama serve` plus `.\scripts\start-stack.ps1`.
