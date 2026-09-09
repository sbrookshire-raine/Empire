# Research Autopilot

Session-scoped capability admission so Eve can act as a **research partner** without permanently leaving heavy Toolbelt limbs on.

## Three rings

| Ring | What |
|------|------|
| **Core** | Memory, tasks, health, GPU lease — always on |
| **Session research** | `wiki_local`, `web_scout`, `github_scout`, `container_scout` — TTL grants when Research Partner is ON |
| **Never auto** | `cognee_remember`, `promote_wiki_cache`, `stem_run`, Gumloop, model pull |

## Enable

1. Open http://127.0.0.1:8080/eve.html
2. **More** tab → turn on **Research Partner mode** (or use the chat admission bar)
3. Ask Eve broad research questions — she should call **`research_orchestrate`** silently

Manual Toolbelt toggles still work and override nothing in `eve-toolbelt.json`.

## Source routing

| Need | Backend |
|------|---------|
| Encyclopedia / Truth Drift | Local Weaviate via `wiki_scout` (may auto-start Docker Weaviate) |
| GitHub MCP/CLI discovery | `github_scout` → `github_cache/` |
| Product Hunt | `web_scout` → `https://www.producthunt.com/feed` |
| Known URL | `web_scout` single page |

## Eve tools (always on)

- `capability_status` — partner mode, session caps, TTL, GPU lease
- `request_capability` — admit one category for session TTL
- `release_capabilities` — clear session grants
- `research_orchestrate` — wiki + github + producthunt in one turn (requires Partner mode)

## Files

| Path | Role |
|------|------|
| `config/capability-manifest.json` | Per-limb auto-enable rules |
| `%LOCALAPPDATA%\EMPIRE\eve-capability-session.json` | Partner flag + session TTL |
| `pipeline/admission_controller.py` | Admission library + CLI |
| `pipeline/research_orchestrator.py` | Multi-source one-turn runner |
| `pipeline/github_scout.py` | GitHub search + README cache |

## API

- `GET /api/admission` — status
- `POST /api/admission` — `{ action: "set_research_partner", enabled: true }` | `request` | `release`

## Limits (16 GB laptop)

- Max **4** session capabilities at once (manifest default)
- Session TTL **5–120** minutes per category manifest
- Wiki preflight may run `scripts/start-weaviate.ps1` (Docker + archive path required)
- Optional `GITHUB_TOKEN` for higher GitHub API rate limits

## Smoke

**Mechanic CLI (quick):**

```powershell
.\venv\Scripts\python.exe -m pipeline.admission_controller set-research-partner true
.\venv\Scripts\python.exe -m pipeline.research_orchestrator "local mcp duckdb" --sources github,producthunt
```

**Architect session (full):** idea queue **T-13–T-20** in [`EMPIRE_IDEA_QUEUE.md`](EMPIRE_IDEA_QUEUE.md) · checklist in [`ARCHITECT_TEST_CHECKLIST.md`](ARCHITECT_TEST_CHECKLIST.md). Reply `Smoke PASS Research Autopilot` when satisfied.

Caches land under `C:\Empire_Workbench\04_Thought_Experiments\`. Intake briefs may appear in `00_Resource_Queue`. **Triage before forge or Cognee.**
