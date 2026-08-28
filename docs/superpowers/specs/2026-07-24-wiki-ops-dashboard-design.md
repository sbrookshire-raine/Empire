# Wiki Ops Dashboard — Design Spec

**Date:** 2026-07-24  
**Status:** Approved base design + ranked priority subject queue (CRUD/reorder anytime) / maintenance resolve (Build1 preferred) + optional per-subject `intent`/`notes` + Codex seed path  
**Stack constraints:** HTMX + Alpine.js + Pico CSS via CDN only; frontend on `:8080` (`frontend/serve.py`); Ollama/Cognee local only; no React; browser never calls Cognee; postgres-mcp not required; no subject matching or report work during 23h ingest.  
**v1 scope lock (priorities):** file-based web queue **only** — `%LOCALAPPDATA%\EMPIRE\priority_subjects.json` + `frontend/serve.py` APIs. **No PocketBase** for priorities in v1. **No Cognee Postgres** for the queue. PocketBase `wiki_priorities` is an explicit **future optional** (v2+), not Build1.

---

## 1. Goals / Non-goals

### Goals

1. **Long ingest windows** that stop cleanly after a wall-clock budget (target **`MaxHours = 23`**), leaving a maintenance gap before the next window.
2. **Maintenance that runs until done** (no hard 1-hour cap): Postgres `ANALYZE` / selective `VACUUM (ANALYZE)` as needed, build/update report artifacts, **resolve priority subjects into ingest-ready JSON**, then optionally start the next ingest window.
3. **Zero extra load during ingest:** no title catalog scans, no subject matching, no report rebuilds, no dashboard-triggered Cognee/Postgres work while the overnight harness is active. Ranked subject-queue planning (CRUD/reorder of a small local JSON file) is allowed and must not affect ingest speed.
4. **Ops visibility** on a local page (`wiki.html`) showing:
   - Documents processed (count)
   - Percent of corpus total (2017 default: **5,347,264** ≈ 5.35M)
   - Article titles processed (browseable / searchable list backed by report files)
   - **New** titles since the previous report snapshot
   - A **ranked priority subject queue** of free-text **search intents** (not ingest JSON): add / edit / delete / reorder **anytime**, including while overnight ingest is running. Optional per-subject **`intent` / `notes`** (planning annotation; does not affect matching). During maintenance, each subject is matched against **article titles** (whole pages / `wiki_*.md` files) — never against free-floating keyword hits inside body text — then confirmed or auto-accepted whole articles are placed at the **front** of the next ingest window
5. **Progress during/after ingest** reads from `%LOCALAPPDATA%\EMPIRE\wiki-checkpoint.json` (and lightweight status JSON produced at stop/maintenance). Title indexes and **subject→article resolution/matching** run **only in the maintenance window** (unchanged). Planning the queue is never gated on maintenance.
6. Heavy artifacts live off OneDrive at **`I:\EMPIRE_DATA\wiki-reports\`**.
7. **Optional Codex seed** of pending subjects from `docs/reference/THE MASTER CODEX! 50 UNIVERSAL PRIMITIVES.md` (maintenance hook or one-shot script) — queue planning only; no Wikipedia auto-ingest until resolve+confirm.

### Non-goals

- Calling Cognee, Ollama, or wiki MCP tools from the browser.
- Requiring postgres-mcp, BrowserStack, or any cloud service.
- Replacing the existing overnight harness (`scripts/start-wiki-ingest-overnight.ps1`); this design wraps/extends it.
- Live per-document UI updates during ingest (poll checkpoint/status only).
- Asking the user for exact Wikipedia titles or structured ingest JSON up front (subjects are free-text search intents; title matching + confirm happens in maintenance / UI).
- Subject→article matching, title catalog scans, or report rebuilds **during** the 23h ingest window (queue **planning** / CRUD / reorder of `priority_subjects.json` is allowed and expected anytime).
- Touching Cognee, Postgres ingest, or the `wiki_ingest` / overnight process when saving the subject queue (tiny local JSON write only).
- **Full-text / body search** of Wikipedia MD for priority matching in v1 (titles + optional frontmatter redirects/aliases only).
- **Auto-enqueue every title** that merely contains a subject token (e.g. every page with “guitar” in the title) — forbidden; see §6.3.
- **PocketBase (or Cognee Postgres) as the priority queue store in v1** — locked out; file + `serve.py` only (PocketBase deferred as future optional — see §6 / §8).
- Cross-year multi-primary parallel ingest (still single-writer / one primary year).
- `VACUUM FULL` or any rewrite that locks the store for hours without an explicit operator flag (default: deferred).
- Drag-and-drop reorder as a Build1 requirement (move up / move down buttons are enough; DnD optional later).

---

## 2. Operating model (23h ingest → maintenance-until-done → restart)

### Phase machine

```text
IDLE ──start──► INGEST(MaxHours≈23) ──clean stop──► MAINTENANCE(until done)
                      ▲                                      │
                      │         optional auto-restart (v2)   │
                      └──────────────────────────────────────┘
