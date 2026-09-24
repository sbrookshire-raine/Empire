---
id: E-XXX
slug: short-kebab-name          # must match the filename
title: One line the Architect would recognise
status: idea                    # idea | ready | in_progress | blocked | parked | done
area: media                     # media | memory | wiki | ui | models | ops | research | docs
priority: later                 # now | next | later | someday
depends_on: []                  # other idea ids, or "nothing"
touches: [pipeline, mcp, toolbelt, frontend, pocketbase, cognee]
created: 2026-09-24
source: Architect (E-XXX)       # who asked, and where it came from
---

# <title>

## Intent

What the Architect actually wants, in plain words. One paragraph. If it cannot be said plainly,
the idea is not ready to record yet.

## Why it matters

The friction or possibility behind it. What gets better, for whom, and what it replaces.

## What "done" looks like (acceptance)

Testable statements. This is the part that lets the work be *asked for* instead of re-derived:

- Ask <question> → <observable outcome>.
- <Action> → <stored/verifiable result>.
- Regression guard: `<command or test>` stays green.

## Stack plan (how it applies in EMPIRE)

| Layer | What it gets |
|-------|--------------|
| `pipeline/` | the real logic (module name, inputs/outputs) |
| `mcp/` + agent tool | how Eve and Cursor reach it (tool name, Toolbelt category, always-on or gated) |
| Storage | PocketBase (state) / Cognee (meaning) / cache path — and why that split |
| Frontend | page or dock panel (zero-build HTML/Alpine) |
| Docs + gates | tool doc in `config/eve-capabilities/tool-docs/`, test file, ceiling/parity entries |

## Constraints and identity

Which non-negotiables apply (local-only, meter-free, no cloud LLM, loopback, prompt budget,
one heavy GPU tenant). State explicitly what this idea must NOT do.

## Open questions

Things the Architect or Mechanic must decide before forging. Keep them as questions, not guesses.

## Promotion checklist (idea → Work Order)

- [ ] Status is `ready` and open questions are answered.
- [ ] Acceptance statements are testable as written.
- [ ] `touches` lists every file/folder the change will modify.
- [ ] Tool doc + test file names are chosen.
- [ ] Identity constraints are restated in the Work Order.
