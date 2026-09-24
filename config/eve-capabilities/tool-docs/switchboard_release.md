---
name: switchboard_release
toolbelt: switchboard
one_line: Release EMPIRE managed services a task no longer needs (pocketbase, frontend)
---

## Description (verbatim from the tool schema, pre-R-03)

Release EMPIRE managed services a task no longer needs (pocketbase, frontend). Never stops Ollama or Eve. Defaults to dry-run planning; pass dry_run=false to actually stop.

## Parameters

- `services` — Service ids to release, e.g. ['frontend'].
- `dry_run` — Plan only (default true). Set false to actually stop.

## Usage

Registered by the Toolbelt category `switchboard`. The model sees the name, the
one-line cue and the parameter names in its schema; this document is the deep syntax it
can fetch with `tool_docs` when a call needs more than the cue.
