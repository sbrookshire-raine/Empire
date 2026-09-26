# EMPIRE operating contract

**Single source of truth for how EMPIRE runs.** Measurement: `python scripts/audit-empire.py`
(exit 0 = contract satisfied; `--json` for machines, `--write` to record a dated snapshot in
`docs/audits/`). If this document and that script ever disagree, one of them is wrong — fix both and
say which changed. Readings below were taken **2026-09-26**.

## 1. Services and ports

| Service | Port | Health probe | Started by |
|---|---|---|---|
| Eve Workbench (frontend + memory API) | 8080 | `/api/memory/status` | `start-stack.ps1` → `venv\Scripts\python.exe -m frontend.serve` |
| Eve agent runtime | 2000 | `/eve/v1/info` | `start-stack.ps1` → `npm exec -- eve start` |
| PocketBase (tasks) | 8090 | `/api/health` | `start-stack.ps1` → `backend\pocketbase\pocketbase.exe` |
| Ollama (inference) | 11434 | `/api/tags`, `/api/ps` | `launch-empire.ps1` → `ollama serve` |
| Speaches (voice, CPU) | 8000 | `/health` | `start-voice.ps1` (container `empire-speaches`) |
| Docker/WSL relay | 8888 | — | Docker Desktop |

Containers: `empire-cognee-postgres` (healthy), `empire-searxng`, `empire-speaches`. Postgres comes up
via `ensure-cognee-postgres.ps1` (starts Docker Desktop if the engine is down).

## 2. Start order and startup budget

Dependencies are real, not conventional: **V:\Cognee → Docker engine → Postgres → Ollama →** then the
independent legs **launch together** (PocketBase, frontend, Eve build check, voice container) and are
awaited in a second pass. That parallelism is what moved cold start from 75 s to:

| Reading | Value |
|---|---|
| Cold start, Docker already up | **25.4 s wall / `Startup: 19.5s`** |
| Cold start including Docker Desktop boot | 42.1 s wall / 33.1 s |
| Threshold | all six services healthy, nothing started twice, ≤ 60 s |

## 3. Model placement — authoritative spec

| Setting | Value | Why |
|---|---|---|
| Context | **24576** | E-41 promotion; verified at her runtime (`contextWindowTokens`) as well as `/api/ps` |
| KV cache | **q8_0** | E-39, A/B-tested against f16 (`eve-audit/ab-toolcalling-*.json`) |
| Flash attention | **on** | required by q8_0 KV at this context |
| `OLLAMA_NUM_PARALLEL` | **1** | one interactive chat model owns the GPU |
| Measured footprint | **10.5 GB VRAM** at 24,576 | `PLACEMENT.md` records 11.3 GB for this row |
| Idle | **0 GB** — no model resident between turns | correct, not a fault |

Apply with the full command — **the switches are not optional**, the script's defaults are stock
(f16 KV, FA off = 12.6 GB at this context):

```powershell
.\scripts\ensure-ollama-parallel.ps1 -NumParallel 1 -ContextLength 24576 -KvCacheType q8_0 -FlashAttention
```

## 4. Eve's context budget — a rationed resource

| Component | Size |
|---|---|
| Always-on: `eve_instructions.md` (repo root) + `agent/empire-routing.md` | **63 L / 4.4 KB + 120 L / 9.1 KB ≈ 13.5 KB** |
| Loadable skills | 33 files, loaded only when a skill is retrieved |
| Tool schemas | 85 tools claimed, coverage `ok: true` |
| Window | 24,576 tokens |

**Rule:** nothing new enters the always-on prompt without an explicit trade. Detail belongs in a skill
(the routing pair shares **0 lines** with its detail skill on purpose); anything that must be always-on
gets measured against this budget first.

## 5. Hands — the one footprint every limb must have

A hand/limb is complete when all four parts exist and agree:

| Part | Path | Content |
|---|---|---|
| Server | `mcp/<name>_mcp.py` | FastMCP tools; stdio transport; `PYTHONPATH=EMPIRE_ROOT` |
| Transport adapter | `agent/lib/<name>-mcp.ts` | a `createEmpireMcpClient({label, clientName, script, env})` config + thin tool adapters |
| Shared client | `agent/lib/mcp-client.ts` | the only place with SDK import, process lifetime, session refcount, env pinning, error shape |
| Contract | `config/eve-capabilities/playbook/<limb>.md` + one capability-registry entry | what the limb is for and when to reach for it |

Uniform rules: tools return `{ ok: false, error }` naming the failing server; **wrapper env overrides
are applied last** (the host carries `OLLAMA_HOST=0.0.0.0`, a bind address); transport is stdio via
`PYTHON_BIN`; adapters stay thin (the consolidated seven average ~43 lines each).

## 6. Data surfaces and boundaries

| Surface | Role | Boundary |
|---|---|---|
| `C:\Empire_Workbench` | the vault; **also the root `read_document` resolves relative paths against** | never reorganised by tooling; ingest is additive |
| `D:\wiki_md\2017` | wiki corpus: 5.35 M files / 20.41 GB | a **build artifact** of `wiki_xml_convert.py` (the one-shot recipe — never delete it); Eve reads ~3 KB/article, never the tree |
| `V:\Cognee` | graph memory on the T7 VHDX | heavy storage stays off C: |
| `I:\EMPIRE_DATA` | wiki reports and logs | — |
| `agents/**/.eve`, `**/.output`, `data/eve_memory/uploads`, dashboard snapshots | generated | git-ignored, excluded from search, never ingested |

## 7. Gates, and what they do not cover

`mechanic-green` (units, capability governance, wiki battery, UI harness, verify-stack, workbench
verify, prompt budget; `-Full` adds live Eve verify) plus `smoke-eve-hands.py` and now
`audit-empire.py`.

**Not covered:** MCP wrapper *runtime* calls (nothing calls them but Eve's live turns — build and gate
prove wiring only); vault ingest completeness; port collisions beyond the start scripts' checks.

## 8. Definition of healthy

A stack is healthy when `audit-empire.py` exits 0: all four HTTP probes 200, Ollama reachable, any
resident model at **ctx 24576**, both always-on prompt files present. Everything beyond that (bench
pass rates, VRAM numbers, doc counts) is recorded, not enforced.

## 9. Change discipline

1. **One fact, one home.** Commands live in `AGENTS.md`, running state here, per-subject detail in its
   specialist doc, "where is it" in `DOC_MAP.md`.
2. **Measure before merging.** Three times this session intuition said merge and measurement said don't
   (routing pair: 0 shared lines; three guide docs: 0–1; wiki modules: the one "dead" file is the
   corpus recipe). Duplication is rare; un-indexed coherence is common.
3. **Contradictions get IDs.** C1–C5 in `docs/audits/2026-09-26.md` were found, argued, and closed on
   the record — the format works, keep using it.
4. **Every claim is dated.** Readings rot; a number without a date is folklore.
5. **Correct the record loudly** when the audit itself is wrong (C3 was my mis-scoped reading, and the
   record says so).

