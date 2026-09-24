---
name: container_scout_docker_status
toolbelt: container_scout
one_line: List local Docker containers matching EMPIRE names (default empire-*)
---

## Description (verbatim from the tool schema, pre-R-03)

List local Docker containers matching EMPIRE names (default empire-*). Auto-admits Container Scout when headroom allows. Status only — does not start/stop.

## Parameters

- `name_filter` — Substring filter for container names (default empire-).

## Usage

Registered by the Toolbelt category `container_scout`. The model sees the name, the
one-line cue and the parameter names in its schema; this document is the deep syntax it
can fetch with `tool_docs` when a call needs more than the cue.
