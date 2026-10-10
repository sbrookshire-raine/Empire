---
title: Architect intent vocabulary (EMPIRE)
dataset: eve_memory
fuel: architect_voice
source: Mechanic synthesis from playbook, estate docs, and Architect session patterns (2026-10)
provenance: Canonical routing lives in config/eve-capabilities/intent-codex.json — this document is recall fuel for Eve, not a second source of truth.
companion: architect-vault-voice-supplement.md (Obsidian + Gemini dialogue harvest)
---

# How the Architect speaks (and what Eve should do)

The Architect (Raine) talks in **plain goals**, not tool names. Eve must **`resolve_intent(message)`** first, then **`cognee_recall`** on **`eve_memory`** / **`eve_core`** when the ask is about *how he phrases things* or *estate/backup context*, then call tools — never answer from training memory when **`local_first`** applies.

**Also recall:** `architect-vault-voice-supplement.md` — phrases from daily notes, vault audit, and (when harvested) live Obsidian. **Gemini Web Clipper exports are mostly model text** — only **You:** / first-person user turns count as his voice; see supplement § "Gemini clippings vs Architect notes".

## Core patterns

| How it sounds | Meaning | Intent (codex id) | Local first | Typical tools |
|---------------|---------|-------------------|-------------|---------------|
| scrape / fetch / pull / get the page / gather from a link | Go to a URL and bring content back | `scrape_gather_web` | no | `web_scout` (+ admit web_scout) |
| research / dig into / investigate / what's going on with | Learn deeply: memory + files, then desk/web | `research_deep` | yes | `cognee_recall`, `workspace_search`, then `research_start`, `searxng_search` |
| lookup / look up / find out / anything about | Search local before claiming ignorance | `lookup_general` | yes | `workspace_search`, `cognee_recall`, then wiki or web |
| who is / wiki / discography / on that page | Local Wikipedia archive | `wiki_fact` | yes | `wiki_scout_search`, `wiki_read_section` |
| remember (question) / what do we know / from memory | Recall graph memory | `remember_recall` | yes | `cognee_recall` (eve_core, eve_memory) |
| remember (command) / add to memory / put in cognee | Store with consent | `save_to_memory` | yes | `propose_remember`, `confirm_remember`, `cognee_remember` |
| reverse engineer / figure out how it works / without source | REA local analysis | `reverse_engineer` | yes | `rea_doctor`, `rea_analyze_javascript`, `rea_invoke` (+ admit rea) |
| spreadsheet / table / make me a sheet | Export structured table | `make_spreadsheet` | yes | `create_spreadsheet` |
| task / todo / on my list | PocketBase tasks (not Work Orders) | `task_todo` | yes | `list_tasks`, `create_task`, … |
| process work orders / forge / wire eve / install mcp / give her the skill | Mechanic forge path | `forge_capability` | yes | `draft_work_order`, `read_active_tool`, playbook; Cursor Mechanic for code |
| mechanic green / verify stack / is the stack up | CI health before UX | `stack_health_verify` | yes | `check_workbench_health`, `switchboard_status`; Mechanic runs `mechanic-green.ps1` |
| backup / hub / z drive / zim / rclone / pool / cloud upload / is anything processing | Estate backup & sync status | `backup_estate_status` | yes | `workspace_search` on docs; honest status from logs — not invented cloud state |
| unplugged / offline / no tokens / out of tokens / local only | Sovereign mode — no cloud LLM | `offline_sovereign` | yes | Ollama path; `resolve_intent`; do not claim cloud tools |
| language barrier / how i talk / words i use / codex / vocabulary | Map human words → intents | `interpret_architect_voice` | yes | `resolve_intent`, `cognee_recall("Architect intent vocabulary")`, `capability_route` |
| query your catalog / minimax repo | External OSS catalog.db | `external_catalog` | yes | `search_catalog` |
| what can you do / do you have a tool | Discovery | `what_can_you_do` | yes | `resolve_intent`, `capability_route`, `playbook` |

## Phrases the Architect uses often (EMPIRE session)

These are **triggers**, not magic commands — match with `resolve_intent`:

- **Backup & cloud:** "is anything processing to my z drive", "hub upload", "zim cloud", "rclone", "pool", "EMPIRE_HUB", "consolidation", "offline disc", "T7", "Cognee VHDX", "remount Z"
- **Trust & offline:** "backup ≠ operational", "wired vs backup-only", "when i hit limits", "stop gap", "unplugged internet", "Eve must do tasks with usable resources"
- **Build & forge:** "process work orders", "full file", "mechanic green before architect smoke", "wire Eve", "MCP tools on command", "future considerations", "idea queue"
- **Research stack:** "NotebookLM", "EmbeddingGemma", "Weaviate → Cognee", "ZIM richness", "retrieve then promote"
- **Models (Architect context, not Eve runtime):** "Composer", "DeepSeek flash", "logicbeat", "Strata", "local Deep mode" — route to `resolve_intent` + explain stack vs Cursor; Eve Fast remains `empire-fast:14b`
- **Plain verbs:** "scrape something" = go to location and gather info; "research or lookup" = local then online tools; "analyze any repo" = workspace_search + optional REA/github_scout — not bulk ingest unless asked
- **Vault-era (Obsidian / pre-EMPIRE):** "close the loop", "energy drained", "shiny objects", "start from zero", "how my mind works" (goal app), "did we already build this", "zet / zettelkasten", "remove n8n", "discard pile" (tool triage), "digital jungle"
- **Gemini dialogue (context):** "entire gemini convo", "stack additions to explore", "winning concepts blueprint" — recall for **decisions and history**, not to mimic Gemini's tone

## Eve recall hint

When the Architect's wording is ambiguous, run:

1. `cognee_recall("Architect intent vocabulary vault Gemini dialogue", dataset="eve_memory")`
2. `resolve_intent(<his message>)`
3. Follow `local_first` in the codex result before any online limb

## File anchors (Mechanic)

- Intent codex JSON: `C:/EMPIRE/config/eve-capabilities/intent-codex.json`
- Docs: `C:/EMPIRE/docs/INTENT_CODEX.md`, `C:/EMPIRE/docs/CAPABILITY_ROUTE.md`
- Playbook: `C:/EMPIRE/config/eve-capabilities/playbook/`
- Vault harvest: `C:/EMPIRE/scripts/harvest-architect-voice-from-vault.py` → `architect-vault-voice-supplement.md`
- Re-ingest after edits: `C:/EMPIRE/scripts/ingest-architect-intent-vocabulary.ps1`
