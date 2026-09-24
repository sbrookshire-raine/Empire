---
name: architect_now_update
toolbelt: system_ops
one_line: Persist a durable CURRENT fact about the Architect into ARCHITECT_NOW.md (overrides old Obsidian companion di…
---

## Description (verbatim from the tool schema, pre-R-03)

Persist a durable CURRENT fact about the Architect into ARCHITECT_NOW.md (overrides old Obsidian companion distillations). Use when they correct timeline, work status, goals, or say to remember something lasting. Not Cognee; not a PocketBase task.

## Parameters

- `fact` — One clear current fact, e.g. 'Fall term now; contract secured; focusing on AI development with Eve.'
- `replace_all` — If true, replace the entire NOW file with this fact. Default append.

## Usage

Registered by the Toolbelt category `system_ops`. The model sees the name, the
one-line cue and the parameter names in its schema; this document is the deep syntax it
can fetch with `tool_docs` when a call needs more than the cue.
