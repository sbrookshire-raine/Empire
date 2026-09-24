---
id: E-20
slug: eve-idea-tools
title: Eve can list, read, and capture ideas (PocketBase index + proposal path)
status: idea
area: memory
priority: next
depends_on: [E-19]
touches: [pipeline, mcp, frontend, pocketbase, cognee, docs, tests]
created: 2026-09-24
source: Architect, 2026-09-24 — "something Eve can learn from as well"
---

# Eve can list, read, and capture ideas (PocketBase index + proposal path)

## Intent

Make the idea store something Eve can use: answer *"what ideas are queued?"*, *"what did I want for
media?"*, and **capture** a new idea the moment the Architect mentions one, so a passing remark stops
being lost.

## Why it matters

The Architect said plainly: *"I have lots of ideas, they all need to be deferred for now, but I don't
want the information lost."* Intake is the bottleneck — not storage. If capture is "edit a markdown
file in Cursor", ideas die in the moment. If capture is "say it to Eve", they survive.

## What "done" looks like (acceptance)

- Say *"note an idea: media player window in the workbench"* → Eve creates the idea (front matter
  filled, file stubbed from `_TEMPLATE.md`, PocketBase row created, status `idea`) and **reads back**
  what she recorded for confirmation.
- Ask *"what ideas are queued for media?"* → Eve lists id, title, status, next action — from the
  index, not from guesswork.
- Ask *"what did I want for the media limb?"* → Eve answers from the idea file's Intent + Stack plan.
- Nothing is auto-remembered in Cognee at capture time; promotion happens on the Architect's confirm
  (`propose_remember` → `confirm_remember`), preserving the staging rule.
- Regression guards: `tests/test_idea_docs.py` still passes after a capture (front matter valid,
  required sections present, slug matches filename), and the queue ledger gets its row.

## Stack plan (how it applies in EMPIRE)

| Layer | What it gets |
|-------|--------------|
| PocketBase | collection `ideas` (slug, id, title, status, area, priority, intent, updated_at, doc_path). The query index; the Architect edits it in `/_/` when convenient |
| `pipeline/` | `ideas.py` — one source of truth: `parse_doc()`, `index()` (optional PB mirror), `create_from_template()`, `capture(intent, area)`; `sync` writes the PB rows from front matter so the files stay canonical |
| `mcp/` + agent tool | `mcp/ideas_mcp.py` + `agent/tools/list_ideas.ts`, `read_idea.ts`, `propose_idea.ts` (gated by a `workspace_search`-class capability or always-on: the index is small text) |
| Frontend | "Ideas" panel beside History: generated from the same pocketbase collection, links to the doc files; no new build step |
| Cognee | promotion only (`propose_remember` on confirm) so *"what did I want for X"* works in words |
| Docs + gates | this file is the contract; `scripts/list-ideas.py` grows into the CLI Eve's tools call; `tests/test_idea_docs.py` + `tests/pipeline/test_ideas.py` |

## Constraints and identity

- **Files are canonical, PocketBase is an index.** Never let a PB edit silently delete thinking — sync
  is one-way (files → PB), and a missing file marks the row stale rather than removing content.
- Capture writes to `docs/ideas/` with `status: idea` only. Eve cannot set `ready` or `done` — those
  are the Architect's calls (same pattern as `evolve_staging` → confirm).
- No auto-remember. Ideas are not memory until confirmed.
- Keep the prompt cost near zero: list/read returns bounded text; `propose_idea` takes an intent string.

## Open questions

1. Should capture ever be implicit (Eve notices "that's an idea" mid-conversation) or always explicit?
   Implicit risks noise; explicit risks loss.
2. One `ideas` collection, or reuse the existing `work_orders`/catalogue tables as the index?
3. Does the queue ledger row get generated automatically on capture (safer) or written by hand?

## Promotion checklist (idea → Work Order)

- [ ] Open question 1 answered (it decides the tool's trigger design).
- [ ] Sync direction and stale-row behaviour written into the tool doc.
- [ ] Demo acceptance script named (browser harness question set, like the R-02/R-03 probes).
- [ ] Confirm the ceilings test still passes with the new tools registered.