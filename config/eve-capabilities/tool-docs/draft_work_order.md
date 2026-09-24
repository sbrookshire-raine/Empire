---
name: draft_work_order
toolbelt: file_ops
one_line: Draft a Work Order markdown for the Systems Mechanic (Cursor) in 05_Work_Orders
---

## Description (verbatim from the tool schema, pre-R-03)

Draft a Work Order markdown for the Systems Mechanic (Cursor) in 05_Work_Orders. Use after triage when something is USEFUL NOW and needs forging. Not a PocketBase task.

## Parameters

- `capability_needed` — Short name of the capability the Mechanic should build.
- `justification` — Why this is USEFUL NOW and what EMPIRE gains.
- `source_file` — Optional basename or relative path under C:/Empire_Workbench/00_Resource_Queue/.

## Usage

Registered by the Toolbelt category `file_ops`. The model sees the name, the
one-line cue and the parameter names in its schema; this document is the deep syntax it
can fetch with `tool_docs` when a call needs more than the cue.
