---
name: claim_ledger
toolbelt: claim_ledger
one_line: Record and re-check claims that carry the command that would prove them wrong
---

# claim_ledger

A store of **claims with checks** — knowledge for execution, not for recall.

## When to use

- A fact should stay true across sessions and you want it re-checked, not
  recalled.
- A claim carried over from earlier work may have gone stale.
- You need to know how much of a store can actually be proven.

## Parameters

- `action` — `add`, `verify`, `health`, or `list`.
- `claim` — the claim text (`add`).
- `check_cmd` — the command that would prove it wrong (`add`).
- `grade` — `promotional`, `community-reported`, `first-party-documented`,
  `independently-corroborated`, `reproduced` (`add`).
- `slug` — one claim to check (`verify`).
- `unchecked` — only claims with no check (`list`).
- `failing` — only claims whose check failed (`list`).

## Notes

Registered by the Toolbelt category `rea`. The model sees the name, the
one-line cue and the parameter names in its schema; this document is the deep
syntax it can fetch with `tool_docs` when a call needs more than the cue.

A claim with no check is a **document** (quotable, not usable). A claim whose
check passes is a **capability**. A claim whose check fails is a **known-false**
— actionable, and the thing worth reporting.

Checks run as shell commands inside a declared local root, with a timeout. Keep
them read-only and cheap.
