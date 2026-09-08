# Eve Local-First Expansion Manifest

**Status:** research complete; implementation plan ready for Cursor

**Verified:** 2026-09-06

## 1. Purpose and non-negotiable constraints

Expand an existing Eve project into a capable local-first personal agent workstation. Keep Eve as the orchestration and interaction layer. Keep Ollama as the default runtime for LLMs, vision models, and embeddings. A dedicated reranker may run as an isolated local CUDA worker when its measured retrieval gain justifies the additional runtime. Keep Cognee, Weaviate Wikipedia, PocketBase, PostgreSQL, Docker, and FastMCP where they already serve distinct responsibilities.

Current hardware profile:

- NVIDIA RTX 5080-class GPU with 16 GB VRAM
- 64 GB system RAM
- Windows host with Docker available

Research-machine Ollama check (not an inventory of the target project machine):

- `ollama list` returned no installed models on 2026-09-06.
- Cursor must inventory the target machine before acting. Make model availability a health check, not an assumption.

Rules:

- All inference endpoints bind to `127.0.0.1`; no cloud model or hosted embedding fallback.
- Local tools expose specific typed operations. Never give the model an arbitrary shell, filesystem path, SQL, Docker, or browser-JavaScript tool.
- PostgreSQL is authoritative for jobs, approvals, audit records, artifacts, and provenance.
- PocketBase is the human-facing task/realtime UI layer, not a second source of truth.
- Weaviate remains the retrieval index for the Wikipedia snapshot and working documents.
- Cognee holds curated durable memories and relationships only. It is not a raw-document dumping ground.
- Every destructive, external, desktop-input, Docker-lifecycle, or source-file mutation action requires an explicit approval token.

## 2. Target architecture

```text
User / Eve UI
    |
    v
Eve: conversation, plans, approvals, scheduling, subagent routing
    |
    +-- FastMCP gateway: typed capability boundary and audit middleware
    |     +-- retrieval tools
    |     +-- document tools
    |     +-- analytics tools
    |     +-- media and voice tools
    |     +-- system observer
    |     +-- desktop observer (later)
    |
    +-- Ollama at 127.0.0.1:11434
    |     +-- text reasoning / tool calls / JSON schemas
    |     +-- embeddings
    |     +-- vision
    +-- optional reranker worker at 127.0.0.1 only
    |
    +-- PostgreSQL: authoritative tasks, jobs, audit, artifacts, provenance
    +-- PocketBase: UI, uploads, realtime projection of task state
    +-- Weaviate: local Wikipedia and working-document retrieval
    +-- Cognee: promoted long-term graph and semantic memory
    +-- Workers: ingestion, indexing, voice, model routing, maintenance
```

Do not add another agent framework, general-purpose memory database, generic database MCP server, or generic shell MCP server. They overlap with Eve, Cognee/Weaviate/Postgres, and FastMCP without improving the actual workflows.

## 3. Ollama runtime policy

Ollama is sufficient for the requested model roles. Its local API supports batch embeddings, vision inputs, tool calls, JSON Schema structured outputs, and an OpenAI-compatible endpoint. Use the native Ollama API for worker internals or its OpenAI-compatible endpoint when Eve already expects OpenAI semantics.

Relevant official references:

