# Product Context — Why EMPIRE exists & UX goals

## Why it exists
Personal, self-hosted AI companion after a multi-year through-line (`docs/MOTIVATION.md`, `docs/ODYSSEY.md`). Reclaim time; remember local knowledge; forge hard builds via Cursor.

## One breath (EMPIRE_CLARITY.md)
> Eve is my partner; Truth Drift, DAZE, and Stem Factory are LEGO products.

## User experience goals
- Chat at http://127.0.0.1:8080/eve.html (optional Speaches push-to-talk).
- Workbench memory → Cognee (`eve_memory` / optimized `eve_core`).
- PocketBase tasks from the Workbench.
- Toolbelt limbs (Wiki Local, DAZE, Stem Factory, scouts) — mostly off until admitted.
- Work Orders → Cursor Forge Protocol when Architect says “Process Work Orders.”
- **Private by default** — inference and chat on the machine; cloud tier is for **backup copies** the Architect controls, not vendor LLM APIs.

## Three layers
| Layer | What it is |
|-------|-----------|
| **Eve Core** | Chat, tasks, Cognee, staging memory, wiki read/scout |
| **LEGO shelf** | Truth Drift, DAZE, Stem Factory |
| **Session reach** | Research Partner + Toolbelt session limbs |

## Memory model
- Recall: `eve_core`, `eve_memory`, `primitives_test`.
- Propose → `eve_staging` → confirm/drop.
- **Memory Bank** (`memory-bank/`) is for IDE agents (Cursor/Cline), not Eve’s graph.

## Primary users
- **Architect** — browser + priorities.
- **Cursor Mechanic** — code, MCP, scripts.
- **Eve** — runtime agent on Ollama (not Cursor’s persona).

## Estate UX (operator, not product UI)
Backup hub and inventory docs support the Architect’s “where is my stuff” anxiety — orthogonal to Eve chat UX but critical for long-running project continuity (see ESTATE §12, ODYSSEY §14).
