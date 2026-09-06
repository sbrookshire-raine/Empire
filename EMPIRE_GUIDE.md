# EMPIRE — Context Guide for Collaborators (Humans & AIs)

**Purpose of this file:** Drop this into Gemini, ChatGPT, Claude, or a fresh Cursor chat when prior context is gone. It is the single starting brief for *what EMPIRE is*, *where it stands (Sep 2026)*, and *where it is going*.

**Canonical repo:** https://github.com/sbrookshire-raine/Empire  
**Local root:** `C:\EMPIRE`  
**Vision shortlist:** [`EMPIRE_MANIFESTO.md`](EMPIRE_MANIFESTO.md)  
**Deep reference:** [`docs/manifest/README.md`](docs/manifest/README.md)

---

## 1. What this project is

EMPIRE is a **meter-free, zero-cloud, local AI workbench** on Windows 11. It is not a SaaS product and not a React app.

**Eve** is the conversational agent: an Autonomous Knowledge Refinery and Cognitive Co-Designer. She helps the Architect (the human) triage tools/ideas, remember local knowledge, manage tasks, and hand hard forge work to Cursor — so the human gets more time for exercise and meditation.

### Non-negotiables (do not violate)

| Rule | Detail |
|------|--------|
| Local-only runtime | Ollama for LLMs; no paid cloud LLM APIs in app code |
| No SPA frameworks | Frontend is plain HTML + HTMX + Alpine.js via CDN |
| No cloud BaaS | No Firebase, Supabase, etc. |
| Loopback binding | Services on `127.0.0.1` — remote access later via Tailscale/Cloudflare Tunnel, never open LAN ports |
| Node only under Eve | `agents/empire-task-agent/` is the only npm project |
| Build vs ops | **Build:** Cursor uses frontier cloud models. Do **not** point Cursor Base URL at Ollama while building. **Ops:** Eve always uses Ollama |

### Who does what

| Role | Who | Job |
|------|-----|-----|
| Architect | Human | Vision, priorities, Work Orders review |
| Systems Mechanic | Cursor (this IDE) | Code, MCP, scripts, Forge Protocol |
| Eve | Local agent (`:2000`) | Chat, triage, memory, tasks — **not** Cursor |

Do **not** inject Eve’s ARC/Scanner personality into Cursor replies. Cursor stays technical.

---

## 2. Stack today (ports)

| Service | URL | Role |
|---------|-----|------|
| Frontend / Workbench | http://127.0.0.1:8080/eve.html | Chat, tasks, memory, models, history |
| Dashboard | http://127.0.0.1:8080/dashboard.html | Service cards / health |
| PocketBase | http://127.0.0.1:8090 | Tasks DB (+ admin `/_/`) |
| Ollama | http://localhost:11434/v1 | Local inference |
| Eve | http://127.0.0.1:2000 | Agent runtime |
| Cognee storage | `V:\Cognee` (VHDX on T7 `I:`) | Graph + vectors |

**Cold start:** plug in T7 → `Start-EMPIRE.bat` (or `.\scripts\launch-empire.ps1`). Stop with `Stop-EMPIRE.bat`. Rebuild Eve after tool TS changes: `Restart-EMPIRE.bat`.

---

## 3. Where we are today (Sep 2026)

### Working now