```

| Phase | Duration rule | Allowed work | Forbidden work |
|-------|---------------|--------------|----------------|
| **INGEST** | Wall clock ≤ `MaxHours` (default **23**); also stops on no remaining batches, or `MaxConsecutiveFailures` | **Priority resolved queue first** (drain `priority_resolved.jsonl` / next-window front queue), then resume linear batch checkpoint; Fast Mode slices (`remember` + embed); checkpoint updates; overnight log/PID; **UI may edit/reorder raw subject queue** (local JSON only) | Title catalog build; subject matching/resolution; report export beyond a tiny stop snapshot; ANALYZE/VACUUM; mid-slice reordering of linear batches; Cognee recall from UI |
| **MAINTENANCE** | **Until done** (no hard 1h cap). Soft warn if > 2h; never kill mid-VACUUM unless operator abort file present | `ANALYZE`; selective `VACUUM (ANALYZE)`; export reports/titles; **resolve pending subjects in rank order → wiki MD → structured ingest JSON**; place resolved articles at front of next ingest queue; mark already-ingested / unmatched | Starting a new ingest window until maintenance marks `maintenance.complete=true` |
| **IDLE** | Until next scheduled/manual start | Serve dashboard; full subject-queue CRUD/reorder; confirm ambiguous title matches (multi-select whole articles) | — |

### Ingest stop (clean)

Reuse / parameterize `scripts/start-wiki-ingest-overnight.ps1`:

| Parameter | Build1 default | Notes |
|-----------|----------------|-------|
| `-MaxHours` | **23** | Primary stop condition |
| `-MaxSlices` | **9999** | Effectively wall-clock gated; keep as safety valve |
| `-FileLimit` | **200** | Matches current overnight recommendation |
| `-FlushEvery` | **50** | Unchanged |
| `-Year` | **2017** | Primary corpus |

On exit (deadline, no batches, or consecutive-failure stop), the harness **must**:

1. Leave checkpoint consistent (no half-written JSON; existing atomic write in `wiki_checkpoint.py`).
2. Clear or mark PID file inactive (`I:\EMPIRE_DATA\logs\wiki-ingest-overnight-{year}.pid`).
3. Write a **stop snapshot** (small): `I:\EMPIRE_DATA\wiki-reports\{year}\wiki-status.json` with `phase: "ingest_stopped"`, counts from checkpoint sum, `ingest_ended_at`, `stop_reason` ∈ `max_hours | batches_complete | consecutive_failures | operator_abort`.
4. Exit 0 when stop is intentional (deadline / complete); non-zero only for unrecoverable harness failure.

**Operator abort:** if `%LOCALAPPDATA%\EMPIRE\wiki-abort.flag` exists, finish current slice (do not start another), then stop with `stop_reason: operator_abort` and delete the flag.

### Maintenance (until done)

Orchestrator script (new): `scripts/wiki-maintenance.ps1` (see §5).

Ordered steps:

1. **Gate:** refuse if overnight PID is alive for that year (duplicate guard same as ingest).
2. **Postgres hygiene (optional but default-on when Docker Postgres is up):**
   - `ANALYZE;` on `public` (fast; ~seconds historically).
   - For each hot table, if `n_dead_tup / nullif(n_live_tup,0) ≥ 0.05` **or** `n_dead_tup ≥ 10000`, run `VACUUM (ANALYZE) <table>`.
   - Hot tables (fixed list): `data`, `graph_node`, `graph_edge`, `DocumentChunk_text`, `EdgeType_relationship_name`, `pipeline_runs`, `TextDocument_name`, `dataset_data`.
   - Never run `VACUUM FULL` unless `-AllowVacuumFull` is passed (not used by scheduler).
3. **Report build:** `scripts/export-wiki-report.ps1` / Python module (see §3–§5) — rebuild/refresh `titles.jsonl`, new-titles delta, `wiki-status.json` progress block.
4. **Priority subject resolution** (see §6): after titles catalog is current (or using `D:\wiki_md\{year}` frontmatter + existing `titles.jsonl`):
   1. Load entries from the **ranked raw subject queue** in **rank order** (rank `1` first; see §6.1). Process `status: pending` (and `needs_confirm` only when re-resolving after edit, or when operator left them for another pass — Build1 default: resolve `pending` in rank order; leave `needs_confirm` for UI confirm).
   2. Match each subject (**search intent**) against **article titles** for that year (catalog / MD frontmatter `title` + optional redirects/aliases) — **not** full-text body (§6.3).
   3. **Auto-queue** only a high-confidence **single primary** article when rules pass; convert that match into a **structured ingest record** (`path`, `page_id`, `title`, `year`, `match_score`, `match_reason`) and append to the **front** of the next-window priority ingest queue (`priority_resolved.jsonl`) **preserving subject rank order** (rank 1 drains before rank 2). **Never** auto-enqueue every title that merely contains the subject token.
   4. Ambiguous / multi-hit subjects → record top **N** title candidates (default **10**); leave `needs_confirm` for the UI. User may pick **0..N** articles; each pick queues that **full MD article**.
   5. Already-ingested selected articles → mark those article rows done / skip re-add (check against `titles.jsonl` done-set and/or Cognee incremental identity when available — maintenance only). Subject stays until user dismisses or **all selected articles** are done.
   6. Unmatched → leave in queue as `unmatched` with suggestion list (title near-misses only).
5. **Mark complete** in `wiki-status.json`: `phase: "idle"`, `maintenance.complete: true`, timestamps; include priority resolution summary counts.
6. **Optional restart (v2 only):** if orchestrator `-AutoRestartIngest` and corpus not complete, launch next ingest window (**resolved priority files first**, then linear checkpoint — §6.4).

### Ingest restart order (next window)

When overnight / orchestrator starts a new ingest window after maintenance:

```text
1. Drain priority_resolved.jsonl (FIFO front queue) — ingest those MD files first
2. Resume linear batch checkpoint (next_index / next batch_*) as today
```

Do **not** scramble mid-batch ordering during a running window. Priority drain happens only at window start (and after each successful priority file, mark the resolved record `ingested` so a crash mid-drain does not re-process forever). Linear checkpoint is untouched by priority drain except that docs ingested via priority may already appear in the done-set (skip if re-encountered in linear walk — same as Cognee incremental / path identity).

### Load isolation rule

| Actor | During INGEST | During MAINTENANCE |
|-------|---------------|--------------------|
| Overnight harness | Writer (priority drain → linear) | Stopped |
| Report exporter | **No** | Yes |
| Subject resolver | **No** | Yes (after titles/report step); processes subjects in **rank order** |
| Dashboard GET status/titles | Read checkpoint + last `wiki-status.json` / titles / priority files only | Same |
| Priority subject CRUD / reorder | **Allowed anytime** — write `%LOCALAPPDATA%\EMPIRE\priority_subjects.json` only (and cancel awaiting lines in `priority_resolved.jsonl` on delete when safe); **MUST NOT** touch Cognee, Postgres ingest, or the overnight / `wiki_ingest` process | Same |
| VACUUM/ANALYZE | **No** | Yes |

**Overnight speed:** editing the ranked subject queue has **zero impact** on ingest throughput beyond a tiny local atomic file write (KB-scale JSON). No matching, no Cognee, no Postgres, no interference with the running harness.

---

## 3. Report artifacts (paths and schemas)

### Root layout

```text
I:\EMPIRE_DATA\wiki-reports\
  {year}\                          # e.g. 2017
    wiki-status.json               # single current status (atomic replace)
    titles.jsonl                   # one line per processed article (append or rebuild)
    titles.prev.jsonl              # previous maintenance snapshot (for New)
    new-titles.jsonl               # delta titles (this maintenance vs prev)
    new-titles.json                # small JSON wrapper for UI convenience
    report-meta.json               # pointers / hashes / line counts
    priority_resolved.jsonl        # next-window front queue (structured ingest records)
    priority_resolution.json       # last maintenance resolution summary for UI
  README.txt                       # optional one-liner: do not sync to OneDrive
