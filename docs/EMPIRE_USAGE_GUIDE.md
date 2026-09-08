# EMPIRE — How to use what you have

**Audience:** Architect (you). Not a forge checklist.  
**Goal:** Know *where to click*, *which limb to turn on*, and *what each piece is for* — without memorizing every tool name.

**Start the stack:** double-click `Start-EMPIRE.bat` (or `.\scripts\launch-empire.ps1`).  
**Main door:** http://127.0.0.1:8080/eve.html

---

## 1. Mental model (three layers)

```text
┌─────────────────────────────────────────────────────────┐
│  PAGES (nav) — different rooms in the house             │
│  Eve · LEGO · DAZE · Wiki · Memory · Dashboard · …      │
└─────────────────────────────────────────────────────────┘
                          │
┌─────────────────────────────────────────────────────────┐
│  ALWAYS ON in Eve chat                                  │
│  Talk · Tasks · Memory (Cognee) · health/models         │
└─────────────────────────────────────────────────────────┘
                          │
┌─────────────────────────────────────────────────────────┐
│  TOOLBELT (optional limbs) — OFF until you flip them    │
│  Wiki, Web, Extract, Voice, Vision, Stem, …             │
└─────────────────────────────────────────────────────────┘
```

**Rule of thumb:** Chat with Eve for everyday work. Flip a Toolbelt switch only when you need that specialty. LEGO is a picture of those specialties — it does not replace Eve.

---

## 2. Pages (what each room is for)

| Page | URL | Use it when… |
|------|-----|----------------|
| **Eve** | `/eve.html` | You want to talk, remember, triage, or use limbs |
| **LEGO** | `/lego.html` | You want to *see* limbs as bricks and turn a set ON via **Apply to Toolbelt** |
| **DAZE** | `/daze.html` | You want a 24-hour day dial (blocks, free time) |
| **Wiki** | `/wiki.html` | You want archive titles / Truth Drift UI (Weaviate must be up) |
| **Tasks** | `/` | Classic PocketBase task list |
| **Primitives** | `/primitives.html` | Curated Cognee ingest for `primitives_test` |
| **Dashboard** | `/dashboard.html` | Service status / stack health |
| **PocketBase admin** | `:8090/_/` | Low-level data (optional) |

Nav bar at the top links these. You do not need every page every day — **Eve + Memory + Toolbelt** covers most of life.

---

## 3. Eve chat basics

### Modes (top of chat)

| Mode | Feel | Use when… |
|------|------|-----------|
| **Fast** | Quicker, smaller model | Everyday chat, light asks |
| **Deep** | Heavier reasoning | Harder questions |
| **Librarian** | Research / retrieval tone | Digging through knowledge |

### Always available (no Toolbelt)

- Normal conversation  
- **Tasks** (PocketBase to-dos — not the same as Work Orders)  
- **Memory** — Cognee remember / recall (Workbench upload uses dataset `eve_memory` by default)  
- Models / health checks  

### Memory vs scratch (important)

| Kind | Where it lives | Auto into Cognee? |
|------|----------------|-------------------|
| **Memory** | Cognee datasets (`eve_memory`, `eve_core`, `primitives_test`, …) | Only when you **Add to memory** or ask Eve/MCP to remember |
| **Scratch** | Workbench folders (`wiki_cache`, `web_cache`, `extract_cache`, …) | **Never** automatic — promote only if you ask |

If a limb “caches” something, treat it as a **draft on disk**, not permanent brain.

### Tasks vs Work Orders

| | Tasks | Work Orders |
|--|-------|-------------|
| What | Your to-dos in PocketBase | Markdown forge tickets for Cursor |
| Where | Eve Tasks / PocketBase | `C:/Empire_Workbench/05_Work_Orders/` |
| Who closes | You / Eve | Cursor deletes WO **after successful forge** |

---

## 4. Toolbelt limbs (optional specialists)

Open the **Toolbelt** panel on Eve. Flip a limb **ON** only for that conversation need, then flip OFF when done (keeps chat focused).

| Limb (UI name) | Plain English | Typical ask | Extra start? |
|----------------|---------------|-------------|--------------|
| **Wiki Local** | Search local Wikipedia years | “Compare X in 2017 vs 2026” | Weaviate: `Start-EMPIRE.bat -Weaviate` |
| **Web Scout** | Fetch a public page → scratch md | “Scout https://…” | No |
| **Browser Local** | Allowlisted local pages only | “Fetch http://127.0.0.1:8080/…” | Frontend up |
| **Structured Extract** | Pull title/tags/summary via llama worker | “Extract metadata from: …” | `.\scripts\start-structured-extract.ps1` |
| **Retrieval Rerank** | Eval/reorder search hits (nomic stays prod) | “Run retrieval rerank eval” | No |
| **Time Reclaim** | Talk to DAZE schedule | “What’s free today?” | PocketBase up; DAZE page helps |
| **Stem Factory** | Split a song into stems | “Make stems from inbox” | Song in `stem_factory/input`; CUDA venv |
| **Thought Experiments** | Capture an idea/YouTube note | “Capture this experiment…” | No |
| **Voice Presence** | Mic → text / speak reply | Speak or ask to read aloud | `.\scripts\start-voice.ps1` if needed |
| **Vision Local** | Describe / observe a screenshot | “What’s on this image?” | `qwen3-vl:8b` in Ollama |
| **Container Scout** | Docker Hub search + local empire-* status | “Search hub for weaviate” | Docker optional for status |
| **Tool Forge** | Read harvested flattened codebases | “Read BANDAPP_flattened.txt” | Files under `03_Active_Tools` |
| **Web Research** | Older external scrape path | Prefer **Web Scout** for new work | — |
| **Gumloop Cloud** | External Gumloop | Parked preference: local-first | Account / external |

