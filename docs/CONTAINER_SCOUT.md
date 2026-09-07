# Container Scout

Eve limb for **investigating container images** (Docker Hub first) and reporting local EMPIRE Docker status. Default Toolbelt **OFF**. Never auto-pulls, never auto-`cognee_remember`.

Full K8s vs Compose context: [KUBERNETES_AND_CONTAINERS.md](KUBERNETES_AND_CONTAINERS.md).

## Architect usage

1. Open http://127.0.0.1:8080/eve.html → Toolbelt → enable **Container Scout**.
2. Ask Eve e.g. “search Docker Hub for local vector databases” or “what tags does semitechnologies/weaviate have?”
3. Scratch notes land in `C:\Empire_Workbench\04_Thought_Experiments\container_cache\`.
4. Promote to Cognee only when you explicitly ask.
5. “Which EMPIRE containers are running?” → local `docker ps` filter `empire-*` (status only; use Start/Stop scripts to change lifecycle).

## CLI / MCP

```powershell
.\venv\Scripts\python.exe -m pipeline.container_scout search "weaviate" --limit 5
.\venv\Scripts\python.exe -m pipeline.container_scout detail semitechnologies/weaviate
.\venv\Scripts\python.exe -m pipeline.container_scout docker-status
```

Cursor MCP server: `empire-container-scout` (tools: `container_scout_search`, `container_scout_detail`, `container_scout_docker_status`).

## Smoke (Mechanic)

- Hub search `weaviate` returns `semitechnologies/weaviate`.
- Cache write under `container_cache/`.
- `docker-status` lists `empire-*` when Docker is up; returns a clear error when Docker CLI/Desktop is unavailable (Hub search still works independently).
