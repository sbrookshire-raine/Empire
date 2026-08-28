# 16 — GitHub prep

Checklist before pushing EMPIRE to a GitHub repository.

## 1. Secrets and local state

Ensure these are **not** staged (they are in `.gitignore`):

| Path | Why |
|------|-----|
| `.env.local` | PocketBase password, tokens |
| `config/cognee.env` | DB passwords, machine paths |
| `venv/` | Python virtualenv |
| `backend/pocketbase/pb_data/` | Your task data |
| `backend/pocketbase/pocketbase.exe` | Downloaded binary |
| `agents/**/node_modules/` | npm deps |
| `agents/**/.eve/`, `.output/` | Eve build cache (optional to ignore — `.output` may be needed for deploy; currently gitignored via agents patterns) |
| `data/cognee_system/` | Local Cognee fallback |
| `frontend/dashboard-status.json` | Regenerated snapshot |

Verify:

```powershell
git status
git check-ignore -v .env.local config\cognee.env venv\
```

## 2. Files to add for clones

Ensure committed:

- [x] `Start-EMPIRE.bat` + `scripts/launch-empire.ps1` (daily launcher)
- [x] `docs/manifest/` (this set)
- [x] `AGENTS.md`
- [x] `.env.example`
- [x] `config/cognee.env.example` (create if missing)
- [x] `requirements.txt`
- [x] `backend/pocketbase/pb_migrations/`
- [x] Source: `frontend/`, `mcp/`, `pipeline/`, `agents/empire-task-agent/agent/`, `scripts/`, `tests/`

## 3. Post-clone setup (document in README)

New clone instructions:

```powershell
git clone <repo-url> C:\EMPIRE
cd C:\EMPIRE
.\scripts\setup.ps1
copy .env.example .env.local
copy config\cognee.env.example config\cognee.env
# Edit cognee.env — SYSTEM_ROOT_DIRECTORY, Postgres if needed
# Update .cursor/mcp.json paths to your clone path
cd agents\empire-task-agent && npm install && npm run build
ollama pull llama3.1:8b
ollama pull nomic-embed-text:latest
.\scripts\start-stack.ps1
```

## 4. Update machine-specific paths

After clone on a new machine, search/replace:

| File | What to update |
|------|----------------|
| `.cursor/mcp.json` | `C:/EMPIRE` → your path |
| `config/cognee.env` | `SYSTEM_ROOT_DIRECTORY`, drive letters |
| Optional wiki MCP env | `D:/wiki_md`, `I:/EMPIRE_DATA` — remove or disable if unused |

## 5. Large / personal data

Do **not** commit:

- `V:\Cognee` / VHDX contents
- `data/eve_memory/uploads/` (user uploads)
- `data/curated_primitives/raw_materials/` if copyrighted — review before push
- Weaviate dumps on `I:` drive

Consider a `data/.gitkeep` pattern and document what users add locally.

## 6. Default credentials warning

`.env.example` contains **default dev credentials**. Add to repo README:

> Change PocketBase admin password before any network exposure.

## 7. Optional `.gitattributes`

For consistent line endings on Windows:

```
* text=auto
*.ps1 text eol=crlf
*.py text eol=lf
```

## 8. License

Add `LICENSE` if you intend open source. Third-party: PocketBase, Eve, Cognee, Ollama each have their own licenses.

## 9. CI (future)

Not included in repo today. Suggested checks:

- `python -m unittest discover -s tests`
- `node tests/frontend/eve_workbench_harness.js`
- `cd agents/empire-task-agent && npm run typecheck`

## 10. Pre-push command summary

```powershell
git status
.\venv\Scripts\python.exe -m unittest discover -s tests -p "test_*.py" -q
node tests\frontend\eve_workbench_harness.js
cd agents\empire-task-agent; npm run typecheck; cd ..\..
git add README.md docs/manifest AGENTS.md config/cognee.env.example
git commit -m "Add project manifest and GitHub documentation"
```

## Next

- [README.md](../../README.md)
- [03-getting-started](03-getting-started.md)
