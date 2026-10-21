---
description: Use when a reverse-engineering finding must be proven rather than asserted — auditing REA evidence records, checking a reconstruction's ledgers, proving a rebuild matches a reference, reading a binary's metadata without a disassembler, or mining a repo's fork network for proven use cases.
---

# REA skills (local verification)

Six skills from the Gumloop REA bundle, vendored and runnable **locally**. They
prove things: a claim either survives a check or it does not.

## When to use it

- A finding needs an audit before it is reported (evidence records).
- A reconstruction needs proof it is correct (ledgers, oracles, parity).
- A binary's metadata is needed without opening a disassembler.
- A question needs prior art: what people actually built from this repo.

## When not to use it

- To *perform* deep analysis — that is `rea_doctor` / `rea_analyze_javascript` /
  `rea_invoke`, which drive the REA engine and Ghidra.
- To store text for recall — that is Cognee (`cognee_recall`).

## Tools

- `rea_skills` — runs one of: `verify_evidence`, `audit_reconstruction`,
  `parity_check`, `build_fixtures`, `forkdive`, `discover`, `list`.

## How to work a goal

1. **Say what must be proven.** "This evidence supports the claim" or "this
   rebuild matches the original" — not "look at this binary".
2. **Call `rea_skills`** with the matching action. `list` first if unsure.
3. **Read the result, not the intent.** A failing check is the finding. Report
   it; do not quietly fix the input and move on.
4. **State the residual limits.** The parity harness proves agreement on a
   frozen corpus, not global equivalence.

## The offline/network split

`verify_evidence`, `audit_reconstruction`, `parity_check` and `build_fixtures`
are fully offline. `forkdive` and `discover` reach the network to inspect a
public repository's forks and stars.

## Hard rules

- Never hand-edit the vendored skills under `vendor/rea-skills/` — they are
  upstream, byte-identical, and a rollback depends on that.
- Report a failing check as a failing check.
- The vendored set is six. The other sixteen skills in the upstream bundle are
  out of scope and are not present — do not look for them.
