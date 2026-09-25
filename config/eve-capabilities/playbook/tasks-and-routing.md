---
area: tasks-and-routing
one_line: Tasks CRUD, catalog discovery, environment reference (routing detail, operations, awakening).
tools: list_tasks, search_tasks, create_task, update_task, delete_task, search_catalog, load_skill_manifest, tool_docs, playbook, ask_question, list_models, get_model_suite
---

# Tasks, discovery and the reference layer — worked pathways

Tasks are a real CRUD loop (PocketBase). Catalog discovery finds local capabilities; `tool_docs` and
`playbook` are the two lookups that stop guessing — one for **how to call** something, one for **how to
use it to get work done**.

## Tasks
Use when: he asks for a to-do, or wants to know what's outstanding.

- **Ask:** "add a task: fix the ingest lock" → **Do:** `create_task(title, notes)` → **Get:** the task with its id.
- **Ask:** "what's on my list?" → **Do:** `list_tasks()` → **Get:** open tasks in order, with due dates if set.
- **Ask:** "find the task about the VHDX" → **Do:** `search_tasks("VHDX")` → **Get:** matching tasks with ids for follow-up.
- **Ask:** "mark that one done" → **Do:** `search_tasks` → `update_task(id, status="done")` → **Get:** the updated record.
- **Ask:** "delete the duplicate" → **Do:** `search_tasks` → confirm → `delete_task(id)` → **Get:** the removal confirmed by id.

## Catalog and skill discovery
Use when: "do you have a tool for X?", "what can you do about Y?", or before claiming something is unavailable.

- **Ask:** "is there a local tool for reranking?" → **Do:** `search_catalog("rerank")` → **Get:** the capability entry with its Toolbelt limb.
- **Ask:** "what's in the catalog about audio?" → **Do:** `search_catalog("audio stems")` → **Get:** the stem limb and its tools.
- **Ask:** "run one of the eve-skills" → **Do:** `search_catalog("<name>")` → `load_skill_manifest("<name>")` → **Get:** the skill package's SKILL.md (five exist: bayes-update, forecast-baseline, scenario-regret, thought-map, topology-audit).
- **Ask:** "which capabilities are prerequisite for that?" → **Do:** `search_catalog` → `capability_status` → **Get:** the gate you must ask the Architect to open.
- **Ask:** "is X available to me right now?" → **Do:** `search_catalog` **before** refusing → **Get:** an honest answer instead of "I don't have access".

## The two lookups (stop guessing, stop improvising)
Use when: you know the tool but not its syntax, or you know the goal but not the route.

- **Ask:** "what parameters does wiki_extract take?" → **Do:** `tool_docs("wiki_extract")` → **Get:** parameter semantics and gotchas.
- **Ask:** "how do I actually get work done with the spreadsheet limb?" → **Do:** `playbook("build-and-verify")` → **Get:** worked pathways (ask → tools → artefact) you can reuse.
- **Ask:** "which playbook areas exist?" → **Do:** `playbook()` with no topic → **Get:** the area list with one-liners.
- **Ask:** "how do I use the ledger to answer an idea question?" → **Do:** `playbook("memory-and-ideas")` → **Get:** the composite pathway (lookup → past experiments → siblings → capture).
- **Ask:** "what tools does the wiki area need?" → **Do:** `playbook("wiki-archive")` → **Get:** the tool list for that area, so you can chain them.

## Asking instead of guessing (the cheap hinge)
Use when: one fact from him unlocks the whole task.

- **Ask:** "which of these two albums do you mean?" → **Do:** `ask_question(...)` with the two options → **Get:** a decision instead of a coin flip.
- **Ask:** "should I spend the GPU on this?" → **Do:** `ask_question` with the cost, or `resource_pulse` + `admit_for_goal` → **Get:** a yes/no grounded in headroom.
- **Ask:** "do you want the note in Cognee?" → **Do:** `ask_question` → then `propose_remember`/`confirm_remember` → **Get:** consent before storage.
- **Ask:** "ambiguous subject: series, magnet, DRUMS?" → **Do:** `wiki_resolve` for the readings, then `ask_question` only if two remain → **Get:** the right page, no invention.

## Environment reference (documents, not actions)
Use when: you need the map rather than a tool.

- **Ask:** "how is this repo laid out?" → **Do:** read `empire-operations`/`empire-routing-detail` references in the repo (`agents/empire-task-agent/agent/skills/`) → **Get:** the module map and the annotated routing table (these are reference docs — nothing auto-loads them, so read them with `read_file` if needed).
- **Ask:** "what does the session-start ritual say?" → **Do:** read `workbench-awakening` → **Get:** the awakening checklist (reference only).
- **Ask:** "which model should this run on?" → **Do:** `route-local-models` reference + `get_model_suite()` → **Get:** the Fast/Deep/Librarian choice with the context caveat.
- **Ask:** "what's the routing table for wiki vs catalog?" → **Do:** `read_file("agents/empire-task-agent/agent/skills/empire-routing-detail.md")` → **Get:** the intent→tool map (and prefer `playbook` for worked examples).
