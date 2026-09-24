---
name: switchboard_tenant
toolbelt: switchboard
one_line: GPU lease: acquire a heavy tenant (chat/stem/vision/voice/extract), release it, or check status
---

## Description (verbatim from the tool schema, pre-R-03)

GPU lease: acquire a heavy tenant (chat/stem/vision/voice/extract), release it, or check status. Only one heavy tenant at a time; release the prior tenant before acquiring another. Acquire defaults to dry-run; pass dry_run=false to actually lease.

## Parameters

- `action` — Lease action to perform.
- `tenant` — Tenant id when action=acquire (chat/stem/vision/voice/extract).
- `dry_run` — Plan only (default true). Set false to actually mutate.

## Usage

Registered by the Toolbelt category `switchboard`. The model sees the name, the
one-line cue and the parameter names in its schema; this document is the deep syntax it
can fetch with `tool_docs` when a call needs more than the cue.
