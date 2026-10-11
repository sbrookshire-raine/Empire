# EMPIRE stack layers (outside in)

Read this top-down when tuning **baseline**, **latency**, or **what to turn on**.

| Layer | What it is | Baseline rule | Primary knobs |
|-------|------------|---------------|---------------|
| **L0 Estate** | Disks, OneDrive, T7 VHDX (`V:\Cognee`), cloud pool (`Z:`) | Heavy data off `C:`; secrets local only | `docs/ESTATE_INVENTORY.md`, `docs/ONEDRIVE.md` |
| **L1 Host** | RAM, VRAM, orphan GPU workers | Meters honest; no dead `llama-server` parents | Ollama tray, `baseline-audit.ps1 -FixOrphans` |
| **L2 Platform** | Docker (Postgres), Ollama tune, PocketBase | One Cognee DB; 24k Fast model baked | `docker-compose.yml`, `ensure-ollama-parallel.ps1` |
| **L3 Services** | Workbench, Eve, optional Wiki/Voice/SearXNG | **Only what toolbelt ON** should listen | Header strip, `start-stack.ps1`, `-NoWiki` / `-NoVoice` |
| **L4 Admission** | Toolbelt, `admit_for_goal`, GPU lease, resource pulse | 0–few limbs ON; DORMANT ≠ running | `docs/EMPIRE_CLARITY.md`, pulse card |
| **L5 Answer path** | intent → resolution → evidence → text | Wiki green path before 14B prose | `wiki_green_path.py`, `REFACTOR_PLAN.md` spine |
| **L6 Experience** | `eve.html` meters, verify UI, voice | One bubble; meters = L1+L4 truth | `eve-workbench.js` |

## Verify one breath

```powershell
.\scripts\baseline-audit.ps1
.\scripts\baseline-audit.ps1 -FixOrphans   # kill orphan llama-server + eve-sbx
```

Workbench JSON: `GET http://127.0.0.1:8080/api/baseline`

**Lighten load** (Eve chat meter): button **Lighten load** or `POST http://127.0.0.1:8080/api/baseline/flush` — clears optional toolbelt, session admits, unloads Ollama models, stops Wiki/Voice Docker, kills orphan GPU workers. Expect **tools** and **RAM/VRAM** bars to drop; **disk** is whole-drive and usually unchanged.

## Design rules (layered)

1. **L3 follows L4** — do not start Weaviate/Voice Docker if the toolbelt limb is off.
2. **L5 before L6 cost** — prefetch evidence in Python; LLM formats only.
3. **L1 before blaming L4** — high RAM/VRAM with 0/14 tools usually means Ollama orphans or Docker, not “Eve turned everything on.”
4. **Mechanic green proves L5–L6**; **baseline audit proves L1–L4** on every boot.
