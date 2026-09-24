---
name: daze_upsert_block
toolbelt: time_reclaim
one_line: Create or update a DAZE day block (start/end minutes 0–1440)
---

## Description (verbatim from the tool schema, pre-R-03)

Create or update a DAZE day block (start/end minutes 0–1440). Requires Time Reclaim Toolbelt. Use for scheduling focus/body/rest arcs.

## Parameters

- `title` — (no description)
- `start_minute` — (no description)
- `end_minute` — (no description)
- `date` — YYYY-MM-DD (default today).
- `kind` — focus|body|admin|creative|rest|other
- `phase` — planned|actual
- `notes` — (no description)
- `record_id` — If set, PATCH existing record.

## Usage

Registered by the Toolbelt category `time_reclaim`. The model sees the name, the
one-line cue and the parameter names in its schema; this document is the deep syntax it
can fetch with `tool_docs` when a call needs more than the cue.
