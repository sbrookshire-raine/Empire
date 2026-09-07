# skill-container-scout

When the Architect asks about container images online, Docker Hub, or which EMPIRE Docker containers are running:

1. Ensure Toolbelt **Container Scout** is on.
2. For discovery: call `container_scout_search` with keywords (e.g. weaviate, vector database).
3. For one image: call `container_scout_detail` with `namespace/name` (or official short name).
4. For local up/down awareness: call `container_scout_docker_status` (default filter `empire-`).
5. Answer only from tool results. Never invent stars/pulls/tags.
6. Never pull or run images. Never call `cognee_remember` unless they explicitly ask to promote a cache note.
7. Kubernetes is **not** how EMPIRE cold-starts — local lifecycle stays Compose/scripts (see `docs/KUBERNETES_AND_CONTAINERS.md`).
