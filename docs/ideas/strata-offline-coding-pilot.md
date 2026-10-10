---
id: E-45
slug: strata-offline-coding-pilot
title: Strata + Qwen3.8-Flash-Next (IQ3_XXS) as offline Cursor coding lane
status: idea
area: models
priority: someday
depends_on: []
touches: [docs, ops]
created: 2026-10-09
source: Architect + NotebookLM (Strata README, ISTA GSQ-RCO GGUF)
---

# Strata offline coding pilot

## Intent

Evaluate [Strata](https://github.com/Niko1221/Strata) with **IQ3_XXS** (ISTA
[Qwen3.8-Flash-Next-GSQ-RCO-GGUF](https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF))
as a **separate** local inference lane for **offline EMPIRE forge work in Cursor** — not as a
replacement for Eve’s Ollama stack (`empire-fast:14b`, tool loop, GPU lease).

## Why it matters

Build-phase Cursor uses hosted agents (e.g. Composer). When subscription usage is exhausted or
the network is unplugged, the repo already documents switching Cursor to **Ollama**
(`docs/OPERATIONAL_HANDOFF.md`). That fallback is **`logicbeat/qwen3.8-27B_GSQ_RCO`** (Deep) class
quality — good, but not the same as a tiered **125B MoE Flash-Next** engine. Strata is the
measured path for “frontier-local” codegen on 64 GB RAM + 16 GB VRAM, at the cost of a second
runtime, ~80 GB disk, and **port 8080** conflict with the EMPIRE Workbench.

## What "done" looks like (acceptance)

- Strata runs on a **non-8080** API port (or EMPIRE frontend stopped during pilot sessions) with
  **IQ3_XXS** on this machine without SSD-thrashing under normal RAM load.
- Cursor (or CLI) completes **three** real EMPIRE tasks via `http://127.0.0.1:<port>/v1`: small
  MCP doc patch, TypeScript tool stub, routing/doc update — with mechanic-green still passing
  afterward.
- Written comparison vs **`logicbeat/qwen3.8-27B_GSQ_RCO`** on the **same three tasks** (quality,
  time, failure modes).
- Explicit **no-go** recorded if tool-calling or multi-file edits are worse than Ollama Deep for
  this repo.

## Stack plan (how it applies in EMPIRE)

| Layer | What it gets |
|-------|--------------|
| Eve / Ollama | **Unchanged** — Fast 14B daily; Deep 27B GSQ; no Strata wiring in `ollama-config.ts` until a separate benchmark says otherwise. |
| Cursor | Optional OpenAI-compatible provider pointing at Strata during offline forge; MCP (`empire-pocketbase`, `empire-cognee`) stays enabled. |
| Frontend | **No change** — avoid default Strata `:8080` clash with `frontend.serve`. |
| Docs | Pilot notes in this file; optional one paragraph in `OPERATIONAL_HANDOFF.md` if promoted. |

## Constraints and identity

- **No** paid cloud LLM in application code; Strata is localhost-only.
- **No** replacing Eve runtime without `ab-fast-toolcalling.py`-class evidence on Strata.
- **One heavy GPU tenant** policy still applies for Eve sessions — do not run Strata + full Eve
  GPU chat + vision without closing one side.
- Strata is **not** a substitute for wiring ZIM / backup corpora into Eve reachability.

## Open questions

- Default Strata port vs EMPIRE 8080 — use setup `--host`/config or stop Workbench during pilot?
- Is **IQ3_XXS** stable with Docker (Cognee Postgres) + browser open, or pilot **IQ2_XS** first?
- Does Cursor Agent mode honor a custom base URL the same as Chat (version-dependent)?

## Promotion checklist (idea → Work Order)

- [ ] Status is `ready` and port/RAM plan decided.
- [ ] Acceptance tasks chosen from real open forge items (not toy prompts).
- [ ] Rollback documented (stop Strata, restore Cursor cloud model).
- [ ] Eve integration explicitly out of scope unless a second WO is opened.
