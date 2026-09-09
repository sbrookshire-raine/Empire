# EMPIRE Idea Queue

Durable **ideas + verification backlog** for EMPIRE as the project grows.

This is **not**:

| Concept | Where it lives |
|---------|----------------|
| PocketBase **Task** | Workbench Tasks tab — day-to-day todos |
| **Work Order** | `C:\Empire_Workbench\05_Work_Orders\` — Cursor Forge Protocol |
| **This queue** | Ideas, smoke tests, and “do next when ready” — Architect + Mechanic shared list |

**Promote path:** Idea here → (optional) Resource Queue brief → Work Order when ready to forge → delete WO on success → mark queue item `done`.

**Capability north star:** [EMPIRE Capability Atlas](../.cursor/plans/empire_capability_atlas_00e4868b.plan.md) (plan file may live under user `.cursor/plans/`). Real Cognee memory + Eve partnership first; limbs default OFF; one heavy GPU tenant at a time.

---

## How to use

1. Architect (or a pasted doc) adds rows under **Incoming from documents** or the right section.
2. Mechanic keeps **status** and **notes** honest after each session.
3. Testing items stay open until you personally smoke them (or explicitly waive).

### Status legend

| Status | Meaning |
|--------|---------|
| `idea` | Captured; not scheduled |
| `ready` | Clear enough to forge or test |
| `in_progress` | Actively being built or tested |
| `blocked` | Needs path, hardware, or Architect decision |
| `done` | Verified or intentionally closed |
| `parked` | Good idea; deferred on purpose |

---

## Capability Atlas waves

Ordered unlock of stack + RTX 5080 16GB + OSS. Smoke Wave 0 before relying on new limbs in daily chat.

| Wave | Theme | Status | Notes |
|------|-------|--------|-------|
| 0 | Prove forged limbs (Wiki / DAZE / Stem) | `in_progress` | Mechanic offline: stem CUDA OK. Live stack was cold 2026-09-06 — Architect UX still required before WO close |
| 1 | Partnership glue (summary, promote, Docling, Fast A/B, Ollama harden) | `done` | Forged 2026-09-06 |
| 2 | Reach (web scout, thought experiments, provenance) | `done` | Forged 2026-09-06 |
| 3 | Senses (voice + vision + GPU lease) | `done` | Forged 2026-09-06; speech server opt-in |
| 4 | Ubiquity + composition (remote, LEGO index, embed A/B) | `done` | Docs + scaffolds; nomic stays production |

### Hard rejects (Bridge / Copilot mismatches)

Do **not** forge: mega FastMCP gateway rewrite, Postgres-as-memory-authority, default `num_ctx` 32k, always-on Weaviate for working docs, near-term ComfyUI/Electron, auto-`cognee_remember` from caches, full Wikipedia → Cognee re-ingest, paid cloud LLM in app code.

---

## Testing now (Architect smoke)

These were shipped or partially forged and need **your** hands-on verification.

| ID | Item | Status | How to test | Notes |
|----|------|--------|-------------|-------|
| T-01 | **Truth Drift / Wiki Local** | `ready` | `Start-EMPIRE.bat -Weaviate` (or `.\scripts\start-weaviate.ps1`). Enable Toolbelt **Wiki Local**. Ask Eve a cross-year topic (e.g. Cambrai 2017 vs 2026 or AI). Confirm **cards** prefer main articles over disambiguation; cache under `wiki_cache`; **no** auto-Cognee. | Wiki Interpreter (heuristics + optional BGE). Tear down: `.\scripts\stop-weaviate.ps1`. |
| T-02 | **DAZE / Time Reclaim** | `ready` | Open http://127.0.0.1:8080/daze.html. Add overlapping blocks → conflict glow. Enable Toolbelt **Time Reclaim**. Ask Eve what’s free today. | PocketBase `day_blocks`. WO open pending UX OK. |
| T-03 | **Shard of the Division / Stem Factory** | `ready` | Drop a song in `C:\Empire_Workbench\stem_factory\input`. Enable Toolbelt **Stem Factory**. Ask Eve to create stems. Check `stem_factory\output`. | Mechanic: `.venv-cuda` + CUDA device OK offline. Default `limit=1`. |
| T-04 | **Chat continuity** | `ready` | Start stack. Chat several turns, refresh page / reopen chat — Eve should see a short rolling summary prepended server-side. | Wave 1 |
| T-05 | **promote_wiki_cache** | `ready` | After T-01 cache hit, ask Eve to promote a specific `.md` (or MCP `promote_wiki_cache`). Confirm Cognee only on explicit call. | Wave 1 |
| T-06 | **Docling convert** | `ready` | Enable nothing special; ask Eve/`docling_convert` on a local PDF → Resource Queue `.md`. | Needs `pip install docling` in venv |
| T-07 | **Web scout** | `ready` | Enable **Web Scout** limb. Ask Eve to scout a public URL → `04_Thought_Experiments/web_cache/`. | Wave 2 |
| T-08 | **Voice presence** | `ready` | `.\scripts\start-voice.ps1` (or Speaches/Voicebox). Enable **Voice Presence**. Mic blob → transcript in composer. | Wave 3; speech API optional |
| T-09 | **Vision local** | `ready` | `ollama pull qwen3-vl:8b`. Enable **Vision Local**. Ask Eve about a screenshot path. | Wave 3; GPU lease |
| T-10 | **Container Scout** | `ready` | Enable Toolbelt **Container Scout**. Ask Eve to search Docker Hub (e.g. weaviate / vector db). Confirm cache under `04_Thought_Experiments/container_cache/`; **no** auto-Cognee. Optional: ask which `empire-*` containers are running. | See `docs/KUBERNETES_AND_CONTAINERS.md` |
| T-11 | **Smoke A — Operational foundation** | `ready` | Follow **Smoke A** in [`EMPIRE_AUTONOMOUS_BUILD_GUIDE.md`](EMPIRE_AUTONOMOUS_BUILD_GUIDE.md). Then reply `Smoke PASS Phase 1`. | Admission audit + release manifest |
| T-12 | **Smoke B — Structured Extract** | `ready` | Follow **Smoke B** in the autonomous build guide (Toolbelt **Structured Extract**). Then `Smoke PASS Phase 2`. | llama.cpp worker; Ollama stays chat |
| T-13 | **Research Partner toggle** | `ready` | `Start-EMPIRE.bat`. Open http://127.0.0.1:8080/eve.html → **More** tab or chat admission bar → enable **Research Partner**. Confirm `GET /api/admission` shows `research_partner: true`. Toggle OFF → partner flag false. | F-29 forged; default OFF in repo template |
| T-14 | **research_orchestrate — GitHub + Product Hunt** | `ready` | With Partner ON, ask Eve: *What's new on Product Hunt today, and find GitHub MCP servers for local DuckDB?* Confirm she uses **`research_orchestrate`** (tool trace or compact multi-source answer). **No** auto-`cognee_remember`. | Same-turn admission bypasses Toolbelt `turn.started` |
| T-15 | **Session capability chips + TTL** | `ready` | During T-14, chat header shows session chips (`github_scout`, `web_scout`, etc.) with TTL countdown. After orchestrator finishes or **Release session** (More tab), chips clear. Optional: wait for TTL expiry. | Polls `/api/admission` every ~30s |
| T-16 | **Research cache artifacts** | `ready` | After T-14, confirm new files under `C:\Empire_Workbench\04_Thought_Experiments\github_cache\` and `web_cache\`. Optional: intake brief in `00_Resource_Queue` for forge-worthy GitHub hits — triage only, no auto-forge. | Provenance footer on cache `.md` |
| T-17 | **Partner OFF guardrail** | `ready` | Partner OFF. Ask the same research question. Eve should **not** silently hit GitHub/Product Hunt; friendly message to enable Research Partner (or manual Toolbelt). | Rings: never auto Cognee / stem / Gumloop |
| T-18 | **Wiki admission preflight (optional)** | `ready` | T7 plugged + Docker available. Partner ON. Ask a cross-year wiki topic (e.g. T-01 style). Confirm admission may run `start-weaviate.ps1` or reports a **clear** error if archive/path missing — no silent full wiki ingest. | Skip if Weaviate archive unavailable |
| T-19 | **GitHub Scout manual limb** | `ready` | Enable **GitHub Scout** on Toolbelt (without Partner). Ask Eve to search repos for `mcp duckdb`. Confirm `github_cache/` only; **no** clone/install/Cognee. Optional: `GITHUB_TOKEN` if rate-limited. | Cursor MCP: `empire-github-scout` |
| T-20 | **Admission CLI smoke** | `ready` | `.\venv\Scripts\python.exe -m pipeline.admission_controller status` → manifest + session + GPU snapshot. `set-research-partner true` → `request github_scout --reason smoke` → `release`. Check `%LOCALAPPDATA%\EMPIRE\` audit append. | Mechanic pre-pass OK; Architect confirms live stack |

---

## Incoming from documents

Paste or summarize the next document here. Mechanic will triage into Testing / Forge / Parked.

| Date | Source doc | Extracted ideas | Triage |
|------|------------|-----------------|--------|
| 2026-09-06 | Bridge `EVE_OLLAMA_EXPANSION_MANIFEST.md` | Voice, Docling, model A/B, promote cache, provenance, web scout | Folded into Atlas waves; rejects noted above |
| 2026-09-06 | EMPIRE Capability Atlas (Mechanic) | GPU lease, vision limb, thought experiments, LEGO index, embed A/B | Waves 0–4 rows |

**Intake rule:** When you share a document, add one row above (or ask Cursor to), then split bullets into the sections below with new `I-xx` / `T-xx` / `F-xx` IDs.

---

## Forge / build backlog

Engineering work not yet (or only partially) shipped.

| ID | Item | Status | Manifesto / docs | Notes |
|----|------|--------|------------------|-------|
| F-01 | Web scout (same md contract as wiki_cache) | `done` | Phase 3; `docs/WEB_SCOUT.md` | Local HTTP; Playwright optional later |
| F-02 | `promote_wiki_cache` → Cognee helper | `done` | WIKI_SCOUT | Explicit promote only |
| F-03 | Chat “continue past chat” (short summary into context) | `done` | EMPIRE_GUIDE near-term | `num_ctx` 8192; rolling summary field |
| F-04 | Always-on Weaviate cold-start profile (optional) | `parked` | WIKI_SCOUT | Only if Architect wants wiki up every boot |
| F-05 | Dedicated Cognee `truth_drift` dataset | `ready` | WIKI_SCOUT | Promote helper accepts dataset override |
| F-06 | Stem Factory WO close after live song smoke | `ready` | WO-stem-factory | Depends on T-03 |
| F-07 | DAZE WO close after Architect UX review | `ready` | WO-daze-time-reclaim | Depends on T-02 |
| F-08 | Model A/B Fast mode only | `done` | Atlas Wave 1 | `%LOCALAPPDATA%\EMPIRE\ollama-fast-ab.json`; Deep/Librarian pinned |
| F-09 | Secure remote access (Tailscale / Cloudflare Tunnel) | `ready` | Phase 6; `docs/REMOTE_ACCESS.md` | Bind localhost until then |
| F-10 | Local voice (STT/TTS) path for composer | `done` | Phase 7; `docs/VOICE_PRESENCE.md` | Toolbelt OFF; OpenAI-compatible speech API |
| F-11 | Docling MCP → Resource Queue markdown | `done` | Atlas Wave 1 | `empire-docling` |
| F-12 | Ollama inventory + loopback harden | `done` | Atlas Wave 1 | Client URL normalize; Fast A/B API |
| F-13 | Thought-experiment limb | `done` | Phase 3 | Notes under `04_Thought_Experiments/` |
| F-14 | Provenance footer on scout caches | `done` | Atlas Wave 2 | `pipeline/provenance.py` |
| F-15 | Vision Local (`qwen3-vl:8b`) | `done` | Atlas Wave 3 | Toolbelt OFF; GPU lease |
| F-16 | GPU lease dashboard surface | `done` | Atlas | `/api/gpu-lease` |
| F-17 | LEGO whiteboard tool index | `done` | Phase 4 | `03_Active_Tools/LEGO_INDEX.md` |
| F-18 | Embedding A/B (`qwen3-embedding:0.6b` test dataset only) | `ready` | Atlas Wave 4 | `docs/EMBEDDING_AB.md`; nomic stays production |
| F-19 | Container Scout (Docker Hub + local empire-* status) | `done` | `docs/KUBERNETES_AND_CONTAINERS.md` | Toolbelt OFF; no auto-Cognee; no auto-pull |
| F-20 | Run EMPIRE core on local Kubernetes | `parked` | KUBERNETES_AND_CONTAINERS | Single-host + Ollama VRAM; Compose/scripts win |
| F-21 | Autonomous build guide + Phase 1 foundation | `done` | `EMPIRE_AUTONOMOUS_BUILD_GUIDE.md` | Manifest, admission audit, lineage, fixtures |
| F-22 | Structured Extract (llama.cpp worker) | `done` | `docs/workers/STRUCTURED_EXTRACT.md` | Toolbelt OFF; Mechanic prelim pass; Architect Smoke B |
| F-23 | Retrieval rerank A/B (lexical + optional CE) | `done` | `docs/EMBEDDING_AB.md` | Eval only; nomic stays production |
| F-24 | Playwright allowlisted Browser Local | `done` | Autonomous guide Phase 4 | Toolbelt `browser_local` |
| F-25 | Voice VAD gate + Kokoro path | `done` | `pipeline/voice_vad.py` | Energy/Silero; STT skip if silence |
| F-26 | Vision UI observe (no actuators) | `done` | `pipeline/vision_ui_observe.py` | Under Vision Local toolbelt |
| F-27 | Mechanic SBOM script | `done` | `scripts/empire-sbom.ps1` | Not Eve-exposed |
| F-28 | PaddleOCR specialist | `parked` | Autonomous guide Phase 7 | Only if Docling loses Architect samples |
| F-29 | Research Autopilot (admission + github scout + orchestrator) | `done` | [`docs/RESEARCH_AUTOPILOT.md`](RESEARCH_AUTOPILOT.md) | Forge complete; Architect smoke **T-13–T-20** before daily reliance |

---

## Ideas (unsorted growth)

Capture sparks here; promote to Testing or Forge when clear.

| ID | Idea | Status | Source |
|----|------|--------|--------|
| I-01 | LEGO Whiteboard composable UI (beyond markdown index) | `in_progress` | Manifesto Phase 4; http://127.0.0.1:8080/lego.html |
| I-02 | Gumloop limb only after local research fails | `parked` | Manifesto Phase 3 |
| I-03 | Thought-experiment YouTube → research limb | `done` | Manifesto Phase 3 / Atlas |
| I-04 | Rebuild Shard `.venv-cuda` documented in ops cheat sheet | `done` | 2026-09-06 CUDA fix |

---

## Session checklist (quick)

When waking EMPIRE to work this queue:

1. `Start-EMPIRE.bat` (or stack script) for Eve / Workbench / PocketBase / Ollama  
2. Weaviate only if doing **T-01** or **T-18**: `Start-EMPIRE.bat -Weaviate` (or `.\scripts\start-weaviate.ps1`)  
3. Voice speech API only if doing **T-08**  
4. **Research Autopilot (T-13–T-17):** enable **Research Partner** in Workbench — no permanent Toolbelt toggles required  
5. Other limbs: enable matching Toolbelt category(s)  
6. Update this file’s status after you test  

---

## Related paths

| Path | Role |
|------|------|
| [EMPIRE_GUIDE.md](../EMPIRE_GUIDE.md) | Collaborator brief |
| [docs/EMPIRE_RESEARCH_SNAPSHOT.md](EMPIRE_RESEARCH_SNAPSHOT.md) | As-built snapshot for research AIs |
| [docs/EMPIRE_AUTONOMOUS_BUILD_GUIDE.md](EMPIRE_AUTONOMOUS_BUILD_GUIDE.md) | Mechanic forge-while-away track |
| [docs/ARCHITECT_TEST_CHECKLIST.md](ARCHITECT_TEST_CHECKLIST.md) | Architect personal smoke list |
| [EMPIRE_MANIFESTO.md](../EMPIRE_MANIFESTO.md) | Phase north star |
| [docs/WIKI_SCOUT.md](WIKI_SCOUT.md) | Wiki Local / Truth Drift |
| [docs/WEB_SCOUT.md](WEB_SCOUT.md) | Web scout cache |
| [docs/VOICE_PRESENCE.md](VOICE_PRESENCE.md) | STT/TTS limb |
| [docs/REMOTE_ACCESS.md](REMOTE_ACCESS.md) | Phase 6 tunnel notes |
| [docs/EMPIRE_USAGE_GUIDE.md](EMPIRE_USAGE_GUIDE.md) | Architect how-to: pages, Toolbelt, recipes |
| [docs/LEGO_WHITEBOARD.md](LEGO_WHITEBOARD.md) | Manifesto Phase 4 LEGO canvas |
| [docs/KUBERNETES_AND_CONTAINERS.md](KUBERNETES_AND_CONTAINERS.md) | K8s vs Compose; Container Scout |
| [docs/CONTAINER_SCOUT.md](CONTAINER_SCOUT.md) | Container Scout limb ops |
| [docs/RESEARCH_AUTOPILOT.md](RESEARCH_AUTOPILOT.md) | Research Partner + admission + orchestrator |
| [docs/WEAVIATE_HEIST.md](WEAVIATE_HEIST.md) | Weaviate boot / tear-down |
| `C:\Empire_Workbench\05_Work_Orders\` | Active Forge Work Orders |
| `C:\Empire_Workbench\stem_factory\input` | Stem inbox |
| http://127.0.0.1:8080/daze.html | DAZE radial day |

*Created 2026-09-06. Updated for Capability Atlas. Append freely; do not confuse with PocketBase Tasks.*