- [Ollama API](https://docs.ollama.com/api)
- [OpenAI compatibility](https://docs.ollama.com/openai)
- [Embeddings](https://docs.ollama.com/capabilities/embeddings)
- [Structured outputs](https://docs.ollama.com/capabilities/structured-outputs)
- [Tool calling](https://docs.ollama.com/capabilities/tool-calling)
- [Vision](https://docs.ollama.com/capabilities/vision)
- [Context and GPU memory](https://docs.ollama.com/context-length)

Set these Windows user environment variables before starting Ollama:

```text
OLLAMA_HOST=127.0.0.1:11434
OLLAMA_NO_CLOUD=1
OLLAMA_CONTEXT_LENGTH=32768
OLLAMA_NUM_PARALLEL=1
OLLAMA_MAX_LOADED_MODELS=1
OLLAMA_MAX_QUEUE=32
OLLAMA_FLASH_ATTENTION=1
OLLAMA_KV_CACHE_TYPE=q8_0
```

Why these defaults:

- 16 GB VRAM is best treated as one interactive model at a time, plus queued background work.
- A 32K context is a practical starting point. Increase only after checking `ollama ps` confirms full GPU loading and acceptable latency.
- `q8_0` KV cache and Flash Attention reduce context pressure. Validate quality on actual tasks before using `q4_0`.
- Per-request `keep_alive` controls model swapping: use `-1` for the active interactive text model and `0` for batch/vision jobs after completion.

The worker scheduler, not Ollama’s implicit queue, decides GPU priority:

1. Voice interaction and user-visible responses
2. Active Eve reasoning and tool calls
3. Query-time embedding and retrieval
4. Reranking/scoring
5. Document ingestion
6. Vision and media analysis
7. Re-indexing and Cognee promotion

## 4. Model manifest

### 4.1 Install first: benchmark candidates, not all models

Pull only the following candidates initially. Record exact tags, Ollama version, context length, full-GPU/CPU split, latency, and evaluation score in PostgreSQL.

| Role | Primary candidate | Alternate | Reason | Ollama library |
|---|---|---|---|---|
| Eve general reasoning and tools | `qwen3:14b` | `qwen3:8b` | Qwen3 explicitly supports tools and thinking; 14B is the strongest practical initial candidate for 16 GB VRAM. | [Qwen3](https://ollama.com/library/qwen3) |
| Coding specialist | `qwen2.5-coder:14b` | `qwen2.5-coder:7b` | Dedicated code generation, repair, and reasoning model. Load only for coding sessions. | [Qwen2.5 Coder](https://ollama.com/library/qwen2.5-coder) |
| Fast local embedding | `qwen3-embedding:0.6b` | `embeddinggemma:300m` | Qwen offers a 32K context and 100+ language/code retrieval positioning. Gemma is a low-memory baseline. | [Qwen3 Embedding](https://ollama.com/library/qwen3-embedding), [EmbeddingGemma](https://ollama.com/library/embeddinggemma) |
| Quality embedding | `qwen3-embedding:4b` | `bge-m3:567m` | Use selectively for curated corpus re-indexing. BGE-M3 is a compact multilingual baseline with 8K context. | [Qwen3 Embedding](https://ollama.com/library/qwen3-embedding), [BGE-M3](https://ollama.com/library/bge-m3) |
| Vision | `qwen3-vl:8b` | `qwen3-vl:4b` | Current Ollama Qwen vision worker supports image input, tools, and thinking; run only when needed. | [Qwen3-VL](https://ollama.com/library/qwen3-vl) |
| Reasoning benchmark only | `gpt-oss:20b` | none | A 14 GB Ollama artifact with tools and structured outputs. It may leave too little VRAM for desired context; benchmark it, do not make it the default without passing latency and full-GPU checks. | [gpt-oss](https://ollama.com/library/gpt-oss) |

Do not pull `qwen3:30b`, `qwen2.5-coder:32b`, `qwen3-vl:30b`, `qwen3-vl:32b`, or `gpt-oss:120b` for interactive use on this hardware. Their published Ollama artifacts exceed practical 16 GB VRAM operation once context and runtime overhead are included.

Suggested initial pulls:

```powershell
ollama pull qwen3:14b
ollama pull qwen2.5-coder:14b
ollama pull qwen3-embedding:0.6b
ollama pull qwen3-embedding:4b
ollama pull qwen3-vl:8b
ollama pull embeddinggemma:300m
```

### 4.2 Model router contract

Create a `ModelRouter` service. Callers specify a task class, not an arbitrary model name. The router applies a pinned model allowlist and returns model/version metadata with every result.

| Task class | Model | API mode | Temperature | Context target |
|---|---|---|---:|---:|
| `chat_reasoning` | selected `qwen3:14b` or `qwen3:8b` | `/api/chat` | 0.4 | 16K-32K |
| `tool_plan` | selected Qwen3 | chat + declared tools | 0.0 | 16K |
| `structured_extract` | selected Qwen3 | JSON Schema `format` | 0.0 | 8K |
| `coding` | selected Qwen Coder | chat + declared tools | 0.2 | 16K-32K |
| `embed_fast` | Qwen3 Embedding 0.6B | `/api/embed` batch | n/a | input <= 24K tokens |
| `embed_curated` | Qwen3 Embedding 4B | `/api/embed` batch | n/a | input <= 32K tokens |
| `vision_observe` | Qwen3-VL 8B | chat with image + JSON Schema | 0.0 | bounded images/prompt |
| `rerank_score` | dedicated reranker if enabled; Qwen JSON scoring otherwise | local score API or JSON Schema scores | 0.0 | top 10-50 snippets |

There is no verified `qwen3-reranker` Ollama library page as of this research. Do not design around `ollama pull qwen3-reranker`. Begin with Weaviate hybrid retrieval and reciprocal-rank fusion.

### 4.3 Optional dedicated reranker worker (recommended after baseline evaluation)

A reranker can and should be separate from Ollama when retrieval quality needs improvement. Unlike a general model, it consumes one query and a bounded candidate list and returns relevance scores. It does not need agent tools, chat history, or general text generation.

Start with [BAAI/bge-reranker-v2-m3](https://huggingface.co/BAAI/bge-reranker-v2-m3), a compact multilingual cross-encoder. Run it in a dedicated Python/CUDA environment using its documented Transformers or Sentence Transformers support. This is an intentional exception to the Ollama-default runtime rule, not a second general LLM runtime. Model weights must be pre-downloaded, version-pinned, license-reviewed, and served only on loopback.

Reranker service contract:

```text
POST /rerank
request: { query, candidates: [{ chunk_id, text }] }
limits: 50 candidates, 1 query, bounded text/token length, no URLs, no tools
response: { model_id, scores: [{ chunk_id, score }], latency_ms }
```

GPU policy:

- The retrieval worker requests a short GPU lease after Weaviate returns candidates.
- It reranks at most 50 candidates and releases the model with an idle timeout of zero or a short configurable timeout.
- Do not keep the reranker resident with `qwen3:14b` or `qwen3-vl:8b` by default on 16 GB VRAM.
- If the GPU lease is unavailable, return reciprocal-rank-fused results or use the existing Qwen JSON scorer on no more than 20 snippets.
- Compare Recall@10, MRR@10, p95 latency, and GPU swap delay before making it a default dependency.

FastMCP exposes `search_evidence(query, filters, retrieval_profile)` only. The gateway owns the reranker invocation; Eve never sees a raw reranker endpoint or selects the model.

### 4.4 Required benchmark gates

Implement an evaluation runner before changing the default models.

- 25 tool-call prompts: schema validity, correct tool selection, no undeclared tool.
- 25 structured extraction prompts: Pydantic validation success and field accuracy.
- 25 project research questions: citation/provenance accuracy from local corpus.
- 20 coding tasks: test pass rate and diff review quality.
- 20 screenshot/document tasks for the vision candidate.
- 100 retrieval queries with known relevant chunks: Recall@10, MRR@10, and latency.

Promote a model only if it is fully GPU-resident at the selected context, has no critical schema/tool failures, and improves the relevant score or latency against the incumbent. Store raw prompts and sensitive source data only where existing privacy policy allows; store redacted evaluation summaries by default.

## 5. Embedding migration: Nomic to Qwen3 Embedding

Recommendation: evaluate `qwen3-embedding:0.6b` against Nomic first. It is a justified likely upgrade for multilingual, long-context, and code retrieval, but an embedding swap invalidates vector comparability. Never mix Nomic and Qwen embeddings in one searchable collection.

Migration procedure:

1. Snapshot current Cognee, Weaviate, PostgreSQL metadata, and model configuration. Confirm restore steps.
2. Add a new index generation, for example `knowledge_qwen3e06_v1`; preserve Nomic collections unchanged.
3. Reuse the identical normalized document/chunk inputs and metadata. Record source hash, chunker version, embedding model/tag, vector dimensions, and index generation.
4. Batch embed with `/api/embed`; Ollama returns normalized vectors. Use cosine similarity and the same model for indexing and query.
5. Run the retrieval evaluation set against Nomic and Qwen indices in parallel.
6. Route a small percentage of non-critical retrieval to the candidate, then promote only if the evaluation gate passes.
7. For Cognee, create or rebuild a separate dataset/namespace using its documented local Ollama configuration. Do not mutate an existing graph/index in place unless the installed Cognee version documents a complete rebuild operation.
8. Keep the old Nomic index until backup restore and rollback have been tested. Delete only through an approved maintenance job.

Cognee must receive only reviewed durable memories: decisions, confirmed user preferences, stable project facts, validated research findings, and resolved task outcomes. Raw chats, full documents, tool traces, and transient observations stay in PostgreSQL/artifacts and Weaviate.

References: [Cognee local Ollama guide](https://docs.cognee.ai/guides/local-ollama), [Cognee repository](https://github.com/topoteretes/cognee).

## 6. Worker and storage contracts

### 6.1 PostgreSQL tables

Create migrations for these minimum tables:

```text
artifacts(id, sha256, media_type, storage_uri, byte_size, created_at)
sources(id, source_type, original_name, artifact_id, content_hash, trust_level, captured_at)
documents(id, source_id, parser_version, status, normalized_artifact_id, metadata_json)
document_chunks(id, document_id, chunk_index, text, token_count, offset_json, chunk_hash)
index_generations(id, name, embedding_model, embedding_tag, dimensions, chunker_version, status)
index_records(id, index_generation_id, chunk_id, external_vector_id, indexed_at)
gpu_jobs(id, job_type, priority, status, idempotency_key, input_artifact_id, output_artifact_id, requested_at, started_at, completed_at, error_json)
approvals(id, action_type, request_hash, actor_id, status, expires_at, decided_at)
tool_audit(id, trace_id, tool_name, validated_input_json, approval_id, result_summary, artifact_id, duration_ms, created_at)
memory_promotions(id, source_id, candidate_json, review_status, cognee_dataset, promoted_at)
model_evaluations(id, role, model_tag, ollama_version, options_json, scores_json, promoted_at)
```

Every job must be idempotent. Queue workers using `FOR UPDATE SKIP LOCKED`, a lease/heartbeat, bounded retries, and a dead-letter status. The job table is the source of truth; PocketBase only mirrors status needed by the UI.

### 6.2 Document pipeline

Use [Docling](https://github.com/docling-project/docling) as the default structured document worker. It is MIT-licensed, supports Windows/Python 3.10+, local operation, high-quality PDF layout/OCR/tables, Markdown and lossless JSON export, and can be run through a local MCP/API boundary.

Use [MarkItDown](https://github.com/microsoft/markitdown) only for fast/simple conversion. Keep it optional and never expose arbitrary input paths.

Pipeline:

```text
PocketBase upload or approved local artifact
  -> immutable artifact + hash
  -> document job
  -> Docling normalized Markdown + JSON + page/table offsets
  -> deterministic chunker
  -> selected index generation in Weaviate
  -> retrieval evaluation / review
  -> optional Cognee memory-promotion candidate
```

FastMCP document tools:

- `inspect_document(document_id)`
- `extract_structured_document(document_id, profile)`
- `extract_tables(document_id)`
- `render_document_pages(document_id, page_numbers)`
- `create_document_summary_artifact(document_id, instruction_profile)`

All tools accept IDs, never URLs or raw filesystem paths. Outputs are bounded JSON plus artifact IDs.

### 6.3 Retrieval pipeline

```text
query -> query classification -> Weaviate hybrid search + metadata filters
      -> reciprocal-rank fusion -> optional bounded rerank_score
      -> top evidence blocks with source/chunk/page provenance
      -> Eve answer with evidence references and freshness state
```

Mandatory retrieval metadata:

```text
source_type, source_id, document_id, chunk_id, document_hash,
index_generation, embedding_model, captured_at, snapshot_version,
project_id, trust_level, review_status, promotion_status
```

For local Wikipedia, preserve snapshot/version date and show it when an answer relies on that corpus. Never let a synthesis response claim current web freshness while offline.

### 6.4 Voice and media

Speech is intentionally outside Ollama; it is a local specialist worker.

- STT: [whisper.cpp](https://github.com/ggml-org/whisper.cpp), MIT. It supports Windows, CUDA, VAD, local HTTP, streaming, and timestamped transcription. Start with `base` or `small`, evaluate `large-v3-turbo` only as a queued batch job.
- TTS: [Piper](https://github.com/OHF-Voice/piper1-gpl), GPL-3.0. It provides a CLI, HTTP service, Python, and C/C++ APIs. Keep it as a separable process because GPL obligations may matter for distribution.
- Media preprocessing: FFmpeg fixed-command wrappers writing only into an artifact directory.

Start voice UX with push-to-talk and a stop button. Add VAD and barge-in only after transcription and cancellation behavior are reliable.

### 6.5 Vision and desktop observation

Use Qwen3-VL for screenshot, chart, and visual-document interpretation. Constrain outputs with a JSON Schema. Images must be converted into bounded artifact references before they reach the model.

For desktop perception, begin with Windows UI Automation via `pywinauto` and screenshots. Add [OmniParser](https://github.com/microsoft/OmniParser) only after the observe-only workflow works; its repository is CC-BY-4.0 and components/weights have separate terms. The current YOLOv9-E detector is MIT-derived while older Ultralytics components are AGPL.

Never permit autonomous desktop input. Separate observer tools from approved action tools:

- observer: list windows, inspect UIA tree, screenshot redaction, locate candidate controls
- action: click, type, shortcut, submit, download, delete

Each action requires a short-lived approval token tied to its exact target and input sequence.

## 7. FastMCP gateway requirements

Build one gateway with separate modules, not a broad aggregation proxy:

```text
fastmcp/
  gateway.py
  authz.py
  audit.py
  artifacts.py
  model_router.py
  servers/
    retrieval.py
    documents.py
    analytics.py
    voice.py
    system.py
    desktop_observer.py
```

Gateway enforcement:

- Resolve inputs through database IDs and canonical allowlisted roots.
- Reject URL inputs unless a separate approved ingestion flow has fetched and stored an artifact.
- Validate all request/response models with Pydantic.
- Limit input bytes, result rows, execution time, concurrent jobs, and artifact size.
- Send argument arrays, never shell strings, to CLI-backed workers.
- Redact secrets, usernames, command lines, and raw document content from default audit logs.
- Write a tool audit event on success, failure, denial, and timeout.

Useful local capabilities to add after the document/retrieval foundation:

| Priority | Component | Narrow surface |
|---|---|---|
| P0 | DuckDB + Polars | profile, compare, aggregate, and chart-data operations against catalogued datasets |
| P0 | psutil | read-only CPU, GPU, memory, disk, and worker health summary |
| P1 | Tesseract/OCRmyPDF/pypdf | fallback OCR, searchable PDF artifact, and basic PDF inspection |
| P1 | Pandoc/LibreOffice | fixed-format conversion into output artifacts |
| P1 | FFmpeg/ImageMagick | metadata, frame/audio extraction, and transforms into output artifacts |
| P2 | Playwright | approved local/LAN origins only; approval for submit, upload, and download |
| P2 | pywinauto | observe-only, then token-approved semantic actions |
| P3 | Docker CLI | named read-only status tools; distinct approved lifecycle operations only |

## 8. Connectivity and privacy behavior

Use `network_state = online | degraded | offline`.

- `online`: local retrieval first, then permitted external research workers.
- `degraded`: return local findings with freshness limits and queue requested external research.
- `offline`: do not attempt external access. Use local Wikipedia, documents, Weaviate, Cognee, and local models. Label source freshness with snapshot/capture dates.

Set Ollama local-only mode with `OLLAMA_NO_CLOUD=1`. Do not expose `11434` to the LAN. If LAN access is necessary later, place an authenticated gateway in front of Ollama instead of changing it to a public bind.

## 9. Implementation sequence and acceptance criteria

### Phase 0: inventory and guardrails

1. Capture versions, Docker services, ports, volumes, model paths, existing schemas, and current Cognee/Weaviate configuration.
2. Add an environment validation command that fails on missing services, non-loopback Ollama, unapproved model tags, and inaccessible artifact roots.
3. Add PostgreSQL migrations and an artifact directory with content hashing.

Accept when: a fresh health report identifies every service, model, index generation, and current network state without exposing secrets.

### Phase 1: Ollama model evaluation and retrieval migration

1. Pull benchmark candidates from section 4.1.
2. Implement `ModelRouter`, structured-output schemas, and evaluation runner.
3. Build a parallel Qwen3 Embedding 0.6B Weaviate index and compare it with Nomic.
4. Promote the winning index through configuration, not hard-coded model names.

Accept when: all selected structured outputs validate, retrieval scores are recorded, rollback routes queries to Nomic, and no collection mixes vector spaces.

### Phase 2: provenance-first document ingestion

1. Add Docling worker and document/job/artifact tables.
2. Add deterministic chunking, source/page/table offsets, Weaviate indexing, and retrieval citations.
3. Expose only the five document FastMCP tools in section 6.2.

Accept when: a PDF, DOCX, XLSX, and scanned PDF are ingested into versioned artifacts; a retrieved answer resolves to a source and page/chunk; failed jobs are retryable without duplicate records.

### Phase 3: voice and scheduling

1. Add whisper.cpp and Piper as local worker processes with health endpoints.
2. Add push-to-talk, cancellation, audio artifact retention policy, and transcript provenance.
3. Activate the PostgreSQL GPU queue and ensure interactive requests preempt batch launches.

Accept when: voice transcription is cancellable, TTS never blocks an interactive model response, and an ingestion job cannot make active chat time out.

### Phase 4: vision and supervised workstation automation

1. Add Qwen3-VL worker with JSON Schema outputs for screenshot/chart/document tasks.
2. Add `pywinauto` observe-only tools and screenshot redaction.
3. Add approval-bound input tools only after reviewing action audit UX.
4. Evaluate OmniParser with pinned component licenses only if UIA coverage is inadequate.

Accept when: visual outputs are schema-valid, action proposals cite observed controls, and no desktop input can occur without a valid single-use approval.

## 10. Explicit non-goals

- No automatic Cognee promotion from arbitrary conversation text.
- No generic model prompt passthrough tool for Eve.
- No direct raw SQL tool for an LLM.
- No unrestricted filesystem or Docker tool.
- No public Ollama port, cloud fallback, or background web search in offline mode.
- No simultaneous always-loaded 14B text, 8B vision, 4B embeddings, and 20B reasoning models on 16 GB VRAM.

## 11. Cursor implementation directive

Implement phases in order. Before each phase, inspect existing code and configuration, preserve user changes, and add only the smallest compatible change. Use feature flags for new workers and model/index selection. Every worker must have health checks, bounded timeouts, structured logs, and integration tests using local fixtures. Do not download models, modify production indexes, delete artifacts, migrate persistent data, or enable desktop input without an explicit user confirmation.

## 12. Target-project contract and preflight gate

This document is portable research for Cursor to apply on a different computer. It is not an inventory of that target computer. Cursor must inspect the target repository and runtime before proposing or applying changes. The following declared components already exist and must be extended in place:

| Component | Owner | Responsibility | Must not become |
|---|---|---|---|
| HMXL + existing GUI | client/presentation | conversation UI, stream rendering, microphone/speaker I/O, approval UI | a second agent orchestrator or direct tool executor |
| Vercel Eve | agent | planning, task delegation, tool selection, approval requests, response synthesis | a raw filesystem, SQL, shell, Docker, or model-management client |
| FastMCP gateway | capability boundary | typed authorization, tool invocation, worker routing, audit events | a generic MCP proxy or unrestricted execution service |
| Ollama | native Windows model runtime | approved text, coding, embedding, and vision inference | a public/LAN endpoint or source of unbounded model selection |
| PostgreSQL | authority | jobs, leases, approvals, artifacts, audit, configuration, evaluation, provenance | a UI cache |
| PocketBase | UI projection | user-facing records, uploads, realtime status projection | a competing authoritative workflow store |
| Weaviate | working retrieval | local Wikipedia and versioned document-vector indexes | a durable memory graph |
| Cognee | curated memory | promoted facts, relationships, validated lessons | raw chat/tool/artifact storage |

Before installing packages, pulling models, changing environment variables, migrating any persistent store, or enabling a new worker, Cursor must perform and present a read-only preflight report containing:

1. Repository structure, existing conventions, language/package managers, existing tests, and Eve/HMXL integration points.
2. Current versions and health of Ollama, Docker/WSL GPU support, NVIDIA driver, PostgreSQL, PocketBase, Weaviate, Cognee, and FastMCP.
3. Listening ports, bind addresses, persistent volumes, artifact roots, existing model tags/Modelfiles, existing vector collections/indexes, and configured embedding dimensions.
4. Existing PostgreSQL schemas and PocketBase collections relevant to jobs, chat, uploads, tasks, and approvals.
5. Backup commands and a verified restoration procedure for PostgreSQL, PocketBase data, Weaviate, Cognee, and artifact volumes.

Stop and request confirmation before the first persistent change. Cursor must not infer state from this handoff or replace working components merely because this manifest lists a newer alternative.

## 13. Deployment, configuration, and worker transport

Use hybrid deployment:

- Run Ollama natively on Windows and bind it to `127.0.0.1:11434`.
- Run stateless specialist workers as isolated Python environments or GPU-enabled Docker/WSL2 containers, selected per upstream Windows/CUDA compatibility.
- Run PostgreSQL, PocketBase, Weaviate, Cognee, and observability services using the target project's existing deployment pattern; do not migrate them just for consistency.
- Bind every worker to loopback. The FastMCP gateway is the only caller permitted to reach worker endpoints. Worker ports are configuration values, not hard-coded public interfaces.

Workers expose narrow loopback HTTP APIs with OpenAPI/Pydantic schemas. CLI tools are executed only inside the owning worker using fixed argument arrays. FastMCP tools invoke gateway services, never a binary directly. Realtime audio is the exception: HMXL communicates with the persistent voice service over an authenticated local WebSocket or WebTransport connection; no MCP request is made per audio packet.

Use a single versioned configuration source and environment overrides only for secrets. Required feature flags:

```text
ENABLE_PARALLEL_EMBEDDING_INDEX=false
ENABLE_DOCLING_INGESTION=false
ENABLE_REALTIME_VOICE=false
ENABLE_STANDALONE_RERANKER=false
ENABLE_VISION_WORKER=false
ENABLE_IMAGE_WORKER=false
ENABLE_DESKTOP_OBSERVER=false
ENABLE_DESKTOP_ACTIONS=false
ENABLE_EXTERNAL_RESEARCH=false
ACTIVE_EMBEDDING_GENERATION=<existing-nomic-generation>
```

Model configuration records must contain role, artifact/tag, immutable digest or local weight hash, source/license, runtime, context limit, VRAM class, benchmark status, and rollback predecessor. Pin container images and package lockfiles. Never use floating `latest` for a production worker or model selection.

## 14. GPU lease manager and execution limits

The 16 GB GPU is a scheduled shared resource. The 64 GB RAM budget supports queues, artifacts, and CPU fallback; it does not make GPU models concurrently affordable. Use PostgreSQL-backed leases rather than trusting each runtime to self-coordinate.

```text
queued -> leasing -> loading -> running -> releasing -> completed
                         |              |
                         +-> cancelled  +-> failed / dead_letter
```

`GpuLeaseRequest` fields: `job_id`, `workload_class`, `model_role`, `priority`, `min_vram_mb`, `max_duration_seconds`, `preemptible`, `idempotency_key`. The response includes `lease_id`, `expires_at`, and `fallback_profile`. Workers heartbeat every 10 seconds; leases expire after 30 seconds without heartbeat. A worker must release its lease and unload/evict the model on completion, cancellation, or lease loss.

Priority and default maximum lease duration:

| Priority | Workload | Maximum lease | Behavior when unavailable |
|---:|---|---:|---|
| P0 | voice VAD/STT and playback interruption | 30 seconds | CPU/low-quality fallback; never wait behind batch work |
| P1 | active Eve response/tool planning | 120 seconds | preempt queued P2-P7 work |
| P2 | query embeddings and retrieval | 20 seconds | hybrid lexical/vector fallback |
| P3 | dedicated reranking | 10 seconds | reciprocal-rank fusion fallback |
| P4 | document/OCR ingestion | 10 minutes | queue |
| P5 | vision | 90 seconds | queue or ask user to retry |
| P6 | image generation/editing | 15 minutes | queue |
| P7 | re-indexing, Cognee promotion, maintenance | 30 minutes | queue |

Never forcibly terminate an actively responding P1 request merely to run a background task. P0 barge-in stops TTS immediately and cancels or marks the related P1 response as superseded. When a higher priority request cannot fit, first cancel queued lower-priority work, then release idle lower-priority model leases, then use the defined fallback. Emit an audit event for every preemption/cancellation.

Default hard limits:

| Operation | Input limit | Output limit | Timeout | Concurrency |
|---|---:|---:|---:|---:|
| `search_evidence` | 8K query tokens | 10 evidence blocks | 10 s | 5 CPU / 1 GPU rerank |
| standalone rerank | 50 candidates, 512 tokens each | 50 scores | 5 s | 1 |
| structured text/vision inference | 64 KB request text, 4 images | 32 KB JSON | 90 s | 1 GPU |
| document ingestion | 100 MB source | 50 MB normalized output | 10 min | 1 |
| dataset analysis | registered dataset only | 1,000 rows or artifact | 60 s | 2 |
| image workflow | 25 MB source image | 500 MB artifact | 15 min | 1 |
| desktop observation | 2 redacted screenshots | 200 controls | 15 s | 1 |

## 15. Complete capability inventory

| Capability | Implementation | Eve-facing surface | GPU lane | Approval |
|---|---|---|---|---|
| General reasoning, tool plans, JSON | Ollama Qwen3 | typed chat/task tools | P1 | no |
| Coding | Ollama Qwen2.5 Coder | typed coding task | P1 | write actions separate |
| Embeddings | Ollama Nomic incumbent, Qwen3 candidates | internal retrieval service | P2/P7 | index promotion only |
| Retrieval | Weaviate hybrid + metadata/RRF | `search_evidence` | CPU/P2 | no |
| Precision rerank | BGE reranker v2 M3 worker | internal only | P3 | no |
| Durable memory | Cognee | `propose_memory_promotion` | P7 | policy dependent |
| Document ingestion | Docling; pypdf/Tesseract/OCRmyPDF fallback | document ID tools | P4 | source replacement only |
| Tabular analysis | DuckDB + Polars | registered dataset tools | CPU | no |
| Audio transcription | faster-whisper + Silero VAD | voice events; transcript tools | P0/P4 | recording consent |
| Speech synthesis | Piper | HMXL audio stream | CPU | no |
| Voice post-processing | WhisperX, optional | queued transcript enrichment | P4 | no |
| Vision/OCR validation | Ollama Qwen3-VL; optional PaddleOCR benchmark | artifact ID tools | P5 | no |
| Image generation/editing | ComfyUI preferred; InvokeAI alternative | named workflow job | P6 | source edit/workflow change |
| Media transform | FFmpeg/ImageMagick | artifact ID tools | CPU/P6 | source replacement only |
| Browser observation | Playwright, local/allowlisted LAN only | observation tools | CPU | navigation no; submit/upload/download yes |
| Desktop observation | pywinauto; OmniParser only for UIA gaps | observation tools | CPU/P5 | no |
| Desktop input | pywinauto/PyAutoGUI fallback | explicit action tools | CPU | always |
| System health | psutil + runtime probes | `get_system_health` | CPU | no |

Do not add vLLM, Qdrant, Chroma, ColBERT, Redis, a second agent framework, generic Git/filesystem/database MCP server, or general command runner by default. Add any of them only after a measured limitation cannot be met by the declared stack. In particular, Weaviate already owns retrieval, and PostgreSQL already owns durable queues.

## 16. Realtime voice implementation contract

Use `faster-whisper` for the real-time transcription worker and Silero VAD via local ONNX/CPU. Both are local, and faster-whisper provides a maintained CTranslate2 GPU path. Use `Piper` for initial local TTS. Keep WhisperX as an opt-in asynchronous post-processing job for word timing/diarization; its diarization path may require a separate model acceptance/token, so it cannot be a baseline no-account requirement.

References: [faster-whisper](https://github.com/SYSTRAN/faster-whisper), [Silero VAD](https://github.com/snakers4/silero-vad), [Piper](https://github.com/OHF-Voice/piper1-gpl), [WhisperX](https://github.com/m-bain/whisperX).

```text
HMXL microphone capture
  -> echo cancellation/noise suppression
  -> 20 ms Opus packets over authenticated local stream
  -> voice service: decode to 16 kHz mono PCM -> CPU VAD -> bounded utterance buffer
  -> partial/final faster-whisper events -> HMXL live transcript
  -> final text -> Eve stream -> Piper streaming output -> HMXL playback
```

Voice event schema: `voice.started`, `voice.partial`, `voice.final`, `voice.no_speech`, `voice.cancelled`, `voice.barge_in`, `voice.error`, `tts.started`, `tts.chunk`, `tts.cancelled`, `tts.completed`. Every event carries `session_id`, `turn_id`, `trace_id`, `sequence`, and `timestamp`.

- Internal audio is 16 kHz mono PCM; client packets are 20 ms Opus frames.
- Segment an utterance after 500-800 ms configurable silence or 30 seconds maximum duration.
- Target partial text within 750 ms of speech onset, final text within 1.5 seconds of endpoint, and first TTS audio within 750 ms of first response text. Treat these as benchmarks, not promises, until measured on target hardware.
- A barge-in event stops playback in under 250 ms, drops buffered TTS, and cancels/supersedes the linked Eve trace.
- Connection resume accepts the last acknowledged event sequence; duplicate packets/events must be idempotent.
- Persist final transcript and configuration provenance. Partial transcripts are ephemeral. Default raw audio retention is 72 hours, configurable by the user; delete through an approved retention job.

Moshi is explicitly not a baseline recommendation: its documented PyTorch path needs substantially more than 16 GB for full quality and Windows support is not primary. It may be evaluated later as a separate research experiment, never as a replacement for the reliable STT -> Eve -> TTS pipeline.

## 17. Retrieval, memory, and artifact lifecycle

### Nomic-safe embedding migration

Cursor must not alter or delete current Nomic collections, vectors, dimensions, or query routing during evaluation. Build a parallel `index_generation` from identical normalized chunks. Each record includes `chunk_hash`, `source_hash`, `chunker_version`, embedding model/tag/hash, dimensions, and collection name. The promotion condition is user approval after candidate Recall@10 is at least the Nomic baseline and candidate p95 latency is no more than 10% worse. Retain Nomic as read-only rollback for 30 days after promotion; deletion is a separate explicit approval.

### Reranking

Use Weaviate hybrid retrieval plus reciprocal-rank fusion first. When `ENABLE_STANDALONE_RERANKER=true`, use [BAAI/bge-reranker-v2-m3](https://huggingface.co/BAAI/bge-reranker-v2-m3), Apache-2.0, as a separate local CUDA worker. It accepts one query plus bounded candidates and returns only scores. It has no tools, chat history, arbitrary URL, or arbitrary prompt endpoint. FastMCP calls it internally after a P3 GPU lease; it falls back to RRF if unavailable. Enable only after it improves MRR@10 or nDCG@10 by at least 5% without violating the retrieval p95 target.

### Cognee promotion states

`candidate -> auto_eligible | pending_user_review -> approved | rejected -> promoted | failed`.

Auto-eligible content is limited to a trusted, versioned source with deterministic extraction/validation or a completed task outcome with passing validation. Conversations, inferred preferences, unverified research, and model-only claims require user approval. Store evidence/source IDs, a concise candidate statement, validation result, and policy decision; do not store a raw full conversation by default. Rebuild into a separate versioned Cognee dataset whenever embedding generation changes.

Artifacts are immutable content-addressed records with media type, source lineage, retention class, lifecycle state, and deletion approval reference. User uploads persist until user deletion. Processing intermediates expire after successful verification. Final voice transcripts follow the project retention policy; raw audio defaults to 72 hours. Never delete a referenced artifact before its dependent job/index/memory records are retired.

## 18. Images, vision, automation, connectivity, and observability

### Image and vision lane

Use Qwen3-VL through Ollama for observation, OCR validation, charts, screenshots, and visual-document gaps. Use JSON Schema outputs and artifact IDs. For local image generation/editing, use [ComfyUI](https://github.com/Comfy-Org/ComfyUI) as the primary engine: it has a local API, asynchronous queue, versioned workflow JSON, offline operation with `--disable-api-nodes`, Windows support, and explicit VRAM/RAM offload. [InvokeAI](https://github.com/invoke-ai/InvokeAI) is a valid alternative when its curated canvas/API better fits the target project's existing design.

FastMCP may submit only named, versioned workflow templates: `generate_image`, `variation`, `inpaint`, `outpaint`, `upscale`, `segment_mask`, `remove_background`. Eve cannot submit arbitrary workflow JSON, install custom nodes, pull models, or alter a workflow definition. Source-image editing and workflow-definition changes require approval. Run exactly one image job at a time; it must release its P6 lease before P0/P1 work proceeds. Review every model-weight license individually; FLUX dev/Kontext weights are not assumed commercially usable.

### Desktop/browser approval state machine

```text
observe -> redact -> create action draft -> user approval -> re-observe/verify
        -> execute once -> verify result -> audit
```

An approval is single-use, expires in 10 minutes, and binds `actor_id`, `trace_id`, action type, exact normalized arguments, target UIA selector or observed-region hash, and screenshot/UI-tree revision. Any target/revision mismatch invalidates it. Observation precedes all action drafts. Desktop redaction occurs before persistence or model input: redact password controls, configured sensitive window titles, user-defined regions, and secret/PII patterns. Default to pywinauto/UIA; use OmniParser only where UIA cannot identify controls. Playwright is restricted to approved local/LAN origins. No tool may enter credentials, submit a form, send a message, approve a purchase, delete data, or download/upload without approval.

### Connectivity and health

`network_state` is set by explicit user override or a configurable, non-sensitive connectivity probe. `online` uses local retrieval first and queues permitted external work only if needed; `degraded` returns local evidence and queues external requests; `offline` performs no external request and labels answers: `Offline mode: conclusions use local sources captured through <latest-source-date>.`

Return a redacted loopback `/health` payload with service status, loaded models, VRAM free/total, queue depth by priority, lease count, active index generation, Cognee dataset, feature flags, network state, and timestamp. Emit JSON logs and OpenTelemetry spans with `trace_id`, service, action, duration, status, model/index/workflow version, and redacted error code. Add Prometheus/Grafana/OpenTelemetry Collector only after the core worker path works. Alert on unavailable services, stalled jobs, expired leases, disk below 10%, VRAM above 90%, failed backups, and evaluation regression.

## 19. Required implementation sequence and objective acceptance tests

1. **Preflight and rollback:** produce the report in section 12 and prove one non-production restore. No mutation until confirmed.
2. **Foundation:** add feature flags, configuration validation, artifact/audit/job/lease schema additions, and `/health`. Test that unapproved mutation, arbitrary path, raw SQL, raw shell, model pull, and arbitrary workflow requests are rejected.
3. **Model router and retrieval:** add model-role allowlists, GPU leases, parallel Nomic/Qwen index generation, and fixed retrieval evaluation. Prove no index contains mixed model/dimension vectors and Nomic rollback works.
4. **Documents/data/media:** add Docling and typed analytics/media tools with fixtures for PDF, scanned PDF, DOCX, XLSX, CSV, Parquet, image, audio, and video. Every output must have a hash, source lineage, retention class, and audit trace.
5. **Realtime voice:** add the section 16 event protocol and fixtures for silence, noise, partial/final text, reconnect, cancellation, barge-in, TTS interruption, and device failure. Report p50/p95 latency and dropped events.
6. **Reranking and memory:** evaluate BGE reranking against RRF, enable only if the stated metric gate passes, and test every Cognee promotion state including rejected and failed.
7. **Vision and image workflows:** validate schema-constrained vision output and run every named image workflow with local fixtures. Assert only one P6 job runs and P0/P1 preemption works.
8. **Observation and supervised actions:** test redaction, stale-snapshot rejection, expired approval rejection, and one harmless fixture-app action end to end before exposing any real desktop/browser input capability.
9. **Observability hardening:** trace an end-to-end voice/retrieval/document/image flow by `trace_id`; test worker crash recovery, dead-letter handling, backup verification, offline behavior, and job priority ordering.

Cursor should deliver each numbered slice as a reviewable change with tests, migration/rollback notes, configuration additions, and evidence of the stated acceptance test. Do not proceed to the next slice if its predecessor fails its objective checks.

## 20. Canonical implementation resource registry

Use these canonical upstream resources when implementing this manifest. Pin a release, commit, container digest, or model-weight hash after target-machine evaluation; links are discovery sources, not approval to install everything. Read license and model-card terms before any download. HMXL and Vercel Eve are existing target-project components: Cursor must discover their actual packages, repositories, versions, and integration contracts during preflight rather than substituting a similarly named public project.

### Core runtime and protocol

| Resource | Canonical link | Use |
|---|---|---|
| Ollama runtime | [Repository](https://github.com/ollama/ollama), [Windows download](https://ollama.com/download), [API](https://docs.ollama.com/api), [OpenAI compatibility](https://docs.ollama.com/openai) | Native Windows local model server and OpenAI-compatible integration point |
| Ollama settings | [FAQ](https://docs.ollama.com/faq), [context length](https://docs.ollama.com/context-length), [Modelfile](https://docs.ollama.com/modelfile) | Bind address, cloud disablement, context/KV cache, residency, and model configuration |
| Model Context Protocol | [Specification](https://modelcontextprotocol.io/specification/2025-11-25), [Python SDK](https://github.com/modelcontextprotocol/python-sdk) | MCP protocol reference; do not expose broad reference-server tools by default |
| FastMCP | [Repository](https://github.com/jlowin/fastmcp), [documentation](https://gofastmcp.com/) | Typed local gateway, Pydantic schemas, authorization middleware, and audit boundary |
| Docker GPU support | [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit), [Docker Compose](https://docs.docker.com/compose/) | Validate before using GPU-enabled worker containers on Windows/WSL2 |

### Ollama models

| Role | Ollama pull target | Canonical model page | Selection rule |
|---|---|---|---|
| General agent | `qwen3:14b` | [Qwen3](https://ollama.com/library/qwen3) | Default candidate; compare with the existing Qwen 2.5 model before replacement |
| Faster general fallback | `qwen3:8b` | [Qwen3 tags](https://ollama.com/library/qwen3/tags) | Use for low-latency/fallback tests |
| Coding | `qwen2.5-coder:14b` | [Qwen2.5 Coder](https://ollama.com/library/qwen2.5-coder) | Load only for coding-specialist work |
| Fast embeddings | `qwen3-embedding:0.6b` | [Qwen3 Embedding](https://ollama.com/library/qwen3-embedding) | Candidate replacement for Nomic; requires a parallel index |
| Curated embeddings | `qwen3-embedding:4b` | [Qwen3 Embedding tags](https://ollama.com/library/qwen3-embedding/tags) | Batch-only candidate; not permanently resident |
| Small embedding baseline | `embeddinggemma:300m` | [EmbeddingGemma](https://ollama.com/library/embeddinggemma) | Low-memory benchmark baseline |
| Alternative multilingual embedding | `bge-m3:567m` | [BGE-M3](https://ollama.com/library/bge-m3) | Benchmark only if Qwen/Nomic evaluation is insufficient |
| Vision | `qwen3-vl:8b` | [Qwen3-VL](https://ollama.com/library/qwen3-vl) | Queue-loaded visual worker; use 4B only if 8B misses latency/memory gate |
| Reasoning experiment | `gpt-oss:20b` | [gpt-oss](https://ollama.com/library/gpt-oss) | Evaluation-only; do not promote without full-GPU/context evidence |

The existing Nomic deployment is the retrieval baseline. Cursor must record its exact tag/digest/dimensions and retain its collections untouched until the explicitly approved migration gate passes. There is no approved Ollama `qwen3-reranker` dependency in this design.

### Retrieval, memory, and storage

| Resource | Canonical link | Use |
|---|---|---|
| Weaviate | [Repository](https://github.com/weaviate/weaviate), [documentation](https://docs.weaviate.io/) | Existing working retrieval store and hybrid search target |
| Cognee | [Repository](https://github.com/topoteretes/cognee), [local Ollama guide](https://docs.cognee.ai/guides/local-ollama), [configuration](https://docs.cognee.ai/setup-configuration/overview) | Existing curated memory layer; use separate dataset generations for embedding changes |
| PostgreSQL | [Repository](https://github.com/postgres/postgres), [documentation](https://www.postgresql.org/docs/) | Existing authority for durable jobs, leases, audit, provenance, and configuration |
| PocketBase | [Repository](https://github.com/pocketbase/pocketbase), [documentation](https://pocketbase.io/docs/) | Existing UI/realtime projection and upload layer |
| BGE reranker | [model card](https://huggingface.co/BAAI/bge-reranker-v2-m3), [FlagEmbedding](https://github.com/FlagOpen/FlagEmbedding), [Sentence Transformers](https://github.com/UKPLab/sentence-transformers) | Optional standalone P3 scoring worker; Apache-2.0 model card; no agent-facing raw endpoint |

### Realtime voice

| Resource | Canonical link | Use |
|---|---|---|
| faster-whisper | [Repository](https://github.com/SYSTRAN/faster-whisper), [PyPI](https://pypi.org/project/faster-whisper/) | Default local GPU STT via CTranslate2; supports word timestamps and integrated VAD filtering |
| Silero VAD | [Repository](https://github.com/snakers4/silero-vad), [PyPI](https://pypi.org/project/silero-vad/) | CPU/ONNX utterance endpoint detection; pin weights locally |
| Piper | [Repository](https://github.com/OHF-Voice/piper1-gpl), [voices](https://github.com/OHF-Voice/piper1-gpl/blob/main/docs/VOICES.md), [HTTP API](https://github.com/OHF-Voice/piper1-gpl/blob/main/docs/API_HTTP.md) | Default local streaming/CLI TTS; GPL-3.0 code and individual voice terms require review |
| WhisperX | [Repository](https://github.com/m-bain/whisperX) | Optional queued word alignment and diarization, not a realtime dependency |
| whisper.cpp | [Repository](https://github.com/ggml-org/whisper.cpp) | Optional low-dependency STT fallback and benchmark reference |
| Moshi | [Repository](https://github.com/kyutai-labs/moshi) | Research-only full-duplex experiment; not a baseline for this Windows/16 GB target |

### Documents, OCR, analysis, and media

| Resource | Canonical link | Use |
|---|---|---|
| Docling | [Repository](https://github.com/docling-project/docling), [documentation](https://docling-project.github.io/docling/) | Primary local structured document conversion and layout/OCR extraction |
| MarkItDown | [Repository](https://github.com/microsoft/markitdown), [documentation](https://github.com/microsoft/markitdown/tree/main/docs) | Optional fast/simple local document conversion; worker restricts input roots |
| Tesseract | [Repository](https://github.com/tesseract-ocr/tesseract), [Windows installer source](https://github.com/UB-Mannheim/tesseract/wiki) | Fallback local OCR |
| OCRmyPDF | [Repository](https://github.com/ocrmypdf/OCRmyPDF), [documentation](https://ocrmypdf.readthedocs.io/) | Generate searchable PDF artifacts only |
| pypdf | [Repository](https://github.com/py-pdf/pypdf), [documentation](https://pypdf.readthedocs.io/) | Basic controlled PDF inspection/extraction |
| PaddleOCR | [Repository](https://github.com/PaddlePaddle/PaddleOCR), [documentation](https://www.paddleocr.ai/) | Later benchmark for high-volume/complex OCR; do not install before Docling baseline is measured |
| DuckDB | [Repository](https://github.com/duckdb/duckdb), [documentation](https://duckdb.org/docs/) | Registered-dataset query/profile/aggregate work |
| Polars | [Repository](https://github.com/pola-rs/polars), [documentation](https://docs.pola.rs/) | Typed dataset comparison/analysis work |
| FFmpeg | [Repository](https://github.com/FFmpeg/FFmpeg), [documentation](https://ffmpeg.org/documentation.html) | Fixed-schema audio/video extraction and transcoding |
| ImageMagick | [Repository](https://github.com/ImageMagick/ImageMagick), [security policy](https://imagemagick.org/script/security-policy.php) | Fixed-schema image transform worker with restrictive policy.xml |
| Pandoc | [Repository](https://github.com/jgm/pandoc), [documentation](https://pandoc.org/) | Sandboxed document conversions |
| LibreOffice | [Repository](https://github.com/LibreOffice/core), [headless documentation](https://help.libreoffice.org/latest/en-US/text/shared/guide/start_parameters.html) | Isolated-profile office conversion/recalculation |

### Visual understanding and image generation/editing

| Resource | Canonical link | Use |
|---|---|---|
| Qwen3-VL | [Ollama model page](https://ollama.com/library/qwen3-vl), [Ollama vision API](https://docs.ollama.com/capabilities/vision) | Primary vision, chart/screenshot understanding, and visual validation |
| OmniParser | [Repository](https://github.com/microsoft/OmniParser), [model weights](https://huggingface.co/microsoft/OmniParser-v2.0) | Optional screen-region parser only when UI Automation is inadequate; review component licenses |
| ComfyUI | [Repository](https://github.com/Comfy-Org/ComfyUI), [API example](https://github.com/Comfy-Org/ComfyUI/blob/master/script_examples/basic_api_example.py), [workflows](https://comfy.org/workflows) | Preferred queued local image generation/editing engine; use `--disable-api-nodes` for offline-only operation |
| InvokeAI | [Repository](https://github.com/invoke-ai/InvokeAI), [documentation](https://invoke-ai.github.io/InvokeAI/) | Alternative local image workflow/canvas engine; choose instead of, not alongside, ComfyUI unless a measured need exists |
| Diffusers | [Repository](https://github.com/huggingface/diffusers), [documentation](https://huggingface.co/docs/diffusers/) | Library-level fallback for a narrow custom image worker; do not create one if ComfyUI/InvokeAI covers the workflow |
| FLUX licenses | [official repository/model license table](https://github.com/black-forest-labs/flux) | Verify before any FLUX model adoption; do not assume dev/Kontext weights are commercial-use compatible |

### Browser, desktop, observability, and evaluation

| Resource | Canonical link | Use |
|---|---|---|
| Playwright | [Repository](https://github.com/microsoft/playwright), [documentation](https://playwright.dev/) | Approved local/LAN browser inspection and supervised action |
| pywinauto | [Repository](https://github.com/pywinauto/pywinauto), [documentation](https://pywinauto.readthedocs.io/) | Primary Windows UI Automation observer/action worker |
| PyAutoGUI | [Repository](https://github.com/asweigart/pyautogui), [documentation](https://pyautogui.readthedocs.io/) | Last-resort, approval-bound screen-coordinate fallback |
| psutil | [Repository](https://github.com/giampaolo/psutil), [documentation](https://psutil.readthedocs.io/) | Read-only host and worker health data |
| OpenTelemetry | [Collector repository](https://github.com/open-telemetry/opentelemetry-collector), [documentation](https://opentelemetry.io/docs/collector/) | Loopback traces/metrics/logs transport after core worker stabilization |
| Prometheus | [Repository](https://github.com/prometheus/prometheus), [documentation](https://prometheus.io/docs/) | Local metrics retention and alert rules |
| Grafana | [Repository](https://github.com/grafana/grafana), [documentation](https://grafana.com/docs/grafana/latest/) | Local dashboards only |
| lm-evaluation-harness | [Repository](https://github.com/EleutherAI/lm-evaluation-harness) | Optional offline model baseline/regression suite; prioritize project-specific fixtures |

## 21. Final completion definition

The manifest is complete as a portable implementation specification when Cursor can complete the preflight, select a minimal vertical slice, locate every needed canonical dependency from section 20, and determine the following without guessing: owner, transport, input/output contract, approval policy, resource limit, GPU priority, feature flag, persistence rule, rollback plan, and acceptance test.

Anything that depends on the target project's actual Eve/HMXL APIs, current schemas, deployed model tags, current directories, service ports, credentials, or deployment policy is intentionally deferred to preflight. That is not a missing resource; it prevents this external research document from inventing unsafe facts about the other computer.

## 22. Optimized Ollama model portfolio

Do not try to make one model permanently serve every role. On 16 GB VRAM, the best finished system is a small, evaluated portfolio selected by `ModelRouter`, with one substantial GPU model resident at a time and fast CPU/small-model helpers where appropriate. Pull only candidates needed for an evaluation stage, record their exact Ollama digest, then remove rejected candidates after a user-approved retention window.

### Recommended evaluation order

| Role | Pull target | Expected artifact size | Use and promotion rule |
|---|---|---:|---|
| Unified central-brain candidate | `qwen3.5:9b` | about 6.6 GB | First unified candidate for general reasoning, tools, coding assistance, image understanding, and long-context work. Benchmark against the existing Qwen 2.5 setup and promote only if its real task suite improves without unacceptable latency. |
| General/tool specialist | `qwen3:14b` | about 9.3 GB | Strong text reasoning/tool candidate. Keep if it scores better than Qwen3.5 for plans, structured output, or local research. |
| Fast conversation/utility | `qwen3:8b` | about 5.2 GB | Lower-latency fallback for routine chats, lightweight task drafting, and CPU/GPU-pressure fallback. |
| Multimodal alternate | `gemma4:12b` | about 7.6 GB | Benchmark for text/image reasoning, long documents, and system-prompt/tool reliability. It supports audio input, but does not replace the dedicated low-latency STT/TTS pipeline. |
| Edge multimodal fallback | `ministral-3:8b` | about 6.0 GB | Optional benchmark for a compact long-context, vision, JSON, and tool-capable fallback. Check Ollama-version compatibility during target preflight. |
| Coding specialist | `qwen2.5-coder:14b` | about 9.0 GB | Default coding benchmark. Keep only if it improves code-task test pass rate over the selected central-brain model. |
| Coding experiment | `devstral:24b` | about 14 GB | Tool/coding experiment only at a small context setting. Do not make it resident or default on 16 GB VRAM. |
| Fast embedding | `qwen3-embedding:0.6b` | about 639 MB | First Nomic replacement candidate. Use only through a parallel versioned index. |
| Curated/batch embedding | `qwen3-embedding:4b` | about 2.5 GB | Higher-quality batch candidate for important corpus rebuilds; not an always-on model. |
| Embedding baselines | `nomic-embed-text-v2-moe`, `embeddinggemma:300m`, `bge-m3:567m` | evaluate on target | Compare only if Qwen3 embedding does not pass the Nomic migration gate. Keep current Nomic as incumbent until an approved switch. |
| Dedicated vision | `qwen3-vl:8b` | about 6.1 GB | Use when the selected central-brain model is not accurate enough for GUI, chart, screenshot, or complex visual-document work. Queue-load only. |
| Document-vision alternate | `granite3.2-vision:2b` | inspect target tag/size | Optional compact benchmark for structured tables/charts/infographics, after Docling baseline. |
| Reasoning experiment | `gpt-oss:20b` | about 14 GB | Offline reasoning/tool benchmark only, at constrained context. It is not a default due to VRAM headroom. |

Canonical sources: [Qwen3.5](https://ollama.com/library/qwen3.5), [Qwen3](https://ollama.com/library/qwen3), [Gemma4](https://ollama.com/library/gemma4), [Ministral 3](https://ollama.com/library/ministral-3), [Qwen2.5 Coder](https://ollama.com/library/qwen2.5-coder), [Devstral](https://ollama.com/library/devstral), [Qwen3 Embedding](https://ollama.com/library/qwen3-embedding), [Nomic Embed Text v2 MoE](https://ollama.com/library/nomic-embed-text-v2-moe), [Qwen3-VL](https://ollama.com/library/qwen3-vl), [Granite Vision](https://ollama.com/library/granite3.2-vision), and [gpt-oss](https://ollama.com/library/gpt-oss).

### Operational model profiles

`ModelRouter` owns these profiles; no caller provides a raw model name:

| Profile | Default route | Options | Residency and fallback |
|---|---|---|---|
| `central_brain` | selected Qwen3.5 9B or Qwen3 14B | thinking enabled only for complex reasoning; temperature 0.3-0.5 | Keep warm only during an active session; route to `fast_utility` if P0 voice needs VRAM |
| `structured_action` | selected central model | JSON Schema, temperature 0, fixed tool allowlist | Validate with Pydantic; reject/retry once on schema failure |
| `research_synthesis` | selected central model | retrieved evidence only, citations required | Query local sources first; queue external research only when allowed |
| `coding_specialist` | Qwen2.5 Coder 14B if benchmark winner | temperature 0.1-0.2, declared coding tools | Load per coding job; never exposes shell/write authority without approval |
| `vision_specialist` | Qwen3-VL 8B if needed | JSON Schema, up to 4 artifact images | Queue-load and unload after result; use `central_brain` vision only if it passes visual evaluation |
| `embed_query` | incumbent or selected fast embedding | `/api/embed`, batch where possible | Small model, short P2 lease; CPU fallback permitted if quality/latency pass |
| `embed_batch` | selected curated embedding | `/api/embed` | P7 only, resumable/idempotent batches |
| `rerank` | standalone BGE worker | max 50 candidates | P3 lease; RRF fallback |
| `fast_utility` | Qwen3 8B or Ministral 3 8B if benchmark winner | low context, temperature 0.2 | Low-pressure fallback; never silently changes the selected central-brain history model |

Encapsulation rules:

- Define an allowlisted `model_profiles` configuration record, mapping profile to exact model digest, context limit, options, health requirements, and fallback profile.
- Create purpose-specific Ollama `Modelfile` derivatives only for stable context and system defaults. Do not embed user-specific memory, credentials, or mutable policy in a Modelfile.
- Pin `num_ctx` per profile. Start at 16K for central/coding, 8K for structured actions, and 4K for utility; raise only after `ollama ps`, p95 latency, and full-GPU tests pass.
- Preserve only final assistant text in conversation history. Do not persist or replay hidden thinking/reasoning tokens across turns.
- Keep model inputs bounded and pass artifacts/evidence excerpts, not full databases, sessions, or arbitrary files.
- A model may suggest an action, but only FastMCP validates authorization, input schema, policy, approvals, and execution.

## 23. Central brain: discussion history, memory, learning, and curiosity

Eve should have four distinct knowledge layers. Do not use a single vector index or prompt history as a substitute for all of them.

| Layer | Storage and owner | Contents | Read/write policy |
|---|---|---|---|
| Canonical conversation record | PostgreSQL, projected to HMXL/PocketBase | every user/assistant/tool-visible turn, attachments, citations, task links, model/profile, timestamps, edits, and consent state | append-only revisions; application-owned and exportable |
| Active context | Eve session manager + bounded PostgreSQL summary | recent turns, current task, selected facts, active plan, and compact rolling summary | assembled by deterministic policy, never raw unbounded replay |
| Recall memory | Cognee session cache plus Weaviate | semantically relevant prior discussion, documents, evidence, and project knowledge | query-scoped; every result includes origin/provenance |
| Durable learned memory | versioned Cognee dataset plus PostgreSQL promotion record | user-approved preferences, trusted facts, validated decisions, reusable lessons, and resolved outcomes | promotion policy only; update/revoke is auditable |

### Canonical discussion history

Replace the basic GUI-only discussion history with a server-owned conversation model. Keep the existing UI design and extend it rather than creating a second chat system. Minimum records:

```text
conversations(id, owner_id, title, status, created_at, updated_at, archived_at)
conversation_turns(id, conversation_id, sequence, role, visible_text, content_hash,
                   model_profile, model_digest, parent_turn_id, trace_id, created_at,
                   edited_at, redaction_state)
turn_artifacts(turn_id, artifact_id, relation, caption)
turn_evidence(turn_id, source_id, chunk_id, index_generation, quote_hash)
conversation_summaries(id, conversation_id, through_sequence, summary_text,
                       facts_json, open_loops_json, model_digest, created_at)
memory_promotion_candidates(id, conversation_id, turn_id, category, statement,
                            evidence_json, confidence, policy_state, created_at)
```

Use `(conversation_id, sequence)` as an immutable ordering key. Store only user-visible text in `visible_text`; tool arguments, hidden reasoning, secrets, and raw sensitive screenshots/audio belong in separately redacted records with narrow access. HMXL reads history and subscribes to its realtime projection, while Eve reads a bounded context package assembled from recent visible turns, latest summary, active task, and retrieved evidence.

### Cognee integration that preserves conversation continuity

Configure Cognee with explicit `user_id` and `session_id=conversation_id`; do not rely on a global default session. Its session cache is valuable for recent conversational continuity and can use PostgreSQL as its cache backend, but it is not the canonical transcript. Cognee's current session history includes only a fixed recent-turn window, so Eve must use the application summary/history layer for older discussions.

Use `CACHING=true`, a PostgreSQL cache backend compatible with the target Cognee version, and a retention value selected from the user's privacy policy. Evaluate `AUTO_FEEDBACK` first: it adds an additional structured model call and derives per-session goals, rules, preferences, and lessons. Enable it only when the selected local model meets latency and accuracy thresholds. Use `SESSION_SEARCH_MODE=concurrent` for responsive chats; use `sequential` only where a same-turn query rewrite is worth the added latency. References: [Cognee sessions and caching](https://docs.cognee.ai/core-concepts/sessions-and-caching), [session distillation](https://docs.cognee.ai/guides/session-distillation), and [Cognee architecture](https://docs.cognee.ai/core-concepts/architecture).

### Safe learning loop

```text
conversation/task/document outcome
  -> deterministic extraction of candidate facts, preferences, decisions, lessons, open questions
  -> validate against source evidence, user feedback, and policy
  -> auto-promote trusted deterministic outcomes OR request review
  -> versioned Cognee durable memory + PostgreSQL audit/provenance
  -> retrieved only when relevant; user can inspect, correct, forget, or disable
```

Candidate categories and policy:

| Category | Default action | Examples |
|---|---|---|
| `trusted_fact` | auto-promote after deterministic source validation | versioned project fact from approved document/source |
| `task_lesson` | auto-promote after passing test/validation | confirmed build step, resolved defect cause, stable workflow rule |
| `user_preference` | request user approval | tone, schedule, preferred tools, retained personal detail |
| `decision` | request user approval unless explicitly confirmed in UI | architectural choice, purchase, external commitment |
| `hypothesis` or `unverified_research` | do not promote | model inference, uncertain claim, unsourced speculation |
| `temporary_context` | never promote | current mood, scratch plans, ephemeral session details |

Every durable item needs source/turn IDs, evidence excerpts/hashes, confidence, creation model/version, policy state, and an explicit deletion/revision path. Eve must expose user controls to view remembered items, correct a memory, forget an item/category, disable future promotion, and export the canonical conversation record.

### Curiosity without uncontrolled autonomy

Curiosity is a controlled background research and learning mechanism, not permission for unbounded browsing or self-modification. After a completed task or conversation, generate a bounded `curiosity_candidate` only when it has an open question, contradiction, stale source, missing prerequisite, or repeated unresolved user goal. It includes objective, expected value, source scope, cost/VRAM class, privacy classification, and stop condition.

- Local-only candidates may query existing local documents, Wikipedia, Weaviate, and Cognee under P7.
- External research candidates require `ENABLE_EXTERNAL_RESEARCH`, a user-approved source allowlist, and a visible queued task before any network request.
- Candidates can create evidence artifacts and memory-promotion proposals, but cannot modify code, configuration, databases, models, tools, prompts, or schedules without the normal approval workflow.
- Enforce quotas: at most three queued curiosity jobs, one concurrent P7 job, 10 minutes/job, and no background work while P0/P1 work is pending.

### Future upgrades after the core brain is stable

These are intentionally deferred and must not delay the central-brain, voice, retrieval, and safety foundation:

| Upgrade | Trigger to evaluate | Constraint |
|---|---|---|
| Personal knowledge graph UI | users cannot inspect/correct promoted memories efficiently | build from PostgreSQL/Cognee provenance, not a second memory store |
| User-approved personal knowledge ingestion | existing document workflow is stable | explicit source roots, privacy classes, and deletion flow |
| Local scheduled research briefs | curiosity queue proves useful and resource controls work | allowlisted local/external sources and daily GPU/compute budget |
| Custom voice or expressive TTS | Piper voice UX is reliable | voice-consent and model-license review |
| Full-duplex speech model research | STT -> Eve -> TTS pipeline misses a measured conversational-latency target | Moshi or future candidate remains separate experiment, not core replacement |
| Advanced image/video/3D workflows | ComfyUI image pipeline is stable and GPU leases remain reliable | queue only; model weights/licensing and storage budgets required |
| Multi-user or LAN agent access | local single-user authorization/audit is fully tested | authenticated gateway, tenant isolation, and threat-model review |