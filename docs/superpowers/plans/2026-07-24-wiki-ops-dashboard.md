# Wiki Ops Dashboard v1 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ship a local Wiki Ops dashboard (`wiki.html`) plus maintenance/export/resolve tooling so operators can track 23h Wikipedia ingest progress, plan a ranked subject queue anytime, and (after ingest stops) resolve subjects to whole articles for front-of-queue drain — without PocketBase, React, Cognee-from-browser, or disrupting a live overnight run.

**Architecture:** Control-plane JSON under `%LOCALAPPDATA%\EMPIRE\` (checkpoint + ranked `priority_subjects.json`); heavy report artifacts on `I:\EMPIRE_DATA\wiki-reports\{year}\`. `frontend/serve.py` serves HTMX/Alpine/Pico UI and file-only wiki APIs. Maintenance scripts (gate on overnight PID) build titles/status, run ANALYZE/VACUUM until done, and title-match subjects → `priority_resolved.jsonl`. Next ingest window drains awaiting resolved articles before linear checkpoint resume.

**Tech Stack:** Python 3 (venv) pipeline modules; PowerShell wrappers; `frontend/serve.py` (stdlib HTTP); HTMX + Alpine.js + Pico CSS via CDN; pytest for matcher unit tests. No React/SPA. No PocketBase for priorities. No Cognee/Postgres from the browser.

**Spec:** `docs/superpowers/specs/2026-07-24-wiki-ops-dashboard-design.md`

## Global Constraints

- **Ingest window default:** `-MaxHours = 23` (change defaults in scripts/docs only; do **not** restart a currently running overnight to pick this up).
- **Maintenance:** runs **until done** (no hard 1h cap); soft warn if > 2h; never `VACUUM FULL` unless explicit `-AllowVacuumFull`.
- **Load isolation during INGEST:** no title catalog scans, subject matching, report rebuilds, ANALYZE/VACUUM, or Cognee from UI while overnight PID is alive. Ranked subject CRUD/reorder (tiny local JSON write) is allowed anytime and must not touch Cognee/Postgres/`wiki_ingest`.
- **Priorities store (v1 lock):** `%LOCALAPPDATA%\EMPIRE\priority_subjects.json` + `serve.py` only. **No PocketBase. No Cognee Postgres queue.**
- **Subjects:** free-text search intents; optional per-subject `intent`/`notes` (planning only; ignored by matcher). Match **article titles** (+ optional frontmatter aliases/redirects) only — **never body/full-text search**. Never auto-enqueue every title that merely contains the subject token.
- **Ambiguity:** auto-accept single high-confidence primary only (exact **or** score ≥ 0.90 with margin ≥ 0.05); else `needs_confirm` with top N=10 title candidates; user multi-selects whole articles.
- **Ingest restart order:** drain `priority_resolved.jsonl` (`awaiting`, sort `subject_rank` then `queued_at`) **before** linear checkpoint.
- **Reports root:** `I:\EMPIRE_DATA\wiki-reports\{year}\` (not OneDrive/repo).
- **Corpus 2017:** `corpus_total = 5347264`; batches ≈ 535.
- **UI stack:** HTMX + Alpine + Pico CDN only; bind `127.0.0.1:8080`.
- **Test safety:** do not stop/kill overnight if active; do not call Cognee MCP; do not `docker compose down`; do not run VACUUM while overnight PID alive (gate maintenance); stub/checkpoint-only status OK for UI smoke.
- **Git:** do **not** commit unless the user explicitly asks (workspace rule overrides skill “frequent commit” defaults — treat commit steps as optional / ask first).

---

## File structure (create / modify)

| Path | Responsibility |
|------|----------------|
| `pipeline/wiki_ops_paths.py` | Shared path helpers: LOCALAPPDATA EMPIRE dir, reports root, PID path, subjects path, year validation |
| `pipeline/wiki_title_matcher.py` | Normalize + score title/alias candidates; decide auto vs needs_confirm vs unmatched |
| `pipeline/wiki_priority_subjects.py` | Load/save/renumber ranked `priority_subjects.json`; CRUD helpers; cancel awaiting on edit/delete |
| `pipeline/wiki_priority_resolved.py` | Read/write/rewrite `priority_resolved.jsonl`; list awaiting; mark status; cancel by subject_id |
| `pipeline/wiki_report_export.py` | Checkpoint progress sum → `wiki-status.json`; optional titles rebuild + new-titles delta + `report-meta.json` |
| `pipeline/wiki_priority_resolve.py` | Maintenance: rank-order pending subjects → title index match → update subjects + append resolved |
| `pipeline/wiki_codex_seed.py` | Parse Master Codex MD → append pending subjects (idempotent) |
| `pipeline/wiki_ingest.py` | Add safe drain of `priority_resolved` before linear work (`--drain-priorities` / start hook); no-op if missing/empty |
| `frontend/serve.py` | `/api/wiki/*` routes (status, titles, new-titles, priorities CRUD/PUT/confirm) |
| `frontend/wiki.html` | Ops UI: progress, new titles, ranked queue CRUD/reorder + intent/notes + needs_confirm |
| `frontend/empire-nav.js` | Add Wiki nav link |
| `scripts/export-wiki-report.ps1` | Thin wrapper → `python -m pipeline.wiki_report_export` |
| `scripts/wiki-maintenance.ps1` | Gate PID → ANALYZE/VACUUM → export → resolve → mark complete; optional `-SeedCodex` |
| `scripts/seed-priority-subjects-from-codex.ps1` | One-shot Codex seed wrapper |
| `scripts/start-wiki-ingest-overnight.ps1` | Default `MaxHours=23`; stop snapshot; drain priorities once at window start |
| `scripts/launch-wiki-ingest-overnight.cmd` | Default `MAXHOURS=23` |
| `tests/pipeline/test_wiki_title_matcher.py` | Unit tests + fixtures for matcher rules |
| `tests/pipeline/fixtures/wiki_title_catalog.json` | Small title→path fixture set |
| `docs/WIKI_INGEST_OVERNIGHT.md` | Short “Ops dashboard” section + MaxHours 23 note |
| `docs/superpowers/specs/2026-07-24-wiki-ops-dashboard-design.md` | Spec (read-only reference; do not rewrite unless gaps found) |

**Existing reuse:** `pipeline/wiki_checkpoint.py` (load), `pipeline/wiki_normalizer.py` (`_parse_frontmatter` / title), overnight PID at `I:\EMPIRE_DATA\logs\wiki-ingest-overnight-{year}.pid`.

---

### Task 1: Shared paths + year validation

**Files:**
- Create: `pipeline/wiki_ops_paths.py`
- Test: `tests/pipeline/test_wiki_ops_paths.py`

**Interfaces:**
- Produces:
  - `EMPIRE_DIR: Path`
  - `subjects_path() -> Path` → `%LOCALAPPDATA%\EMPIRE\priority_subjects.json` (override `EMPIRE_PRIORITY_SUBJECTS`)
  - `reports_dir(year: str) -> Path` → `I:\EMPIRE_DATA\wiki-reports\{year}` (override `EMPIRE_WIKI_REPORTS_ROOT`)
  - `resolved_path(year: str) -> Path`
  - `status_path(year: str) -> Path`
  - `pid_path(year: str) -> Path`
  - `checkpoint_path() -> Path`
  - `validate_year(year: str) -> str` — must match `^\d{4}$` or raise `ValueError`
  - `CORPUS_TOTALS: dict[str, int]` with `"2017": 5347264`
  - `BATCHES_TOTAL: dict[str, int]` with `"2017": 535`
  - `overnight_pid_alive(year: str) -> bool`

- [ ] **Step 1: Write the failing test**

```python
# tests/pipeline/test_wiki_ops_paths.py
from pipeline.wiki_ops_paths import validate_year, CORPUS_TOTALS

def test_validate_year_ok():
    assert validate_year("2017") == "2017"

def test_validate_year_rejects_traversal():
    import pytest
    with pytest.raises(ValueError):
        validate_year("../2017")

def test_corpus_total_2017():
    assert CORPUS_TOTALS["2017"] == 5347264
```

- [ ] **Step 2: Run test to verify it fails**

Run: `.\venv\Scripts\python.exe -m pytest tests/pipeline/test_wiki_ops_paths.py -v`  
Expected: FAIL (module missing)

- [ ] **Step 3: Implement `pipeline/wiki_ops_paths.py`**

Implement the helpers above using `pathlib` + `os.environ`. `overnight_pid_alive` reads PID file, `int(strip)`, `os.kill(pid, 0)` or Windows `OpenProcess` via `ctypes` / try `psutil` only if already in deps — prefer stdlib: PowerShell not required; on Windows use `ctypes.windll.kernel32.OpenProcess` or catch `ProcessLookupError` from a minimal check. YAGNI: subprocess `tasklist` is OK for v1 if documented.

- [ ] **Step 4: Run tests — expect PASS**

- [ ] **Step 5: Commit only if user asked** (skip by default)

---

### Task 2: Title matcher (TDD) — normalize, tiers, auto vs needs_confirm

**Files:**
- Create: `pipeline/wiki_title_matcher.py`
- Create: `tests/pipeline/fixtures/wiki_title_catalog.json`
- Create: `tests/pipeline/test_wiki_title_matcher.py`

**Interfaces:**
- Produces:
  - `normalize_text(s: str) -> str` — Unicode NFKC, casefold, collapse whitespace
  - `strip_parens(s: str) -> str` — strip trailing `(...)` for secondary exact
  - `dataclass Candidate`: `title, path, page_id, score, match_tier` (`exact` | `exact_stripped` | `starts_with` | `contains`)
  - `score_subject_against_titles(subject: str, catalog: list[dict], *, candidate_limit: int = 10) -> list[Candidate]`
  - `decide_match(candidates: list[Candidate], *, auto_min_score: float = 0.90, auto_margin: float = 0.05) -> dict` with keys:
    - `decision`: `"auto" | "needs_confirm" | "unmatched"`
    - `primary`: `Candidate | None`
    - `candidates`: top list (for needs_confirm)
    - `suggestions`: near-misses when unmatched

**Scoring (locked):**
| Tier | Score |
|------|-------|
| exact title/alias | 1.00 |
| exact after paren strip | 0.95 |
| starts_with (title startswith subject preferred) | 0.80–0.94 |
| token/contains | 0.60–0.79 |
| below 0.60 | drop |

**Auto-accept:** best is exact (1.00) **or** (best ≥ 0.90 **and** (only one ≥ 0.60 **or** best−second ≥ 0.05)). Else if any ≥ 0.60 → `needs_confirm`. Else `unmatched`.

- [ ] **Step 1: Write fixture catalog**

```json
[
  {"title": "Guitar", "path": "D:\\\\wiki_md\\\\2017\\\\batch_00042\\\\Guitar.md", "page_id": "1", "aliases": []},
  {"title": "Guitar Hero", "path": "D:\\\\wiki_md\\\\2017\\\\batch_00042\\\\Guitar_Hero.md", "page_id": "2", "aliases": []},
  {"title": "Bass guitar", "path": "D:\\\\wiki_md\\\\2017\\\\batch_00007\\\\Bass_guitar.md", "page_id": "3", "aliases": []},
  {"title": "Cambrai", "path": "D:\\\\wiki_md\\\\2017\\\\batch_00012\\\\Cambrai.md", "page_id": "4", "aliases": ["Battle of Cambrai"]},
  {"title": "Paris (mythology)", "path": "D:\\\\wiki_md\\\\2017\\\\batch_00001\\\\Paris_mythology.md", "page_id": "5", "aliases": []}
]
```

- [ ] **Step 2: Write failing tests**

```python
import json
from pathlib import Path
from pipeline.wiki_title_matcher import (
    normalize_text,
    score_subject_against_titles,
    decide_match,
)

FIXTURE = json.loads(Path("tests/pipeline/fixtures/wiki_title_catalog.json").read_text(encoding="utf-8"))

def test_normalize_collapses_whitespace():
    assert normalize_text("  Battle   of  Cambrai ") == "battle of cambrai"

def test_exact_alias_auto_accepts_cambrai():
    cands = score_subject_against_titles("Battle of Cambrai", FIXTURE)
    decision = decide_match(cands)
    assert decision["decision"] == "auto"
    assert decision["primary"].title == "Cambrai"

def test_guitar_needs_confirm_does_not_auto_all_contains():
    cands = score_subject_against_titles("guitar", FIXTURE)
    decision = decide_match(cands)
    assert decision["decision"] == "needs_confirm"
    assert len(decision["candidates"]) >= 2
    # Must NOT imply enqueue-all: decision is needs_confirm, not auto with multiple

def test_unmatched_subject():
    cands = score_subject_against_titles("zzzxnotapage999", FIXTURE)
    decision = decide_match(cands)
    assert decision["decision"] == "unmatched"
```

- [ ] **Step 3: Run tests — expect FAIL**

Run: `.\venv\Scripts\python.exe -m pytest tests/pipeline/test_wiki_title_matcher.py -v`

- [ ] **Step 4: Implement matcher** (title/alias only; no body fields)

- [ ] **Step 5: Run tests — expect PASS**

- [ ] **Step 6: Commit only if user asked**

---

### Task 3: Ranked subject queue IO + resolved JSONL helpers

**Files:**
- Create: `pipeline/wiki_priority_subjects.py`
- Create: `pipeline/wiki_priority_resolved.py`
- Test: `tests/pipeline/test_wiki_priority_subjects.py`

**Interfaces — subjects:**
- `empty_queue(year_hint: str = "2017") -> dict`
- `load_subjects(path: Path | None = None) -> dict` — migrate legacy `reason`→`intent`, dense renumber ranks
- `save_subjects(doc: dict, path: Path | None = None) -> None` — atomic tmp+replace; max 500 subjects; reject empty subject; subject ≤200 chars; intent ≤500
- `renumber(doc: dict) -> dict`
- `add_subjects(doc, items: list[str | dict], *, updated_by: str = "api") -> dict`
- `patch_subject(doc, subject_id: str, *, subject=None, intent=None, rank=None) -> dict` — subject-text edit resets to `pending` and clears match fields unless consumed (`resolved_done` / all selected done) → reject with clear error
- `delete_subject(doc, subject_id: str) -> dict`
- `move_subject(doc, subject_id: str, direction: "up" | "down") -> dict`
- `put_full_list(payload: dict) -> dict` — validate, renumber, save

**Interfaces — resolved:**
- `load_resolved_lines(year: str) -> list[dict]`
- `save_resolved_lines(year: str, lines: list[dict]) -> None` — atomic
- `cancel_awaiting_for_subject(year: str, subject_id: str) -> int` — mark `cancelled` or drop awaiting
- `append_resolved(year: str, record: dict) -> None`
- `list_awaiting(year: str) -> list[dict]` — sort `subject_rank` asc, `queued_at` asc; skip `cancelled`

**Subject schema (locked fields):** `id`, `rank`, `subject`, `intent`, `added_at`, `status` ∈ `pending|needs_confirm|queued|resolved_done|unmatched|skipped`, `candidates`, `selected_articles`, `resolved`, `suggestions`. Document `schema_version: 2`.

- [ ] **Step 1: Write failing tests** for add → move up → renumber dense; edit subject resets pending; intent-only edit keeps status; delete removes id

- [ ] **Step 2: Implement subjects + resolved modules**

- [ ] **Step 3: Pass tests**

- [ ] **Step 4: Commit only if user asked**

---

### Task 4: Checkpoint progress + status-only report export

**Files:**
- Create: `pipeline/wiki_report_export.py`
- Modify: (none yet for overnight)
- Test: `tests/pipeline/test_wiki_report_export_progress.py`

**Interfaces:**
- `sum_docs_processed(checkpoint: dict, year: str) -> int` — for keys starting with `{year}/`, if `status==complete` and `total` present use `max(processed, total)` else `processed`
- `build_progress_block(checkpoint, year) -> dict` — docs_processed, corpus_total, percent_complete (3 dp), batches_complete, batches_total, active_batch_key, active_next_index, source=`checkpoint_sum`
- `write_wiki_status(year: str, *, phase: str, ingest: dict | None = None, maintenance: dict | None = None, priorities: dict | None = None, titles: dict | None = None, skip_titles: bool = True) -> Path`
- `export_report(year, *, wiki_md_root, out_root, rebuild_titles: bool, skip_titles: bool) -> dict` — CLI entry
- CLI: `python -m pipeline.wiki_report_export --year 2017 [--skip-titles|--rebuild-titles] [--corpus-total N]`

**Safe during overnight:** `--skip-titles` (default for smoke) writes/merges `wiki-status.json` from checkpoint only; does **not** walk `D:\wiki_md`.

- [ ] **Step 1: Failing test for sum/percent with mock checkpoint**

```python
def test_sum_complete_prefers_total():
    from pipeline.wiki_report_export import sum_docs_processed
    cp = {"batches": {
        "2017/batch_00000": {"processed": 100, "total": 10000, "status": "complete"},
        "2017/batch_00001": {"processed": 50, "status": "partial", "next_index": 50},
    }}
    assert sum_docs_processed(cp, "2017") == 10050
```

- [ ] **Step 2: Implement progress helpers + status writer (atomic replace)**

- [ ] **Step 3: Pass tests; manual smoke:**  
  `.\venv\Scripts\python.exe -m pipeline.wiki_report_export --year 2017 --skip-titles`  
  Expected: creates/updates `I:\EMPIRE_DATA\wiki-reports\2017\wiki-status.json` without scanning MD. If overnight running, still OK (read-only checkpoint + write reports dir only).

- [ ] **Step 4: Commit only if user asked**

---

### Task 5: Titles rebuild + new-titles delta (maintenance path)

**Files:**
- Modify: `pipeline/wiki_report_export.py`
- Create: `scripts/export-wiki-report.ps1`

**Behavior:**
- When `--rebuild-titles`: walk `D:\wiki_md\{year}\batch_*` for files with index `< next_index` (or all if batch complete); read frontmatter title only (reuse `wiki_normalizer._parse_frontmatter`); write `titles.jsonl.tmp` then replace; before replace, move existing → `titles.prev.jsonl`; compute set diff on `t` → `new-titles.jsonl` + `new-titles.json`; update `report-meta.json`.
- Line schema: `{"t","y","b","i","p","at"}`.
- **Forbidden while overnight PID alive** when rebuilding titles: `export-wiki-report.ps1` and maintenance must call `overnight_pid_alive` and refuse `--rebuild-titles` (or skip with warn) if alive.

- [ ] **Step 1: Add unit test for new-titles set difference on tiny in-memory lists** (no full corpus walk in CI)

- [ ] **Step 2: Implement rebuild + delta; PS1 wrapper**

```powershell
# scripts/export-wiki-report.ps1
param([string]$Year = "2017", [switch]$SkipTitles, [switch]$RebuildTitles)
$Root = Split-Path -Parent $PSScriptRoot
$py = Join-Path $Root "venv\Scripts\python.exe"
$args = @("-m", "pipeline.wiki_report_export", "--year", $Year)
if ($SkipTitles) { $args += "--skip-titles" }
elseif ($RebuildTitles) { $args += "--rebuild-titles" }
& $py @args
```

- [ ] **Step 3: Document that full rebuild waits until overnight stops**

- [ ] **Step 4: Commit only if user asked**

---

### Task 6: Priority resolve (maintenance) + Codex seed

**Files:**
- Create: `pipeline/wiki_priority_resolve.py`
- Create: `pipeline/wiki_codex_seed.py`
- Create: `scripts/seed-priority-subjects-from-codex.ps1`
- Test: `tests/pipeline/test_wiki_codex_seed.py`, extend matcher integration in `test_wiki_priority_resolve.py`

**Resolve interfaces:**
- `build_title_index(year, wiki_md_root, *, limit_batches: int | None = None) -> list[dict]` — maintenance only; for tests inject catalog
- `resolve_pending_subjects(year: str, *, catalog: list[dict] | None = None, candidate_limit: int = 10) -> dict` — process `pending` in rank order; update subjects file; append auto resolved lines; write `priority_resolution.json`; leave `needs_confirm` for UI
- Already-ingested: if path/title in `titles.jsonl` done-set → `skipped_already_done` / subject `resolved_done` when sole primary already done

**Codex seed:**
- Path: `docs/reference/THE MASTER CODEX! 50 UNIVERSAL PRIMITIVES.md`
- Parse `##` section + `^\d+\.\s+\*\*(.+?)\*\*:` → subject = bold name; `intent = "codex_primitive | {section}"`
- Idempotent skip on normalized subject already present; missing file → print message, exit 0
- Does **not** write `priority_resolved.jsonl`

- [ ] **Step 1: Failing tests** — parse ~few primitives from a tiny fixture string; seed skips duplicates; resolve `"Cambrai"` auto with fixture catalog; `"guitar"` → needs_confirm and **zero** resolved appends

- [ ] **Step 2: Implement resolve + seed modules + PS1**

```powershell
.\scripts\seed-priority-subjects-from-codex.ps1 -DryRun  # if DryRun: print would-add count, no write
```

- [ ] **Step 3: Pass tests; dry-run against real Codex path**

- [ ] **Step 4: Commit only if user asked**

---

### Task 7: `wiki_ingest` priority drain (safe if missing/empty)

**Files:**
- Modify: `pipeline/wiki_ingest.py`
- Optionally thin helper in `pipeline/wiki_priority_resolved.py`: `drain_awaiting(year, ingest_one_path_cb) -> dict`

**Behavior:**
- New CLI flag `--drain-priorities`: before linear `--year/--batch` work (or standalone), load awaiting resolved for year; for each path, run same normalize+remember(+embed flush policy as one-file) path used by batch ingest; mark `ingested` / `failed` / `skipped_already_done`; rewrite JSONL atomically.
- If file missing or no awaiting lines → log one line and continue (exit 0 for standalone drain).
- Overnight script (Task 9) calls drain **once** at window start; do not drain every mid-window slice.

- [ ] **Step 1: Add unit-level test** with temp JSONL + mock callback counting calls (no Cognee)

- [ ] **Step 2: Wire `--drain-priorities` into `main()` / `_async_main`

- [ ] **Step 3: Manual:** `python -m pipeline.wiki_ingest --year 2017 --drain-priorities` with empty/missing file → exits 0, no Cognee load required if early-return before client init preferred

- [ ] **Step 4: Commit only if user asked**

---

### Task 8: Maintenance orchestrator script

**Files:**
- Create: `scripts/wiki-maintenance.ps1`

**Steps (ordered):**
1. **Gate:** if `overnight_pid_alive(Year)` → throw/exit non-zero with clear message (do not VACUUM).
2. Optional `-SkipAnalyze` / `-SkipVacuum` / `-SkipPriorityResolve` / `-SeedCodex` / `-AllowVacuumFull`.
3. Postgres (if Docker `empire-cognee-postgres` healthy): `ANALYZE`; for hot tables if dead ratio ≥ 0.05 or dead ≥ 10000 → `VACUUM (ANALYZE) <table>`. Hot list from spec. If PG down → warn and continue.
4. Run export with `--rebuild-titles` (unless `-SkipTitles`).
5. Unless `-SkipPriorityResolve`: `python -m pipeline.wiki_priority_resolve --year …`
6. Optional `-SeedCodex`: call seed script (planning only).
7. Mark `wiki-status.json` `phase=idle`, `maintenance.complete=true`, timestamps, priority summary counts.
8. Log to `I:\EMPIRE_DATA\logs\wiki-maintenance-{year}-{timestamp}.log`

- [ ] **Step 1: Write script with gate first**

- [ ] **Step 2: While overnight running — verify gate refuses** (expected fail message); do **not** force through

- [ ] **Step 3: Commit only if user asked**

---

### Task 9: Overnight defaults + stop snapshot + drain at start

**Files:**
- Modify: `scripts/start-wiki-ingest-overnight.ps1` — `[double]$MaxHours = 23.0`; at start after preflight call drain; on exit write stop snapshot via `wiki_report_export` / small Python one-liner; clear PID; detect stop_reason (`max_hours|batches_complete|consecutive_failures|operator_abort`); honor `%LOCALAPPDATA%\EMPIRE\wiki-abort.flag` (finish current slice, stop, delete flag)
- Modify: `scripts/launch-wiki-ingest-overnight.cmd` — `MAXHOURS` default `23`
- **Do not restart** the live overnight process in this task

- [ ] **Step 1: Change defaults + document in script comment header**

- [ ] **Step 2: Add stop-snapshot function writing `wiki-status.json` with `phase: ingest_stopped`**

- [ ] **Step 3: At loop start (once):**  
  `& $Python -m pipeline.wiki_ingest --year $Year --drain-priorities`

- [ ] **Step 4: Verify current overnight still alive** (PID file + process) — do not kill

- [ ] **Step 5: Commit only if user asked**

---

### Task 10: `serve.py` wiki APIs

**Files:**
- Modify: `frontend/serve.py`
- Test: manual curl / `Invoke-RestMethod` (no Cognee)

**Routes:**
| Method | Path | Behavior |
|--------|------|----------|
| GET | `/api/wiki/status?year=2017` | Merge live checkpoint progress + `wiki-status.json` + `overnight_pid_alive` → effective phase |
| GET | `/api/wiki/titles?year=&q=&offset=&limit=` | Page `titles.jsonl` (empty + message if missing) |
| GET | `/api/wiki/new-titles?year=&offset=&limit=` | Page `new-titles.jsonl` |
| GET | `/api/wiki/priorities` | Load subjects + optional resolution summary + awaiting head |
| PUT | `/api/wiki/priorities` | Full ordered list replace (simplest Build1) |
| POST | `/api/wiki/priorities` | Append subjects (strings or `{subject,intent}`) |
| PATCH | `/api/wiki/priorities/{id}` | Edit subject/intent/rank |
| DELETE | `/api/wiki/priorities/{id}` | Delete + cancel awaiting resolved |
| POST | `/api/wiki/priorities/confirm` | Multi-article confirm → append resolved `user_confirm` |

**Rules:** `year` via `validate_year`; CORS allow PATCH/DELETE/PUT; reject payloads with `path`/`page_id` on subject create; **no** Cognee/Postgres/`wiki_ingest` process calls.

- [ ] **Step 1: Extend `end_headers` methods + `do_GET`/`do_POST`/`do_PUT`/`do_PATCH`/`do_DELETE`**

- [ ] **Step 2: Manual CRUD smoke** against `%LOCALAPPDATA%\EMPIRE\priority_subjects.json`

- [ ] **Step 3: Commit only if user asked**

---

### Task 11: `wiki.html` + nav

**Files:**
- Create: `frontend/wiki.html`
- Modify: `frontend/empire-nav.js` — add `{ id: "wiki", label: "Wiki", href: "http://127.0.0.1:8080/wiki.html" }`

**UI sections (single column, Pico):**
1. Header “Wiki Ops” + year selector (default 2017)
2. Progress: docs / corpus, percent bar, phase badge, last updated
3. Window meta: stop reason, slices, maintenance flag, copyable log path
4. Titles: search + paged list
5. New: count + paged list
6. Priorities: ranked table — rank #, subject, intent/notes, status; Add; Edit; Delete; Move up/down; bulk newline paste; needs_confirm multi-select Confirm/Skip; unmatched suggestions

**Refresh:** status poll 30s only while ingest/PID alive; manual Refresh always. Mutations PUT/PATCH local file only.

- [ ] **Step 1: Implement page mirroring `dashboard.html` CDN pattern**

- [ ] **Step 2: Open `http://127.0.0.1:8080/wiki.html` — CRUD smoke; confirm overnight unaffected**

- [ ] **Step 3: Commit only if user asked**

---

### Task 12: Docs touch + safe end-to-end verification

**Files:**
- Modify: `docs/WIKI_INGEST_OVERNIGHT.md` — short **Ops dashboard** section: UI URL, subject queue path, reports root, maintenance command after stop, MaxHours default 23, link to design spec; update recommended table from 14h → 23h for **future** runs

**Verification checklist (while overnight may run):**
- [ ] Matcher unit tests PASS
- [ ] Codex seed dry-run prints would-add / skip message
- [ ] `wiki_report_export --skip-titles` writes status from checkpoint
- [ ] serve `wiki.html` + priorities CRUD
- [ ] `wiki-maintenance.ps1` **refuses** if overnight PID alive
- [ ] Overnight PID still alive after all changes (if it was at start)
- [ ] **After overnight ends:** run `.\scripts\wiki-maintenance.ps1 -Year 2017` (VACUUM/ANALYZE + titles rebuild + resolve)

- [ ] **Step 1: Write docs section**
- [ ] **Step 2: Run verification checklist**
- [ ] **Step 3: Commit only if user asked**

---

## Out of scope (do not implement in v1)

- `wiki-ops-orchestrator.ps1` auto-restart loop (v2)
- PocketBase `wiki_priorities`
- Body/full-text search; auto-enqueue all contains-hits
- Drag-and-drop reorder
- `VACUUM FULL` by default
- Calling Cognee MCP / starting cognify from dashboard or maintenance UI
- Restarting/killing the currently running overnight to apply MaxHours=23

---

## Spec coverage self-check

| Spec area | Task(s) |
|-----------|---------|
| 23h ingest default + clean stop snapshot | 9, 12 |
| Maintenance until done + ANALYZE/VACUUM gate | 8 |
| File ranked queue CRUD/reorder anytime + intent/notes | 3, 10, 11 |
| Codex seed from Master Codex | 6, 12 |
| Title-match resolve, needs_confirm, no body search | 2, 6 |
| Priority drain before linear checkpoint | 7, 9 |
| wiki.html HTMX/Alpine/Pico; no React/PB | 10, 11 |
| Reports on `I:\EMPIRE_DATA\wiki-reports` | 1, 4, 5 |
| Progress from checkpoint; New titles | 4, 5, 11 |
| Do not disrupt overnight during test | Global + 8 gate + 12 checklist |

**Placeholder scan:** none intentional — commit steps explicitly optional per workspace git rule.

---

## Execution handoff

Plan complete and saved to `docs/superpowers/plans/2026-07-24-wiki-ops-dashboard.md`.

**Two execution options:**

1. **Subagent-Driven (recommended)** — fresh subagent per task, review between tasks  
2. **Inline Execution** — execute tasks in this session with checkpoints  

**Which approach?** (Do not start implementation until you choose.)
