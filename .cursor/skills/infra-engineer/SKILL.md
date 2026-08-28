---
name: infra-engineer
description: Adds observability (tracing/metrics/profiling), manages containers/Kubernetes/object storage, and works with event queues (Kafka/RabbitMQ/Redis). Activate for requests like "add tracing to this", "list pods", "produce to Kafka", "profile this function", or "Docker logs". Touches Build1's Nervous System (FastMCP tool calls and Ollama inference can be wrapped with local tracing/metrics) and, where object storage is needed, prefers local/self-hosted storage over PocketBase's own file fields to stay zero-cloud.
icon: server
color: Yellow
---

# Infra Engineer

## Activate when
"add tracing" · "add metrics" · "Docker/K8s/object storage" · "Kafka/RabbitMQ/Redis" · "profile this" ·
"list containers" · "event queue"

## Scripts and reference catalog
Move the full tool catalog and code into these subdirectories rather than inlining them here:
- `scripts/observability_tools.py` — `@traced`, `@timed`, `emit_counter`, `profile_function`, `benchmark`
- `scripts/infra_tools.py` — `docker_list_containers`, `k8s_list_pods`, `object_store_list` (dry_run=True by
  default for anything that could mutate infra state)
- `scripts/queue_tools.py` — `kafka_produce`/`consume`, `rabbitmq_publish`, `redis_stream_add`,
  `InMemoryQueue`
- `references/08_infra.md` — full command/flag reference for all three script modules

## Quick start
```python
from scripts.observability_tools import traced, timed, emit_counter

@traced("my_step")
def process(data):
    ...
```

## Zero-cloud adjustments
- Prefer **self-hosted, containerized** infra over managed cloud services: run Kafka/RabbitMQ/Redis and
  Kubernetes (e.g. via k3s/minikube) as local Docker containers rather than managed cloud offerings.
- Where the original catalog defaults to AWS S3 for object storage, default instead to a **local
  S3-compatible store (e.g. self-hosted MinIO)** or plain local filesystem — never a managed cloud bucket —
  to keep the stack zero-cloud.
- All `infra_tools` calls that could mutate state stay `dry_run=True` by default regardless of target
  (local or containerized); require an explicit opt-in to execute for real.

## Build1 Integration
- Wrap FastMCP tool handlers and Ollama inference calls with `@traced`/`@timed`/`emit_counter` from
  `observability_tools` to get local latency/error visibility without any cloud APM vendor.
- For simple file/blob storage needs, check whether **PocketBase's** built-in file field storage already
  covers the use case before standing up MinIO or another object store — only add infra when PocketBase's
  storage is insufficient (e.g. very large binary assets, high-throughput uploads).
- Event queues (Kafka/RabbitMQ/Redis) are useful for decoupling long-running Cognee ingestion jobs from
  FastMCP request handling; run them as local containers alongside the rest of the stack.
