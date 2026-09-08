# EMPIRE Local Upgrade Research

**Status:** Initial research brief for Cursor / Systems Mechanic
**Research date:** 2026-09-07
**Canonical project:** `https://github.com/sbrookshire-raine/Empire` (not inspected from this workspace)
**Hardware target:** Windows 11, approximately 16 GB VRAM, 64 GB RAM
**Runtime goal:** Local-first, no-account, eventually offline-capable

**Build posture:** Online-assisted construction is explicitly allowed. Registries, cloud APIs, hosted benchmarks, frontier models, remote build systems, and temporary paid services may be used to acquire, convert, evaluate, debug, or accelerate construction. Each must have a documented exit path before it becomes operational EMPIRE state.

**Cost posture:** No new memberships, accounts, subscriptions, or recurring fees by default. Prefer public downloads, anonymous registries, existing local tools, and locally reproducible alternatives. An account or paid service is justified only when its capability is unusually valuable and there is high certainty that the useful artifact can be copied, exported, reproduced, or replaced locally.
**Forge decision:** `forge now`, `smoke existing`, `park with reason`, or `idea-queue only`.

Build/runtime labels:

- **`build-only`:** an online resource used temporarily for acquisition, conversion, evaluation, debugging, or scaffolding and then removed.
- **`optional operational`:** local operation is primary, but an online enhancement remains available only by explicit choice.
- **`required operational`:** runtime depends on the service. This is rejected for Eve unless the Architect explicitly changes the local-runtime directive.

Account-cost labels:

- **`none`:** no account or fee required.
- **`free account optional`:** useful convenience, but public/local path exists.
- **`free account required`:** allowed only for unusually high-value acquisition with a concrete local exit.
- **`paid one-time`:** allowed only when the exported artifact and license clearly support the intended use.
- **`recurring paid`:** strongly disfavored; must beat a suitable local alternative by a large margin.

For every online build aid, record what data may leave the machine, what local artifact or replacement it produces, the removal trigger, cleanup steps, and an offline smoke test proving the operational path survives without it.

Before recommending an account-dependent resource, compare it against a suitable local version and state why the local option is insufficient. Record whether continued account access is needed to use, update, export, or redistribute the acquired artifact.

## How to use this brief

This document is a research handoff, not proof that any candidate is installed or compatible with the canonical repository. The Architect should run the proposed smoke tests on the EMPIRE computer before a candidate is added to the catalog or forged into a Work Order.

Evidence labels:

- **Verified source:** observed in an official repository or official documentation during this research pass.
- **Snapshot fact:** stated in `1. EMPIRE_RESEARCH_SNAPSHOT.md` supplied to this workspace.
- **Inference:** proposed EMPIRE integration or resource estimate; not measured here.
- **Unverified:** requires a canonical-machine smoke test.

## Executive verdict

The highest-hit path is to improve specialist workers around the existing Eve/Ollama/Cognee/PocketBase/FastMCP core. Do not add another general agent framework, vector database, orchestration platform, or container runtime merely because it is available as an image.

| Rank | Candidate / capability | Verdict | Why |
|---:|---|---|---|
| 1 | `llama.cpp` constrained-output worker | forge now | Adds GGUF portability, CPU/GPU fallback, local HTTP, multimodal support, and grammar-constrained structured output without replacing Ollama. |
| 2 | Retrieval rerank A/B using Qwen3-Reranker-0.6B | smoke existing | Strongly targets Cognee/Weaviate recall quality, but model loading and embedding dimensions must be validated against the current path. |
| 3 | PaddleOCR / PP-Structure as an OCR specialist | smoke existing | Adds a different document-layout and multilingual OCR path; only worth keeping if it beats the current Docling/Tesseract path on real samples. |
| 4 | Playwright MCP / CLI limb | forge now, bounded | High practical value for approved local web workflows; existing catalog entry means this is a wiring and guardrail task, not a new platform. |
| 5 | OmniParser screenshot parser | smoke existing | Expands vision from description to structured screen regions, but desktop action must remain separately approved. |
| 6 | Silero VAD plus existing faster-whisper | forge as a small extension | Tiny CPU-friendly voice gate that improves the existing speech limb without another heavy model. |
| 7 | Kokoro-82M TTS | smoke existing | Lightweight local voice option; compare against the existing Coqui/Piper direction and verify Windows audio packaging. |
| 8 | Audit and GPU admission control | forge now | Not an external tool, but the highest operational multiplier: prevents specialists from competing with Eve's interactive model and creates evidence for later upgrades. |
| 9 | Prometheus/Grafana or VictoriaMetrics | idea-queue only | Useful only when current health cards and logs cannot answer operational questions. Low direct AI value. |
| 10 | Podman | park with reason | Windows uses a Podman-managed VM; this adds a second container environment without solving a documented EMPIRE problem. |
| 11 | containerd | park with reason | Officially a low-level embedded runtime, not an end-user orchestration interface; Docker Compose/scripts remain the better EMPIRE boundary. |
| 12 | Prefect, Dagster, Airflow, Milvus, Vespa, Kubernetes core | reject or park | Platform tax and duplication exceed demonstrated value on a single Windows host. |

## Current baseline and duplicate map

### Snapshot facts

EMPIRE already has:

- Eve as the local agent and Ollama as the inference host.
- Cognee as durable graph/vector memory and Weaviate as an on-demand Wiki Local service.
- PocketBase for tasks and day blocks.
- Plain HTML, HTMX, and Alpine.js for the workbench.
- FastMCP servers under `mcp/`, Python workers under `pipeline/`, and Eve tools under `agents/*`.
- Default-OFF Toolbelt limbs for voice, vision, web, containers, stems, and other heavy capabilities.
- Existing Docling conversion, faster-whisper/voice scaffolding, Qwen vision scaffolding, Docker discovery, GPU lease status, provenance footers, and explicit memory promotion policy.

### Do not duplicate

| Existing surface | Do not add another copy of | Prefer |
|---|---|---|
| Ollama | Another general model router or agent framework | `llama.cpp` only for constrained/offline/specialized GGUF jobs. |
| Cognee + Weaviate | Qdrant, Chroma, Milvus, Vespa as a third memory authority | Retrieval workers, reranking, metadata filters, and measured A/B evaluation. |
| Docling + Tesseract + pypdf | A second general document platform | PaddleOCR only for a measured OCR/layout gap. |
| faster-whisper + voice scaffold | A second full speech server by default | Silero VAD and a narrow TTS comparison. |
| Playwright catalog entry | Another browser automation framework | Forge the existing Playwright boundary with origin and action controls. |
| Docker Compose/scripts | Podman/containerd as a parallel lifecycle system | Keep one operational path unless a measured blocker appears. |
| PocketBase + APScheduler | Airflow, Dagster, Prefect by default | Add a bounded queue/admission layer first. |

## Ranked integration briefs

## 1. llama.cpp constrained-output worker

**Verdict:** `forge now`

**Verified source:** [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)

The official repository describes MIT-licensed C/C++ inference, GGUF quantization, CUDA support, CPU/GPU hybrid inference, a local server, Docker documentation, multimodal support, and GBNF grammar documentation. It supports Windows builds and publishes releases. These are source facts; performance on the EMPIRE laptop is unverified.

**EMPIRE outcome**

Use it for jobs where malformed JSON is costly:

