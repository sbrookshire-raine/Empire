---
area: tasks-and-routing
one_line: Tasks CRUD, catalog discovery, environment reference (routing detail, operations, awakening).
tools: list_tasks, search_tasks, create_task, update_task, delete_task, resolve_intent, capability_route, search_catalog, tool_docs, playbook, list_models, get_model_suite
skills: empire-operations, empire-routing-detail, manage-tasks, memory-recall, skill-capability-routing
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

## Plain language (intent codex — use first)
Use when: the user speaks in normal verbs — scrape, research, lookup, remember — without tool names.

- **Ask:** "scrape this blog post and summarize" → **Do:** `resolve_intent(message)` → `web_scout(url)` after admitting **web_scout** → **Get:** cached markdown summary, URL cited.
- **Ask:** "research whether yt-dlp changed recently" → **Do:** `resolve_intent` → `cognee_recall` → `research_start("yt-dlp changes")` → **Get:** desk digest, not a wall of text in chat.
- **Ask:** "look up magnets in the archive" → **Do:** `resolve_intent` → `wiki_scout_search("Magnetism")` (not training memory).

## Route index (Eve's tools — use second)
Use when: "do you have a tool for X?", "what can you do about Y?", or before claiming something is unavailable.

- **Ask:** "is there a local tool for reranking?" → **Do:** `capability_route("rerank")` → **Get:** `retrieval_rerank` limb + tools + `load` hints → `playbook` / `tool_docs` as needed.
- **Ask:** "what's available for audio stems?" → **Do:** `capability_route("audio stems")` → **Get:** stem_factory limb + `stem_run` tools.
- **Ask:** "reverse engineer this Electron app" → **Do:** `capability_route("reverse engineer")` → admit **REA** if off → `rea_doctor` → `playbook("reverse-engineering")`.
- **Ask:** "is X available to me right now?" → **Do:** `capability_route("X")` → `resource_pulse()` → **Get:** limb status instead of "I don't have access".

## External OSS catalog (catalog.db only)
Use when: mining the **intake catalog** for third-party repos/MCP candidates — not for Eve's built-in tools.

- **Ask:** "find minimax in the catalog" → **Do:** `search_catalog("minimax")` → **Get:** repository rows from catalog.db.
- **Ask:** "run one of the eve-skills" → **Do:** `capability_route("<name>")` first; `search_catalog` only if hunting an external package row.
- **Ask:** "which capabilities are prerequisite for that?" → **Do:** `capability_route` → `capability_status` → **Get:** the gate to ask the Architect to open.

## The two lookups (stop guessing, stop improvising)
Use when: you know the tool but not its syntax, or you know the goal but not the route.

- **Ask:** "what parameters does wiki_extract take?" → **Do:** `tool_docs("wiki_extract")` → **Get:** parameter semantics and gotchas.
- **Ask:** "how do I actually get work done with the spreadsheet limb?" → **Do:** `playbook("build-and-verify")` → **Get:** worked pathways (ask → tools → artefact) you can reuse.
- **Ask:** "which playbook areas exist?" → **Do:** `playbook()` with no topic → **Get:** the area list with one-liners.
- **Ask:** "how do I use the ledger to answer an idea question?" → **Do:** `playbook("memory-and-ideas")` → **Get:** the composite pathway (lookup → past experiments → siblings → capture).
- **Ask:** "what tools does the wiki area need?" → **Do:** `playbook("wiki-archive")` → **Get:** the tool list for that area, so you can chain them.

## Asking instead of guessing (the cheap hinge)
Use when: one fact from him unlocks the whole task.

**There is no ask tool.** `ask_question` is switched off on purpose (it produced malformed tool
calls on local Ollama). Ask **in prose**, finish the turn, and act on his reply — that is the
supported hinge.

- **Ask:** "which of these two albums do you mean?" → **Do:** name both readings in plain text and stop → **Get:** a decision instead of a coin flip (his reply continues the chat).
- **Ask:** "should I spend the GPU on this?" → **Do:** `resource_pulse()` then `admit_for_goal(...)` first, and ask in prose only for the judgement call → **Get:** a yes/no grounded in headroom.
- **Ask:** "do you want the note in Cognee?" → **Do:** `propose_remember(text)` → say what is proposed, in prose → `confirm_remember(id)` once he agrees → **Get:** consent before storage.
- **Ask:** "ambiguous subject: series, magnet, DRUMS?" → **Do:** `wiki_resolve("magnets")` for the readings, then name the candidates in prose if two remain → **Get:** the right page on his reply, no invention.

## Environment reference (documents, not actions)
Use when: you need the map rather than a tool.

- **Ask:** "how is this repo laid out?" → **Do:** `playbook("tasks-and-routing")` → **Get:** the map as worked pathways. The `agents/empire-task-agent/agent/skills/*.md` files (`empire-operations`, `empire-routing-detail`) are the Mechanic's reference: they never enter context and no tool of hers reads `C:\EMPIRE` (E-29).
- **Ask:** "what does the session-start ritual say?" → **Do:** `playbook("workbench-and-files")` → **Get:** the awakening steps as examples (the `workbench-awakening` file is reference, not runtime).
- **Ask:** "which model should this run on?" → **Do:** `get_model_suite()` + `playbook("machine-and-services")` → **Get:** the Fast/Deep/Librarian choice with the context caveat.
- **Ask:** "what's the routing table for wiki vs catalog?" → **Do:** `playbook("wiki-archive")` for archive asks, `playbook("web-and-sources")` for outside sources → **Get:** the intent→tool map as examples (the `empire-routing-detail.md` file itself is not readable at runtime).
