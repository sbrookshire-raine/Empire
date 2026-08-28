# Wikipedia → Cognee overnight ingestion

Resumable batch infrastructure for harnessing the full Wikipedia Markdown corpus on `D:\wiki_md`
into Cognee graph memory on `V:\Cognee`, with Truth-Drift snapshot-year isolation.

## Data layout

| Path | Contents |
|------|----------|
| `D:\wiki_md\2017\batch_*` | 2017 snapshot (~5.35M articles, 535 batches × 10k) |
| `D:\wiki_md\2021\batch_*` | 2021 snapshot (~6.3M articles, 126 batches × 50k) |
| `D:\wiki_md\2026\batch_*` | 2026 snapshot (~7.1M articles, 143 batches × 50k) |
| `V:\Cognee` | Cognee graph + LanceDB + Kuzu (NTFS VHDX on `I:\EMPIRE_VHDX`) |
| `%LOCALAPPDATA%\EMPIRE\wiki-checkpoint.json` | Per-batch resume index |
| `%LOCALAPPDATA%\EMPIRE\cognee.lock` | Cross-process lock (MCP + CLI) |
| `I:\EMPIRE_DATA\logs\` | Overnight logs, PIDs, convert status |

## Truth Drift design

Each article becomes a **snapshot-scoped node**: `Title (YEAR)` with explicit edges:

- `{Title} ({YEAR}) snapshot_year {YEAR}`
- `{Title} ({YEAR}) is_snapshot_of {Title}`

Datasets are year-scoped: `wikipedia_2017`, `wikipedia_2021`, `wikipedia_2026`. Cross-year
queries use `wiki_recall` with `dataset=""` to search all snapshots.

## Fast Mode pipeline (default overnight)

1. **remember** — `cognee.add` only (Truth-Drift edges already in normalized text)
2. **embed_dataset** — classify → chunk → nomic-embed-text vectors (no llama)

**Do not** run per-slice `cognify` / `improve` in Fast Mode. Full Mode (`--mode full`) adds
llama3.1 graph extract + memify for spot checks only.

## Throughput (observed Jul 2026, RTX 5080 16GB, nomic-only Fast Mode)

| Metric | Value |
|--------|-------|
| FileLimit 30 slice | ~150–170 s (~0.18–0.20 docs/s, ~5.1–5.7 s/doc) |
| FileLimit 150 slice | ~614 s (**0.24 docs/s**, **4.1 s/doc**) — better amortization |
| Dominant cost | serial `cognee.add` + end-of-slice embed |
| VRAM (nomic pinned, no llama) | ~7 / 16 GB — headroom for embed batch knobs |

### Safe knobs (5080 / 64GB class — Just Postgres)

| Knob | Recommended | Notes |
|------|-------------|-------|
| `FileLimit` | **200** | Larger slices amortize embed startup |
| `FlushEvery` | **50** | Checkpoint window; normalize+remember run concurrent inside window |
| `EMPIRE_REMEMBER_CONCURRENCY` | **20** | Cap for in-flight remember docs (pool 24) |
| `EMPIRE_REMEMBER_DATA_PER_BATCH` | **16** | Wired to Cognee `add(..., data_per_batch=)`; list-batches when >1 |
| `EMBEDDING_BATCH_SIZE` | **512** | nomic-only ~3GB VRAM; drop to 384 if embed slows |
| `EMPIRE_EMBED_DATA_PER_BATCH` | **16** | Keep aligned with `OLLAMA_NUM_PARALLEL=8` (higher mostly queues) |
| `POOL_ARGS` | pool_size/max_overflow **24** | Modest bump for rememberConc=20 ([PR #2234](https://github.com/topoteretes/cognee/pull/2234)) |
| `EMPIRE_QUIET_COGNEE` | **1** | Drop Cognee INFO spam; keep `[wiki]` progress |
| `OLLAMA_NUM_PARALLEL` | **8** (on **ollama serve**) | Must be on serve PID — `ensure-ollama-parallel.ps1` verifies/skips restart |

### Speed tuning (Jul 2026 overnight prep)

**Postgres maintenance (idle ingest):** `ANALYZE` all public (~3.3s) then `VACUUM (ANALYZE)` on hot tables
(`data`, `graph_node`, `graph_edge`, `DocumentChunk_text`, `EdgeType_relationship_name`,
`pipeline_runs`, `TextDocument_name`, `dataset_data`, …). Notable: `public.data` had
~3033 dead tuples (~11.5% of live) → **0** after VACUUM; table sizes unchanged (~22 MB `data`,
~1.4 GB `DocumentChunk_text`). No `VACUUM FULL`. Expect planner + dead-tuple cleanup to
help remember degradation as the store grows; re-run VACUUM between long overnight legs if
`n_dead_tup` on `data` climbs again.

**Ollama parallel:** Live `ollama serve` PID already had `OLLAMA_NUM_PARALLEL=8` (verified via
process env). `ensure-ollama-parallel.ps1` now **skips restart** when the value matches
(keeps nomic pin). `EMPIRE_OVERNIGHT_PIN_LLAMA` unset; `ollama ps` showed nomic-only.

**Code fix:** `pipeline/cognee_client.py` `remember_many` no longer hardcodes
`data_per_batch=1` while env claimed 16 — list-batches through Cognee when
`EMPIRE_REMEMBER_DATA_PER_BATCH>1`.

### Watch live

```powershell
.\scripts\watch-wiki-ingest.ps1
```

Compares checkpoint vs Postgres `data` / `DocumentChunk_text` counts. If `data` grows but chunks stall, embed is skipping (see pipeline-cache note below).

### Pipeline-cache footgun (Cognee 1.x)

`use_pipeline_cache=True` marks the whole dataset COMPLETED after the first embed pass and
skips later slices ([qualification layer](https://github.com/topoteretes/cognee)). EMPIRE sets
`use_pipeline_cache=False` and keeps `incremental_loading=True` so new `cognee.add` rows still
get chunked/embedded.

### Just Postgres backend

Upstream reference for Postgres/pgvector/graph wiring and issues:
https://github.com/topoteretes/cognee

Local Docker Compose (`docker-compose.yml`) runs `pgvector/pgvector:pg16` as `empire-cognee-postgres`
on port **5432** (`cognee` / `cognee` / `cognee_db`). Env wiring lives in `config/cognee.env` and
`cognee/.env`. Cross-process `cognee.lock` is skipped (`EMPIRE_COGNEE_SKIP_FILE_LOCK=1`).

```powershell
docker compose up -d
docker compose ps
```

**Note:** Postgres is a fresh store — prior SQLite/Kuzu data on `V:\Cognee` is not auto-migrated.
Wiki checkpoint (`next_index`) still resumes file offsets; re-ingest into the new DB as needed.

### Unsafe / avoided

- Re-enabling per-slice llama cognify in Fast Mode
- Running Cognee MCP tools against a different backend while overnight writes to Postgres without care
- Leaving `GRAPH_DATABASE_PROVIDER=postgres` unset while still on a pre-1.0 Cognee (EMPIRE pins `cognee[postgres-binary]>=1.0`)

### Known footgun: `pipeline_runs.id = inf`

A corrupt SQLite UUID (`id` stored as float `inf`) makes every later `cognee.add` fail with
`'float' object has no attribute 'replace'`. EMPIRE auto-deletes such rows on Cognee env load.
If overnight stops with that error, check checkpoint `next_index` (skip-forward may have
advanced past a good resume point) and resume from the last successful slice end.

## Recommended overnight limits

| Parameter | Recommended | Rationale |
|-----------|-------------|-----------|
| `--limit` / `-FileLimit` | **200** | Fast Mode; amortize embed (~150 was prior) |
| Max slices/night | **300** | Wall-clock capped by `-MaxHours` (**23h** default for future runs) |
| `--flush-every` | **50** | Checkpoint + remember flush cadence |
| Mode | **fast** | remember + nomic embed only |
| Parallel years | **1 primary** | Avoid lock contention |

## Commands

### Detached Cursor-safe launch (breakaway + live console)

Prefer the wrapper (avoids Windows `start` title-quoting traps):

```bat
scripts\launch-wiki-ingest-overnight.cmd
scripts\launch-wiki-ingest-overnight.cmd 2017 200 300 23 50
```

Or from **cmd.exe** directly — the first quoted string is the **window title**, not a program:

```bat
start "EMPIRE-wiki-2017" /MIN powershell.exe -NoProfile -ExecutionPolicy Bypass -File C:\EMPIRE\scripts\start-wiki-ingest-overnight.ps1 -Year 2017 -FileLimit 200 -MaxSlices 300 -MaxHours 23 -FlushEvery 50
```

**Wrong** (produces `The system cannot find the file EMPIRE-wiki-2017.`):

```bat
cmd /c start "EMPIRE-wiki-2017" /MIN cmd /c "powershell ... -Year 2017 ..."
```

`/MIN` keeps a taskbar window. The harness **live-tees** high-signal `[wiki]` lines (slice
start/end, docs/s, checkpoint idx) to the console and appends the full stream to the log.
Omit `/MIN` for a full-size window. Parent breakaway keeps the job alive if Cursor exits.

### Foreground (same script)

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File "C:\EMPIRE\scripts\start-wiki-ingest-overnight.ps1" `
  -Year 2017 -FileLimit 200 -MaxSlices 300 -MaxHours 23 -FlushEvery 50
