# Wiki Glasses Forward — Momentum Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make local Wikipedia a sharp, everyday resource for Eve — tighter extracts, one-button regression, then sparse memory — without another research rabbit hole.

**Architecture:** Phone book (Title DNS) → Library (`D:\wiki_md`) → Glasses (`pipeline/wiki_extract.py` Evidence JSON + `[[EMPIRE_WIKI_EXTRACT]]` fail-closed). Cognee only stores **ok** extracts you choose to keep. No full-wiki ingest. No DuckDB/ZIM until latency or residual misses force it.

**Tech Stack:** Python extract pipeline, frontend wiki inject (`frontend/wiki_drift_api.py`), Eve tools (`wiki_extract` / `wiki_resolve` / `wiki_remember`), MCP `wiki_scout_mcp`, Ollama-local Eve, PocketBase/HTMX Workbench unchanged.

**Momentum rule (Architect):** One sitting = **one checkbox task** that ends with a green battery or a visible Eve answer. If a task takes >45 minutes, stop and split it. Do not open DuckDB, Weaviate, or “rebuild the wiki stack” tickets in this plan.

## Global Constraints

- Stack rules: HTMX/Alpine CDN UI, PocketBase `127.0.0.1:8090`, Ollama `localhost:11434/v1`, no SPA / no cloud BaaS / no paid LLM in app code.
- Fail closed: empty EXTRACT → refuse; never invent from training memory.
- Non-destructive: copy, don’t destroy Resource Queue / wiki corpus.
- Windows paths only; Eve rebuild via `npm run build` in `agents/empire-task-agent` when TS tools change.
- Baseline commit: `8a03097` — “Ship local Wikipedia structured extract path for Eve.”

## Already proven (do not re-litigate)

- Locate → extract → refuse works (CLI **11/11**, live Eve **8/8**).
- Switch specs, Python paradigm, Following ratings, See also lists, hard miss, empty-structure refuse.
- Soft gaps only: field asks sometimes attach extra tables; some multi-column tables flatten headers.

## Files this plan owns

| File | Responsibility |
|------|----------------|
| `pipeline/wiki_extract.py` | Evidence parse + `_filter_by_need` precision |
| `tests/pipeline/test_wiki_extract.py` | Unit tests for filter / table shape |
| `tmp/wiki_extract_battery_live.py` (or promote to `scripts/`) | Live Eve regression |
| `data/eval/wiki_extract.jsonl` | Offline eval ledger |
| `frontend/wiki_drift_api.py` | Injection contract (only if filter changes need it) |
| Eve `wiki_remember.ts` + Cognee path | Sparse remember pilot (Phase C only) |

---

### Task 1: Promote the battery to a one-command smoke

**Why first:** Visible win in <15 minutes; protects interest when you next open the repo.

**Files:**
- Create: `scripts/wiki-extract-battery.ps1`
- Move/adapt: `tmp/wiki_extract_battery.py` + `tmp/wiki_extract_battery_live.py` → `scripts/wiki_extract_battery.py` (CLI + optional `-Live`)

- [ ] Copy the working battery scripts into `scripts/` with a thin `wiki-extract-battery.ps1` wrapper that uses `venv\Scripts\python.exe`.
- [ ] Default = CLI only (~5s). `-Live` runs the 8 Eve sessions (slower, needs stack up).
- [ ] Run CLI mode; confirm **11/11** (or update counts in the script docstring).
- [ ] Commit: `Add wiki extract regression battery script.`

**Done when:** From repo root, `.\scripts\wiki-extract-battery.ps1` prints a pass count without opening Cursor plans.

---

### Task 2: Field-only asks must not dump unrelated tables

**Why:** This is the #1 “feels sloppy” gap from your manual run (Python paradigm / Switch infobox).

**Files:**
- Modify: `pipeline/wiki_extract.py` (`_filter_by_need`)
- Modify: `tests/pipeline/test_wiki_extract.py`

