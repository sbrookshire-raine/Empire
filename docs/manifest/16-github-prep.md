# 16 — GitHub, backup & clone

Canonical remote for this project.

| | |
|--|--|
| **GitHub** | https://github.com/sbrookshire-raine/Empire |
| **SSH remote** | `git@github.com:sbrookshire-raine/Empire.git` |
| **Default branch** | `main` |

---

## Clone on a new machine

```powershell
git clone git@github.com:sbrookshire-raine/Empire.git C:\EMPIRE
cd C:\EMPIRE

.\scripts\setup.ps1

copy .env.example .env.local
copy config\cognee.env.example config\cognee.env
# Edit config\cognee.env — SYSTEM_ROOT_DIRECTORY, Postgres if needed

# Cursor MCP paths (required if not cloning to C:\EMPIRE)
# Edit .cursor\mcp.json — replace C:/EMPIRE with your clone path

cd agents\empire-task-agent
npm install
npm run build
cd ..\..

ollama pull llama3.1:8b
ollama pull nomic-embed-text:latest
# Optional suite models — see docs/manifest/10-models-and-ollama.md

# One-time VHDX (Administrator) if using T7 / V:\Cognee
# powershell -ExecutionPolicy Bypass -File scripts\create-cognee-vhdx.ps1

# Daily use
# Double-click Start-EMPIRE.bat at the repo root
```

**Daily start after setup:** double-click **`Start-EMPIRE.bat`** (or `.\scripts\launch-empire.ps1`).

---

## What is **not** on GitHub (stays local)

These paths are in `.gitignore` or are machine-specific. They are **not** restored by `git clone` — you recreate or copy them separately.

| Item | Location | How to restore |
|------|----------|----------------|
| Python venv | `venv/` | `.\scripts\setup.ps1` |
| Secrets | `.env.local` | `copy .env.example .env.local` |
| Cognee config | `config/cognee.env` | `copy config\cognee.env.example config\cognee.env` |
| PocketBase binary | `backend/pocketbase/pocketbase.exe` | `setup.ps1` downloads it |
| Task / PB data | `backend/pocketbase/pb_data/` | Empty on fresh clone; your data stays on the old machine |
| Eve npm deps | `agents/**/node_modules/` | `npm install` in `agents/empire-task-agent` |
| Eve build cache | `agents/**/.eve/`, `agents/**/.output/` | `npm run build` |
| Workbench uploads | `data/eve_memory/uploads/` | Re-upload files in Memory tab |
| Upload job state | `data/eve_memory/jobs/` | Regenerated per upload |
| Cognee graph data | `V:\Cognee` (VHDX) | Mount T7 / VHDX on each machine; not in git |
| Ollama models | `~/.ollama` or Ollama store | `ollama pull …` on each machine |
| Dashboard snapshot | `frontend/dashboard-status.json` | `.\scripts\refresh-dashboard.ps1` |
| Local Cognee override | `cognee/.env` | Optional; usually use `config/cognee.env` |

**Backing up personal data:** copy `pb_data/`, `V:\Cognee`, and `data/eve_memory/` separately (external drive, zip, etc.) — do not commit them to GitHub.

---

## After clone checklist

- [ ] `.\scripts\setup.ps1` completed without errors
- [ ] `.env.local` and `config/cognee.env` exist and are edited
- [ ] `.cursor/mcp.json` paths point to **your** clone directory
- [ ] `agents\empire-task-agent`: `npm install` + `npm run build`
- [ ] Ollama models pulled (`llama3.1:8b`, `nomic-embed-text:latest`, plus suite gaps)
- [ ] Docker Desktop running (Cognee Postgres)
- [ ] `V:\Cognee` mounted if using VHDX workflow
- [ ] `Start-EMPIRE.bat` opens http://127.0.0.1:8080/eve.html
- [ ] Rotate PocketBase password if repo is or becomes **public**

---

## Ongoing backup (push changes)

From repo root after you change code or docs:

```powershell
git status
git add -A
git commit -m "Describe your change"
git push origin main
```

Before pushing, confirm secrets are not staged:

```powershell
git check-ignore -v .env.local config\cognee.env venv\
git status
```

Suggested pre-push tests:

```powershell
.\venv\Scripts\python.exe -m unittest discover -s tests -p "test_*.py" -q
node tests\frontend\eve_workbench_harness.js
cd agents\empire-task-agent; npm run typecheck; cd ..\..
```

---

## Monorepo — no nested `.git` folders

EMPIRE is a **single** git repository. Nested `.git` directories inside the tree (e.g. under `agents/empire-task-agent/` or `tools/archify/`) must be removed before `git add`, or Git will record an empty submodule/gitlink instead of the real files.

If you see `embedded git repository` warnings:

```powershell
Remove-Item -Recurse -Force path\to\nested\.git
git rm --cached -r path\to\folder
git add path\to\folder\
```

---

## Files committed that need per-machine edits

| File | What to change |
|------|----------------|
| `.cursor/mcp.json` | `C:/EMPIRE` → your clone path (Python exe + MCP script paths) |
| `config/cognee.env` | `SYSTEM_ROOT_DIRECTORY`, drive letters (created locally from `.example`) |
| Optional wiki MCP env in `mcp.json` | `D:/wiki_md`, `I:/EMPIRE_DATA` — disable if unused |

`.cursor/mcp.json` is committed with **default dev** PocketBase credentials (`admin@empire.local`). Treat as local-dev only; rotate before any network exposure or if the repo is public.

---

## Pre-first-push checklist (reference)

Use when initializing git on a **new** copy of the tree:

1. Secrets and local state excluded (see table above)
2. Remove nested `.git` folders under subprojects
3. Commit includes: `Start-EMPIRE.bat`, `scripts/launch-empire.ps1`, `docs/manifest/`, `config/cognee.env.example`
4. `git remote add origin git@github.com:sbrookshire-raine/Empire.git`
5. `git push -u origin main`

---

## Large / personal content policy

Do **not** commit:

- `V:\Cognee` / VHDX contents
- `data/eve_memory/uploads/` and `jobs/`
- Weaviate dumps on external drives
- Copyrighted `raw_materials/` unless you intend to publish them

Curated primitives **are** in the repo today (`data/curated_primitives/`). Review licensing before making the repository public.

---

## Default credentials warning

`.env.example` and committed MCP config use **local dev defaults**. Change PocketBase admin password before any non-loopback exposure.

---

## CI (future)

Not in repo today. Suggested checks:

- `python -m unittest discover -s tests`
- `node tests/frontend/eve_workbench_harness.js`
- `cd agents/empire-task-agent && npm run typecheck`

---

## Next

- [03-getting-started](03-getting-started.md)
- [README.md](../../README.md)