```

## Ops dashboard (Wiki Ops v1)

Local HTMX/Alpine/Pico UI for checkpoint progress, title browse/new-titles, and a ranked
**priority subject queue** (planning anytime — including while overnight runs).

| Item | Value |
|------|-------|
| UI | http://127.0.0.1:8080/wiki.html |
| Subject queue | `%LOCALAPPDATA%\EMPIRE\priority_subjects.json` |
| Reports | `I:\EMPIRE_DATA\wiki-reports\{year}\` |
| Design spec | [docs/superpowers/specs/2026-07-24-wiki-ops-dashboard-design.md](superpowers/specs/2026-07-24-wiki-ops-dashboard-design.md) |
| Default `MaxHours` | **23** (applies to **future** overnight launches; do not restart a live run) |

```powershell
# Frontend
.\scripts\start-frontend.ps1

# Seed Master Codex primitives into the subject queue (idempotent; planning only)
.\scripts\seed-priority-subjects-from-codex.ps1

# After overnight PID stops — ANALYZE/VACUUM + titles rebuild + subject resolve
.\scripts\wiki-maintenance.ps1 -Year 2017
```

While overnight is alive, maintenance **refuses** (no VACUUM). Status-only export is safe anytime:

```powershell
.\scripts\export-wiki-report.ps1 -Year 2017 -SkipTitles
```

### Manual single slice

```powershell
cd C:\EMPIRE
$env:PYTHONPATH = (Get-Location).Path
.\venv\Scripts\python.exe -m pipeline.wiki_ingest --year 2017 --batch 0 --mode fast --limit 200 --flush-every 50
```

### Check progress

```powershell
Get-Content "$env:LOCALAPPDATA\EMPIRE\wiki-checkpoint.json" | ConvertFrom-Json | ConvertTo-Json -Depth 5
Get-Content "I:\EMPIRE_DATA\logs\wiki-ingest-overnight-2017-*.log" -Tail 40
```

### Cross-year recall (Truth Drift proof)

```powershell
.\venv\Scripts\python.exe -m pipeline.cognee_worker recall --query "Cambrai snapshot_year"
```

## MCP tools (Cursor mid-conversation)

Registered in `mcp/wiki_mcp.py` (empire-wiki):

| Tool | Purpose |
|------|---------|
| `wiki_ingest_batch` | Ingest one `D:\wiki_md\{year}\batch_{n}` slice |
| `wiki_ingest_status` | Read checkpoint JSON |
| `wiki_recall` | Query graph (`dataset=""` for cross-year) |
| `wiki_ingest_export_dir` | Weaviate staging (heist stopped; partial at `I:\EMPIRE_DATA\weaviate_dump\2017\`) |

## Preflight checklist

1. **V: mounted** — `Test-Path V:\Cognee` (see `docs\COGNEE_VHDX.md`, `scripts\mount-cognee-vhdx.ps1`)
2. **Ollama** — `ollama serve` on `:11434`; Fast Mode needs `nomic-embed-text:latest` (llama only for full mode)
3. **PocketBase** — `.\scripts\start-pocketbase-background.ps1` (batch job logging)
4. **No lock contention** — kill stray `cognee_worker recall` processes before ingest
5. **Convert complete** — `D:\wiki_md\2017` has 535 `batch_*` dirs (5,347,264 files as of Jul 2026)

## Logs and PIDs

| File | Purpose |
|------|---------|
| `I:\EMPIRE_DATA\logs\wiki-ingest-overnight-{year}-{timestamp}.log` | Main overnight log |
| `I:\EMPIRE_DATA\logs\wiki-ingest-overnight-{year}.pid` | Active run PID |
| `I:\EMPIRE_DATA\logs\wiki-convert-2017.log` | XML→MD convert completion record |

## Scale path (beyond overnight)

1. **Continue 2017** — `batch_00000` → `batch_00534` via checkpoint resume
2. **2021 / 2026** — same pipeline, datasets `wikipedia_2021` / `wikipedia_2026`
3. **Weaviate export** — optional supplement from `I:\EMPIRE_DATA\weaviate_dump\2017\` (50 chunks piloted)
4. **Hardware** — faster embed path / dedicated ingest host; cognify remains optional offline
5. **Parallelism** — separate Cognee roots per year (future); current design is single-writer lock

## Do NOT

- Run `--limit 0` on millions without checkpointing
- Store heavy data on `C:` or exFAT `I:` (Cognee DB must stay on `V:`)
- Delete `I:\EMPIRE_DATA\weaviate_dump` or `D:\wiki_md`
- Launch multiple concurrent wiki ingests (cognee.lock serializes access)
- Re-enable llama cognify inside Fast Mode overnight loops