- `TaskDraft`
- `ResearchEvidence`
- `MemoryPromotionCandidate`
- `DocumentMetadata`
- `DesktopActionPlan`
- bounded extraction from local artifacts

Keep Ollama as the interactive default. This worker should not become a second chat brain.

**Smallest integration**

- Pipeline or local worker under `pipeline/`.
- Fixed local `llama-server` process or approved binary, bound to loopback.
- Narrow FastMCP wrapper such as `structured_extract`.
- Model allowlist containing pinned GGUF files and recorded model hashes/licenses.
- CPU fallback or queued GPU lane; never silently contend with Eve's interactive model.
- JSON Schema input converted to an approved grammar; bounded prompt and output sizes.
- Artifact output includes model id, hash, schema id, input hash, timestamp, and validation result.

**Smoke test for the canonical machine**

1. Start one small Qwen GGUF through `llama-server` on `127.0.0.1`.
2. Submit the same 20 task/extraction prompts through Ollama JSON prompting and llama.cpp grammar output.
3. Record parse success, latency, VRAM peak, RAM peak, and malformed-output count.
4. Accept only if grammar output materially reduces repair work without making Eve interactive latency unacceptable.
5. Reject if the build or CUDA path is unstable on Windows, or if the worker creates unsafe model-pull behavior.

**Risks**

- Separate model files and runtime lifecycle increase operational surface.
- Grammar definitions require maintenance when schemas change.
- The project is highly active; pin a release or commit rather than using a moving nightly.

## 2. Qwen3 embedding and reranking A/B

**Verdict:** `smoke existing`

