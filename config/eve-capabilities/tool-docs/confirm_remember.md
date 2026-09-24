---
name: confirm_remember
toolbelt: file_ops
one_line: Promote a staging entry into permanent Cognee memory (eve_memory or eve_core)
---

## Description (verbatim from the tool schema, pre-R-03)

Promote a staging entry into permanent Cognee memory (eve_memory or eve_core). Only when the Architect explicitly says to keep/save/confirm that staging id.

## Parameters

- `entry_id` — Staging id from list_staging / propose_remember.
- `dataset` — Target dataset: eve_memory (default) or eve_core.

## Usage

Registered by the Toolbelt category `file_ops`. The model sees the name, the
one-line cue and the parameter names in its schema; this document is the deep syntax it
can fetch with `tool_docs` when a call needs more than the cue.