- **Eve Workbench** — Neon Storm themed UI; tabs: Chat, Tasks, Memory, Projects, Models, More
- **Chat** — Eve via Ollama; tool calls for memory, tasks, workbench files, work orders
- **Chat history** — durable local JSON under `%LOCALAPPDATA%\EMPIRE\chat-history\`; panel behind **☰** (starts **closed**; blank new chat by default; open history only when needed)
- **Chat modes** (header picker) + per-mode sampling, shared **8192** context for 16 GB VRAM:
  - **Fast** (Qwen 14b abliterated) — temp **0.2** (strict tools)
  - **Deep** (Qwen 32b) — temp **0.7** (creative)
  - **Librarian** (Command-R 35b) — temp **0.4** (balanced)
- **Toolbelt** — optional limbs default **OFF**: Gumloop, Web Research, Tool Forge, Wiki Local, Time Reclaim, Stem Factory. Memory + Tasks always on
- **Wiki Local scout** — on-demand Weaviate Wikipedia (`:8091`) → Truth Drift markdown cache under `04_Thought_Experiments/wiki_cache/` → triage → optional `cognee_remember` (no full wiki re-ingest). See [`docs/WIKI_SCOUT.md`](docs/WIKI_SCOUT.md)
- **DAZE (Phase 5)** — radial day at http://127.0.0.1:8080/daze.html; PocketBase `day_blocks`; Eve tools behind **Time Reclaim** Toolbelt
- **Stem Factory** — drop songs in `C:\Empire_Workbench\stem_factory\input`, enable Toolbelt **Stem Factory**, ask Eve to run stems (Shard of the Division / Demucs) |
- **Cognee memory** — upload `.md/.txt/.pdf` → dataset `eve_memory`; optimize → `eve_core` for fast recall; curated primitives → `primitives_test`
- **PocketBase Tasks** — CRUD from Workbench (these are **not** Work Orders)
- **Workbench filesystem** — `C:\Empire_Workbench\` with:
  - `00_Resource_Queue` — intake for triage
  - `01_Memory_Bank`
  - `02_Skills_and_Prompts`
  - `03_Active_Tools` — harvested/flattened tools (Tool Forge)
  - `04_Thought_Experiments`
  - `05_Work_Orders` — markdown handoffs for Cursor
- **Triage + Work Orders** — Eve skill + `draft_work_order` MCP; Cursor runs **Forge Protocol** when Architect says “Process Work Orders”
- **Workbench health** — `check_workbench_health` (disk + folder counts)
- **Sandbox tools disabled** — Eve must not use cloud `bash` / `read_file` / `web_search` etc.; use `workbench_*` and EMPIRE tools
- **Persona** — `eve_instructions.md`: Triage Officer + Scanner frameworks + light co-worker wit (substance first)
- **MCP (Cursor)** — `empire-pocketbase`, `empire-cognee`, `empire-workbench`, `empire-work-orders`, `empire-wiki-scout`
- **GitHub backup** — latest meaningful push includes chat history, triage/work orders, mode sampling (`d7e6d75` era and later local edits)

### Halted / do not restart casually

- **Wikipedia / Wiki Ops full ingest** — halted; do not dump the corpus into Cognee. **On-demand scout** (Weaviate → `wiki_cache` → triage → optional remember) is active — see [`docs/WIKI_SCOUT.md`](docs/WIKI_SCOUT.md)

### Important distinctions

| Concept | Meaning |
|---------|---------|
| **Task** | PocketBase row — todo/in_progress/done |
| **Work Order** | `.md` in `05_Work_Orders` for Cursor to forge |
| **Chat history** | Local transcript archive (UI); does **not** revive Eve’s old server session |
| **Cognee memory** | Long-term knowledge Eve recalls — different from chat history |

---

## 4. Plans for the future (Manifesto phases)

From [`EMPIRE_MANIFESTO.md`](EMPIRE_MANIFESTO.md) — vision order, not a sprint board:

| Phase | Theme | Status |
|-------|--------|--------|
| **1** Intake & Triage | Shortlist tools/guides/architecture | **In progress** (Resource Queue + triage skill + Work Orders) |
| **2** Evaluation | USEFUL NOW / COOL IDEA / JUNK | **In progress** (Eve categorizes; Mechanic forges) |
| **3** Thought Experiments | YouTube/ideas → autonomous research; Gumloop later | Planned (Toolbelt limb exists, not default-on) |
| **4** LEGO Whiteboard | Tools as composable blocks on a whiteboard | Planned |
| **5** Time reclamation | Daze / personal tracking; free time for body & mind | **In progress** — PocketBase `day_blocks` + http://127.0.0.1:8080/daze.html + Eve **Time Reclaim** limb |
| **6** Secure remote access | Tailscale or Cloudflare Tunnels | Planned (bind localhost now) |
| **7** Real-time voice | Local STT/TTS (Faster-Whisper, Kokoro/Piper); UI must stay audio-capable | Planned (chat UI must not lock to text-only posts) |

### Near-term engineering backlog (practical)

Canonical living list: **[`docs/EMPIRE_IDEA_QUEUE.md`](docs/EMPIRE_IDEA_QUEUE.md)** (ideas + smoke tests; not PocketBase Tasks / not Work Orders).

- **Test next:** Truth Drift (Wiki Local), DAZE, Stem Factory / Shard — see queue **T-01…T-03**
- Stronger “continue past chat” (optional short summary into Eve context — careful with VRAM)
- Thought-experiment pipeline without cloud lock-in (web scout sharing wiki_cache contract — see [`docs/WIKI_SCOUT.md`](docs/WIKI_SCOUT.md) future expansions)
- Remote access hardening when Architect is ready
- Voice path that fits HTMX/Alpine (blob/WebRTC-friendly composer)
- Keep Cognee storage healthy on VHDX; avoid filling C:

---

## 5. How to help (instructions for Gemini / any AI)

When the Architect pastes this guide:

1. **Assume local Windows EMPIRE** — paths like `C:\EMPIRE`, `C:\Empire_Workbench`.
2. **Respect banned stack** — no React/Next, no Firebase, no paid cloud LLM in runtime code.
3. **Prefer full files** when proposing Eve/Cursor mechanic edits the Architect will paste (EMPIRE Mechanic rule).
4. **Do not confuse roles** — you may advise; Cursor forges; Eve runs locally on Ollama.
5. **Tasks ≠ Work Orders** — never “close” triage by inventing PocketBase tasks unless asked.
6. **Ask before large refactors** — Architect owns vision; small clear steps beat rewrites.
7. **Point to code** under `frontend/`, `agents/empire-task-agent/`, `mcp/`, `scripts/` rather than inventing new clouds.

### Key files to open next

| Need | Path |
|------|------|
| Eve soul / persona | `eve_instructions.md` |
| Eve tool routing | `agents/empire-task-agent/agent/empire-routing.md` |
| Mechanic rules | `.cursor/rules/empire-architecture.mdc` |
| Chat UI | `frontend/eve.html`, `eve-workbench.js`, `eve-workbench.css` |
| Chat history API | `frontend/chat_history.py` |
| Mode temps / ctx | `frontend/ollama_chat_profiles.py`, `agents/.../lib/ollama-config.ts` |
| Work Orders MCP | `mcp/work_order_mcp.py` |
| Wikipedia Weaviate scout | `docs/WIKI_SCOUT.md` |
| Idea / test queue | `docs/EMPIRE_IDEA_QUEUE.md` |
| Day-to-day ops | `AGENTS.md` |

---

## 6. One-paragraph elevator pitch

> EMPIRE is a fully local AI workbench on Windows: Eve chats via Ollama, remembers through Cognee, tracks tasks in PocketBase, and triages tools into Work Orders for Cursor to forge — all without cloud meters — aiming toward remote voice presence and reclaiming the Architect’s time for a healthier life.

---

*Last updated: 2026-09-05 (local). Update this file when major capabilities land so Gemini (and humans) can re-bootstrap fast.*
