# EMPIRE Idea Queue

Durable **ideas + verification backlog** for EMPIRE as the project grows.

This is **not**:

| Concept | Where it lives |
|---------|----------------|
| PocketBase **Task** | Workbench Tasks tab — day-to-day todos |
| **Work Order** | `C:\Empire_Workbench\05_Work_Orders\` — Cursor Forge Protocol |
| **This queue** | Ideas, smoke tests, and “do next when ready” — Architect + Mechanic shared list |

**Promote path:** Idea here → (optional) Resource Queue brief → Work Order when ready to forge → delete WO on success → mark queue item `done`.

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

## Testing now (Architect smoke)

These were shipped or partially forged and need **your** hands-on verification.

| ID | Item | Status | How to test | Notes |
|----|------|--------|-------------|-------|
| T-01 | **Truth Drift / Wiki Local** | `ready` | Boot Weaviate (`docs/WEAVIATE_HEIST.md` / `docs/WIKI_SCOUT.md` on `:8091`). Start stack. Enable Toolbelt **Wiki Local**. Ask Eve a cross-year topic (e.g. Cambrai 2017 vs 2026). Confirm cache under `C:\Empire_Workbench\04_Thought_Experiments\wiki_cache\` and **no** auto-Cognee. | Hybrid BM25+vector; pure nearVector empty on this archive. Tear down Weaviate when done. |
| T-02 | **DAZE / Time Reclaim** | `ready` | Open http://127.0.0.1:8080/daze.html. Add overlapping blocks → conflict glow. Enable Toolbelt **Time Reclaim**. Ask Eve what’s free today. | PocketBase `day_blocks`. WO may still be open pending your UX OK. |
| T-03 | **Shard of the Division / Stem Factory** | `ready` | Drop a song in `C:\Empire_Workbench\stem_factory\input`. Enable Toolbelt **Stem Factory**. Ask Eve to create stems. Check `stem_factory\output` (`1_stems`, `3_focus`). | `.venv-cuda` fixed (torch cu128 / RTX 5080). Default `limit=1`. |

---

## Incoming from documents

Paste or summarize the next document here. Mechanic will triage into Testing / Forge / Parked.

| Date | Source doc | Extracted ideas | Triage |
|------|------------|-----------------|--------|
| _(awaiting)_ | _(your next document)_ | — | — |

**Intake rule:** When you share a document, add one row above (or ask Cursor to), then split bullets into the sections below with new `I-xx` / `T-xx` / `F-xx` IDs.

---

## Forge / build backlog

Engineering work not yet (or only partially) shipped.

| ID | Item | Status | Manifesto / docs | Notes |
|----|------|--------|------------------|-------|
| F-01 | Web scout (same md contract as wiki_cache) | `idea` | Phase 3; `docs/WIKI_SCOUT.md` future | Local HTTP then Playwright; no paid search APIs |
| F-02 | `promote_wiki_cache` → Cognee helper | `idea` | WIKI_SCOUT | Explicit promote only |
| F-03 | Chat “continue past chat” (short summary into context) | `idea` | EMPIRE_GUIDE near-term | Careful with VRAM / `num_ctx` 8192 |
| F-04 | Always-on Weaviate cold-start profile (optional) | `parked` | WIKI_SCOUT | Only if Architect wants wiki up every boot |
| F-05 | Dedicated Cognee `truth_drift` dataset | `idea` | WIKI_SCOUT | For promoted compares only |
| F-06 | Stem Factory WO close after live song smoke | `ready` | WO-stem-factory | Depends on T-03 |
| F-07 | DAZE WO close after Architect UX review | `ready` | WO-daze-time-reclaim | Depends on T-02 |
| F-08 | Model A/B (Fast/Deep) one mode at a time | `parked` | After scout path | Keep `num_ctx=8192` |
| F-09 | Secure remote access (Tailscale / Cloudflare Tunnel) | `idea` | Phase 6 | Bind localhost until then |
| F-10 | Local voice (STT/TTS) path for composer | `idea` | Phase 7 | Keep UI audio-blob capable |

---

## Ideas (unsorted growth)

Capture sparks here; promote to Testing or Forge when clear.

| ID | Idea | Status | Source |
|----|------|--------|--------|
| I-01 | LEGO Whiteboard composable tool blocks | `idea` | Manifesto Phase 4 |
| I-02 | Gumloop limb only after local research fails | `parked` | Manifesto Phase 3 |
| I-03 | Thought-experiment YouTube → research limb | `idea` | Manifesto Phase 3 |
| I-04 | Rebuild Shard `.venv-cuda` documented in ops cheat sheet | `done` | 2026-09-06 CUDA fix |

---

## Session checklist (quick)

When waking EMPIRE to work this queue:

1. `Start-EMPIRE.bat` (or stack script) for Eve / Workbench / PocketBase / Ollama  
2. Weaviate only if doing **T-01**  
3. Enable the matching Toolbelt limb(s)  
4. Update this file’s status after you test  

---

## Related paths

| Path | Role |
|------|------|
| [EMPIRE_GUIDE.md](../EMPIRE_GUIDE.md) | Collaborator brief |
| [EMPIRE_MANIFESTO.md](../EMPIRE_MANIFESTO.md) | Phase north star |
| [docs/WIKI_SCOUT.md](WIKI_SCOUT.md) | Wiki Local / Truth Drift |
| [docs/WEAVIATE_HEIST.md](WEAVIATE_HEIST.md) | Weaviate boot / tear-down |
| `C:\Empire_Workbench\05_Work_Orders\` | Active Forge Work Orders |
| `C:\Empire_Workbench\stem_factory\input` | Stem inbox |
| http://127.0.0.1:8080/daze.html | DAZE radial day |

*Created 2026-09-06. Append freely; do not confuse with PocketBase Tasks.*