- [ ] Add a failing test: question containing `paradigm field` / `infobox fields` on a fixture with both fields + an extra table → result has fields, **zero** tables (or only tables whose caption/headers match the need tokens).
- [ ] Implement filter: if need looks field-scoped (`field`, `infobox`, `paradigm`, `developer`, `os`) and not `table`/`specs`/`ratings`, drop tables unless a table caption clearly matches.
- [ ] Run `.\venv\Scripts\python.exe -m pytest tests/pipeline/test_wiki_extract.py -q`.
- [ ] Re-run CLI battery; live spot-check:  
  `What paradigm field is listed for the Python programming language?`  
  Expect paradigm line **without** the built-in types table.
- [ ] Commit: `Tighten wiki extract need filter for field-only asks.`

**Done when:** Live Eve G2-style ask is short and field-focused.

---

### Task 3: Multi-column wikitable shape (Following ratings)

**Why:** Data is right; presentation looks broken. Quick polish = felt quality.

**Files:**
- Modify: `pipeline/wiki_extract.py` (`_parse_wikitable_block` / Evidence table render)
- Modify: `tests/pipeline/test_wiki_extract.py`

- [ ] Add fixture snippet from Following-style header row + 1–2 data rows.
- [ ] Failing test: rendered Markdown keeps multiple columns (not one Property/Value mash of all headers).
- [ ] Fix parser/render for multi-column `{|` tables when first row is headers.
- [ ] CLI + one live ask: `Pull the U.S. television ratings table rows from The Following page.`
- [ ] Commit: `Preserve multi-column layout in wiki extract tables.`

**Done when:** Ratings table is readable as a real grid in Eve.

---

### Task 4: Sparse remember pilot (three titles only)

**Why:** This is the bridge from “lookup tool” to “Eve’s resource” — without swallowing the library.

**Files:**
- Touch: `agents/.../wiki_remember.ts`, `pipeline/wiki_extract.py` `remember_wiki_extract`
- Optional dataset: Cognee `wiki_extracts` or reuse `eve_memory` with clear tags

- [ ] Allowlist pilot titles: `Nintendo Switch`, `Python (programming language)`, `The Following`.
- [ ] Manual: run extract → `wiki_remember` (or Workbench phrasing “remember this extract”) only when state=`ok`.
- [ ] Verify Cognee recall returns the extract packet (or a clear pointer), not a prose hallucination.
- [ ] Document 5-line “how to remember / recall” in `docs/WIKI_EXTRACT_FIDELITY.md`.
- [ ] Commit: `Pilot sparse Cognee remember for ok wiki extracts.`

**Done when:** You can remember Switch specs once, then recall them in a later chat without re-opening the page (or with a clear extract_id hit).

---

### Task 5 (parked): DuckDB / ZIM / GBNF

- [ ] Only reopen if: Title DNS latency hurts, extract miss rate stays high after Tasks 2–3, or you need offline ZIM as a second library.
- [ ] Until then: leave Phase 5 gated. Do not schedule it to “feel productive.”

---

## Session card (paste into a new chat)

```
Continue docs/superpowers/plans/2026-09-15-wiki-glasses-forward.md
Start at the first unchecked task.
One task only. End with battery green or a live Eve proof.
Do not open DuckDB/Weaviate/full-wiki ingest.
```

## Interest insurance

| Feeling | Move |
|---------|------|
| Bored / heavy | Do **Task 1** only — ship the battery, close the laptop |
| Annoyed at sloppy answers | **Task 2** — one filter, one live proof |
| Want “Eve is smarter” | **Task 4** after 2 is green |
| Urge to redesign storage | Re-read Global Constraints + Task 5 parked |

North star reminder: EMPIRE is a **local knowledge refinery**, not an encyclopedia clone. Glasses that refuse are a feature. Momentum comes from short closed loops, not bigger scopes.
