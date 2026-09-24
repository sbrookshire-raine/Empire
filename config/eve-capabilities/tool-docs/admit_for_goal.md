---
name: admit_for_goal
toolbelt: always
one_line: Admit a light session skill for the current goal when resource_pulse headroom is OK (GitHub/Web/Container sco…
---

## Description (verbatim from the tool schema, pre-R-03)

Admit a light session skill for the current goal when resource_pulse headroom is OK (GitHub/Web/Container scout, etc.). Does not require Research Partner. If need_architect is true, ask the Architect — do not force GPU/Vision/Stem. Never writes Cognee.

## Parameters

- `category` — Toolbelt category to admit (e.g. github_scout, web_scout, container_scout).
- `reason` — Why this skill is needed for the goal.
- `ttl_min` — Session TTL minutes.

## Usage

Registered by the Toolbelt category `always`. The model sees the name, the
one-line cue and the parameter names in its schema; this document is the deep syntax it
can fetch with `tool_docs` when a call needs more than the cue.