**GPU note:** Only one heavy GPU job at a time (chat vs extract vs vision). If extract worker is running, stop it before a big chat/vision session: `.\scripts\stop-structured-extract.ps1`.

---

## 5. LEGO whiteboard (how it fits — keep it simple)

http://127.0.0.1:8080/lego.html

| Do | Don’t |
|----|-------|
| Place bricks you care about | Treat edges as automatic pipelines |
| Connect bricks to *sketch* a workflow | Expect Eve to “run the board” yet |
| Click **Apply to Toolbelt** to turn those limbs ON | Expect Cognee to fill from the diagram |

**Think of LEGO as a light-switch board + sticky notes**, not a factory control panel. Understanding still happens in Eve chat.

Human brick list: `C:/Empire_Workbench/03_Active_Tools/LEGO_INDEX.md`  
Detail: [`LEGO_WHITEBOARD.md`](LEGO_WHITEBOARD.md)

---

## 6. Common recipes

### A. “Remember this document”

1. Eve → Memory / Workbench upload (or drop into curated primitives flow)  
2. Ask Eve about it later (“recall …”)  
3. Optional: `.\scripts\optimize-eve-memory.ps1` after big bulk ingest  

### B. “Truth Drift / compare years”

1. Start with Weaviate  
2. Toolbelt → **Wiki Local** ON  
3. Ask a cross-year question  
4. Scratch lands in `wiki_cache` — promote only if you want it in Cognee  

### C. “Extract structure from a note”

1. `.\scripts\start-structured-extract.ps1`  
2. Toolbelt → **Structured Extract** ON  
3. Ask Eve to extract metadata  
4. Stop worker when done  

### D. “Plan my day”

1. Open **DAZE** or ask Eve with **Time Reclaim** ON  
2. Add blocks; ask what’s free  

### E. “Compose which limbs I want on”

1. Open **LEGO**, place bricks, Apply  
2. Or flip switches on Eve Toolbelt  
3. Chat on Eve  

---

## 7. Folders that matter (Workbench)

| Folder | Role |
|--------|------|
| `00_Resource_Queue` | Incoming material to process |
| `01_Memory_Bank` | Memory-related files |
| `02_Skills_and_Prompts` | Prompt / skill text |
| `03_Active_Tools` | Harvested tools + LEGO index/boards |
| `04_Thought_Experiments` | Scratch caches (wiki/web/extract/…) |
| `05_Work_Orders` | Forge requests for Cursor |

Root of Workbench: `C:\Empire_Workbench`

---

## 8. What you can ignore for now

- Kubernetes / Podman / extra vector DBs (parked on purpose)  
- PaddleOCR (only if Docling fails your scans)  
- SBOM scripts (Mechanic maintenance, not Eve)  
- pr-lens-style animated PR diagrams (optional later; not required to use limbs)  
- Every MCP tool name — Eve + Toolbelt labels are enough day to day  

---

## 9. One-page “who do I ask?”

| I want… | Go to… |
|---------|--------|
| Talk / think / remember | **Eve** |
| Turn specialists on/off | Eve **Toolbelt** or **LEGO Apply** |
| Day schedule | **DAZE** / Time Reclaim |
| Local wiki years | Wiki Local + Weaviate |
| Document metadata JSON | Structured Extract + worker |
| Screenshot understanding | Vision Local |
| Song stems | Stem Factory |
| See if services are up | **Dashboard** |
| Get Cursor to build something | Work Order in `05_Work_Orders` |

---

## 10. Related docs (deeper, not required to start)

| Doc | Role |
|-----|------|
| [`EMPIRE_GUIDE.md`](../EMPIRE_GUIDE.md) | Collaborator brief |
| [`EMPIRE_MANIFESTO.md`](../EMPIRE_MANIFESTO.md) | Vision phases |
| [`ARCHITECT_TEST_CHECKLIST.md`](ARCHITECT_TEST_CHECKLIST.md) | Smoke tests |
| [`EMPIRE_RESEARCH_SNAPSHOT.md`](EMPIRE_RESEARCH_SNAPSHOT.md) | As-built for research AIs |
| Per-limb docs | `WIKI_SCOUT`, `WEB_SCOUT`, `VOICE_PRESENCE`, `CONTAINER_SCOUT`, `workers/STRUCTURED_EXTRACT`, `LEGO_WHITEBOARD` |

---

*Written for understanding first. Prefer flipping one limb and asking Eve one clear question over wiring a complex LEGO graph.*
