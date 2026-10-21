---
name: claim-ledger
description: Record what you believe alongside the command that would prove it wrong, so knowledge can be executed rather than recalled and cannot go stale silently. Use when a fact should stay true across sessions, when a claim carried over from earlier work needs checking, or when you need to know how much of a store can actually be trusted. Keywords: claim, check, verify, health, staleness, falsify, capability, document, ledger, reliability. Do not use to store text for retrieval - use agent-memory-architecture for tiers and promotion.
icon: IconChecklist
color: Green
---

# Claim ledger

Knowledge that is **done**, not read.

## When to use it

- A fact should stay true across sessions — a version, a path, a count, a
  behaviour.
- A claim was carried over from earlier work and may have gone stale.
- You need to know how much of what is recorded can actually be proven.

## When not to use it

To store text for retrieval. That is `agent-memory-architecture` — tiers,
promotion by use, and the size cap. This skill stores claims for **execution**,
not prose for recall.

## Prerequisites

Python 3.8+ and the stdlib. No other dependency. The reference implementation is
`scripts/claim_ledger.py`. Checks run as shell commands, so they are POSIX-shaped
— on Windows they need the equivalent form.

## The problem, stated precisely

A guide, a memory entry, a lookup table are all **text**. Text is *read*.
Reading does not create capability. You can read every word about a tool and
still not be able to use it. That is not a retrieval problem — the wrong *kind*
of thing was stored.

## The unit

```
claim  +  check  +  last_result
```

- the **claim** is what you believe
- the **check** is the command that would prove you wrong
- together they are something you can act on and get a result from

| state | meaning |
| --- | --- |
| no check | a **document** — quotable, not usable |
| check passes | a **capability** — reliable |
| check fails | a **known-false** — actionable |

## Procedure

1. **Record the claim with its check.**
   ```bash
   python3 claim_ledger.py add \
     --claim "binwalk 3.1.0 is installed" \
     --check "binwalk --version 2>&1 | grep -q '3.1.0'" \
     --grade reproduced
   ```
   If you have no check, record it anyway — it will be counted as a document,
   which is the honest accounting.

2. **Run the checks.**
   ```bash
   python3 claim_ledger.py verify
   ```
   A failing check is the finding. Report it; do not quietly fix it and move on.

3. **Read the health number.**
   ```bash
   python3 claim_ledger.py health
   ```
   One number: the fraction of claims that have a check and pass. A store where
   most claims have no check is a library, not a forge.

4. **Work the two queues.**
   ```bash
   python3 claim_ledger.py list --unchecked   # documents: still need a check
   python3 claim_ledger.py list --failing     # known-false: needs attention
   ```

## Why a check and not a memory entry

A memory entry can go stale and stay silent. A check cannot: it either passes or
it does not, right now.

Demonstrated: a claim `the ledger stays under 600 lines` was recorded, the file
grew past 600 lines during unrelated work, and the check failed on its own — with
nobody reporting the change. A memory entry would have sat there saying "keep it
small" while the file tripled.

## The interface

One question: **"show me the check."** If there is not one, say so plainly
rather than asserting. That is the whole discipline, and it is what makes the
store trustworthy rather than merely large.

## Common failure modes

| Symptom | Cause | Fix |
| --- | --- | --- |
| A claim is repeated and turns out false | it was never checked | record the check, run it |
| The store looks large but is not reliable | most claims are documents | read `health`; work the unchecked queue |
| A check passes but the fact is false | the check does not test the claim | the check must fail when the claim is false |
| Nothing is ever re-checked | `verify` is manual | run it on a cadence |

## Done when

- Every claim you would repeat has a check, or is explicitly marked a document.
- `verify` has run and the failures are reported, not hidden.
- `health` reports a number you can defend.

## Confidence

- **Reproduced** (2026-10-18): the ledger ran on nine real claims. Three passed,
  three failed, three were documents. The staleness demonstration worked — a
  size claim failed on its own after the file grew.
- **Two failures were real findings:** a `binwalk 3.1.0` claim carried from a
  skill's confidence section failed (not installed), and a ledger-size claim
  failed (974 lines against a 600-line cap).
- **Not solved:** checks run with `shell=True` inside a declared root, but the
  guard is on the working directory, not on every path a command names. `verify`
  is manual — nothing schedules it. Checks are POSIX-shaped.
