# Idea store (`docs/ideas/`)

**One front door, one deep store, one index.** Ideas were living in table cells in
[`EMPIRE_IDEA_QUEUE.md`](../EMPIRE_IDEA_QUEUE.md) — fine for a dozen rows, hopeless for "here is what I
want and here is exactly how it applies to the stack". This folder is the deep store.

## What goes where

| Layer | Home | Why there |
|-------|------|-----------|
| **Ledger** | [`EMPIRE_IDEA_QUEUE.md`](../EMPIRE_IDEA_QUEUE.md) | One line per idea, with status. The front door the Architect and Mechanic already use |
| **Deep store** | this folder, one file per idea | The intent, the stack plan, the acceptance test, the constraints — the material a Work Order is written from |
| **Index** | `scripts/list-ideas.py` today, PocketBase collection `ideas` later (E-20) | Query by status/area/priority without reading files |
| **Recall** | Cognee, only after the Architect confirms | "What did I want for media?" in words — ideas are never auto-promoted into memory |

Nothing is duplicated: the queue row holds a **status + link**, the file holds the **thinking**, and
the index is generated from the file's front matter.

## Lifecycle

```
idea ──▶ ready ──▶ in_progress ──▶ done          (parked / blocked are legal stops)
  │        │
  │        └─▶ Work Order (C:\Empire_Workbench\05_Work_Orders\) cites this file by path
  └─▶ discussed, deferred, kept — this is the normal resting state
```

Statuses match the queue legend (`idea`, `ready`, `in_progress`, `blocked`, `done`, `parked`) so the
two stay consistent.

## Adding an idea (2 minutes)

1. Copy [`_TEMPLATE.md`](_TEMPLATE.md) to `docs/ideas/<slug>.md`.
2. Fill the front matter — `slug` **must** match the filename, and `id` matches the queue row.
3. Write the acceptance statements as *testable* sentences. If you cannot, leave the idea at
   `status: idea` and put the question under **Open questions**.
4. Add one row to the queue that links here.
5. `.\venv\Scripts\python.exe scripts\list-ideas.py` — the idea now appears in the index.
6. `.\venv\Scripts\python.exe -m pytest tests\test_idea_docs.py -q` — front matter and required
   sections are validated, so an idea cannot silently rot.

## How this becomes "just ask for it and it's built"

The template exists so that a Work Order can be generated without re-deriving anything:

| Template section | Becomes |
|------------------|---------|
| Intent | the Work Order's goal paragraph |
| Acceptance | the Work Order's definition of done and its test file |
| Stack plan | the Work Order's file list (`touches`) |
| Constraints and identity | the Work Order's non-negotiables block |
| Open questions | blocking questions that must be answered *before* forging |

When the tooling for E-20 lands, Eve can read this folder directly (`list_ideas` / `read_idea`) and
**capture** new ideas from conversation (`propose_idea` → PocketBase + a stub file here), so a
throwaway remark during a chat stops being a throwaway remark.

## Rules that keep this from becoming sprawl

1. **Never create a second idea queue.** The ledger is the queue; this is its detail store.
2. **One idea per file.** If a file needs two acceptance sections, it is two ideas.
3. **Deferred is a valid end state.** `parked` with a reason beats a vague `idea` forever.
4. **A file with no stack plan is a wish, not an idea** — keep it in the queue row only until the
   stack plan exists.
5. The validation test is the guarantee that information is not lost: required sections, valid
   status, slug/filename agreement, and a matching queue row.