**Verified source:** [QwenLM/Qwen3-Embedding](https://github.com/QwenLM/Qwen3-Embedding)

The official repository documents 0.6B, 4B, and 8B embedding and reranking models, 32K model context, multilingual support, instruction-aware queries, Transformers/vLLM/Sentence Transformers examples, and model-specific evaluation. The repository has no published releases in the observed GitHub view, so pin model revisions and preserve the current Nomic production path until results justify change.

**EMPIRE outcome**

Improve retrieval precision before increasing chat context. Candidate flow:

```text
query -> existing Weaviate/Cognee candidate retrieval -> top 30-80
     -> Qwen3-Reranker-0.6B -> top 5-10 evidence blocks -> Eve
```

Use the 0.6B reranker as the first test. Do not keep 4B/8B models resident with the interactive Qwen model until measured.

**Smallest integration**

- Keep current production embeddings unchanged.
- Add an offline evaluation worker, not an automatic production swap.
- Store query, candidate ids, scores, model revision, and evaluation set version.
- Add explicit `retrieval_eval` or `rerank_candidates` boundary behind a Toolbelt or maintenance mode.
- Promote a new embedding only after a versioned migration plan; vector dimensions and dataset rebuild are not implicit.

**Smoke test**

1. Build 30-50 representative queries from existing memory/research use cases.
2. Label the expected evidence blocks manually.
3. Compare current retrieval, current retrieval plus reranking, and a small embedding A/B.
4. Record recall@5, recall@10, latency, VRAM peak, and whether irrelevant but semantically similar documents rise.
5. Accept reranking only if it improves evidence recall without unacceptable latency or GPU contention. Keep Nomic production if the result is ambiguous.

**Risks**

- The repository's benchmark scores are authors' evaluations, not EMPIRE measurements.
- Model licenses and weight distribution terms must be checked at the exact model source.
- A model swap can invalidate existing vector collections; do not make it part of a casual Work Order.

## 3. PaddleOCR / PP-Structure specialist

**Verdict:** `smoke existing`

**Verified source:** [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)

The official repository is Apache-2.0 and documents local deployment, PP-OCR, PP-Structure, OCR APIs, an MCP server directory, multilingual OCR, ONNX/TensorRT/CPU options, and structured Markdown/JSON outputs. Current repository marketing and benchmark claims require independent testing.

**EMPIRE outcome**

Use this as a specialist for scanned documents, multilingual pages, tables, coordinates, and forms where the existing Docling/Tesseract result is weak. It is not a replacement for Docling's broader document representation.

**Smallest integration**

- Separate Python environment or pinned container.
- Fixed local input root and artifact output root.
- Narrow functions: `ocr_image`, `parse_page`, `extract_regions`.
- Return text, confidence, bounding boxes, page number, model revision, and content hash.
- Keep outputs in Resource Queue or scratch artifacts; no automatic Cognee promotion.
- Run CPU first where acceptable; GPU use must acquire the existing lease.

**Smoke test**

Use a small corpus containing clean PDFs, scanned pages, tables, handwriting if relevant, and at least one non-English sample. Compare character error rate, table fidelity, coordinates, processing time, and memory against Docling/Tesseract. Keep PaddleOCR only for a clearly superior document class.

**Risks**

- Paddle dependencies may be more difficult to keep stable on Windows than the current chain.
- The model family is changing quickly; pin versions and weights.
- A container image may hide large model downloads and GPU assumptions.

## 4. Playwright MCP / CLI limb

**Verdict:** `forge now`, bounded

**Verified source:** [Microsoft Playwright](https://github.com/microsoft/playwright)

The official project documents browser automation across Chromium, Firefox, and WebKit, a Playwright MCP server, a CLI for coding agents, screenshots, traces, network controls, and an Apache-2.0 license. The EMPIRE snapshot already lists Playwright in the catalog and describes origin allowlists and approval for submit/upload.

**EMPIRE outcome**

This is the most practical path to local web interaction, testing the local workbench, approved localhost workflows, and selected allowlisted LAN resources. It must not become an unrestricted web-research substitute or an account automation system.

**Smallest integration**

- Extend the existing Playwright entry instead of adding another browser framework.
- Default to read, inspect, screenshot, and trace.
- Allow only explicit origins, preferably `127.0.0.1` services first.
- Block downloads, uploads, navigation outside the allowlist, and credential access by default.
- Require approval for click-submit, destructive actions, uploads, and form submission.
- Store trace metadata and artifact hashes in a local audit record.
- Add an Eve limb only after the MCP surface is narrowed and audited.

**Smoke test**

Run against a local static page and the EMPIRE workbench only: inspect a page, capture a screenshot, read a table, and perform one approved non-destructive action. Reject if the tool can navigate outside the allowlist or access browser secrets without an explicit approval path.

## 5. OmniParser screenshot understanding

**Verdict:** `smoke existing`

**Verified source:** [Microsoft OmniParser](https://github.com/microsoft/OmniParser)

The official repository describes screenshot parsing into structured UI elements, interactive-region detection, local model weights, and a Windows 11 VM demonstration. The observed repository is CC-BY-4.0; model components and weights have separate licenses, including MIT components and earlier AGPL-related detector history. Exact weight licensing must be recorded before redistribution.

**EMPIRE outcome**

Add structured screen perception to the existing `vision_local` limb. Keep action execution separate: OmniParser may identify a region and suggest an action, but Playwright/pywinauto should require independent allowlists and Architect approval.

**Smallest integration**

- `parse_screenshot(path)` returns regions, labels, confidence, coordinates, and source hash.
- Input must be an approved local screenshot or captured window.
- Output goes to a review artifact, not directly to an input actuator.
- GPU lease required for caption/VLM steps; CPU/ONNX detector path preferred where sufficient.
- Redact or avoid sensitive screen regions before persistence.

**Smoke test**

Use screenshots of the EMPIRE UI and a few fixed local applications. Measure region detection stability across scaling/DPI, false positives, latency, and VRAM. Accept only as an observation tool first. Do not forge autonomous clicking from this result.

## 6. Silero VAD with existing faster-whisper

**Verdict:** `forge as a small extension`

**Verified source:** [Silero VAD](https://github.com/snakers4/silero-vad) and [faster-whisper](https://github.com/SYSTRAN/faster-whisper)

Silero's official repository documents a small local VAD model, CPU processing, ONNX portability, no keys or registration, and a CC-BY-NC-4.0 repository license page that must be reconciled with the README's component-license statement before commercial redistribution. Faster-whisper officially documents integrated Silero VAD filtering, local model loading, CPU/GPU modes, and MIT code licensing.

**EMPIRE outcome**

Add speech gating before transcription to reduce silence processing and improve push-to-talk/barge-in behavior. It should not create a second speech server.

**Smallest integration**

- Add VAD to the existing voice pipeline.
- Store timestamps and confidence with the transcript artifact.
- Default to push-to-talk or explicit mic activation.
- Keep microphone access outside the generic shell/tool executor.
- Acquire GPU lease only for STT; VAD should run CPU/ONNX where possible.

**Smoke test**

Use quiet speech, background noise, music, and overlapping speech. Measure false starts, clipped first words, silence removed, end-to-end latency, and CPU load. Reject if it harms conversational turn-taking more than it saves.

## 7. Kokoro-82M TTS comparison

**Verdict:** `smoke existing`

**Verified source:** [hexgrad/kokoro](https://github.com/hexgrad/kokoro)

The official repository documents an 82M open-weight TTS model, Apache-licensed weights, Python usage, WAV output, multiple languages/voices, and Windows installation guidance for espeak-ng. The repository has no published GitHub releases in the observed view, so pin package/model revisions.

**EMPIRE outcome**

Use as a lightweight alternative to the existing Coqui/Piper direction if voice latency, quality, or licensing is a problem. Voice is presentation, not Eve personality or memory authority.

**Smallest integration**

- Local voice worker with fixed voice allowlist.
- Output only to an artifact or approved local audio stream.
- Record model/voice id and input hash.
- Keep voice consent and sensitive-text rules in the voice limb.
- Do not keep it resident if it competes with Eve's interactive model.

**Smoke test**

Compare one short response and one longer response against the current TTS option for startup latency, real-time factor, intelligibility, voice quality, CPU/VRAM, and Windows packaging friction. Keep only one default voice path.

## 8. Audit trail and GPU admission control

**Verdict:** `forge now`

This is an EMPIRE-native upgrade rather than an external repository addition. It has higher expected value than another service because it makes every later local worker safer and measurable.

**Smallest integration**

Create a narrow local operational record for:

- Eve turn id and tool call id.
- Tool/category and approval state.
- Input/output artifact hashes.
- Model/runtime id and revision.
- Requested and observed resource lane.
- Start/end time, status, error class, and human acceptance.

Extend `gpu_lease_status` into admission control. A GPU job should declare its lane, estimated weight, and whether it can wait or fall back to CPU. The lease must be acquired before model load, not merely reported after contention occurs.

**Smoke test**

Queue a text turn, a vision request, and a speech request with overlapping start times. Confirm that only the allowed heavy tenant runs, waiting jobs have clear status, and a failed/locked service degrades without corrupting chat or memory.

## Conditional candidates

| Candidate | Verdict | Condition for reconsideration |
|---|---|---|
| Prometheus + Grafana | idea-queue only | Current health cards and logs cannot explain readiness, GPU contention, or job latency. Prefer a small metrics endpoint first. |
| VictoriaMetrics | park | Prometheus cardinality or storage becomes a demonstrated bottleneck. |
| Loki | park | A local log correlation problem exists after structured audit events. |
| vLLM | smoke existing | Ollama throughput or batching becomes the measured bottleneck, or a future multi-GPU host appears. |
| Sentence Transformers | smoke existing | Use only as an evaluation wrapper if it enables a clear reranker/embedding A/B; do not add another permanent embedding authority. |
| Qdrant / Chroma | park | A specific workload cannot be served by Cognee/Weaviate and the data boundary is explicit. |
| Prefect / Dagster | park | APScheduler and existing workers demonstrably cannot express required retries, dependencies, and provenance. |
| pywinauto / PyAutoGUI / OpenAdapt | idea-queue only | Observe-only screen understanding and explicit approval are implemented first. |

## Container and registry appendix

### Docker Hub

Docker Hub is useful for discovering and retrieving a pinned image, but an image listing is not an integration decision. For every candidate image, record:

- exact digest, not only `latest`;
- source repository and Dockerfile;
- image license and included model license;
- exposed ports and required mounts;
- user/UID and filesystem permissions;
- CPU/RAM/VRAM assumptions;
- healthcheck and graceful shutdown behavior;
- whether it phones home or downloads weights at startup;
- whether it binds only to loopback in the Compose configuration.

Use the existing Container Scout for discovery. It must not auto-pull or auto-run images.

### Google Artifact Registry / other OCI registries

A registry can be a distribution location, not a reason to add a hosted dependency. A useful candidate must support local export/pull and offline restart after the image and model weights are present. Prefer public, reproducible OCI images from the project's official repository. Avoid any image requiring Google Cloud credentials, a private registry, telemetry, or a runtime API key.

Proposed discovery fields:

```yaml
registry:
  host: docker.io | ghcr.io | <official-registry>
  repository: <publisher>/<image>
  tag: <pinned-tag>
  digest: sha256:<digest>
  source_repository: https://github.com/<owner>/<repo>
  offline_after_pull: true
  credential_required_at_runtime: false
```

### containerd

**Verified source:** [containerd/containerd](https://github.com/containerd/containerd)

The official project describes containerd as an Apache-2.0 industry-standard runtime available for Linux and Windows, designed to be embedded into larger systems rather than used directly by end users. It supports OCI registries and manages low-level image, execution, storage, and lifecycle concerns.

**EMPIRE verdict:** `park with reason`.

Containerd is relevant underneath a platform, but it does not improve the current Compose/PowerShell lifecycle enough to justify a direct Eve/MCP surface. Do not build a generic `containerd_exec` tool. Reconsider only for a measured Docker Desktop resource or lifecycle problem, with a fixed service wrapper rather than arbitrary runtime access.

### Podman

**Verified source:** [containers/podman](https://github.com/containers/podman)

The official project describes a daemonless, rootless-capable OCI container manager with a Docker-compatible CLI, REST API, and Windows support through `podman machine`. Its Windows path introduces a managed VM.

**EMPIRE verdict:** `park with reason`.

Podman is a credible alternative runtime, but operating both Docker and Podman would create duplicated images, volumes, health checks, and troubleshooting paths. It is worth a separate benchmark only if Docker's daemon, licensing, or resource behavior becomes a measured blocker.

### Runtime policy

- Keep Docker Compose and PowerShell scripts as the default optional-service lifecycle.
- Keep core Eve/Ollama/PocketBase as local processes as documented.
- Do not expose Docker, Podman, or containerd control as a generic Eve capability.
- If a containerized limb is forged, expose only its narrow localhost API through FastMCP.
- Use image digests, read-only mounts where possible, bounded resources, healthchecks, and explicit stop behavior.

## Rejected or parked platform expansions

| Candidate | Decision | Reason |
|---|---|---|
| Kubernetes for core EMPIRE | reject | Direct conflict with the snapshot's single-host and cold-start constraints. |
| Airflow | reject | Too much control-plane and dependency overhead for current local workers. |
| Milvus / Vespa | park | Retrieval platform duplication and resource cost without a demonstrated gap. |
| Another general agent framework | reject | Eve already owns orchestration and role boundaries. |
| Cloud LLM, hosted embedding, cloud BaaS | reject | Violates local runtime directives. |
| Full Wikipedia ingest | reject | Explicitly halted; use Wiki Local and explicit promotion. |
| Always-on Weaviate | reject | Explicitly parked for RAM and lifecycle reasons. |
| Default 32K context | reject | Conflicts with the documented shared 8192 context budget and VRAM class. |
| Auto-promote scout caches to Cognee | reject | Conflicts with explicit human promotion and provenance policy. |

## Cursor-ready forge sequence

1. **Operational foundation:** GPU admission control and structured audit events.
2. **Structured local worker:** llama.cpp with one pinned GGUF and one schema.
3. **Retrieval evaluation:** Qwen3 reranker against a labeled local query set; no production swap yet.
4. **Existing-limb wiring:** Playwright MCP/CLI behind localhost origin and approval controls.
5. **Document specialist:** PaddleOCR only if sample comparison shows a real Docling/Tesseract gap.
6. **Voice extension:** Silero VAD, then Kokoro comparison if current TTS remains weak.
7. **Vision extension:** OmniParser observation-only screenshot parsing; defer actuators.
8. **Observability:** Add Prometheus/Grafana only if the operational foundation cannot answer real questions.

Each accepted item should follow the snapshot's Forge Protocol: pipeline or service boundary, narrow FastMCP wrapper, Eve tool and skill, routing row, Toolbelt category if optional, docs, smoke row, rebuild, and no automatic Cognee ingestion.

## Acceptance record template

Use this on the canonical machine for each candidate:

```yaml
candidate: <name>
source_url: <official-source>
source_revision: <tag-or-commit>
license: <code-and-weight-license>
status: forge-now | smoke-existing | park | reject
input_fixture: <path-or-description>
output_artifact: <path-or-description>
local_only_after_install: true | false
runtime: native | docker-compose | local-api | cli | library | mcp
vram_peak_gb: <measured>
ram_peak_gb: <measured>
latency_ms: <measured>
interactive_regression: none | acceptable | unacceptable
provenance_recorded: true | false
approval_required: true | false
memory_promoted: false
acceptance_reason: <one sentence>
rejection_reason: <one sentence or null>
```

## Primary sources checked

- [EMPIRE snapshot supplied in this workspace](../1.%20EMPIRE_RESEARCH_SNAPSHOT.md)
- [Existing no-account catalog](local-no-account-tools.yaml)
- [llama.cpp](https://github.com/ggml-org/llama.cpp)
- [Qwen3-Embedding](https://github.com/QwenLM/Qwen3-Embedding)
- [Docling](https://github.com/docling-project/docling)
- [MarkItDown](https://github.com/microsoft/markitdown)
- [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)
- [faster-whisper](https://github.com/SYSTRAN/faster-whisper)
- [Silero VAD](https://github.com/snakers4/silero-vad)
- [Kokoro](https://github.com/hexgrad/kokoro)
- [Playwright](https://github.com/microsoft/playwright)
- [OmniParser](https://github.com/microsoft/OmniParser)
- [Podman](https://github.com/containers/podman)
- [containerd](https://github.com/containerd/containerd)

## Research limitations

- The canonical EMPIRE repository and runtime were not available in this workspace.
- No candidate was installed or benchmarked here.
- Resource figures from prior research are estimates unless explicitly marked as an official project benchmark; they must not be treated as laptop measurements.
- Current versions and registry tags are time-sensitive. Pin exact revisions during forging.

## Expanded research avenues

The following source families materially widen discovery without changing EMPIRE's architecture. They are discovery and evaluation channels, not automatic adoption channels.

### Model registries

| Avenue | Best use | EMPIRE rule |
|---|---|---|
| [Hugging Face Hub](https://huggingface.co/models) | GGUF, ONNX, embeddings, rerankers, OCR, VLM, ASR, TTS, datasets | Pin immutable revisions, inspect code and weight licenses separately, stage locally, and disable runtime downloads. |
| [ModelScope](https://www.modelscope.cn/) | Qwen, multilingual, OCR, speech, video, and alternate model artifacts | Compare hashes and licenses against upstream or Hugging Face; do not assume mirrored files are equivalent. |
| [Ollama Library](https://ollama.com/library) | Lowest-friction model A/B because Ollama is already the interactive boundary | Inspect exact tags and Modelfiles; no unrestricted model-pull tool for Eve. |
| [NVIDIA NGC](https://catalog.ngc.nvidia.com/) | CUDA, TensorRT, Triton, and specialized NVIDIA containers | Installation-time source only; no account/API-key dependency at runtime; review image digest, SBOM, and terms. |
| [ONNX Model Zoo](https://github.com/onnx/models) and model cards | Small CPU/GPU specialist models | Record preprocessing, postprocessing, provider support, and model/data licenses. |

Useful registry queries:

```text
site:huggingface.co/models reranker 0.6B multilingual
site:huggingface.co/models GGUF structured output
site:huggingface.co/models ONNX OCR layout Windows
site:huggingface.co/models whisper VAD ONNX
site:modelscope.cn/models Qwen embedding reranker
site:modelscope.cn/models OCR document parsing
site:ollama.com/library vision tools structured outputs
site:catalog.ngc.nvidia.com TensorRT Windows WSL2
```

### Package and Windows ecosystems

- [PyPI](https://pypi.org/), [uv](https://github.com/astral-sh/uv), [Conda](https://conda.io/), [conda-lock](https://github.com/conda/conda-lock), and [Miniforge](https://github.com/conda-forge/miniforge) are useful for finding and pinning local workers.
- [WinGet](https://github.com/microsoft/winget-cli), [Scoop](https://github.com/ScoopInstaller/Scoop), and [Chocolatey](https://github.com/chocolatey/choco) are intake mechanisms, not trust decisions.
- [ONNX Runtime](https://github.com/microsoft/onnxruntime), [TensorRT](https://github.com/NVIDIA/TensorRT), [OpenVINO](https://github.com/openvinotoolkit/openvino), and [Windows ML](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/overview) expose acceleration options.

For each package or installer, capture the exact version, source URL, hash, Authenticode/signature state, license, install script behavior, wheel/platform support, and whether the installed artifact works with network access disabled.

### MCP discovery

Search the [official MCP Registry](https://registry.modelcontextprotocol.io/), [MCP Registry repository](https://github.com/modelcontextprotocol/registry), [official reference servers](https://github.com/modelcontextprotocol/servers), and vendor-maintained repositories. Search for narrow local tools in databases, documents, browser inspection, media, host observability, policy, and provenance.

Reject generic servers that expose arbitrary shell, filesystem, SQL, Docker, browser JavaScript, or model management. Registry presence is not maturity evidence. Verify source ownership, release activity, license, tool count, network behavior, Windows support, and whether the surface can be reduced to fixed typed operations.

### Benchmarks and evaluation data

| Area | Candidate | Use |
|---|---|---|
| Retrieval | [BEIR](https://github.com/beir-cellar/beir), [MTEB](https://github.com/embeddings-benchmark/mteb) | Compare retrieval/reranking before changing Cognee or Weaviate. Dataset terms remain separate from framework licenses. |
| OCR/layout | [RapidOCR](https://github.com/RapidAI/RapidOCR), [DocLayNet](https://github.com/DS4SD/DocLayNet) | Compare OCR/layout specialists against Docling/Tesseract. Keep large datasets selective and locally hashed. |
| Speech | [LibriSpeech](https://www.openslr.org/12/) plus consented noisy fixtures | Reproducible ASR baseline plus real Architect conditions. |
| Multimodal | [MMMU](https://github.com/MMMU-Benchmark/MMMU) | Evaluate charts, tables, diagrams, and visual reasoning; inspect source-data terms. |
| Browser | [MiniWoB++](https://github.com/Farama-Foundation/MiniWoB-plusplus) | Synthetic, local, account-free browser tasks before any real-site automation. |
| General local models | [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) | Repeatable local model comparisons; avoid hosted model endpoints. |

Public benchmark results are selection evidence only. The final gate should be a small versioned EMPIRE fixture set with hashes, expected outputs, latency thresholds, and a rejection rule.

## New high-value candidates

### Retrieval and model workers

| Candidate | Status | Why it matters | Boundary |
|---|---|---|---|
| [Qwen3-Reranker-0.6B](https://huggingface.co/Qwen/Qwen3-Reranker-0.6B) | smoke existing | 0.6B, multilingual, instruction-aware reranking; strongest candidate for improving evidence selection without changing the memory authority. | `rerank_candidates` after Weaviate/Cognee top 30-80. |
| [Granite Embedding 30M English](https://huggingface.co/ibm-granite/granite-embedding-30m-english) | smoke existing | Tiny CPU-first baseline for English chat-history or scratch retrieval. | Evaluation-only embedding worker; never silently rebuild production vectors. |
| [GTE multilingual base/reranker](https://huggingface.co/Alibaba-NLP/gte-multilingual-base) | park | Credible multilingual runner-up if Qwen3 custom runtime setup is awkward. | A/B worker with pinned model commits. |
| [Qwen3-14B-GGUF](https://huggingface.co/Qwen/Qwen3-14B-GGUF) | forge now, bounded | Official Q4_K_M GGUF is a practical constrained-output or offline worker for a 16 GB GPU. | Loopback `llama-server`, fixed schemas, no model pull. |

### Document and vision specialists

| Candidate | Status | Why it matters | Boundary |
|---|---|---|---|
| [Granite-Docling-258M](https://huggingface.co/ibm-granite/granite-docling-258M) | smoke existing | Extends the already-approved Docling path for visual pages, formulas, charts, layout, and region queries. | Docling visual profile with source/page hashes and bounded artifacts. |
| [PaddleOCR-VL](https://huggingface.co/PaddlePaddle/PaddleOCR-VL) | smoke existing | Multilingual OCR, formulas, tables, charts, coordinates, and structured Markdown/JSON. | OCR/layout fallback; Windows/Paddle CUDA compatibility must be proven. |
| [GOT-OCR-2.0](https://huggingface.co/stepfun-ai/GOT-OCR-2.0-hf) | park | Targeted region, formula, chart, and formatted OCR fallback. | `ocr_region` only; not a general document authority. |
| [MiniCPM-V-4.5](https://huggingface.co/openbmb/MiniCPM-V-4_5) | park | Image/video/OCR capability with quantized variants, but incomplete Windows/Ollama confidence. | Benchmark-only vision worker. |
| [Moondream2](https://huggingface.co/vikhyatk/moondream2) | park | Small fast observer for captions, OCR, pointing, and UI localization. | `vision_fast_observe`; no actuator connection. |

### Speech and TTS

| Candidate | Status | Why it matters | Boundary |
|---|---|---|---|
| [Qwen3-TTS 0.6B](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-0.6B-Base) | smoke existing | Multilingual local TTS, streaming, and optional voice cloning. | Existing speech API; explicit voice consent and GPU lease. |
| [Kokoro-82M](https://huggingface.co/hexgrad/Kokoro-82M) | smoke existing | Lightweight Apache-licensed CPU-friendly fallback with Windows guidance. | Default low-resource TTS candidate. |
| [Moonshine Base](https://huggingface.co/moonshine-ai/moonshine-base) | smoke existing | 61M English ASR designed for low latency and on-device use. | Push-to-talk or command recognizer before faster-whisper. |
| [Parakeet TDT 0.6B v2](https://huggingface.co/nvidia/parakeet-tdt-0.6b-v2) | park | Timestamped English transcription, but NeMo/Linux and CC-BY terms add friction. | Queued meeting transcription only if Windows path succeeds. |

## Acceleration and runtime findings

| Candidate | Verdict | EMPIRE interpretation |
|---|---|---|
| [ONNX Runtime CUDA](https://onnxruntime.ai/docs/execution-providers/CUDA-ExecutionProvider.html) | smoke existing | Best general acceleration boundary for fixed OCR, vision, encoder, and reranker workers; supports native Windows and CPU fallback. |
| [ONNX Runtime GenAI](https://onnxruntime.ai/docs/genai/) | smoke existing | Structured generation and local ONNX models, but preview API and conversion surface add risk. |
| [TensorRT RTX EP](https://onnxruntime.ai/docs/execution-providers/TensorRTRTX-ExecutionProvider.html) | smoke existing | Worth testing for fixed ONNX specialists on RTX hardware; JIT/cache behavior must be recorded. |
| [whisper.cpp](https://github.com/ggml-org/whisper.cpp) | forge now, bounded | Small offline Windows/CUDA/Vulkan/CPU voice fallback beside faster-whisper. |
| [OpenVINO](https://github.com/openvinotoolkit/openvino) | park | Useful CPU fallback, but not an NVIDIA GPU accelerator on the stated laptop. |
| [vLLM](https://github.com/vllm-project/vllm) | smoke only if needed | WSL2/Linux path for measured throughput problems; overlaps Ollama and consumes the heavy GPU lane. |
| [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) | park | Linux/server-oriented and too operationally heavy for the current single-host default. |
| [Triton Inference Server](https://github.com/triton-inference-server/server) | park | Consider only when multiple backends, batching, or model repositories are proven necessary. |
| [DirectML](https://onnxruntime.ai/docs/execution-providers/DirectML-ExecutionProvider.html) | fallback only | Sustained-engineering path and unlikely to beat CUDA on NVIDIA; retain only as compatibility fallback. |

**Runtime rule:** keep Ollama as the interactive model boundary. Use llama.cpp, ONNX Runtime, whisper.cpp, or TensorRT only as bounded specialist workers. WSL2 is an experiment boundary for Linux-only tools, not a reason to move the core stack.

## Evaluation, integrity, and supply-chain infrastructure

These are upgrades to the research and forge process itself. They have unusually high leverage because they make every later model or container decision safer.

| Candidate | Status | Purpose |
|---|---|---|
| [Syft](https://github.com/anchore/syft) + [Grype](https://github.com/anchore/grype) | forge now | Generate local SBOMs and scan approved artifacts with a pinned offline vulnerability database. |
| [OSV-Scanner](https://github.com/google/osv-scanner) | forge now | Scan lockfiles/SBOMs, including offline mode with a staged database. |
| [pip-audit](https://github.com/pypa/pip-audit) | forge now | Audit Python environments and lockfiles as a focused complement to OSV-Scanner. |
| [Microsoft SBOM Tool](https://github.com/microsoft/sbom-tool) | forge now | Generate and validate SPDX records for Windows-delivered artifacts. |
| [Cosign](https://github.com/sigstore/cosign) | forge selectively | Verify pinned binaries or OCI artifacts with local keys or offline bundles; avoid keyless runtime dependence. |
| [OPA](https://github.com/open-policy-agent/opa) + [Conftest](https://github.com/open-policy-agent/conftest) | smoke then forge | Evaluate fixed policies for tool requests, Work Orders, MCP manifests, approvals, and artifact metadata. |
| [osquery](https://github.com/osquery/osquery) | smoke existing | Typed, read-only Windows host facts without exposing arbitrary shell or SQL. |
| [RapidOCR](https://github.com/RapidAI/RapidOCR) | smoke existing | Small ONNX OCR comparison worker against Docling/Tesseract. |
| [BEIR](https://github.com/beir-cellar/beir) + [MTEB](https://github.com/embeddings-benchmark/mteb) | forge evaluation | Versioned retrieval and embedding evaluation without changing memory authority. |
| [MiniWoB++](https://github.com/Farama-Foundation/MiniWoB-plusplus) | smoke existing | Account-free synthetic browser tasks for Playwright guardrails. |
| [nvidia-ml-py](https://pypi.org/project/nvidia-ml-py/) + `nvidia-smi` | forge evidence | GPU telemetry and contention evidence; Windows WDDM may not expose per-process memory reliably. |
| [prumo](https://github.com/TomD4vs/prumo) | smoke Mechanic-only | Read-only context-file integrity and drift checks for Forge Protocol inputs. |
| [OPA](https://github.com/open-policy-agent/opa) + [Conftest](https://github.com/open-policy-agent/conftest) | smoke then forge | Fixed policy evaluation for Work Orders, MCP manifests, approvals, bindings, and promotion records. Do not expose arbitrary Rego or network policy loading. |
| [osquery](https://github.com/osquery/osquery) | smoke existing | Windows processes, services, ports, hashes, and host facts through fixed query IDs; never expose arbitrary SQL. |
| [Otito](https://github.com/BASHBOP/otito) | smoke Mechanic-only | Repository maps, context packs, impact analysis, staged-tree gates, and validation receipts; disposable checkout only until maturity is proven. |
| [Agent Observability](https://github.com/RudrenduPaul/agent-observability) | smoke existing | Local record/replay and failure inspection for HTTP workers; redact prompts, headers, and secrets before persistence. |
| [HOL Guard](https://github.com/hashgraph-online/hol-guard) | park or smoke | Local tool/MCP risk checks and receipts; keep cloud sync off and prevent it becoming a competing approval authority. |
| [Frictionless](https://github.com/frictionlessdata/frictionless-py) | smoke existing | Validate CSV/JSON/XLS/SQL inputs before DuckDB/Polars analysis. |

### Proposed research and supply-chain worker

```text
candidate manifest
  -> pinned source/revision/license/hash
  -> uv or conda-lock environment record
  -> SBOM (Syft / Microsoft SBOM Tool)
  -> vulnerability scan (Grype / OSV-Scanner / pip-audit)
  -> offline smoke test
  -> acceptance record
  -> optional Work Order
```

The worker must never auto-install, auto-pull, auto-run, or promote artifacts to Cognee. It produces evidence for the Architect and Mechanic.

## Unified research order

1. Forge evaluation and GPU evidence first: a small fixture manifest, metrics writer, audit record, and admission-control evidence.
2. Smoke Qwen3-Reranker-0.6B against current retrieval without changing production embeddings.
3. Forge a bounded official Qwen3-14B-GGUF llama.cpp worker for schema-constrained extraction.
4. Compare Granite-Docling-258M, RapidOCR, and PaddleOCR-VL against real document classes.
5. Wire the existing Playwright boundary and test it on local pages plus MiniWoB++ before real-site workflows.
6. Compare Moonshine, faster-whisper, whisper.cpp, Kokoro, and Qwen3-TTS in separate voice lanes.
7. Test ONNX Runtime CUDA/TensorRT RTX only for fixed specialists where provider performance is measurable.
8. Add SBOM, policy, vulnerability, and artifact-signing evidence before downloading a large set of external workers.
9. Keep vLLM, TensorRT-LLM, Triton, OpenVINO, Podman, containerd, heavyweight OCR-VLMs, and new vector databases parked until a measured bottleneck justifies them.

## Candidate acceptance gate

Every candidate discovered through any avenue must answer all of these before promotion from research:

1. Can it run after installation with network blocked?
2. Is the exact code, model, image, and data license known?
3. Can the source and artifact be pinned by revision, digest, or hash?
4. Does it support the required Windows/native or WSL2 path?
5. What is the measured CPU, RAM, VRAM, latency, and cold-start cost?
6. Does it duplicate an existing EMPIRE boundary?
7. Can it be exposed as a narrow pipeline, CLI, library, local API, or MCP tool?
8. What approval, origin, path, model, or resource guardrails are required?
9. Does it preserve provenance and explicit Cognee promotion?
10. What result would cause the Architect to reject it?

If any answer is unknown, the candidate remains `smoke existing`, `park`, or `idea-queue only`; it does not enter the production catalog.

## Eve model acquisition plan

This section answers a narrower question: which open-weight models should EMPIRE acquire to cover modern AI capabilities locally, and how should they be run on approximately 16 GB VRAM and 64 GB RAM?

### Operating principle

Do not try to make one model do every job. Keep one resident interactive reasoning model and load specialist models one at a time under the GPU lease. CPU-first workers may remain resident when their memory footprint is small.

Resource lanes:

- **L0:** CPU or under approximately 2 GB VRAM.
- **L1:** approximately 2-6 GB VRAM; short specialist jobs.
- **L2:** approximately 7-12 GB VRAM; interactive text or one moderate specialist.
- **L3:** approximately 12-16+ GB VRAM; queued batch only.

Actual usage depends on context, KV cache, image size, batching, CUDA buffers, and runtime. The figures below are acquisition guidance, not measured EMPIRE results.

### Recommended acquisition manifest

| Capability | Model to acquire | Format/runtime | Lane | Sampling or decode settings | Status |
|---|---|---|---:|---|---|
| Eve reasoning/tool planning | `qwen3:14b` | Ollama; retain official artifact digest | L2 | Thinking: `temperature 0.6`, `top_p 0.95`, `top_k 20`; tool route: `0-0.2` | Acquire first; resident candidate |
| Fast Eve fallback | `qwen3:8b` | Ollama or official Q4_K_M GGUF | L1/L2 | Chat `0.4-0.6`; tools `0-0.2`; `top_p 0.8-0.95`, `top_k 20` | Acquire second; unload/swap as needed |
| Coding specialist | `qwen2.5-coder:14b` | Ollama; Q4_K_M GGUF fallback | L2 | `temperature 0.1-0.3`, bounded output, `top_p 0.8-0.95` | Acquire on demand; do not keep resident with Eve |
| Strict structured extraction | Official Qwen3-14B GGUF | `llama.cpp` Q4_K_M; GBNF/JSON Schema | L2 | `temperature 0`, bounded `max_tokens`; simple schemas only | Acquire after llama.cpp smoke |
| Fast embeddings | `qwen3-embedding:0.6b` | Ollama embedding API or local Transformers | L0/L1 | No temperature; batch inputs; record dimensions | Acquire for A/B; separate index |
| Retrieval reranking | `Qwen/Qwen3-Reranker-0.6B` | Transformers/Sentence Transformers | L1 | Deterministic scoring; no sampling; top 30-50 candidates | Acquire as queued worker |
| General vision/video/screens | `qwen3-vl:4b` or `qwen3-vl:8b` | Ollama | L1/L2 | Observation/OCR `0-0.2`; visual reasoning `0.5-0.7`; bounded frames | Acquire 4B first; 8B if quality warrants |
| Document visual parsing | `granite-docling-258M` | Docling/Transformers/ONNX | L0/L1 | Deterministic; `temperature 0` where applicable | Acquire for Docling extension |
| OCR/layout specialist | PaddleOCR-VL 1.5 or RapidOCR | PaddleOCR/ONNX; local model files | L0/L1 | Deterministic OCR thresholds; no sampling | Smoke against Docling/Tesseract |
| Speech-to-text | Whisper large-v3-turbo | faster-whisper INT8/FP16 or whisper.cpp quantized | L1/L2 | VAD on; timestamps on; beam 5 baseline; temperature fallback `[0.0, 0.2, 0.4]` | Acquire for voice worker |
| Low-latency English STT | Moonshine Base | CPU/ONNX/local toolkit | L0 | Greedy/deterministic; VAD preceding | Smoke as command front end |
| Voice activity detection | Silero VAD v6.x | ONNX Runtime CPU | L0 | No sampling; 8/16 kHz; tune speech/silence thresholds | Acquire after license review |
| Default TTS | Kokoro-82M | Python or ONNX; CPU/light GPU | L0/L1 | Fixed voice; speed about `1.0`; deterministic | Acquire first TTS |
| Expressive/voice cloning TTS | Qwen3-TTS 0.6B or Chatterbox Nano | Local Transformers/PyTorch | L1/L2 | Fixed seed where supported; explicit speaker consent | Smoke only; default OFF |
| Video generation | Wan2.1 T2V 1.3B | Diffusers; pinned weights | L2/L3 | Fixed seed; 480p; 4-8 steps if supported; short clips | Batch limb; acquire only when needed |
| Image generation baseline | SDXL 1.0 | Diffusers/ComfyUI only as optional worker | L2/L3 | Fixed seed; 20-30 steps; CFG 5-8 baseline; 512-768px | Smoke; default OFF |
| Image editing | SDXL inpainting | Diffusers; controlled masks | L2/L3 | Fixed seed; denoise `0.3-0.7`; CFG 5-8 | Smoke after image baseline |
| Audio separation | Demucs `htdemucs` or `mdx_q` | Existing Stem Factory CUDA venv | L1/L2 | Deterministic; segment/overlap recorded | Retain existing limb |
| Prediction/classification | Embedding + calibrated classifier first | CPU Python/ONNX; Qwen JSON only for low volume | L0/L1 | Classification `temperature 0`; calibration on held-out data | Forge evaluation path; no unverified forecaster yet |
| Browser grounding | Playwright accessibility tree + Qwen3-VL/OmniParser when needed | Existing Playwright MCP plus vision observer | L0/L2 | Grounding `0-0.2`; action plan schema `0` | Forge bounded browser limb |

### Resident versus queued

**Resident by default:**

- `qwen3:14b` or `qwen3:8b`, but not both simultaneously unless measured.
- Silero VAD CPU/ONNX.
- Small CPU embedding or classification worker only if it does not compete with Eve.
- Kokoro CPU TTS only if voice interaction is actively enabled.

**Queued and GPU-leased:**

- Qwen3-VL.
- Whisper turbo GPU mode.
- Qwen3 reranker if GPU inference is selected.
- PaddleOCR-VL or visual Docling profiles.
- Wan2.1, SDXL, Qwen3-TTS, Chatterbox, and Demucs.

Never assume Qwen3-VL, diffusion, TTS, STT, and Eve can remain simultaneously resident in 16 GB VRAM. The lease must be acquired before model loading, and a worker must be able to wait or use a CPU fallback.

### Quantization rules

For GGUF models:

- **Q4_K_M:** default 14B capacity choice; best first test when context and headroom matter.
- **Q5_K_M:** use when quality gain is measurable and full GPU residency remains possible.
- **Q6_K:** batch or quality experiment; likely too expensive for interactive 14B plus large KV cache.
- **Q8_0:** evaluation only on this host unless the model is small.
- **IQ formats:** do not make them the baseline until CUDA stability and quality are measured.

For Transformers models:

- Prefer an official 4-bit NF4, AWQ, or GPTQ checkpoint when the runtime officially supports it.
- Use 8-bit when quality matters and the worker still fits the lane.
- Record compute dtype, quantization format, tokenizer revision, runtime version, and file hashes.
- Do not treat an unofficial quantization as equivalent to the original model card.

For Ollama:

- Record `ollama show --modelfile`, the model digest, and `ollama ps` processor placement.
- Nominal artifact size is not total VRAM usage; KV cache, vision encoders, CUDA buffers, and context length add cost.
- Pin the tag and digest in the acquisition manifest; never use `latest` for a forged worker.

### Context and generation defaults

Keep EMPIRE's shared 8192 context as the starting point. Use retrieval, summary injection, and staged extraction before increasing context.

| Route | Context start | Temperature | Output bound |
|---|---:|---:|---:|
| Fast chat | 8192 | `0.4-0.6` | 512-1536 tokens |
| Deep reasoning | 8192 | `0.6` thinking | 1024-3072 tokens |
| Tool planning | 8192 | `0-0.2` | strict tool schema |
| Structured extraction | 4096-8192 | `0` | schema maximum |
| Coding | 8192-12288 | `0.1-0.3` | task-specific bound |
| Vision observation | 4096-8192 | `0-0.2` | JSON schema |
| Vision reasoning | 8192 | `0.5-0.7` | bounded explanation |
| Retrieval synthesis | 8192 | `0.2-0.5` | evidence-linked answer |

Qwen3's official thinking defaults are approximately `temperature 0.6`, `top_p 0.95`, `top_k 20`; its non-thinking defaults are approximately `temperature 0.7`, `top_p 0.8`, `top_k 20`. Use lower temperatures for tool/schema routes. Always bound `num_predict` or `max_new_tokens`.

Temperature does not apply to OCR, embeddings, VAD, or diffusion in the same way. For those, record deterministic preprocessing, seed, inference steps, CFG/guidance, denoise strength, frame count, duration, and sampler instead.

### Capability coverage and model choices

**Text, reasoning, and tools:** Qwen3-14B is the default. Qwen3-8B is the fast fallback. Qwen2.5-Coder-14B is an on-demand coding specialist. Do not acquire a second 30B+ resident brain on this hardware.

**Video understanding:** Qwen3-VL 4B first, 8B second. Extract representative frames with FFmpeg for long videos and keep video analysis queued. Do not send full recordings through interactive chat.

**Video creation:** Wan2.1 T2V 1.3B is the first candidate because its published VRAM requirement is more plausible for this host. Keep LTX-Video and CogVideoX as alternatives with separate license/runtime review. Generate short 480p clips only.

**Audio input:** Whisper large-v3-turbo through faster-whisper or whisper.cpp for quality; Moonshine Base for low-latency English commands; Silero VAD CPU-first. Do not keep turbo resident beside vision.

**Audio output:** Kokoro-82M is the default low-resource TTS. Qwen3-TTS or Chatterbox is an expressive/voice-cloning experiment requiring consent and a separate GPU lease.

**OCR and documents:** Docling remains the representation/provenance owner. Granite-Docling and PaddleOCR-VL are visual specialists. RapidOCR is a small ONNX comparison. None should auto-promote to Cognee.

**Browser manipulation:** Playwright handles ordinary DOM/accessibility interaction. Qwen3-VL or OmniParser supplies observation/grounding only when accessibility data is insufficient. Action execution remains approval-gated and allowlisted.

**Resource and document creation:** Qwen3 structured output creates Markdown/JSON/Work Order artifacts; llama.cpp grammars protect high-integrity extraction. SDXL, Wan2.1, and TTS create media artifacts with seed and model provenance.

**Prediction:** Start with embeddings plus a calibrated classifier or a conventional local forecasting library and evaluate it against a labeled fixture. Do not install an unverified “forecasting LLM” as Eve's prediction authority. Numeric predictions require confidence intervals, backtesting, and explicit uncertainty in the output schema.

### Models not to acquire initially

- Qwen3 30B/32B, Qwen2.5-Coder 32B, Qwen3-VL 30B/32B, and GPT-OSS 120B as resident models.
- Qwen3 Embedding 4B/8B or reranker 4B/8B as always-on services.
- FLUX or Qwen-Image as assumed 16 GB fits merely because community quantizations exist.
- HunyuanImage-3.0 and other 24-80 GB-class image/video models.
- Stable Audio or MusicGen for production without a separate non-commercial/data-license decision.
- OpenCUA/UI-TARS as autonomous actuators before observation, approval, and audit are forged.

### Acquisition smoke sequence

On the canonical EMPIRE computer, acquire and test one heavy model at a time:

1. Record Ollama version, NVIDIA driver, GPU VRAM, installed model digests, and baseline Eve latency.
2. Test Qwen3-14B at 8192 context for ordinary chat, 25 tool calls, and 25 JSON Schema extractions.
3. Test Qwen3-8B for latency and quality as a fast route.
4. Test Qwen3-VL 4B, then 8B, on screenshots and sampled video frames while Eve is unloaded.
5. Test Qwen3 Embedding 0.6B and Qwen3 Reranker 0.6B against the current retrieval set without changing production indexes.
6. Test Whisper turbo, Kokoro, and Silero as the voice path; compare CPU and GPU modes.
7. Test Granite-Docling, RapidOCR, and PaddleOCR-VL against representative document classes.
8. Test Wan2.1 1.3B or SDXL only as a queued artifact generator.
9. Re-run the relevant worker with network blocked and verify no runtime downloads.
10. Accept a model only when it improves a defined outcome, fits the lease, records provenance, and has a fallback or explicit rejection path.

Every acquired model should enter the manifest as `candidate` until this smoke sequence records measured VRAM, RAM, latency, quality, license, and offline behavior.

## Final recommendations before forging

The remaining high-value work is operational rather than another model server. EMPIRE already has the right primitives; the next gains come from making them reversible, measurable, recoverable, and enforceable.

### 1. Versioned release manifests and rollback

Create a local release manifest containing model digests, runtime versions, prompts, schemas, package locks, configuration hashes, and evaluation results. Activate a candidate through a staged release pointer and retain the last known-good release.

The first vertical slice should be one structured-extraction worker:

```text
candidate manifest
  -> staged model/runtime
  -> golden evaluation
  -> acceptance record
  -> active-release pointer
  -> audit envelope
  -> one-step rollback
```

Do not begin with unattended upgrades, multi-host deployment, or a general package manager.

### 2. Golden evaluations and shadow routing

Create a versioned EMPIRE fixture set covering tool calls, retrieval, OCR, structured extraction, and voice/vision where relevant. Record quality, latency, VRAM, RAM, parse success, refusal behavior, and failure recovery. New models should run in maintenance or shadow mode before becoming active.

Public benchmarks help select candidates; they should not be the production gate.

### 3. Restore-tested backup and disaster recovery

EMPIRE state is distributed across Cognee's VHDX, PocketBase, workbench files, chat history, manifests, and configuration. Define backup tiers, hash backup contents, retain at least one disconnected copy, and perform a documented restore drill for each authoritative state.

A copied file is not a proven backup until the service can be restored and queried.

### 4. Typed artifact and lineage envelope

Standardize a machine-readable envelope for every worker output:

```yaml
artifact_id: <id>
run_id: <id>
parent_ids: []
source_hash: <sha256>
schema_version: <version>
model_revision: <revision>
runtime_revision: <revision>
created_at: <timestamp>
sensitivity_class: <class>
retention_class: <class>
promotion_state: scratch | reviewed | promoted
```

This supports correlation, idempotency, replay, deletion, and explicit Cognee promotion without introducing an event-bus platform.

### 5. Enforceable privacy and local-security policy

Add data classification, Windows ACL expectations, DPAPI or Windows Credential Manager for secrets, outbound-egress deny-by-default for workers, redaction before logs, CSRF/auth checks on local mutation APIs, and isolated browser profiles.

Loopback binding is necessary but is not a complete security boundary. Do not expose secrets, browser credentials, raw screen captures, or audio in generic audit logs.

### 6. Explicit failure and recovery semantics

Every job should expose states such as `queued`, `starting`, `running`, `cancelled`, `failed`, `degraded`, and `completed`. Add timeouts, cancellation, stale-lock recovery, bounded retries, idempotent reruns, partial-artifact cleanup, and clear CPU fallback behavior.

Model unloads, stale Cognee locks, killed containers, interrupted GPU jobs, and disk pressure are normal single-workstation failure modes.

### 7. Admission control beyond VRAM

Extend the GPU lease into a resource policy covering estimated VRAM, RAM, disk space, model-load I/O, CPU saturation, and Windows paging. Reserve an interactive Eve budget. A worker must pass preflight checks before loading a model and report post-run measurements afterward.

Do not build multi-GPU scheduling or Kubernetes for this host.

### 8. Retention and deletion semantics

Add retention classes for chat history, scout caches, screenshots, audio, failed artifacts, backups, and durable memory. A user-visible purge operation should identify copies across scratch folders, indexes, audit records, and eligible backups.

Keep ordinary deletion distinct from backup expiry or cryptographic destruction. Never silently delete durable Cognee memory.

### 9. Operational UX for truth

The workbench should show whether Eve is ready, queued behind a model swap, running in degraded CPU mode, using stale memory, or awaiting approval. A run-status surface should show the active release, model state, queue position, resource reason, provenance link, failure class, and recovery action.

Approval prompts should identify the exact origin, paths, model, and data being sent to a limb.

### Final acceptance question

Before calling an upgrade production-ready, ask:

> Can EMPIRE explain, reproduce, undo, and restore one model-backed operation without network access or manual filesystem archaeology?

If not, keep the candidate in research, maintenance, or shadow mode. Explicitly remain out of scope: Kubernetes, a second agent framework or memory authority, automatic model pulling/upgrades, automatic Cognee promotion, unrestricted shell/filesystem/browser/Docker control, LAN exposure, cloud backup, mandatory accounts, autonomous desktop actuation, and simultaneous heavy resident models on the 16 GB GPU.