```

Control-plane (light) stays on `%LOCALAPPDATA%\EMPIRE\`:

| Path | Role |
|------|------|
| `%LOCALAPPDATA%\EMPIRE\wiki-checkpoint.json` | Source of truth for per-batch `processed` / `next_index` / `status` |
| `%LOCALAPPDATA%\EMPIRE\priority_subjects.json` | **Ranked raw subject queue** (user free text; editable anytime; Build1) |
| `%LOCALAPPDATA%\EMPIRE\priority_manifest.json` | Deprecated alias — Build1 may write the same document as `priority_subjects.json` or keep a symlink/copy for one release |
| `%LOCALAPPDATA%\EMPIRE\wiki-abort.flag` | Operator stop request |
| `I:\EMPIRE_DATA\wiki-reports\{year}\priority_resolved.jsonl` | **Resolved** ingest-ready records; drained at next window start |
| `I:\EMPIRE_DATA\logs\wiki-ingest-overnight-*` | Existing overnight logs/PIDs |

**Rationale for `I:\EMPIRE_DATA\wiki-reports\`:** titles for millions of articles will be hundreds of MB; OneDrive/`Desktop/EMPIRE` must not hold that index. Matches existing `I:\EMPIRE_DATA\logs\` pattern. Resolved priority queue stays on `I:` with reports (paths + scores can grow; not OneDrive).

### Corpus totals (fixed constants)

| Year | `corpus_total` | Source |
|------|----------------|--------|
| 2017 | **5347264** | `docs/WIKI_INGEST_OVERNIGHT.md` (5,347,264 files) |
| 2021 | **6300000** | Approx from overnight doc (~6.3M); exact count filled by first report export via directory walk once, then cached in `report-meta.json` |
| 2026 | **7100000** | Same pattern (~7.1M); exact count cached on first export |

Build1 implements **2017** fully; other years use the same schema with their `corpus_total` from `report-meta.json` once measured.

### `wiki-status.json` schema

```json
{
  "schema_version": 1,
  "year": "2017",
  "dataset": "wikipedia_2017",
  "phase": "idle",
  "updated_at": "2026-07-24T18:00:00Z",
  "ingest": {
    "max_hours": 23,
    "started_at": "2026-07-23T19:00:00Z",
    "ended_at": "2026-07-24T18:00:00Z",
    "stop_reason": "max_hours",
    "slices_done": 120,
    "docs_this_window": 24000,
    "pid_file": "I:\\\\EMPIRE_DATA\\\\logs\\\\wiki-ingest-overnight-2017.pid",
    "log_glob": "I:\\\\EMPIRE_DATA\\\\logs\\\\wiki-ingest-overnight-2017-*.log"
  },
  "progress": {
    "docs_processed": 125000,
    "corpus_total": 5347264,
    "percent_complete": 2.337,
    "batches_complete": 12,
    "batches_total": 535,
    "active_batch_key": "2017/batch_00012",
    "active_next_index": 4500,
    "checkpoint_path": "%LOCALAPPDATA%\\\\EMPIRE\\\\wiki-checkpoint.json",
    "source": "checkpoint_sum"
  },
  "titles": {
    "catalog_path": "I:\\\\EMPIRE_DATA\\\\wiki-reports\\\\2017\\\\titles.jsonl",
    "catalog_lines": 125000,
    "new_titles_path": "I:\\\\EMPIRE_DATA\\\\wiki-reports\\\\2017\\\\new-titles.jsonl",
    "new_titles_count": 24000,
    "built_at": "2026-07-24T18:15:00Z",
    "build_source": "md_frontmatter"
  },
  "maintenance": {
    "started_at": "2026-07-24T18:01:00Z",
    "ended_at": "2026-07-24T18:20:00Z",
    "complete": true,
    "analyze_ran": true,
    "vacuum_tables": ["data", "DocumentChunk_text"],
    "vacuum_skipped": ["graph_edge"],
    "duration_sec": 1140
  },
  "priorities": {
    "subjects_path": "%LOCALAPPDATA%\\\\EMPIRE\\\\priority_subjects.json",
    "subjects_pending": 2,
    "subjects_needs_confirm": 1,
    "subjects_unmatched": 1,
    "subjects_resolved_done": 5,
    "resolved_queue_path": "I:\\\\EMPIRE_DATA\\\\wiki-reports\\\\2017\\\\priority_resolved.jsonl",
    "resolved_queued": 3,
    "resolved_awaiting_ingest": 3,
    "last_resolution_at": "2026-07-24T18:18:00Z",
    "updated_at": "2026-07-24T12:00:00Z"
  }
}
```

**`progress.docs_processed` computation (authoritative during/after ingest):**

```text
sum(batch.processed for batch in checkpoint.batches where key starts with "{year}/")
```

If a batch has `status: complete` and `total`, prefer `max(processed, total)` for that batch to avoid under-count. Do **not** query Postgres for this metric on the dashboard path.

**`percent_complete`:** `round(100.0 * docs_processed / corpus_total, 3)`.

**`phase` enum:** `idle` | `ingest` | `ingest_stopped` | `maintenance`.

Live ingest may leave `phase: ingest` only if the orchestrator sets it at start; the overnight script itself writes `ingest_stopped` on exit. Dashboard treats alive PID + checkpoint as “ingest running” even if status file is briefly stale.

### `titles.jsonl` line schema

One UTF-8 JSON object per line, **no pretty-print**:

```json
{"t":"Cambrai","y":"2017","b":"batch_00012","i":4501,"p":"D:\\\\wiki_md\\\\2017\\\\batch_00012\\\\Cambrai.md","at":"2026-07-24T18:10:00Z"}
```

| Field | Meaning |
|-------|---------|
| `t` | Article title from MD YAML frontmatter `title` |
| `y` | Snapshot year |
| `b` | Batch directory name |
| `i` | 0-based file index within batch (sorted `.md` order, same as ingest) |
| `p` | Absolute source path (optional in rebuilds; include when known) |
| `at` | ISO time the line was written |

**Build source priority (maintenance only):**

1. **Preferred:** Walk `D:\wiki_md\{year}\batch_*` files with `index < checkpoint next_index` (or all files if batch `complete`), read frontmatter `title` only (stop after second `---`). Do not open body.
2. **Fallback (readonly PG):** if MD missing, `SELECT` document name/title from Cognee Postgres **read-only** connection during maintenance only. Never from browser; never required for Build1 happy path.

**Idempotency:** maintenance rebuilds `titles.jsonl` into `titles.jsonl.tmp` then atomic replace when `--RebuildTitles` is set (default for Build1 after each window). Incremental append is allowed later if line counts match `docs_processed`; Build1 ships full rebuild for correctness.

### Previous / New titles

1. Before replacing `titles.jsonl`, if it exists, copy/rename to `titles.prev.jsonl` (or keep last good prev).
2. Compute set difference on title strings (`t`): `new = current − prev`.
3. Write `new-titles.jsonl` (same line schema) and:

```json
{
  "schema_version": 1,
  "year": "2017",
  "compared_at": "2026-07-24T18:15:00Z",
  "prev_lines": 101000,
  "current_lines": 125000,
  "new_count": 24000,
  "new_titles_path": "I:\\\\EMPIRE_DATA\\\\wiki-reports\\\\2017\\\\new-titles.jsonl"
}
```

as `new-titles.json`.

First-ever report: `prev` empty ⇒ all current titles are “New”.

### `report-meta.json`

```json
{
  "schema_version": 1,
  "year": "2017",
  "corpus_total": 5347264,
  "batches_total": 535,
  "titles_bytes": 0,
  "last_export_at": "2026-07-24T18:15:00Z",
  "wiki_md_root": "D:\\\\wiki_md"
}
```

---

## 4. UI (`wiki.html` + nav; fields; ranked priority queue)

### Stack

- `frontend/wiki.html` — Pico CSS CDN + Alpine.js CDN + HTMX CDN (same pattern as `dashboard.html`).
- Shared `empire-nav.js` / `empire-nav.css`.
- No React, no build step, no Cognee from the page.

### Nav

Add to `NAV_LINKS` in `frontend/empire-nav.js`:

```js
{ id: "wiki", label: "Wiki", href: "http://127.0.0.1:8080/wiki.html" }
```

`wiki.html` mounts `<nav id="empire-nav" data-current="wiki"></nav>`.

### Page sections (single column, minimal)

1. **Header** — “Wiki Ops” + year selector (default 2017; Alpine state `year`).
2. **Progress** — large `docs_processed` / `corpus_total`, percent bar, phase badge (`idle` / `ingest` / `maintenance`), last updated.
3. **Window meta** — last stop reason, slices this window, maintenance complete flag, link text to log path (copyable `code`, not remote fetch).
4. **Titles** — search box filters client-side over a **paged** fetch (`limit`/`offset` via API). Show title list (not the whole 5M file in one response).
5. **New** — count + list from `new-titles` API (default last 200; “load more”).
6. **Priorities (ranked subject queue)** — easy-to-use ranked list of **search intents** the operator can plan **anytime** (including overnight ingest). Each intent must resolve to **whole Wikipedia articles** (page titles / MD files), not keyword hits in body text. See below. Do **not** ask for wiki paths, `page_id`, or ingest JSON up front.

### Priority SUBJECTS panel (v1 UX)

A single ranked queue, not a free-form dump box alone:

| Column / control | Behavior |
|------------------|----------|
| **Rank #** | 1-based position in the ordered list (1 = resolve / drain first) |
| **Subject** | Free-text **search intent** (topic phrase used for title matching) |
| **Intent / notes** | Optional free-text annotation (e.g. `systems_primitive`, cross-domain why, Codex section). Shown and editable in the queue UI. **Does not** affect title matching (§6.3) |
| **Status** | Badge: `pending` / `resolved` (UI label for `queued` or `resolved_done`) / `unmatched` / `needs_confirm` (map schema statuses for display) |
| **Add** | Append a new subject at the end (or optional “insert at rank”); status `pending`; optional intent/notes on create |
| **Edit** | Inline or modal edit of subject text and/or intent/notes. Editing **subject** text → resets that entry to `pending` and clears prior match fields (§6.6) unless already consumed this cycle. Editing **intent/notes alone** does **not** reset match status |
| **Delete** | Remove from queue; cancel awaiting resolved record(s) if not yet started (§6.6) |
| **Move up / Move down** | Swap with neighbor; renumber ranks 1…N. Drag-and-drop is **optional**, not required for v1 |

Also show (same panel or adjacent Pico sections):

- **Needs confirm** — ambiguous title matches with top candidates (default up to **10** article titles) + multi-select Confirm / Skip. Operator explicitly picks which **whole article(s)** to prioritize; each pick queues that full MD file. Do not imply “all guitar* titles will ingest.”
- **Unmatched** — subject + suggestion **titles** (edit subject text to re-queue as `pending`)
- Counts of resolved-awaiting-ingest vs already-done (**per article**, not per keyword hit)
- Per-subject progress: selected articles done / remaining; subject remains until dismissed or all selected are done

**Planning anytime:** Add / edit / delete / reorder work while overnight ingest is active. Writes hit only the small local subject file (and safe cancel of awaiting resolved lines). Resolution/matching still runs **only** in maintenance.

### Data loading

| UI need | Endpoint | Backend source |
|---------|----------|----------------|
| Status metrics | `GET /api/wiki/status?year=2017` | Merge live checkpoint sum + `wiki-status.json` |
| Titles page | `GET /api/wiki/titles?year=2017&q=&offset=0&limit=100` | Stream/scan `titles.jsonl` (maintenance artifact); empty list + message if missing |
| New titles | `GET /api/wiki/new-titles?year=2017&offset=0&limit=100` | `new-titles.jsonl` |
| Read ranked queue | `GET /api/wiki/priorities` | `priority_subjects.json` (ordered) + optional `priority_resolution.json` + head of `priority_resolved.jsonl` |
| Replace full ordered list | `PUT /api/wiki/priorities` | Atomic write of entire ranked `subjects[]` (preferred for reorder + bulk sync) |
| Add subject(s) | `POST /api/wiki/priorities` | Append new `pending` entries; assign next ranks |
| Patch one entry | `PATCH /api/wiki/priorities/{id}` | Edit subject text and/or `intent`/`notes`, status reset rules, or move to new rank |
| Delete one entry | `DELETE /api/wiki/priorities/{id}` | Remove + cancel awaiting resolved if safe (§6.6) |
| Confirm ambiguous | `POST /api/wiki/priorities/confirm` | Pick **one or more** candidate **articles** → append one resolved record **per** chosen article; update subject selected set; clear or keep `needs_confirm` until picks are recorded |

Build1 may implement **either** granular POST/PATCH/DELETE **or** a single **PUT of the full ordered list** after each UI mutation (Alpine holds the list; Save/Apply writes the whole file). Both are valid; PUT-full-list is simplest and still tiny.

**Refresh:** Alpine `setInterval` 30s for status only while `phase === 'ingest'` or PID alive; manual Refresh button always. Titles/New load on demand. Priority queue reloads after each mutation and on manual refresh — **no** resolve/match work from UI; no polling that triggers Cognee.

### Priority queue form behavior

- Subjects are **free text** only (1–200 chars). Optional bulk paste (newline-separated) still accepted as **Add many** → append as `pending` at end ranks.
- Optional **intent / notes** per subject (free text, recommended ≤ 500 chars): planning annotation only — e.g. `systems_primitive`, “cross-domain why”, Codex section label. Displayed and editable in `wiki.html`; stored on the subject row; **ignored by the title-matching algorithm**.
- Reject payloads that look like ingest records (`path` / `page_id`).
- Validate: max **500** entries; reject empty subject text; intent/notes may be empty/omitted.
- After delete/reorder, **renumber** ranks to a dense 1…N sequence.
- Success toast; do **not** trigger ingest, Cognee, title matching, or wake the overnight process.
- Confirm UI: for `needs_confirm`, show ranked **article title** candidates (`title`, `score`, `path` short, `match_tier`); operator **multi-selects** which whole articles to prioritize. Confirm writes one resolved record per chosen article (`match_reason: user_confirm`); subject tracks selected articles until all are done or user dismisses. Skip marks `skipped` (no auto-enqueue of leftover candidates).

### serve.py extensions (Build1)

Add GET / POST / PATCH / DELETE (and/or PUT) handlers under `/api/wiki/*` that only touch:

- checkpoint file (status merge — read)
- `I:\EMPIRE_DATA\wiki-reports\{year}\*` (including `priority_resolved.jsonl` cancel-on-delete when `ingest_status: awaiting`, `priority_resolution.json`)
- `%LOCALAPPDATA%\EMPIRE\priority_subjects.json` (**primary write target for planning**)

Bind remains `127.0.0.1:8080`. Path traversal rejected (`year` must match `^\d{4}$`). **No Cognee, no Postgres, no `wiki_ingest` process interaction** from these handlers. Writing the subject queue during INGEST is explicitly allowed and must remain a KB-scale atomic file replace.

---

## 5. Scripts (export report, maintenance, scheduler)

### New / extended scripts

| Script | Role |
|--------|------|
| `scripts/export-wiki-report.ps1` | Thin wrapper → `python -m pipeline.wiki_report_export` |
| `pipeline/wiki_report_export.py` | Build `wiki-status.json`, titles JSONL, new-titles, report-meta |
| `pipeline/wiki_priority_resolve.py` | Match raw subjects → wiki MD; write `priority_resolved.jsonl` + resolution summary |
| `scripts/wiki-maintenance.ps1` | Gate → ANALYZE/VACUUM → export report → **resolve subjects** → mark complete; optional Codex seed step (§6.7) |
| `scripts/seed-priority-subjects-from-codex.ps1` | One-shot (or maintenance hook): parse Codex MD → append pending subjects (§6.7); **no** Wikipedia ingest |
| `scripts/wiki-ops-orchestrator.ps1` | v2: loop ingest(23h) → maintenance → optional restart |
| `scripts/start-wiki-ingest-overnight.ps1` | Extend: `-MaxHours 23`; on start **drain priority_resolved first**, then linear checkpoint; on exit write stop snapshot |

### `export-wiki-report` CLI

```powershell
.\venv\Scripts\python.exe -m pipeline.wiki_report_export `
  --year 2017 `
  --wiki-md-root D:\wiki_md `
  --out-root I:\EMPIRE_DATA\wiki-reports `
  --rebuild-titles
```

Flags:

| Flag | Default | Meaning |
|------|---------|---------|
| `--rebuild-titles` | on in maintenance wrapper | Full titles rebuild |
| `--skip-titles` | off | Status-only (faster; UI titles stale) |
| `--readonly-pg` | off | Enable PG title fallback |
| `--corpus-total` | 5347264 for 2017 | Override constant |

### `wiki-maintenance.ps1`

```powershell
.\scripts\wiki-maintenance.ps1 -Year 2017
# optional:
.\scripts\wiki-maintenance.ps1 -Year 2017 -SkipVacuum -SkipAnalyze -SkipPriorityResolve
```

Steps as in §2. Writes maintenance + priorities blocks into `wiki-status.json`. Duration unbounded; logs to `I:\EMPIRE_DATA\logs\wiki-maintenance-{year}-{timestamp}.log`.

Postgres connection: reuse `config/cognee.env` / Docker `empire-cognee-postgres` credentials already used by the stack. If Postgres is down, log warn, skip VACUUM/ANALYZE, still build MD-based reports and still run subject resolution against titles/MD (no Cognee required for matching).

`-SkipPriorityResolve` is for emergency/maintenance debugging; default is **resolve on**.

### Orchestrator (v2)

`scripts/wiki-ops-orchestrator.ps1`:

```powershell
.\scripts\wiki-ops-orchestrator.ps1 -Year 2017 -MaxHours 23 -AutoRestartIngest
```

Loop:

1. Start overnight with `-MaxHours 23` (wait for process exit).
2. Run `wiki-maintenance.ps1`.
3. If `docs_processed >= corpus_total` → exit 0 (“corpus complete”).
4. If `-AutoRestartIngest` → goto 1; else exit 0.

Build1 ships export + maintenance (**including subject resolve**) + UI + overnight priority drain; orchestrator can exist as a stub that only documents the loop, or full script deferred to v2 (§8).

### Manual Build1 operator flow

```powershell
# Terminal A — ingest window
.\scripts\start-wiki-ingest-overnight.ps1 -Year 2017 -FileLimit 200 -MaxHours 23 -FlushEvery 50

# After clean stop — Terminal B
.\scripts\wiki-maintenance.ps1 -Year 2017

# UI
.\scripts\start-frontend.ps1
# open http://127.0.0.1:8080/wiki.html
```

---

## 6. Priority subjects → maintenance resolve → front-of-queue ingest

### Matching mental model

You type **subjects** (topics you care about). The system does **not** hunt for that word inside article bodies. It looks for likely **Wikipedia page titles** (whole articles / `*.md` files). When several titles look plausible, **you confirm** which page(s) you want. Only those **full articles** jump to the front of the next ingest window. Tracking and ingest are always **per article** (title / path / page_id) — never per keyword occurrence in text.

```text
You ask for subjects  →  system finds likely page titles  →  you confirm  →  full articles jump the queue
```

### Design intent

Wikipedia ingest units are **articles** (one page title ↔ one MD file under `D:\wiki_md\{year}\…`). The user thinks in **subjects** (“Cambrai”, “guitar”, “tank warfare WWI”) — free-text **search intents**, not ingest JSON and not a promise to scrape every page that mentions a word. The UI is a **ranked list queue**: plan and reorder anytime (even overnight); wrong titles / missing corpus topics are caught in **maintenance**, not mid-overnight. Resolved **whole articles** jump the line for the **next** 23h window in **subject rank order**; linear batch checkpoint continues afterward.

One subject can resolve to **0..N selected articles**. The subject row stays until the operator **dismisses** it or **all selected articles** are done (ingested / skipped_already_done). Progress and the front queue are keyed by **article identity** (`page_id` / `path` / `title`), not by counting subject-keyword hits.

### Decision: file + `serve.py` ONLY for v1 (PocketBase deferred)

**v1 scope lock:** the priority / subject queue is **file-based + `serve.py` only**. Do not introduce PocketBase collections, Cognee Postgres tables, or any other store for priorities in Build1 / v1.

**Choice:**

| Layer | Path | Who writes | When |
|-------|------|------------|------|
| Ranked raw subjects (search intents) | `%LOCALAPPDATA%\EMPIRE\priority_subjects.json` | UI via `serve.py` GET/POST/PATCH/DELETE and/or single **PUT** of full ordered list | **Anytime** — including during INGEST |
| Resolved front queue (whole articles) | `I:\EMPIRE_DATA\wiki-reports\{year}\priority_resolved.jsonl` | Maintenance resolver (producer); UI confirm (producer per pick); UI delete may cancel `awaiting` lines only | Resolve in MAINTENANCE; confirm anytime after; cancel-on-delete anytime if not started |
| Resolution summary | `I:\EMPIRE_DATA\wiki-reports\{year}\priority_resolution.json` | Maintenance resolver | MAINTENANCE only |

**Isolation (must):** Writing `priority_subjects.json` is a tiny local atomic replace. It **MUST NOT** touch Cognee, Postgres ingest, or the overnight / `wiki_ingest` process. Zero impact on overnight speed beyond that KB-scale write.

**Justification:** agents already read `%LOCALAPPDATA%\EMPIRE\`; heavy/path-heavy resolved rows stay on `I:`. **PocketBase `wiki_priorities` is explicitly out of v1** — a **future optional** (v2+) mirror/store if richer forms are needed later. Cognee Postgres is never the queue.

Env overrides: `EMPIRE_PRIORITY_SUBJECTS`, `EMPIRE_PRIORITY_RESOLVED` (optional).

### 6.1 Ranked subject queue schema

`priority_subjects.json` is an **ordered ranked queue**. Array order **is** rank order (index 0 = rank 1). The `rank` field mirrors position for clarity and API convenience; after every mutation, rewrite dense ranks `1…N`.

```json
{
  "schema_version": 2,
  "updated_at": "2026-07-24T12:00:00Z",
  "updated_by": "wiki.html",
  "year_hint": "2017",
  "notes": "Optional free text for the whole queue (operator memo)",
  "subjects": [
    {
      "id": "subj_001",
      "rank": 1,
      "subject": "Battle of Cambrai",
      "intent": "Truth-Drift demo",
      "added_at": "2026-07-24T12:00:00Z",
      "status": "pending",
      "candidates": [],
      "selected_articles": [],
      "resolved": null,
      "suggestions": []
    },
    {
      "id": "subj_002",
      "rank": 2,
      "subject": "guitar",
      "intent": "Example ambiguous topic; cross-domain why TBD",
      "added_at": "2026-07-24T12:05:00Z",
      "status": "needs_confirm",
      "candidates": [
        {"title": "Guitar", "path": "D:\\\\wiki_md\\\\2017\\\\batch_00042\\\\Guitar.md", "page_id": "123", "score": 1.0, "match_tier": "exact"},
        {"title": "Guitar Hero", "path": "D:\\\\wiki_md\\\\2017\\\\batch_00042\\\\Guitar_Hero.md", "page_id": "456", "score": 0.82, "match_tier": "starts_with"},
        {"title": "Bass guitar", "path": "D:\\\\wiki_md\\\\2017\\\\batch_00007\\\\Bass_guitar.md", "page_id": "789", "score": 0.72, "match_tier": "contains"}
      ],
      "selected_articles": [],
      "resolved": null,
      "suggestions": []
    },
    {
      "id": "subj_003",
      "rank": 3,
      "subject": "The Reinforcing Loop",
      "intent": "codex_primitive | I. CYBERNETICS & SYSTEM DYNAMICS (Feedback & Flow)",
      "added_at": "2026-07-24T12:10:00Z",
      "status": "pending",
      "candidates": [],
      "selected_articles": [],
      "resolved": null,
      "suggestions": []
    }
  ]
}
```

| Field | Rules |
|-------|-------|
| `subjects[]` order | Canonical rank order; rank 1 is first |
| `subjects[].rank` | Dense integer `1…N`; lower = sooner; **must** match array position after save |
| `subjects[].subject` | Required free text, 1–200 chars — **search intent / topic phrase** used for title matching; not required to be an exact wiki title |
| `subjects[].intent` | Optional free text (recommended ≤ 500 chars) — operator annotation only (e.g. `systems_primitive`, cross-domain why, Codex section). **Shown/editable in `wiki.html`.** **Does not** affect title matching (§6.3). API may accept synonym key `notes` on the subject object and normalize to `intent` on write |
| `subjects[].id` | Stable id (`subj_` + increment) |
| `subjects[].status` | `pending` \| `needs_confirm` \| `queued` \| `resolved_done` \| `unmatched` \| `skipped` |
| `subjects[].candidates` | Filled by resolver when not auto-accepted (top **N**, default **10** article titles) |
| `subjects[].selected_articles` | Operator- or auto-chosen **whole articles** (`title`, `path`, `page_id`, `resolved_id`); 0..N; subject stays until dismiss or all selected are done |
| `subjects[].resolved` | Optional snapshot of the auto-accepted primary (if any); prefer `selected_articles` as canonical |
| `subjects[].suggestions` | Near-miss **titles** when `unmatched` (not body snippets) |
| Max length | 500 subjects in file |

**Legacy alias:** earlier drafts used `subjects[].reason` for the same annotation role. Build1 readers should treat `reason` as a fallback for `intent` when loading older files; writers persist `intent` only. Document-level `notes` (queue memo) remains separate from per-subject `intent`.

**Status lifecycle (article-centric):**

- `pending` → maintenance title-match → `queued` (auto single primary) **or** `needs_confirm` **or** `unmatched` **or** `resolved_done` (already ingested primary).
- `needs_confirm` → user picks 0..N articles → each pick appends a resolved ingest line; subject becomes `queued` while any selected article is still awaiting/in flight; becomes `resolved_done` when **all** selected articles are `ingested` / `skipped_already_done`; or `skipped` if user dismisses with no picks.
- Do **not** clear a subject merely because one of N selected articles finished.

**Example:** 5 subjects ranked 1–5; user deletes rank 3 → remaining renumber to 1–4; move up/down swaps neighbors and renumbers.

**Deprecated:** free-floating `priority: 1–100` default-50 scoring from earlier drafts — Build1 uses **explicit list rank** only. If an old file still has `priority`, migrate by sorting ascending then assigning dense `rank`.

### 6.2 Resolved ingest record schema (front queue)

One UTF-8 JSON object per line in `priority_resolved.jsonl` — **one whole article per line** (never a subject-keyword blob):

```json
{
  "schema_version": 1,
  "id": "res_001",
  "subject_id": "subj_001",
  "subject": "Battle of Cambrai",
  "subject_rank": 1,
  "year": "2017",
  "title": "Cambrai",
  "page_id": "12345",
  "path": "D:\\\\wiki_md\\\\2017\\\\batch_00012\\\\Cambrai.md",
  "batch": "batch_00012",
  "file_index": 4501,
  "match_score": 0.97,
  "match_reason": "exact_normalized_title",
  "queued_at": "2026-07-24T18:18:00Z",
  "ingest_status": "awaiting"
}
```

| Field | Meaning |
|-------|---------|
| `path` | Absolute MD path — required for overnight drain (the **full article** file) |
| `page_id` | From MD frontmatter when present; else empty string — primary article identity with `path`/`title` |
| `title` | Canonical wiki title from frontmatter |
| `subject_rank` | Rank at resolve time (drain order among awaiting) |
| `match_score` | 0.0–1.0 |
| `match_reason` | `exact_normalized_title` \| `alias` \| `title_starts_with` \| `title_contains` \| `user_confirm` |
| `ingest_status` | `awaiting` \| `ingested` \| `skipped_already_done` \| `failed` \| `cancelled` |

**Pipeline contract:** overnight / `wiki_ingest_batch` (or a thin priority preflight) must accept these records and run the **same** remember/embed path as a normal file, then mark `ingest_status: ingested` (atomic rewrite or companion `.done` sidecars — implementer’s choice; prefer rewrite of the single line via temp file for Build1 at small N). Drain order: `ingest_status=awaiting`, sort by `subject_rank` asc then `queued_at` asc. Skip `cancelled`. Deduplicate by article identity (`page_id` or normalized `path`/`title`) so two subjects selecting the same page do not double-drain.

### 6.3 Matching & ambiguity rules (maintenance only)

**Unit of match:** Wikipedia **articles** identified by **page title** (and optional frontmatter redirects/aliases). Ingest always queues the **full MD article**. Subjects are only intents that must resolve to articles.

**Not in v1:** full-text / body search; auto-enqueue of every title that contains a subject token; PocketBase or Postgres as the match store.

#### Worked example: subject `"guitar"`

Fear: “guitar” matches tons of pages. Required behavior:

| Step | Behavior |
|------|----------|
| 1. Match index | Compare subject only to **article titles** (+ optional redirects/aliases in frontmatter). **Do not** search MD bodies. |
| 2. Rank candidates | Prefer **exact title** (casefold) > **title starts-with** > **title token / contains**. Return top **N** (default **10**), e.g. `Guitar`, `Guitar Hero`, `Bass guitar`, … — **candidates only**, not an enqueue list. |
| 3. Auto-queue? | **Only** if there is a high-confidence **single primary** article (exact title, or score ≥ **0.90** with margin rule). Example: exact `Guitar` alone → may auto-queue that **one** full article. |
| 4. Otherwise | Status `needs_confirm` with the candidate list. **Do not** auto-enqueue every title containing “guitar”. |
| 5. User picks | Operator explicitly selects which article(s) to prioritize (0..N). Each pick queues that **full MD article** front-of-line. |
| 6. Tracking | Per **article** (`page_id` / `path` / `title`). Subject `"guitar"` stays until dismissed or all selected articles are done. |

#### Index sources (in order)

1. **Corpus title→path map** (for locating articles to ingest) — prefer a map built in the same maintenance job from `D:\wiki_md\{year}\batch_*` frontmatter `title` (+ `page_id`, and optional `redirects` / `aliases` arrays when present). Build1 may reuse export’s frontmatter reader; a lightweight `title-index.sqlite` / sidecar under `wiki-reports\{year}\` is an allowed optimization so resolve does not re-walk 5M files every night once the index exists.
2. **`titles.jsonl` done-set** (processed catalog) — used to detect **already ingested** matches (`resolved_done` / skip re-add), not as the sole discovery index (it only contains processed titles).
3. Do **not** run corpus walks or title matching during INGEST.
4. Do **not** scan article body text for priority matching in v1.

**Process subjects in rank order (1 first).** Unchanged: matching runs only in maintenance.

**Normalize:** Unicode NFKC, casefold, collapse whitespace. Parenthetical disambiguators on titles may be stripped for secondary scoring only (exact-with-parens still preferred when both sides match).

**Match tiers & scoring (Build1 — title/alias only):**

| Tier / score | Condition | Rank priority |
|--------------|-----------|---------------|
| **exact** — 1.00 | Exact normalized **title** equality (casefold), or exact alias/redirect equality | Highest |
| **exact_stripped** — 0.95 | Exact after stripping trailing `(...)` disambiguator on either side | Next |
| **starts_with** — 0.80–0.94 | Normalized title **starts with** normalized subject (or vice versa when subject is clearly the longer form — prefer title-startswith-subject) | Next |
| **token / contains** — 0.60–0.79 | Subject is a whole token inside the title, or title contains subject as a substring | Lowest eligible |
| below 0.60 | Ignore as candidate | — |

Within a tier, prefer shorter titles, then lexicographic title for stable ordering. Return at most **top N = 10** candidates (configurable `--candidate-limit`).

**Decision rule (clear):**

1. Collect top **N** (default **10**) candidates with score ≥ 0.60 using the tier order above.
2. **Auto-accept exactly one primary article** if:
   - best is **exact** title/alias (score 1.00), **or**
   - best score ≥ **0.90** **and** (only one candidate ≥ 0.60 **or** `(best − second) ≥ 0.05`).
   Write **one** resolved record for that article; set subject `status: queued`; put that article in `selected_articles`.
3. Else if any candidates ≥ 0.60 but rule (2) fails → `status: needs_confirm`, store `candidates` (title, path, page_id, score, match_tier); **do not** enqueue any of them (including all “contains guitar” hits).
4. Else → `status: unmatched`, store `suggestions` (nearest titles); **do not** enqueue.
5. **Already ingested:** if the auto-accepted (or later user-selected) article’s `path` / `page_id` / normalized `title` appears in `titles.jsonl` done-set (or Cognee incremental says present — maintenance-only check), mark that article `skipped_already_done` / do not place on front queue for re-ingest; update subject selected progress; subject → `resolved_done` only when **all** selected articles are done (or auto primary alone was already done).
6. User confirm (`POST .../confirm`): body lists chosen candidate article ids/paths (1..N). Each pick → resolved line with score 1.0 / `match_reason: user_confirm`; append to `selected_articles`; subject `queued` until all selected done. Choosing zero + Skip → `skipped`.

**Forbidden:** auto-enqueue every title containing the subject string. Candidates may *list* many contains-hits; only explicit auto-primary or user picks become ingest rows.

Threshold / limit constants live in resolver config / CLI flags (`--auto-min-score 0.90 --auto-margin 0.05 --candidate-limit 10`); document defaults in ops README.

### 6.4 Ingest restart order

```text
Window start:
  A. While priority_resolved.jsonl has ingest_status=awaiting (stable sort: subject_rank asc, queued_at asc):
        ingest that MD path → mark ingested (or failed)
  B. Resume linear checkpoint (batch_*/next_index) as today
