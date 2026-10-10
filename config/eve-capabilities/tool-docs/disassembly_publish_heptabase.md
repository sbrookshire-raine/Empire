---
name: disassembly_publish_heptabase
toolbelt: always
one_line: Publish a local Disassembly Card to the Heptabase EMPIRE Disassembly Catalog board (orange/blue/purple by sta…
---

## Description (verbatim from the tool schema, pre-R-03)

Publish a local Disassembly Card to the Heptabase EMPIRE Disassembly Catalog board (orange/blue/purple by stage). Requires architect_confirm=true and Heptabase desktop app running. Auto-admits heptabase limb.

## Parameters

- `card_id` — Local disassembly card id (dc_…).
- `architect_confirm` — Must be true — Architect approved publish in this turn.

## Usage

Registered by the Toolbelt category `always`. The model sees the name, the
one-line cue and the parameter names in its schema; this document is the deep syntax it
can fetch with `tool_docs` when a call needs more than the cue.
