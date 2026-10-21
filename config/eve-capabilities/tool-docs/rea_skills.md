---
name: rea_skills
toolbelt: rea_skills
one_line: Run one of six local REA skills that prove a finding instead of asserting it
---

# rea_skills

Runs the six approved Bin-1 skills from the Gumloop REA bundle, vendored under
`vendor/rea-skills/` and executed on this host.

## When to use

- Before reporting a REA-derived finding: `verify_evidence` audits an Evidence
  record and the claims resting on it.
- When a reconstruction must be proven: `audit_reconstruction` checks the
  ledgers; `parity_check` proves a rebuild matches a reference over a frozen
  scenario corpus.
- When a binary's metadata is needed without a disassembler:
  `build_fixtures` prepares the local reader fixtures.
- When the question needs prior art: `forkdive` mines a repo's fork network;
  `discover` finds high-signal repos by topic.

## Parameters

- `action` — `verify_evidence`, `audit_reconstruction`, `parity_check`,
  `build_fixtures`, `forkdive`, `discover`, or `list`.
- `files` — Evidence JSON files (`verify_evidence`).
- `claims` — claims.json to cross-check (`verify_evidence`).
- `config_dir` — reconstruction config directory (`audit_reconstruction`).
- `reference` / `candidate` / `scenarios` — the parity triple
  (`parity_check`). The first two are *commands*, not bare paths.
- `out` — output directory (`build_fixtures`).
- `repo` — `OWNER/REPO` (`forkdive`).
- `topics` / `min_stars` — discovery filters (`discover`).
- `work_dir` — working directory, always inside the EMPIRE scratch root.

## Notes

Registered by the Toolbelt category `rea`. The model sees the name, the
one-line cue and the parameter names in its schema; this document is the deep
syntax it can fetch with `tool_docs` when a call needs more than the cue.

The first four actions are fully offline. `forkdive` and `discover` need the
network. All paths are jailed to the EMPIRE scratch root, and a path outside it
is refused rather than rewritten.

Only six skills are reachable. The other sixteen in the upstream bundle are out
of scope and are not vendored.
