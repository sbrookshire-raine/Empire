---
name: propose_remember
toolbelt: file_ops
one_line: Propose remembering a short note into Eve's staging sandbox (eve_staging)
---

## Description (verbatim from the tool schema, pre-R-03)

Propose remembering a short note into Eve's staging sandbox (eve_staging). Use when something seems worth keeping. Do NOT confirm permanence yourself — ask the Architect to keep or drop. Never bulk-ingest Wikipedia.

## Parameters

- `content` — Short note to stage.
- `reason` — Why this might have value (one line).
- `crumb` — Optional success marker / recall crumb (not encyclopedia dump).

## Usage

Registered by the Toolbelt category `file_ops`. The model sees the name, the
one-line cue and the parameter names in its schema; this document is the deep syntax it
can fetch with `tool_docs` when a call needs more than the cue.
