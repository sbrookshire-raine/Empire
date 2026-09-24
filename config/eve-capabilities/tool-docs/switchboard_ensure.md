---
name: switchboard_ensure
toolbelt: switchboard
one_line: Start the EMPIRE services a task needs (pocketbase, frontend) after a headroom check
---

## Description (verbatim from the tool schema, pre-R-03)

Start the EMPIRE services a task needs (pocketbase, frontend) after a headroom check. Never starts Ollama or Eve (external/self). Defaults to dry-run planning; pass dry_run=false to actually start. If ok is false with headroom reasons, do not retry — ask the Architect.

## Parameters

- `services` — Service ids to ensure, e.g. ['pocketbase', 'frontend'].
- `dry_run` — Plan only (default true). Set false to actually start.

## Usage

Registered by the Toolbelt category `switchboard`. The model sees the name, the
one-line cue and the parameter names in its schema; this document is the deep syntax it
can fetch with `tool_docs` when a call needs more than the cue.
