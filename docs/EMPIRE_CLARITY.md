# EMPIRE Clarity

**One breath:** Eve is my partner; Truth Drift, DAZE, and Stem Factory are LEGO products.

This document is the bounding box for how the space stays clean. It does not replace [`EMPIRE_MANIFESTO.md`](../EMPIRE_MANIFESTO.md); it organizes how we use what is already built.

## Three layers

| Layer | What it is | What it is not |
|-------|------------|----------------|
| **Eve Core** | Chat, PocketBase tasks, Cognee recall, staging→confirm memory, wiki *glasses* (locate→extract→refuse) when Wiki Local is in session | Not a stem engineer, not a day planner UI, not Truth Drift year-compare |
| **LEGO shelf** | Named products with their own pages or drop-folder workflows: Truth Drift (Wiki Ops), DAZE, Stem Factory (Shard) | Not 16 peer checkboxes that redefine Eve’s personality |
| **Session reach** | Research Partner grants + short Toolbelt session limbs (GitHub/Web scout, forge, etc.) | Not always-on; research caches never silently enter Cognee |

## Eve Core (always)

- Modes: fast / deep / librarian
- Tasks tab → PocketBase
- Memory: `cognee_recall` on `eve_core` / `eve_memory`; **propose** to `eve_staging`; Architect **confirm** → core or **drop**
- **Ready strip** (header beside mode): Voice + Wiki as clickable status pills (green = on+healthy, amber = on+down, dim = off). Same toolbelt limbs Eve already uses — not a second permission system.
- Voice / Wiki are **not** in the Tools dock checklist; dock is Session + Products.
- **Resource pulse (Phase 2 first step):** Eve calls `resource_pulse` / `admit_for_goal` to see headroom and admit light skills herself. GPU/heavy → she asks you. Goal: you manage goals; she manages the capability space. Dock stays a display window (e.g. DAZE), not a gear panel.

## LEGO products (open / call when intent matches)

| Product | Open | Eve may |
|---------|------|---------|
| **Truth Drift** | [wiki.html](http://127.0.0.1:8080/wiki.html) + Toolbelt Wiki Local for chat compare | `wiki_scout_compare_years` only when you ask to compare years — not everyday lookup |
| **Wiki glasses** | Same Wiki Local session | `wiki_scout_search` / `wiki_extract` / `wiki_read_section` — Eve resolves the subject and pronouns herself; empty EXTRACT fails closed |
| **DAZE** | [daze.html](http://127.0.0.1:8080/daze.html) or chat dock | `daze_*` tools when Time Reclaim enabled |
| **Stem Factory** | Drop songs in `C:\Empire_Workbench\stem_factory\input` | `stem_list_inbox` / `stem_run` when Stem Factory enabled (GPU) |

## Staging memory (Eve decides value; Architect gates permanence)

```
work → propose_remember → eve_staging (+ ledger file)
                         ↓
              Architect: keep → confirm → eve_memory / eve_core
              Architect: drop → drop_staging
              TTL expiry     → sweep
```

- Cast trivia may be a **crumb** (proof of successful recall), not a reason to ingest an encyclopedia page.
- No full Wikipedia → Cognee. No auto-remember from wiki_cache / scout caches.
- Eve may create/revise/delete **her** staging sandbox. Mechanic never deletes your Resource Queue or wiki corpus.
- TTL sweeper: `.\scripts\sweep-eve-staging.ps1` (or `python -m pipeline.eve_staging sweep`).

### Approved ambient-memory exception

The `EMPIRE-AmbientMemoryWatchdog` Task Scheduler worker may extract at most one
bounded fact from a successful user turn when the user's text contains one of the
approved whole-phrase triggers: `that worked`, `perfect`, `finally`,
`this is exactly it`, `keep this`, `looks good`, `resolved`, or `nailed it`.
It writes only to Cognee dataset `eve_ambient`, capped at 10 facts per hour,
with event provenance and audit output. Deliberate memories remain in `eve_memory`;
research abstracts remain in the SQLite catalog and are never automatically promoted.

## Toolbelt buckets

| Bucket | Examples | Default |
|--------|----------|---------|
| **Always (core UX)** | Voice Presence (header ready strip, not dock list) | On |
| **Session** | Wiki Local (header ready strip), scouts, forge, loom, browser, extract, rerank | Wiki Local on; rest off |
| **Products** | Time Reclaim (DAZE), Stem Factory | Off until you need the product |

Research Partner (More tab) can admit read-only research limbs for a short TTL without permanent checklist clutter.

## Mechanic before Architect

After forge or fix, Mechanic runs `.\scripts\mechanic-green.ps1` (and `-Full` when live Eve matters) **before** asking the Architect to click through UX. Architect smoke = “does this feel like the product?”, not CI.

## Box rule (updated)

| Keep locked | May grow / prune |
|-------------|------------------|
| Personal workbench files, Resource Queue originals, wiki_md corpus | Eve staging ledger + `eve_staging` Cognee dataset |
| Non-destructive harvest (copy, don’t destroy queue) | Scratchpads, Error Book, extract cache under Thought Experiments |

Hard rejects unchanged: no mega FastMCP rewrite, no paid cloud LLM in app code, no silent full-wiki ingest.

## Related

- Idea / test queue: [`EMPIRE_IDEA_QUEUE.md`](EMPIRE_IDEA_QUEUE.md)
- Structural plan (diagnosis, spine contract, tool triage, phases): [`REFACTOR_PLAN.md`](REFACTOR_PLAN.md)
- Wiki extract fidelity: [`WIKI_EXTRACT_FIDELITY.md`](WIKI_EXTRACT_FIDELITY.md)
- Usage how-to: [`EMPIRE_USAGE_GUIDE.md`](EMPIRE_USAGE_GUIDE.md)
