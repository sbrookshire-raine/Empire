---
name: daze_free_windows
toolbelt: time_reclaim
one_line: Compute free time arcs in the DAZE day for coaching (exercise/meditation)
---

## Description (verbatim from the tool schema, pre-R-03)

Compute free time arcs in the DAZE day for coaching (exercise/meditation). Requires Time Reclaim Toolbelt.

## Parameters

- `date` — YYYY-MM-DD only. Omit entirely for today — never pass 'today' or natural language.
- `phase` — planned|actual (default planned).
- `min_minutes` — Minimum free window length (default 30).

## Usage

Registered by the Toolbelt category `time_reclaim`. The model sees the name, the
one-line cue and the parameter names in its schema; this document is the deep syntax it
can fetch with `tool_docs` when a call needs more than the cue.
