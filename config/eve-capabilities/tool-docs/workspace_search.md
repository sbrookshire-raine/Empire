---
name: workspace_search
toolbelt: workspace_search
one_line: Search local text across allowlisted roots (C:/Empire_Workbench, C:/EMPIRE/docs) for a literal substring
---

## Description (verbatim from the tool schema, pre-R-03)

Search local text across allowlisted roots (C:/Empire_Workbench, C:/EMPIRE/docs) for a literal substring. Read-only; results are redacted. Use to find notes, files, or code references locally without the network.

## Parameters

- `query` — Literal substring to search for.
- `max_results` — Max results (default 100).
- `note` — Optional Architect note.

## Usage

Registered by the Toolbelt category `workspace_search`. The model sees the name, the
one-line cue and the parameter names in its schema; this document is the deep syntax it
can fetch with `tool_docs` when a call needs more than the cue.
