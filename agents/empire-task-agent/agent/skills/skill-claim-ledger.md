---
description: Use when a fact must stay true across sessions, when a claim carried over from earlier work may have gone stale, or when you need to know how much of what is recorded can actually be proven. Records a claim together with the command that would falsify it.
---

# Claim ledger

Knowledge that is **done**, not read.

## When to use it

- A fact should stay true across sessions — a version, a path, a count, a
  behaviour.
- A claim was carried over from earlier work and may have gone stale.
- You need to know how much of a store can actually be trusted.

## When not to use it

- To store text for retrieval. That is Cognee (`cognee_recall` /
  `cognee_remember`). This limb stores claims for **execution**, not prose for
  recall.

## Tools

- `claim_ledger` — `add`, `verify`, `health`, `list`.

## The unit

```
claim  +  check  +  last_result
```

| state | meaning |
| --- | --- |
| no check | a **document** — quotable, not usable |
| check passes | a **capability** — reliable |
| check fails | a **known-false** — actionable |

## How to work a goal

1. **Record the claim with its check.** `claim_ledger(action="add", claim=…,
   check_cmd=…)`. If there is no check, record it anyway — it is counted as a
   document, which is the honest accounting.
2. **Run the checks.** `claim_ledger(action="verify")`. A failing check is the
   finding: report it, do not quietly fix it and move on.
3. **Read the health number.** `claim_ledger(action="health")` gives the
   fraction of claims that have a check and pass, plus a verdict. A store where
   most claims have no check is a library, not a forge — say so plainly.
4. **Work the two queues.** `claim_ledger(action="list", unchecked=true)` for
   documents that still need a check; `failing=true` for what is known-false.

## The rule

One question: **"show me the check."** If there is not one, say so plainly
rather than asserting.

## Hard rules

- Checks run as shell commands inside a declared local root. Keep them
  read-only and cheap.
- Run the check before repeating a claim carried over from an earlier session.
- Prefer the smallest honest claim. "Documented but not reproduced" is a fine
  outcome.
