---
name: github_scout_search
toolbelt: github_scout
one_line: Search GitHub repositories by keyword; cache markdown under 04_Thought_Experiments/github_cache
---

## Description (verbatim from the tool schema, pre-R-03)

Search GitHub repositories by keyword; cache markdown under 04_Thought_Experiments/github_cache. Auto-admits GitHub Scout when resource headroom allows (no Toolbelt click). Does NOT clone or write Cognee. Never claim you lack internet — call this tool.

## Parameters

- `query` — Search keywords (e.g. duckdb mcp server local).
- `limit` — Max results (default 10).
- `note` — Optional Architect note.

## Usage

Registered by the Toolbelt category `github_scout`. The model sees the name, the
one-line cue and the parameter names in its schema; this document is the deep syntax it
can fetch with `tool_docs` when a call needs more than the cue.