```

- Priority drain is **bounded** by remaining MaxHours like any other work.
- Do not reorder files inside an in-progress linear batch mid-window for new subjects (subjects wait for next maintenance **resolve**; the raw ranked queue may still be edited anytime).
- If a priority path later appears in linear walk, skip via done-set / incremental (same as duplicate protection).

### 6.5 Agent / script handoff contract

1. **Operators / UI** edit the ranked raw subject queue (`priority_subjects.json`) anytime (file + `serve.py` only in v1).
2. **Maintenance resolver** is the sole producer of new ingest-ready JSON from auto-accept (except UI confirm enqueue of 1..N articles and UI cancel of awaiting).
3. **Overnight harness** consumes `priority_resolved.jsonl` at window start (rank order), then checkpoint — each line is one **whole article**.
4. Agents (Eve / Cursor) may:
   - Append / reorder subjects in the raw queue (same schema), or
   - Read resolution summary to explain unmatched / needs_confirm to the user,
   - **Must not** invent paths during ingest; **must not** call Cognee from the browser; **must not** slow overnight by doing resolve work out of band; **must not** treat subjects as body-keyword search.
5. After a subject’s selected articles are all `ingested` / `resolved_done`, agents should prefer leaving historical rows (status) rather than deleting, so the UI can show “recently resolved” — unless the operator explicitly deletes/dismisses.

### 6.6 Edit / delete / reorder rules (anytime planning)

| Action | Effect on `priority_subjects.json` | Effect on `priority_resolved.jsonl` | Status / match fields |
|--------|--------------------------------------|-------------------------------------|------------------------|
| **Add** | Append at end (rank N+1) or insert + renumber | None | `pending`; optional `intent`; clear candidates/selected_articles/resolved/suggestions |
| **Reorder** (move up/down or PUT full list) | Dense renumber 1…N | None (rank at resolve time is snapshotted into `subject_rank` on next maintenance) | Unchanged |
| **Edit subject text** | Update `subject` string | If resolved lines exist for this `subject_id` with `ingest_status: awaiting`, **cancel** them (`cancelled` or remove lines) so stale matches are not ingested | **Reset to `pending`**; clear `candidates`, `selected_articles`, `resolved`, `suggestions` — **unless already consumed this cycle** (see below) |
| **Edit intent / notes only** | Update `intent` (synonym `notes` normalized to `intent`) | None | **Unchanged** status/match fields — annotation only; does not re-trigger matching |
| **Delete / dismiss** | Remove entry; renumber remaining 1…N | If resolved lines for `subject_id` have `ingest_status: awaiting` (not yet started), **remove or mark `cancelled`** so they will not drain | Gone from queue |
| **Confirm picks** | Update `selected_articles`; status `queued` (or `resolved_done` if all already done) | Append one awaiting line **per** chosen article | Does not clear other subjects |

**“Already consumed this cycle” (edit does not reset):**

- All linked resolved records for this subject are `ingested` or `skipped_already_done`, **or**
- subject `status` is `resolved_done` and every selected article was already drained/ingested.

In that case: treat edit as **new planning intent** — Build1 should **fork**: keep the historical row as-is for audit **or** add a **new** `pending` subject with the edited text (prefer: edit creates a new pending entry at the same rank and leaves the consumed row as `resolved_done` history). Do **not** un-ingest from Cognee. Simplest Build1 rule: **if consumed → reject in-place edit with message “already ingested; add a new subject instead”**, or clone-as-new-pending. Document the chosen behavior in UI copy.

**Not yet started** = resolved `ingest_status: awaiting` (and overnight has not begun draining that line). Once drain has marked `ingested` / `failed`, delete of the subject row does not roll back Cognee; only remove from the subject list / leave resolved history. Partial completion (some of N selected articles done): delete still cancels remaining `awaiting` lines only.

### 6.7 Seed from Master Codex (pending subjects only)

**Purpose:** Bootstrap the **new** ranked priority queue from the systems-primitives reference while the operator decides what else to explore. Seeding writes **pending** subjects into `priority_subjects.json` only. It does **not** auto-ingest Wikipedia, does **not** write `priority_resolved.jsonl`, and does **not** bypass resolve + confirm rules in §6.3 / §6.6.

**Seed document path (repo):**

`docs/reference/THE MASTER CODEX! 50 UNIVERSAL PRIMITIVES.md`

**Status as of 2026-07-24 design update:** this file **exists** in the repo. If it is missing at runtime, the seed path must still no-op cleanly — see below.

#### Observed document structure (parse heuristics)

| Layer | Pattern | Example |
|-------|---------|---------|
| Document title | Single `#` H1 | `# THE MASTER CODEX: 50 UNIVERSAL PRIMITIVES` |
| Domain sections | `##` H2 with Roman numeral + theme | `## I. CYBERNETICS & SYSTEM DYNAMICS (Feedback & Flow)` |
| Primitives | Restarting numbered list under each H2: `N. **Name:** rest of line…` | `1. **The Reinforcing Loop:** Output feeds back…` |
| Count | Six H2 sections; ~50 primitives total (lists restart at 1 per section) | I–VI |

