# EMPIRE Autonomous Build Guide

**Purpose:** Let the Systems Mechanic (Cursor) forge while the Architect is away. Architect returns only for smoke/acceptance.

**Authority**

| Source | Role |
|--------|------|
| [`EMPIRE_RESEARCH_SNAPSHOT.md`](EMPIRE_RESEARCH_SNAPSHOT.md) | Implementation truth |
| [`expansion_docs/docs/EMPIRE_LOCAL_UPGRADE_RESEARCH.md`](expansion_docs/docs/EMPIRE_LOCAL_UPGRADE_RESEARCH.md) | Ranked recommendations |
| [`expansion_docs/CURSOR_HANDOFF.md`](expansion_docs/CURSOR_HANDOFF.md) | First-task contract |
| [`ARCHITECT_TEST_CHECKLIST.md`](ARCHITECT_TEST_CHECKLIST.md) | Your personal smoke list |
| This file | Execution track + status |

Do **not** treat older expansion catalogs as permission to add Qdrant-as-memory, Kubernetes core, or auto-Cognee.

---

## Roles

| Role | Does | Does not |
|------|------|----------|
| **Mechanic** | Forge pipeline/MCP/Eve tools/scripts/docs; run headless evals; write acceptance `pending_architect` | Invent platforms; expose SBOM to Eve |
| **Architect** | Smoke UI/Toolbelt; reply `Smoke PASS Phase N` | Need to babysit downloads/file edits |

---

## Hard rules (every phase)

1. Limb pattern: `pipeline/` → FastMCP → Eve tool → skill → routing → Toolbelt **OFF** unless core.
2. Never auto-`cognee_remember` from scout/worker artifacts.
3. No generic shell, Docker control, model-pull, or arbitrary FS for Eve.
4. Pin versions/hashes in [`config/empire-release-manifest.json`](../config/empire-release-manifest.json).
5. Bind workers to `127.0.0.1` only.
6. One heavy GPU tenant at a time via [`pipeline/gpu_lease.py`](../pipeline/gpu_lease.py).
7. Rebuild Eve only when TypeScript tools change.

---

## Resume protocol

- `Smoke PASS Phase N` — mark phase `architect_pass`
- `Accept mechanic soft-smoke Phases 1-6 and 8` — mark those phases `architect_pass` from Mechanic soft-smoke evidence
- `Park Phase N: <reason>`
- `Continue autonomous build from Phase N` — only if Mechanic stopped mid-track

Architect authorized continued forge of Phase 3+ while they smoke personally (2026-09-07).

---

## Phase status board

| Phase | Name | Mechanic status | Architect gate |
|------:|------|-----------------|----------------|
| 0 | Guide + queue | `done` | — |
| 1 | Operational foundation | `architect_pass` | accepted 2026-09-07; **re-confirmed 2026-09-09** |
| 2 | llama.cpp structured-extract | `architect_pass` | Soft Smoke B accepted |
| 3 | Retrieval rerank A/B | `architect_pass` | accepted; **re-confirmed 2026-09-09** |
| 4 | Playwright Browser Local | `architect_pass` | accepted; **re-confirmed 2026-09-09** |
| 5 | Voice VAD + Kokoro path | `architect_pass` | accepted (VAD CLI) |
| 6 | UI observe (no actuators) | `architect_pass` | accepted |
| 7 | PaddleOCR | `parked` | only if Docling fails your scans |
| 8 | Mechanic SBOM scripts | `architect_pass` | accepted; **re-confirmed 2026-09-09** |

**Architect acceptance (2026-09-09):** `Smoke PASS Phase 1, Phase 3, Phase 4, and Phase 8` (stack + CLI evidence)

**Architect acceptance (2026-09-07):** `Accept mechanic soft-smoke Phases 1-6 and 8`

**Forgeable build list exhausted** (except Phase 7 parked). No further autonomous phases until Architect unparks 7 or adds new research.

---

## Mechanic prelim / soft-smoke notes (2026-09-07)

- Phase 1–2: GGUF+llama-server installed; extract 5/5; Eve Soft Smoke B used `structured_extract` and wrote `extract_cache/Architect_smoke_*.md`; worker stopped; Toolbelt reset OFF.
- Phase 3: lexical rerank eval 3/3 hits; nomic untouched.
- Phase 4: allowlist blocks `example.com`; localhost fetch OK with frontend up.
- Phase 5: energy VAD silent=False speech / tone=True speech; Silero optional via torch hub.
- Phase 6: pulled `qwen3-vl:8b`; observe Eve screenshot returned UI regions, `actuators: false` (OmniParser not vendored).
- Phase 8: `scripts/empire-sbom.ps1` wrote `data/eval/sbom/` (scanners optional).

Evidence JSON: `data/eval/architect_soft_smoke_b.json`, `data/eval/architect_smoke_scorecard.json`

---

## Smoke B reminder (Architect)

Mechanic already Soft Smoke B’d via Eve API. Optional re-check in UI, or trust evidence and reply PASS.

1. `Start-EMPIRE.bat` (if stack down)
2. `.\scripts\start-structured-extract.ps1`
3. Toolbelt **Structured Extract** ON → one extract chat
4. `.\scripts\stop-structured-extract.ps1`
5. Reply `Smoke PASS Phase 2`

Full checklist: [`ARCHITECT_TEST_CHECKLIST.md`](ARCHITECT_TEST_CHECKLIST.md) · reply card: [`ARCHITECT_SMOKE_REPLY_CARD.md`](ARCHITECT_SMOKE_REPLY_CARD.md)

Quick helpers:

```powershell
cd C:\EMPIRE
.\scripts\architect-smoke-helper.ps1
.\scripts\architect-smoke-helper.ps1 -Scorecard
# after Start-EMPIRE.bat:
.\scripts\architect-smoke-helper.ps1 -StartWorker
```
