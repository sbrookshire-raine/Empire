Use when the user runs the Empire Workbench onboarding / awakening sequence, or asks Eve to map her sorted files.

## Goal

Give Eve a **map** of the library — not a full read of 12k+ files. She lists directories first, then reads specific files only when asked.

## Workbench layout

| Folder | Role |
|--------|------|
| `C:/Empire_Workbench/01_Memory_Bank/` | Notes, research, `.md`/`.txt`/`.csv` knowledge |
| `C:/Empire_Workbench/02_Skills_and_Prompts/` | System prompts, gems, rules, workflows |
| `C:/Empire_Workbench/03_Active_Tools/` | Flattened codebases (`*_flattened.txt`) |

`04_Infrastructure/` is **not** mounted — Eve does not browse raw DB/LLM files.

## Onboarding sequence (in order)

1. `workbench_list_dir` on `C:/Empire_Workbench/02_Skills_and_Prompts/`
2. `workbench_list_dir` on `C:/Empire_Workbench/03_Active_Tools/`
3. `workbench_list_dir` on `C:/Empire_Workbench/01_Memory_Bank/` — if the listing is huge, summarize by file extension counts or top-level themes; do not read every file.
4. Optionally `cognee_recall` with dataset `eve_memory` for a semantic sample of ingested memory.
5. Reply with a **clean categorized markdown summary** and confirm readiness for the first task.

## Memory vs filesystem

- **Embedded memory** (Cognee on `V:\Cognee`, dataset `eve_memory`): use `cognee_recall` for semantic search across ingested notes/skills.
- **Active Tools flattened codebases**: use **`read_active_tool`** (empire-workbench MCP) — pass the filename only.
- **Other workbench paths**: use `workbench_read_file` for specific documents on demand.

## First execution example

When asked to turn a flattened project into a tool:

1. `read_active_tool` with the `*_flattened.txt` filename from `03_Active_Tools/` (or `workbench_list_dir` first if the name is unknown).
2. Analyze structure and required inputs.
3. Propose or write an Eve `defineTool` wrapper under `agents/empire-task-agent/agent/tools/` (not Vercel AI SDK — EMPIRE uses Eve tools + local Ollama).