**Subject text extraction:**

1. Ignore the H1 and italic blurb lines under H2.
2. Track `current_section` = full H2 heading text (without leading `## `) whenever a `##` line is seen.
3. For each list item matching `^\d+\.\s+\*\*(.+?)\*\*:` (or `^\d+\.\s+\*\*(.+?)\*\*\s*$` if no trailing colon):
   - `subject` = capture group 1 (the bold primitive name), trimmed. Keep parentheticals inside the bold span (e.g. `The Structural Echo (Conway’s Law)`).
   - Do **not** use the prose after the colon as `subject` (that is definition text, not a queue topic).
4. If a future Codex revision uses bare `## Primitive Name` headings instead of numbered bold lists, fall back: treat each `##` that is **not** a Roman-numeral section header as a primitive name, and use the nearest Roman/`I.`–`VI.` ancestor (or `"codex_primitive"`) for intent context.
5. Skip empty captures; skip lines that are only section blurbs (`*italic*`).

**Intent annotation on seeded rows:**

- Default: `intent = "codex_primitive"`.
- Preferred richer form: `intent = "codex_primitive | {current_section}"` (e.g. `codex_primitive | I. CYBERNETICS & SYSTEM DYNAMICS (Feedback & Flow)`).
- Intent is planning metadata only — **never** passed into the title-matching scorer.

