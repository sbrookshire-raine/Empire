# Kubernetes and containers for EMPIRE

Architect-plain guide: what Kubernetes (K8s) actually is, how registries and runtimes fit, and what EMPIRE should (and should not) do with them on this Windows local stack.

**Related:** [CONTAINER_SCOUT.md](CONTAINER_SCOUT.md) (limb ops), [WIKI_SCOUT.md](WIKI_SCOUT.md) (on-demand Docker Weaviate), [WEB_SCOUT.md](WEB_SCOUT.md), [docker-compose.yml](../docker-compose.yml) (Cognee Postgres).

---

## Vocabulary (plain English)

| Term | Meaning |
|------|---------|
| **Image** | A packaged filesystem + startup command (e.g. `semitechnologies/weaviate:1.27.0`). Built once, run many times. |
| **Container** | One running instance of an image. |
| **Registry** | Where images are stored and discovered (Docker Hub, GHCR, Google Artifact Registry). |
| **Runtime** | Software that actually starts containers. **Docker Engine** and **containerd** are both runtimes. Modern Kubernetes usually talks to **containerd** via the CRI. |
| **Pod** | K8s unit: one or more tightly coupled containers that share network/storage on one node. |
| **Deployment / ReplicaSet** | K8s objects that keep **N** identical Pods running and can roll updates. |
| **Service** | Stable network name/port in front of Pods (load-balances among replicas). |
| **Compose** | Docker’s single-host “bring these containers up together” file (`docker compose up`). |

---

## Misconceptions (mapped to common hunches)

1. **“K8s manages containers up and down”** — Yes, but so do Compose and EMPIRE’s `start-*.ps1` / `stop-*.ps1`. K8s adds a **control plane** (API server, scheduler, etcd) that uses RAM even when quiet. On one PC, Compose/scripts are enough.

2. **“K8s lets us find containers online to investigate”** — That’s **registry search**, not Kubernetes. Discovery lives on **Docker Hub**, **GHCR**, **Artifact Registry**. K8s only *pulls* an image you already named.

3. **Docker Hub / Google Container Registry / containerd**
   - **Docker Hub** — public catalog; EMPIRE’s Container Scout searches it first.
   - **GCR** — legacy Google registry; use **Artifact Registry** (`*.pkg.dev`) instead.
   - **containerd** — a **runtime**, not a third image store. Not “Docker’s competitor registry.”

4. **“Multiple copies, switchable”** — K8s Deployments scale replicas and do rolling updates. The app must be **designed** for multi-instance (shared DB, ports, GPU). Ollama-on-GPU, PocketBase SQLite, and Cognee-on-VHDX are poor multi-replica defaults.

5. **“Built-in 5× RAID uptime”** — Replicas are **your choice** (`replicas: N`), often 3 for HA—not a fixed five. Restart/reschedule is real; it is **not RAID** (no disk bit-mirroring). One Windows box + Docker Desktop K8s ≠ datacenter HA.

---

## When Kubernetes pays off vs Compose

| Prefer Compose / scripts | Prefer Kubernetes |
|--------------------------|-------------------|
| Single host (this EMPIRE PC) | Many machines / cloud nodes |
| Few services, on-demand limbs (Weaviate) | Dozens of microservices, rolling deploys |
| Protect RAM/VRAM for Ollama | Dedicated cluster capacity |
| Fast edit–run–test | Production self-heal across nodes |

Industry practice: **local = Compose**; **production multi-node = K8s**. EMPIRE is local-first.

---

## What EMPIRE already does with Docker

- **Cognee Postgres:** [`docker-compose.yml`](../docker-compose.yml) → `empire-cognee-postgres`.
- **Weaviate (Wiki Local):** on-demand `docker run` via [`scripts/start-weaviate.ps1`](../scripts/start-weaviate.ps1); tear down with `stop-weaviate.ps1`. See [WEAVIATE_HEIST.md](WEAVIATE_HEIST.md) / [WIKI_SCOUT.md](WIKI_SCOUT.md).

Pattern to keep: **heavy limbs on demand**, not an always-on local cluster.

---

## What we forged instead of “EMPIRE on K8s”

**Container Scout** (Toolbelt limb, default OFF):

- Search Docker Hub; optional repo/tag detail; cache markdown under `C:\Empire_Workbench\04_Thought_Experiments\container_cache\`.
- Report local `empire-*` container status (up/down awareness).
- Never auto-`cognee_remember`. Never auto-pull/run arbitrary Hub images (intake → triage → Work Order if USEFUL NOW).

Enable **Container Scout** in the Workbench Toolbelt, then ask Eve e.g. “search Docker Hub for local vector databases.”

---

## Parked on purpose

- Migrating Eve / Ollama / PocketBase / Cognee onto Kubernetes.
- Enabling Docker Desktop Kubernetes as cold-start default.
- Paid Google Cloud / private Artifact Registry as a dependency.
- Claiming replica-count HA equals RAID on one host.

Revisit only if EMPIRE moves to multi-node or a dedicated always-on lab box that is **not** sharing 16 GB VRAM with chat models.

---

## Architect quick commands

```powershell
# Container Scout (Python)
.\venv\Scripts\python.exe -m pipeline.container_scout search "weaviate" --limit 5
.\venv\Scripts\python.exe -m pipeline.container_scout detail semitechnologies/weaviate
.\venv\Scripts\python.exe -m pipeline.container_scout docker-status

# Existing Weaviate limb
.\scripts\start-weaviate.ps1
.\scripts\stop-weaviate.ps1
```
