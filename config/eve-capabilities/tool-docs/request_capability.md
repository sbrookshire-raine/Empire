---
name: request_capability
toolbelt: always
one_line: Request a session-scoped Toolbelt capability (Research Partner Autopilot path)
---

## Description (verbatim from the tool schema, pre-R-03)

Request a session-scoped Toolbelt capability (Research Partner Autopilot path). Prefer admit_for_goal + resource_pulse for day-to-day light skills so the Architect is not the button.

## Parameters

- `category` — Toolbelt category (wiki_local, web_scout, github_scout, container_scout).
- `reason` — Why Eve needs this capability.
- `ttl_min` — Session TTL minutes.

## Usage

Registered by the Toolbelt category `always`. The model sees the name, the
one-line cue and the parameter names in its schema; this document is the deep syntax it
can fetch with `tool_docs` when a call needs more than the cue.