**Delivery (either is valid for v1):**

1. **Optional step inside** `scripts/wiki-maintenance.ps1` (e.g. `-SeedCodex` / default-off, or once-flag file), **or**
2. **One-shot script:** `scripts/seed-priority-subjects-from-codex.ps1`

```powershell
.\scripts\seed-priority-subjects-from-codex.ps1
# optional overrides:
.\scripts\seed-priority-subjects-from-codex.ps1 `
  -CodexPath "docs\reference\THE MASTER CODEX! 50 UNIVERSAL PRIMITIVES.md" `
  -SubjectsPath "$env:LOCALAPPDATA\EMPIRE\priority_subjects.json"
```

**Idempotency:**

- Load existing `priority_subjects.json` (create empty ranked queue if missing).
- Normalize existing subject strings (NFKC + casefold + collapse whitespace) into a set.
- For each parsed Codex primitive name, if normalized name is **already** present as any subject’s `subject` text, **skip** (do not duplicate).
- Append new rows at the end as `status: pending` with next ranks; assign new `id`s; set `intent` as above; leave candidates/selected empty.
- Atomic write of the full JSON file (same isolation rules as UI: local file only; no Cognee / Postgres / overnight touch).

**Missing file:**

- If the Codex path does not exist, print a clear message (e.g. `Codex seed skipped: file not found at <path>`) and **exit 0** (no-op). Do not create subjects; do not fail maintenance if invoked as an optional step.

