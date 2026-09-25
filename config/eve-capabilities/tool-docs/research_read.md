---
name: research_read
toolbelt: web_research
one_line: Read a research job's digest (bounded)
---

## Description (verbatim from the tool schema, pre-R-03)

Read a research job's digest (bounded). Returns more_available when the desk holds more than the budget allowed.

## Parameters

- `job_id` — Job id from research_start.
- `budget` — Max characters to return (default 2400).

## Usage

Registered by the Toolbelt category `web_research`. The model sees the name, the
one-line cue and the parameter names in its schema; this document is the deep syntax it
can fetch with `tool_docs` when a call needs more than the cue.
