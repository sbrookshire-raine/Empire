# Architect personal testing checklist

Your job while Mechanic forges: **run these smokes** and reply in Cursor with `Smoke PASS Phase N` (or paste the failure).

Fastest path if you trust Mechanic soft-smoke evidence: open [`ARCHITECT_SMOKE_REPLY_CARD.md`](ARCHITECT_SMOKE_REPLY_CARD.md) and paste the PASS block.

**One-command helpers:**

```powershell
cd C:\EMPIRE
.\scripts\architect-smoke-helper.ps1              # Phase 1 + Soft Smoke B prep
.\scripts\architect-smoke-helper.ps1 -Scorecard   # CLI scorecard Phases 1–8
.\scripts\architect-smoke-helper.ps1 -StartWorker # after Start-EMPIRE.bat
```

Scorecard writes `data/eval/architect_smoke_scorecard.json`. Helper never marks PASS for you — reply in this Cursor chat.

Mechanic CLI scorecard (latest): Phase **1, 3, 4, 8 architect_pass** (2026-09-09) · Phase 2 CLI_PASS · 5–6 WIRED · 7 PARKED.

---

## Do first (highest value)

### T-A — Phase 1 foundation (helper can auto-check)

- [x] Run `.\scripts\architect-smoke-helper.ps1` and confirm `SMOKE_A_RESULT=PASS`
- [x] Reply: `Smoke PASS Phase 1` — **accepted 2026-09-09**

### T-B — Phase 2 Structured Extract (do this in Eve)

- [ ] Start EMPIRE (`Start-EMPIRE.bat`) so Eve + Ollama are up
- [ ] `.\scripts\start-structured-extract.ps1` (or helper `-StartWorker`)
- [ ] http://127.0.0.1:8080/eve.html → Toolbelt → **Structured Extract** ON
- [ ] Chat: *Extract document metadata from: Title: Architect smoke. Author: Architect. Date: 2026-09-07. Tags: smoke, extract. Summary: verifying structured extract limb.*
- [ ] Confirm a reply with title/tags/summary (tool result)
- [ ] Optional: new file under `C:\Empire_Workbench\04_Thought_Experiments\extract_cache\`
- [ ] Confirm Memory was **not** auto-updated
- [ ] Normal chat still works (“hello”)
- [ ] `.\scripts\stop-structured-extract.ps1`
- [ ] Reply: `Smoke PASS Phase 2`

---

## After Mechanic marks each phase `mechanic_prelim_pass`

### T-3 — Retrieval rerank A/B (eval only) — mechanic_prelim_pass

- [x] `.\venv\Scripts\python.exe -m pipeline.retrieval_rerank eval` → expect 3/3 hits
- [x] Skim `docs/EMBEDDING_AB.md` — **nomic** still production (no re-ingest)
- [ ] Optional: Toolbelt **Retrieval Rerank** ON, ask Eve to run eval
- [x] Reply: `Smoke PASS Phase 3` — **accepted 2026-09-09**

### T-4 — Playwright allowlisted browser — mechanic_prelim_pass

- [x] Stack up (frontend on :8080)
- [ ] Toolbelt **Browser Local** ON
- [ ] Ask Eve to fetch `http://127.0.0.1:8080/` (allowlisted)
- [ ] Ask Eve to fetch `https://example.com/` → must refuse / block
- [x] Reply: `Smoke PASS Phase 4` — **accepted 2026-09-09** (CLI allowlist + stack evidence)

### T-5 — Voice VAD / Kokoro path — mechanic_prelim_pass

- [ ] `.\scripts\start-voice.ps1` if speech API needed
- [ ] Toolbelt **Voice Presence** ON
- [ ] One mic transcript + one speak (if hardware available)
- [ ] Reply: `Smoke PASS Phase 5` or skip with note if no mic

### T-6 — Vision UI observe — mechanic_prelim_pass

- [ ] Toolbelt **Vision Local** ON
- [ ] Point Eve at a local screenshot; confirm observation text only (no clicking)
- [ ] Reply: `Smoke PASS Phase 6`

### T-7 — PaddleOCR — parked

- [ ] **Skip** until Docling fails on a real scanned PDF you care about
- [ ] Then ask Mechanic to unpark Phase 7

### T-8 — SBOM scripts (Mechanic-only) — mechanic_prelim_pass

- [x] `.\scripts\empire-sbom.ps1`
- [x] Confirm reports under `data/eval/sbom/`
- [x] Confirm Eve Toolbelt has **no** SBOM tool
- [x] Reply: `Smoke PASS Phase 8` — **accepted 2026-09-09**

---

## Research Autopilot (F-29 — queue T-13–T-20)

Run after `Start-EMPIRE.bat` and Eve rebuild. Detail in [`EMPIRE_IDEA_QUEUE.md`](EMPIRE_IDEA_QUEUE.md).

- [ ] **T-13** — Enable **Research Partner** (More tab or chat bar); `/api/admission` reflects ON/OFF
- [ ] **T-14** — Partner ON → ask: *What's new on Product Hunt today, and find GitHub MCP servers for local DuckDB?* → multi-source answer, no auto-Cognee
- [ ] **T-15** — Session chips appear during research; clear after release or TTL
- [ ] **T-16** — `github_cache/` + `web_cache/` under `04_Thought_Experiments/`; optional `00_Resource_Queue` brief
- [ ] **T-17** — Partner OFF → same question → guardrail message, no silent network
- [ ] **T-18** *(optional)* — Wiki question with T7/Docker → Weaviate preflight or clear admission error
- [ ] **T-19** — Manual Toolbelt **GitHub Scout** without Partner → search only, no clone/Cognee
- [ ] **T-20** — CLI: `pipeline.admission_controller status` / request / release

Reply when done: `Smoke PASS Research Autopilot` (or note which T-xx failed).

---

## Already on the board (older limbs — smoke when convenient)

| ID | Item | Quick test |
|----|------|------------|
| T-01 | Wiki Local / Truth Drift | `-Weaviate`, Toolbelt Wiki Local, cross-year ask |
| T-02 | DAZE | `/daze.html` + Time Reclaim |
| T-03 | Stem Factory | drop song + Stem Factory ON |
| T-07 | Web Scout | Toolbelt ON, scout a public URL |
| T-10 | Container Scout | Hub search weaviate |

Full detail: [`EMPIRE_IDEA_QUEUE.md`](EMPIRE_IDEA_QUEUE.md) · track: [`EMPIRE_AUTONOMOUS_BUILD_GUIDE.md`](EMPIRE_AUTONOMOUS_BUILD_GUIDE.md)

---

## Reply phrases

- `Smoke PASS Phase N`
- `Park Phase N: <reason>`
- `Continue autonomous build from Phase N` (only if Mechanic stopped)

*Checklist created 2026-09-07. Mechanic continues forgeable phases in parallel.*
