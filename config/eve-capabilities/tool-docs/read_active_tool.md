---
name: read_active_tool
toolbelt: tool_forge
one_line: Read a flattened codebase or script from Empire Workbench 03_Active_Tools via the local empire-workbench MCP …
---

## Description (verbatim from the tool schema, pre-R-03)

Read a flattened codebase or script from Empire Workbench 03_Active_Tools via the local empire-workbench MCP server (read-only). Pass the filename only, e.g. BANDAPP_flattened.txt. Requires Tool Forge enabled in the Workbench Toolbelt.

## Parameters

- `filename` — Basename or relative path under C:/Empire_Workbench/03_Active_Tools/, e.g. cursor_HOL_flattened.txt

## Usage

Registered by the Toolbelt category `tool_forge`. The model sees the name, the
one-line cue and the parameter names in its schema; this document is the deep syntax it
can fetch with `tool_docs` when a call needs more than the cue.
