---
name: drop_staging
toolbelt: file_ops
one_line: Drop an eve_staging proposal (delete staging file + mark dropped)
---

## Description (verbatim from the tool schema, pre-R-03)

Drop an eve_staging proposal (delete staging file + mark dropped). Use when the Architect says drop/forget that staging id, or after TTL sweep.

## Parameters

- `entry_id` — Staging id to drop.

## Usage

Registered by the Toolbelt category `file_ops`. The model sees the name, the
one-line cue and the parameter names in its schema; this document is the deep syntax it
can fetch with `tool_docs` when a call needs more than the cue.