**Explicit non-goals for seed:**

- Does **not** run title matching or produce ingest-ready JSON.
- Does **not** start overnight ingest or place anything on `priority_resolved.jsonl`.
- Wikipedia ingest of seeded topics still requires maintenance resolve → auto-primary or operator confirm per existing rules.

### API bodies

**PUT full ordered list** (simplest Build1):

```json
{
  "year_hint": "2017",
  "notes": "",
  "subjects": [
    { "id": "subj_001", "rank": 1, "subject": "Cambrai", "intent": "Truth-Drift demo", "status": "pending" },
    { "id": "subj_002", "rank": 2, "subject": "Arras", "intent": "", "status": "pending" }
  ]
}
```

**POST add** (append strings or objects):

```json
{ "year_hint": "2017", "notes": "", "subjects": ["Cambrai", "Arras"] }
```

```json
{
  "year_hint": "2017",
  "subjects": [
    { "subject": "The Reinforcing Loop", "intent": "codex_primitive" }
  ]
}
```

Server expands bare strings into objects with `status: "pending"`, next ranks, empty `intent`. Accept optional `intent` or subject-level `notes` (normalize `notes` → `intent`). Reject payloads that include `path` / `page_id` (those belong to the resolved queue, not user input).

**PATCH** `{ "subject": "…" }` and/or `{ "intent": "…" }` / `{ "notes": "…" }` or `{ "rank": 3 }` — apply edit/reset or move rules in §6.6. Intent-only patch does not reset match status.

**DELETE** `/api/wiki/priorities/{id}` — delete + cancel awaiting resolved.

**POST confirm** (multi-article picks):

```json
{
  "subject_id": "subj_002",
  "articles": [
    { "path": "D:\\\\wiki_md\\\\2017\\\\batch_00042\\\\Guitar.md", "title": "Guitar", "page_id": "123" },
    { "path": "D:\\\\wiki_md\\\\2017\\\\batch_00007\\\\Bass_guitar.md", "title": "Bass guitar", "page_id": "789" }
  ]
}
```

Empty `articles` with explicit skip flag → `skipped`. Each listed article becomes one `priority_resolved.jsonl` line (`match_reason: user_confirm`). Subject tracks all picks in `selected_articles`.
---

## 7. Risks / growth

