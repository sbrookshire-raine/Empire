---
area: workbench-and-files
one_line: The Workbench folders, local file search, staging, health, triage, active tools.
tools: workbench_list_dir, workbench_read_file, workspace_search, read_active_tool, check_workbench_health, list_staging, drop_staging, skill_triage_manifest
skills: skill-tool-forge, skill-triage-officer, skill-workbench-health, skill-workspace-search, workbench-awakening
---

# Workbench and files — worked pathways

The Workbench is the Architect's world: `C:/Empire_Workbench`. Paths passed to `workbench_*` are
**relative** (`00_Resource_Queue`, `01_Memory_Bank`, `02_Skills_and_Prompts`, `04_Thought_Experiments`) —
never absolute, never `/home/vercel-sandbox`. Code that ships lives in `C:/EMPIRE/03_Active_Tools` and
must be read with `read_active_tool`.

## Listing and reading the Workbench
Use when: "what's in my queue?", "show me that file", "where did that note go?".

- **Ask:** "what's in my Resource Queue?" → **Do:** `workbench_list_dir("00_Resource_Queue")` → **Get:** the file names with sizes.
- **Ask:** "read me my current facts card" → **Do:** `workbench_read_file("00_Core_Profile/ARCHITECT_NOW.md")` → **Get:** the living card text.
- **Ask:** "what skills and prompts do I have?" → **Do:** `workbench_list_dir("02_Skills_and_Prompts")` → **Get:** the folder listing to choose from.
- **Ask:** "what's in my Memory Bank?" → **Do:** `workbench_list_dir("01_Memory_Bank")` → **Get:** the bank contents, one level at a time.
- **Ask:** "where are my thought experiments?" → **Do:** `thought_experiment_read()` (preferred) or `workbench_list_dir("04_Thought_Experiments")` → **Get:** notes vs caches, clearly distinguished.

## Searching inside files
Use when: the answer is somewhere in his notes and you don't know where.

- **Ask:** "find every mention of yt-dlp in my notes" → **Do:** `workspace_search("yt-dlp")` → **Get:** file hits with line context (read-only, no network).
- **Ask:** "which script writes the ledger?" → **Do:** `workspace_search("primitive_ledger")` → **Get:** hits with line context (allowlisted roots: `C:/Empire_Workbench` and `C:/EMPIRE/docs`).
- **Ask:** "where is that constant defined?" → **Do:** `workspace_search("SHARED_NUM_CTX")` → **Get:** the definition site when it is in an allowlisted root, otherwise an honest miss (code under `C:/EMPIRE` outside `docs/` belongs to the Mechanic, not to you).
- **Ask:** "read me the file I just dropped" → **Do:** `workbench_read_file("<relative path>")` → **Get:** the file text. The Workbench tools are hard-rooted at `C:/Empire_Workbench` and take **relative** paths only.
- **Ask:** "what's in this folder?" → **Do:** `workbench_list_dir("<relative dir>")` → **Get:** the listing, one level at a time. (`glob` and `grep` are switched off — these two are the supported path.)

## Active tools (flattened codebases)
Use when: a flattened harvest, a `*_flattened.txt`, or anything under `03_Active_Tools`.

- **Ask:** "what's in the yt-dlp harvest?" → **Do:** `read_active_tool("03_Active_Tools/<name>")` → **Get:** the tool's code/docs (required for this folder — do not treat it as an ordinary file).
- **Ask:** "does the harvested tool have a CLI entry?" → **Do:** `read_active_tool` the package, then `workspace_search("__main__")` → **Get:** the entry point.
- **Ask:** "which harvested scripts could become a limb?" → **Do:** `workbench_list_dir("03_Active_Tools")` → `read_active_tool` one → `draft_work_order` → **Get:** a scoped limb proposal.
- **Ask:** "does this flattened file contain its licence?" → **Do:** `read_active_tool(...)` then search within → **Get:** licence text or an honest absence.

## Staging (drop / promote)
Use when: something was captured (uploaded file, fetched page) and needs promoting or clearing.

- **Ask:** "what's staged right now?" → **Do:** `list_staging()` → **Get:** staged files with sizes and age.
- **Ask:** "promote the staged report into memory" → **Do:** `list_staging()` → `promote_wiki_cache(path, dataset="eve_memory")` (or the repo's ingest path) → **Get:** the file ingested, confirmed by name.
- **Ask:** "clear the staging folder" → **Do:** `list_staging()` → confirm with the Architect → `drop_staging(path)` → **Get:** the staging area cleared, named items only.
- **Ask:** "where did the upload go after I added it to memory?" → **Do:** `list_staging()` → `workbench_list_dir("04_Thought_Experiments/eve_staging")` → **Get:** the path trail.

## Health and triage
Use when: "is everything up?", "is the workbench healthy?", "what needs triage?".

- **Ask:** "is the workbench healthy?" → **Do:** `check_workbench_health()` → **Get:** services, disk, active-tool count, and anything red.
- **Ask:** "run triage on my queue" → **Do:** `workbench_list_dir("00_Resource_Queue")` → `skill_triage_manifest(...)` → **Get:** USEFUL NOW / COOL IDEA / JUNK with reasons.
- **Ask:** "how much disk is left?" → **Do:** `check_workbench_health()` → **Get:** the volume figures (`I:`, `V:`, `D:` matter most: archive + Cognee + wiki corpus).
- **Ask:** "is anything stale in my queue?" → **Do:** `workbench_list_dir("00_Resource_Queue")` → **Get:** names and dates; propose, never delete.
- **Ask:** "what did the last ingestion do?" → **Do:** `check_workbench_health()` then `pb_health()` → **Get:** service state plus ingestion hints.
