---
name: daze_list_day
toolbelt: time_reclaim
one_line: List DAZE day_blocks for a date (YYYY-MM-DD, default today)
---

## Description (verbatim from the tool schema, pre-R-03)

List DAZE day_blocks for a date (YYYY-MM-DD, default today). Requires Time Reclaim Toolbelt limb. Returns blocks + conflicts.

## Parameters

- `date` — YYYY-MM-DD only. Omit entirely for today — never pass 'today' or natural language.
- `phase` — planned or actual (optional filter).

## Usage

Registered by the Toolbelt category `time_reclaim`. The model sees the name, the
one-line cue and the parameter names in its schema; this document is the deep syntax it
can fetch with `tool_docs` when a call needs more than the cue.
