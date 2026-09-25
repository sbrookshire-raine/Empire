---
area: build-and-verify
one_line: Write and verify code, query local data, make spreadsheets, draft work orders.
tools: author_code, python_verify, query_data, create_spreadsheet, structured_extract, retrieval_rerank, draft_work_order, read_document
---

# Build and verify — worked pathways

The rule that makes this safe on a 14B: **claim only what a tool returned.** Write code in a
disposable worktree, run it, show the diff; never merge without the Architect.

## Session limbs (admit BEFORE you can call the tool)
The Toolbelt is mostly off at session start — measured 2026-09-24, only `wiki_local` was active, so
`create_spreadsheet` did not exist as a tool and the turn ended in *"Let's create a spreadsheet…"*
with nothing written. Light limbs are yours to admit (the Architect should not have to flip switches):

- **Ask:** "make me a spreadsheet of X" → **Do:** `resource_pulse()` → if `create_spreadsheet` is in `can_admit_now`, then `admit_for_goal("create_spreadsheet")` → **Get:** the limb admitted (say so, and that it lands next turn).
- **Ask:** "write a script for this" → **Do:** `resource_pulse()` → `admit_for_goal("author_code")` → **Get:** the coding limb admitted, then `author_code`/`python_verify` next turn.
- **Ask:** "query my data file" → **Do:** `resource_pulse()` → `admit_for_goal("query_data")` → **Get:** DuckDB admitted, then the SELECT next turn.
- **Ask:** "search my notes" → **Do:** `resource_pulse()` → `admit_for_goal("workspace_search")` (or `read_document`) → **Get:** the file limb admitted.
- **Ask:** "check the web for X" → **Do:** `resource_pulse()` → `admit_for_goal("web_scout")` / `github_scout` / `container_scout` → **Get:** the scout admitted (light network skills work even when the GPU is busy).
- **Ask:** anything on the `ask_architect_first` list (vision, stems, thought experiments, loom, rerank) → **Do:** `resource_pulse()` then ask him in one line → **Get:** an honest "this one needs your switch", never a silent failure.

Admitting is per category and expires (`ttl_min`, default short); a tool resolved at `turn.started`, so
admitted limbs are callable **from the next turn** — say that plainly instead of pretending to have run it.

## Writing and changing code
Use when: they ask for a script, a fix, a small tool, or "make X do Y".

- **Ask:** "write a script that renames my screenshots by date" → **Do:** `admit_for_goal("author_code")` → `author_code(goal, files=[...])` → `python_verify` → **Get:** a diff in a disposable worktree plus test output; you never merge.
- **Ask:** "this JSON parser keeps dying — fix it" → **Do:** `author_code("make the parser tolerate trailing commas")` → `python_verify` → **Get:** the patch + the failing→passing test.
- **Ask:** "add a retry to the ingest call" → **Do:** `glob`/`read_file` to find the call → `author_code` → `python_verify` → **Get:** a reviewable diff with the reason.
- **Ask:** "is this change safe?" → **Do:** `python_verify` alone (syntax + lint + tests in the worktree) → **Get:** a verdict with the test list.
- **Ask:** "turn this snippet into a reusable script" → **Do:** `author_code` → `python_verify` → **Get:** the file path in the worktree for review.

## Verifying before you claim
Use when: any numeric, structural, or logical claim you are about to make.

- **Ask:** "does a 3-ball cascade map onto a 4-limb drum pattern?" → **Do:** `author_code` a small simulation → `python_verify` → **Get:** numbers (periods, duty cycles) instead of prose.
- **Ask:** "how many of these entries are duplicates?" → **Do:** `query_data("SELECT count(*) …")` → **Get:** the count with the query shown.
- **Ask:** "is the claim in this doc actually true for our data?" → **Do:** `read_document` → `query_data` → **Get:** a checked statement, or an honest "not checkable here".
- **Ask:** "prove the parsing rule works on the last 20 events" → **Do:** `author_code` + `python_verify` → **Get:** pass/fail with the sample.

## Local data files (CSV/JSON/Parquet/SQLite)
Use when: the data is on disk and they want facts out of it, not a reading of it.

- **Ask:** "which primitives do I use most in my ledger?" → **Do:** `query_data("SELECT primitives, count(*) c FROM data GROUP BY primitives ORDER BY c DESC LIMIT 12", data_file="C:/Empire_Workbench/04_Thought_Experiments/loom/workspace_data/primitive_ledger.csv")` → **Get:** the ranked list (read-only DuckDB; SELECT only).
- **Ask:** "how many rows mention timing?" → **Do:** `query_data("SELECT count(*) FROM data WHERE lower(primitives) LIKE '%timing%'", data_file=...)` → **Get:** the number.
- **Ask:** "join my tasks export with the ledger" → **Do:** `query_data` over both files (register one as `data`, one as `other` when allowed) → **Get:** the joined rows.
- **Ask:** "what's in this SQLite file?" → **Do:** `query_data("SELECT name FROM sqlite_master WHERE type='table'", data_file="<path>.sqlite")` → **Get:** the schema, then targeted SELECTs.
- **Ask:** "which ledger rows look like the pencil eraser?" → **Do:** `primitive_lookup("eraser reversibility")` **then** `query_data` on the ids it returned → **Get:** the rows with evidence.

## Spreadsheets as artefacts
Use when: they want something they can open, sort, or send.

- **Ask:** "make me a spreadsheet of White Stripes albums" → **Do:** `wiki_scout_search("The White Stripes")` → `wiki_read_section(..., section="Discography")` → `create_spreadsheet(rows, path="eve-output/white-stripes.xlsx")` → **Get:** an `.xlsx` with the archive rows.
- **Ask:** "turn the ratings table into a sheet" → **Do:** `wiki_extract(need_hint="ratings table")` → `create_spreadsheet` → **Get:** the table as a file (formula injection is blocked).
- **Ask:** "give me a comparison sheet of these three tools" → **Do:** `research_orchestrate`/`web_scout` → `structured_extract` → `create_spreadsheet` → **Get:** a decision table.
- **Ask:** "export my tasks" → **Do:** `list_tasks`/`search_tasks` → `create_spreadsheet` → **Get:** a snapshot file in `eve-output`.

## Work orders (plan before build)
Use when: the idea is bigger than one turn — they want it recorded, not half-built.

- **Ask:** "write this up as a work order: local media limb with yt-dlp" → **Do:** `draft_work_order(...)` → **Get:** a Work Order draft under the Workbench for triage.
- **Ask:** "plan the steps to add a new limb" → **Do:** `draft_work_order` + `search_catalog` for existing pieces → **Get:** a scoped plan with what already exists.
- **Ask:** "what's in the Resource Queue to build next?" → **Do:** `workbench_list_dir("00_Resource_Queue")` → `skill_triage_manifest` → **Get:** ranked candidates with a recommendation.