| Risk | Impact | Mitigation |
|------|--------|------------|
| **VACUUM time grows** with DB size | Maintenance gap longer than expected; delays next 23h window | Threshold-gated VACUUM; skip healthy tables; never `VACUUM FULL` by default; log per-table duration; operator `-SkipVacuum` |
| **`titles.jsonl` size** (~5.35M lines) | Disk on `I:`; slow full rebuild; UI must not load entire file | Store on `I:\EMPIRE_DATA\wiki-reports\`; paged API; Build1 full rebuild after window only; later: incremental append + sqlite FTS if needed |
| **Frontmatter parse cost** | Multi-hour title rebuild if naive | Read only YAML header; parallelize carefully without competing with ingest (maintenance-only); cache file mtimes in a sidecache later if needed |
| **Checkpoint vs titles drift** | UI titles count ≠ docs_processed | Status shows both `docs_processed` (checkpoint) and `catalog_lines`; maintenance rebuild aligns them |
| **PID / phase races** | Dashboard shows idle while ingest runs | Prefer live PID check + checkpoint `updated` over stale `phase` |
| **OneDrive / C: pressure** | Accidental write of titles under repo | Hardcode out-root to `I:\EMPIRE_DATA\wiki-reports`; refuse repo-relative heavy paths |
| **Subject not in corpus / wrong title** | User expects overnight to ingest a topic that does not exist | Maintenance marks `unmatched` + title suggestions; UI shows it; nothing wrong enters the ingest JSON queue |
| **Ambiguous subject (e.g. “guitar”)** | Fear of auto-ingesting dozens of related titles | Title-only match; top-N candidates; auto-queue **single** high-confidence primary only; else `needs_confirm`; **never** auto-enqueue all contains-hits |
| **Body / full-text search creep** | Wrong articles, huge false positives | v1 explicitly forbids body search; titles + optional aliases only |
| **Priority drain vs linear fairness** | Many priorities starve batch progress | Cap optional later (`MaxPriorityPerWindow`); Build1 drains all awaiting then continues linear within MaxHours |
| **Resolver cost** | Title index for matching slows maintenance | Reuse titles rebuild path map; no matching during ingest; `-SkipPriorityResolve` escape hatch |
| **Stale resolved after edit/delete** | Edited/deleted subject still drains old match | On edit/delete: cancel `awaiting` resolved lines for that `subject_id`; overnight skips `cancelled` |
| **Edit after already ingested** | Operator tries to “change” a consumed subject | §6.6 consumed rule — reject in-place reset or clone-as-new-pending; never un-ingest Cognee |
| **Queue write during ingest** | Fear of slowing overnight | Explicit isolation: KB-scale `priority_subjects.json` only; no Cognee/PG/`wiki_ingest` touch; zero meaningful speed impact |
| **Concurrent PUT races** | Two tabs overwrite ranks | Atomic replace + `updated_at`; last-write-wins Build1; optional If-Match later |
| **PocketBase / PG queue drift** | Accidental dual stores | **v1 scope lock:** file + `serve.py` only; PocketBase deferred optional; no Cognee Postgres queue |
| **Codex seed mistaken for ingest** | Operator expects seeded primitives to jump overnight queue immediately | Seed only writes `pending` subjects + `intent`; matching/confirm still required; copy in script/UI must say “queue planning only” |

### Growth ceilings (design targets)

| Artifact | 2017 full corpus estimate | Action if exceeded |
|----------|---------------------------|--------------------|
| `titles.jsonl` | ~400–800 MB (title + short path) | Split per-batch JSONL under `titles.d/`; UI concatenates via API |
| Maintenance title rebuild | Possibly 1–3+ hours at full scale | Run only on completed batches since last export; ship incremental in v1.1 if rebuild > 30 min observed |
| `new-titles.jsonl` | Typically ≪ full catalog | Cap UI default page 100; file can be large after first run (first run = all titles “new”) — on first run set `new_titles_count` but UI may show “First catalog: N titles (all new)” and sample first 500 |
| `priority_subjects.json` | ≪ 1 MB at 500 entries | Keep under LOCALAPPDATA; never on ingest critical path |

---

## 8. Implementation phases

### v1 (Build1) — metrics + new titles + subject queue + maintenance resolve (preferred)

**v1 scope lock — priorities:** `priority_subjects.json` + `serve.py` **only**. No PocketBase for priorities. No Cognee Postgres for the queue. PocketBase is a **future optional** (v2+), not a Build1 deliverable.

**Ship:**

1. `pipeline/wiki_report_export.py` + `scripts/export-wiki-report.ps1`
2. `scripts/wiki-maintenance.ps1` (ANALYZE/VACUUM + export + **priority subject resolve**; until done)
3. `pipeline/wiki_priority_resolve.py` — pending subjects → **title/alias match** (no body search) → auto single primary or `needs_confirm` top-N → `priority_resolved.jsonl` / status updates (§6)
4. Overnight: stop snapshot into `wiki-status.json`; document `-MaxHours 23`; **on start drain `priority_resolved` then linear checkpoint**
5. `frontend/wiki.html` + nav link — **ranked subject queue** UI (rank #, subject, **intent/notes**, status; add / edit / delete / move up / move down); needs_confirm multi-select / unmatched / newly resolved panels; HTMX + Alpine + Pico
6. `serve.py` routes: status, titles (paged), new-titles (paged), priorities GET + POST/PATCH/DELETE and/or PUT full ordered list, priorities confirm POST (1..N articles) — subject-file writes allowed during ingest; no Cognee/PG/`wiki_ingest` touch
7. Spec/docs cross-link from `docs/WIKI_INGEST_OVERNIGHT.md` (short “Ops dashboard” section)
8. Codex seed (§6.7): `scripts/seed-priority-subjects-from-codex.ps1` and/or optional maintenance `-SeedCodex` — append pending primitives from `docs/reference/THE MASTER CODEX! 50 UNIVERSAL PRIMITIVES.md`; idempotent; missing-file no-op; **no** auto Wikipedia ingest

**Prefer include resolver in v1 maintenance** because subject UX without resolve still leaves users typing titles/JSON by hand. If schedule pressure forces a split:

| Slice | Contents |
|-------|----------|
| **v1** (minimum) | Reports, UI metrics/New, ranked subject CRUD/reorder (**local JSON + serve.py only**) |
| **v1.1** (immediate follow) | Resolver + overnight priority drain + multi-select confirm UI |

Do **not** ship v1 UI copy that promises “next window will ingest these” unless resolve+drain are present.

**Explicitly out of v1:** auto-restart orchestrator loop, **PocketBase priorities**, Cognee Postgres queue, PG-required title build, Cognee from browser, matching during ingest, **full-text body search**, **auto-enqueue all title contains-hits**, drag-and-drop reorder (buttons suffice).

### v2 — auto-restart scheduler

1. `scripts/wiki-ops-orchestrator.ps1` with `-AutoRestartIngest` (maintenance includes resolve; restart already drains priorities first)
2. Stronger phase locking (single `wiki-ops.lock` under `%LOCALAPPDATA%\EMPIRE`)
3. Optional incremental titles append
4. Optional mirror of subject queue into PocketBase `wiki_priorities` for richer forms (**first time PocketBase may enter priorities** — still optional)
5. Dashboard badge on main `dashboard.html` linking wiki phase (read-only status file)
6. Optional `MaxPriorityPerWindow` fairness cap

### Acceptance checks (v1)

- After a short ingest (`-MaxHours 0.05` or small `-MaxSlices`), stop snapshot exists and `docs_processed` matches checkpoint sum.
- `wiki-maintenance.ps1` produces `titles.jsonl`, `new-titles.json`, updated `wiki-status.json` with `maintenance.complete: true`, and runs subject resolution (unless `-SkipPriorityResolve`).
- Subject “Cambrai” (or fixture title) with a real MD match becomes a line in `priority_resolved.jsonl` with path/title/score; next overnight start ingests that path **before** advancing linear checkpoint.
- Resolver processes subjects in **rank order** (rank 1 before rank 2).
- Ambiguous subject (e.g. `"guitar"`) stays `needs_confirm` with top-N **title** candidates; does **not** auto-enqueue every contains-hit; confirm endpoint enqueues **only** chosen article path(s) (multi-select allowed).
- Matching uses title/alias only — no body search in v1.
- Unmatched subject stays `unmatched` with title suggestions; already-ingested selected article → skip re-queue; subject `resolved_done` only when all selected articles are done (or dismissed).
- `wiki.html` shows count, percent of 5,347,264, New list, and ranked priority queue (rank #, subject, **intent/notes**, status) with add / edit / delete / move up / move down; saves to `%LOCALAPPDATA%\EMPIRE\priority_subjects.json` via serve.py (**no PocketBase**).
- Editing intent/notes alone does not reset match status; editing subject text still resets non-consumed entries per §6.6.
- Codex seed script (or maintenance `-SeedCodex`) appends pending subjects from the Master Codex when present; skips duplicates; no-ops with a clear message if the file is missing; does **not** write `priority_resolved.jsonl` or start ingest.
- While overnight PID is alive: add/edit/delete/reorder subjects succeeds; no Cognee/Postgres/`wiki_ingest` calls from those requests; ingest throughput unaffected beyond tiny JSON write.
- Edit of non-consumed subject → `pending` + cleared match; delete of subject with `awaiting` resolved line → cancelled/removed from resolved queue.
- No Cognee HTTP from browser network tab; no postgres-mcp dependency for the UI path; no resolve/title build while overnight PID is alive.

---

## Appendix A — Constants cheat sheet

| Name | Value |
|------|-------|
| Default year | `2017` |
| Corpus total 2017 | `5347264` |
| Batches 2017 | `535` (`batch_00000` … `batch_00534`) |
| Ingest `MaxHours` | `23` |
| Wiki MD root | `D:\wiki_md` |
| Reports root | `I:\EMPIRE_DATA\wiki-reports` |
| Checkpoint | `%LOCALAPPDATA%\EMPIRE\wiki-checkpoint.json` |
| Priorities (ranked raw subjects) | `%LOCALAPPDATA%\EMPIRE\priority_subjects.json` (**v1 store — file only**) |
| Priorities (resolved queue) | `I:\EMPIRE_DATA\wiki-reports\{year}\priority_resolved.jsonl` |
| Match surface (v1) | Article titles + optional frontmatter aliases/redirects (**not** body text) |
| Per-subject annotation | Optional `intent` (API synonym `notes`); ignored by matcher |
| Codex seed source | `docs/reference/THE MASTER CODEX! 50 UNIVERSAL PRIMITIVES.md` |
| Candidate limit | top **10** |
| Auto-match threshold | exact **or** score ≥ 0.90 and margin ≥ 0.05 (single primary only) |
| Frontend | `http://127.0.0.1:8080/wiki.html` |

## Appendix B — Related existing pieces

- `docs/WIKI_INGEST_OVERNIGHT.md` — overnight ops, Fast Mode, VACUUM notes
- `scripts/start-wiki-ingest-overnight.ps1` — ingest harness to extend
- `pipeline/wiki_checkpoint.py` — checkpoint IO
- `pipeline/wiki_normalizer.py` — frontmatter `title` parsing (reuse for catalog + resolver)
- `pipeline/wiki_priority_resolve.py` — subject→MD resolve (new; maintenance only; title/alias match)
- `scripts/seed-priority-subjects-from-codex.ps1` — optional Codex → pending subjects seed (§6.7; new)
- `frontend/serve.py` / `dashboard.html` — control API + Pico/Alpine patterns
- `docs/reference/THE MASTER CODEX! 50 UNIVERSAL PRIMITIVES.md` — seed source (## sections + numbered `N. **Name:**` lists)
