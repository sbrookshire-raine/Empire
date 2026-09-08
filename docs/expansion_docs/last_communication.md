
Completed

Yes. Several of the earlier repositories materially expand Eve’s capabilities without replacing the strengths you already have. The important decision is to add specialists and workers, not overlapping agent frameworks, databases, or generic “do everything” MCP servers.

Your laptop is powerful enough for a strong, mostly offline multimodal workstation:

RTX 5080-class GPU, 16 GB VRAM
64 GB RAM
local Qwen 2.5 16B already running
local Weaviate Wikipedia
Cognee memory layer
Postgres/PocketBase operational layer
Eve orchestration
FastMCP capability layer
You will not run frontier 70B+ models fully in VRAM at high speed, but you can run excellent quantized 7B–16B text and vision models, high-quality embeddings/rerankers, transcription, TTS, OCR, structured document ingestion, data analysis, and supervised computer control.

Recommended offline-first model architecture

                           ┌────────────────────────┐
                           │ Eve                    │
                           │ Planning / personality │
                           │ Task delegation        │
                           └───────────┬────────────┘
                                       │
                         OpenAI-compatible local APIs
                                       │
┌──────────────────────────────────────┼──────────────────────────────────────┐
│                                      │                                      │
▼                                      ▼                                      ▼
Text reasoning                    Vision worker                         Voice worker
Qwen 2.5 16B                      Qwen VL 7B                            whisper.cpp
or Qwen 3 14B                     / Qwen 2.5 VL 7B                      Piper or Coqui
Tool calling                      Screens / docs / charts               VAD + STT + TTS
Structured output                 GUI perception                         Barge-in handling
│                                      │                                      │
└───────────────┬──────────────────────┴──────────────────────┬───────────────┘
                │                                             │
                ▼                                             ▼
      Retrieval worker                                FastMCP internal gateway
      Qwen embedding 0.6B/4B                           Data / docs / media /
      Qwen reranker 0.6B                               browser / desktop / system
      Weaviate + Cognee
What should remain unchanged
Existing part	Keep it?	Reason
Eve	Yes	It is your operating brain: sessions, skills, tools, approvals, subagents, evaluations, scheduling.
Cognee	Yes	Use it only for curated durable semantic/graph memory.
Weaviate Wikipedia	Yes	Excellent local factual reference layer.
PocketBase	Yes	Good task/UI/realtime layer.
PostgreSQL	Yes	Keep as source of truth for audit, job state, provenance, artifacts, and authoritative data.
FastMCP	Yes	Correct boundary for local specialist tools and CLI wrappers.
Qwen 2.5 16B	Yes	Keep as the primary text reasoning/planning model until evals show a different model performs better for your tasks.
Additions that are genuinely worth adding
1. Docling — best document-ingestion upgrade
Repository: docling-project/docling
License: MIT
Interface: Python API and CLI
Priority: P0

Docling is a major improvement over a simple PDF-text-extraction pipeline. It handles:

PDFs, DOCX, PPTX, XLSX, HTML, EPUB, email, images, audio/video-related formats;
PDF layout understanding;
tables;
charts;
OCR and visual document parsing;
structured output and Markdown export;
local operation on Windows/Linux/macOS;
optional vision-language model processing.
Use it in your stack

PocketBase upload / external research node output
        │
        ▼
Postgres ingestion job
        │
        ▼
Docling worker
        │
        ├── structured Markdown
        ├── tables / chart descriptions
        ├── page/source offsets
        ├── content hash
        └── normalized metadata
        │
        ├── Weaviate: searchable working knowledge
        ├── Postgres: source/provenance/job status
        └── Cognee: only promoted durable knowledge
Expose only narrow FastMCP tools:


inspect_document
extract_structured_document
extract_tables
render_document_pages
create_document_summary_artifact
Do not let Eve pass arbitrary URLs or filesystem paths into Docling.

2. MarkItDown — lightweight companion to Docling
Repository: microsoft/markitdown
License: MIT
Priority: P1

Use MarkItDown for quick, low-cost conversions:

Office documents;
PDFs;
HTML;
ZIP-contained formats;
standard local text/document conversion into Markdown.
Use Docling when layout, tables, charts, complex PDFs, OCR, or high-quality document structure matters.


Simple file / quick conversion       → MarkItDown
Complex PDF / OCR / tables / charts  → Docling
MarkItDown warns that it performs I/O with the invoking process’s privileges. Wrap only convert_local() or convert_stream() equivalents inside a directory-restricted worker. Do not expose its broad permissive convert() behavior to the model.

3. Qwen 3 Embedding + Reranker — highest-value retrieval upgrade
Repository: QwenLM/Qwen3-Embedding
Priority: P0

This is probably the best model-side upgrade for your Wikipedia, thought-experiment, research, and Cognee retrieval workflow.

Available sizes include:

embedding: 0.6B, 4B, 8B
reranker: 0.6B, 4B, 8B
Recommended choice for your hardware
Worker	Recommendation	Why
Default embedding	Qwen3-Embedding-0.6B	Fast enough for continuous ingestion and query-time retrieval.
High-quality embedding	Qwen3-Embedding-4B	Use for curated documents, thought experiments, and important project knowledge.
Default reranker	Qwen3-Reranker-0.6B	Strong practical reranking after Weaviate candidate retrieval.
Premium reranker	Qwen3-Reranker-4B	Use selectively for high-value research synthesis and memory promotion.
Do not use the 8B embedding/reranker models as your default on a 16 GB card while Qwen 16B is loaded. They can be used as separately loaded job workers, but not as a constant concurrent service unless latency is acceptable.

Retrieval pipeline upgrade

Question / task / thought experiment
        │
        ▼
Weaviate hybrid search
  - vector candidates
  - keyword candidates
  - metadata filters
        │
        ▼
Top 30–80 snippets
        │
        ▼
Qwen3-Reranker-0.6B
        │
        ▼
Top 5–10 evidence blocks
        │
        ▼
Qwen 2.5 16B / Eve synthesis
This gives Eve better local factual grounding than merely increasing Qwen’s context window.

Use metadata filters aggressively:


source_type
source_id
snapshot_version
project_id
organization_id
document_hash
created_at
review_status
trusted_level
promotion_status
4. llama.cpp — best control-oriented runtime addition
Repository: ggml-org/llama.cpp
License: MIT
Priority: P0

Ollama is great for convenience. Add llama.cpp when you need tighter local control:

CUDA/NVIDIA support;
quantized GGUF model execution;
CPU + GPU hybrid offload for models larger than VRAM;
OpenAI-compatible local server;
multimodal/VLM support;
GBNF grammars for constrained structured output;
minimal dependency/runtime footprint.
Why it matters for Eve
For task creation, tool arguments, approvals, memory promotion candidates, and research records, you want strict output structure.

Use grammars or schema-constrained generation for local jobs such as:


TaskDraft
ResearchEvidence
ThoughtExperimentRecord
MemoryPromotionCandidate
DesktopActionPlan
DocumentMetadata
Do not depend on “please return JSON” prompt instructions alone.

Runtime strategy

Ollama:
  Default developer-friendly Qwen runtime

llama.cpp:
  Controlled GGUF / constrained-output worker
  Vision worker experimentation
  Larger model CPU+GPU fallback
  Offline emergency runtime
You do not need to replace Ollama. Run both for their strengths.

5. Qwen VL model — best multimodal extension
Repository: QwenLM/Qwen3-VL
License: Apache-2.0
Priority: P1

A Qwen vision-language model gives Eve local understanding of:

screenshots;
UI state;
charts;
scanned/visual documents;
diagrams;
images;
short video frames;
desktop visual context.
Qwen3-VL specifically positions itself for visual agent work, GUI understanding, spatial reasoning, visual coding, tool invocation, and PC/mobile interaction.

Hardware recommendation
For 16 GB VRAM, use a quantized 7B-class vision model as the starting point. It should be treated as a dedicated worker, not continuously loaded alongside Qwen 2.5 16B unless your GPU memory budget proves it can coexist.


Default text agent:
  Qwen 2.5 16B, quantized

Vision worker:
  Qwen 2.5 VL 7B or Qwen 3 VL 7B, quantized

Fast screen parser:
  OmniParser detector + OCR

Heavy document image job:
  temporarily unload/swap text model or queue job
Do not use vision for everything
Use a routing policy:

Input	First tool
Text/PDF with reliable extractable text	Docling / MarkItDown
Screenshot/UI controls	OmniParser + pywinauto UI Automation
Chart/diagram/image explanation	Qwen VL
Visual document requiring layout understanding	Docling first, Qwen VL only for unresolved visual regions
Desktop action grounding	OmniParser + UI Automation selectors; VLM as validation/fallback
6. OmniParser — use for visual grounding, not general reasoning
Repository: microsoft/OmniParser
Priority: P2

OmniParser converts screenshots into structured screen regions, icons, labels, and interactability signals. That is exactly what you need for desktop control.

Use it as a perception preprocessor:


Screenshot
   │
   ├── pywinauto / Windows UIA tree, if available
   ├── OCR / Tesseract
   └── OmniParser interactive regions
             │
             ▼
Qwen VL validates goal / identifies candidate control
             │
             ▼
Eve proposes action for user approval
This is safer and more reliable than asking a vision model to invent coordinates from pixels.

License caution
The repository is CC-BY-4.0, while components have different terms:

current YOLOv9-E detector: MIT-derived;
older Ultralytics detector components: AGPL;
caption model: MIT.
Pin the exact component set and document its license before product distribution.

7. whisper.cpp + Piper / Coqui — complete offline voice stack
Speech-to-text
Repository: ggml-org/whisper.cpp
License: MIT
Priority: P0

It has:

local C/C++ inference;
CPU and GPU support;
quantized models;
VAD support;
realtime microphone streaming example;
local HTTP server;
whisper-command voice-assistant example.
Use:


whisper-stream
+ Silero VAD
+ push-to-talk initially
+ barge-in interruption
Text-to-speech
Option	License	Use
Piper	GPL-3.0	Fast, practical, local voice for daily use. CLI, web server, Python, C/C++ APIs.
Coqui TTS	MPL-2.0	Higher-quality expressive/custom voice; XTTS supports streaming and voice-cloning workflows.
Recommendation
Start with:


whisper.cpp + VAD
Piper
Then evaluate Coqui XTTS for the conversational Eve voice after the UX works.

Remember: “personality” comes from Eve’s instruction and interaction policy. Voice is the auditory presentation. Do not expect a custom voice alone to create personality.

Tools from the prior catalog that strengthen your stack
Add now
Tool	What it adds	Placement
Docling	High-quality document ingestion/OCR/layout/table extraction	Document worker → FastMCP
MarkItDown	Fast lightweight document-to-Markdown conversion	Document worker → FastMCP
DuckDB	Local analytical SQL over files/Parquet/JSON/SQLite	Analytics FastMCP server
Polars	Fast typed data analysis/comparison	Analytics FastMCP server
Qwen embedding/reranker	Better Weaviate/Cognee retrieval quality	Retrieval worker
whisper.cpp	Offline realtime speech input	Voice worker
Piper	Fast offline voice output	Voice worker
Coqui TTS	Optional expressive/custon voice	Voice worker
llama.cpp	Controlled GGUF inference / grammar-constrained JSON	Model utility worker
Tesseract + OCRmyPDF + pypdf	Reliable fallback document and OCR path	Document worker
Pandoc + LibreOffice headless	Report/document conversions	Artifact worker
FFmpeg + ImageMagick	Audio/video/image artifacts and visual preprocessing	Media worker
psutil	Local health/CPU/GPU/process summaries	Read-only system FastMCP server
uv	Reproducible isolated Python environments	Infrastructure, not model-facing
Add later
Tool	Why defer
Playwright	Useful for your internal GUI and local LAN apps, but requires a careful approval policy.
pywinauto	Excellent Windows semantic automation, but should start observe-only.
PyAutoGUI	Necessary fallback for input simulation, but risky and brittle.
OpenAdapt	Good for human demonstration recording; only use once action logging and review UX exists.
OmniParser	Valuable but more setup and license-component review than docs/data/voice improvements.
Docker CLI tools	Do not expose to Eve except through narrow admin operations.
Qdrant/Chroma/Kùzu	You already have Cognee + Weaviate + Postgres. Add only after a measured gap.
Do not add by default
Tool	Reason
Another agent framework	Eve already owns the orchestrator role.
Generic filesystem / shell MCP	Too much authority; use narrow project tools.
Generic PocketBase management MCP	Keep PocketBase domain operations typed and scoped.
Generic database MCP	Keep raw SQL and schema changes away from model control.
Extra vector database	Weaviate + Cognee already cover retrieval/memory.
gpt-oss-20b as default	Strong option, but 20B still strains a 16 GB card once KV cache/context and runtime overhead are counted. Test as a CPU+GPU hybrid or secondary model rather than replacing stable Qwen 16B immediately.
LLaVA	Still useful, but newer Qwen VL models are generally better aligned with your Qwen text stack and GUI-agent objective.
Molmo as primary VLM	Worth benchmarking for image understanding, but Qwen VL is the more coherent first choice for tool/agent integration.
What your hardware can realistically do
Keep simultaneously active
A realistic always-on stack:


Qwen 2.5 16B quantized
Weaviate
PostgreSQL
PocketBase
Cognee services
FastMCP gateway
Qwen embedding 0.6B
Qwen reranker 0.6B
whisper.cpp small/base model
Piper
Whether all model workers share the GPU depends on the exact quantization, context length, CUDA overhead, and Weaviate load. Do not assume it will fit cleanly just because parameter arithmetic looks close.

Better scheduling approach
Treat GPU memory as a scheduled resource:


Interactive lane:
  Qwen 2.5 16B
  whisper.cpp
  Piper
  embedding/reranker small models

Batch/vision lane:
  Qwen VL 7B
  Docling VLM or OCR
  heavy reranker 4B
  media analysis

Never run both lanes' largest models concurrently by default.
Use a local worker queue in Postgres:


gpu_jobs
- id
- type
- priority
- required_vram_class
- status
- requested_by
- input_artifact_id
- output_artifact_id
- started_at
- completed_at
Suggested priority levels

P0: voice interaction / user is waiting
P1: active chat reasoning
P2: retrieval/reranking
P3: document ingestion
P4: visual analysis
P5: reindexing / batch Cognee promotion
This prevents background embedding or document ingestion from making Eve feel slow while you are talking to her.

Offline-continuity design
If online interaction disappears, Eve should degrade gracefully rather than lose core capabilities.


Online available:
  Local Wikipedia
  Local project knowledge
  External research nodes
  Optional cloud model/research sources

Offline:
  Local Qwen reasoning
  Local Weaviate Wikipedia
  Local Cognee memory
  Local Postgres/PocketBase tasks
  Local documents/artifacts
  Local STT/TTS
  Local analysis/OCR/media tools
  Local LAN desktop/browser workers
Add a connectivity-aware policy

network_state = online | degraded | offline

online:
  local retrieval first
  then permitted external research nodes

degraded:
  explain freshness limitation
  queue external research requests

offline:
  never attempt external research
  search local Wikipedia/project evidence/Cognee
  label outputs with:
  "Offline mode: conclusions are based on local sources current through [snapshot date]."
Store external research requests in Postgres when offline, then let Eve resume them after connectivity returns.

Suggested project modules

agent/
  instructions.md
  skills/
    companion/
    research/
    thought-experiment/
    task-management/
    offline-mode/
    data-analysis/
    document-analysis/
    voice-interaction/
  tools/
    create_task_draft.ts
    approve_task.ts
    search_local_wikipedia.ts
    request_external_research.ts
    request_memory_promotion.ts
    get_system_capabilities.ts
  memory/
    profile.ts
    project.ts
  hooks/
    audit.ts
    task-sync.ts
    memory-promotion.ts
    gpu-job-events.ts
  subagents/
    researcher/
    analyst/
    document-specialist/
    vision-specialist/

fastmcp/
  gateway.py
  servers/
    retrieval.py
    documents.py
    analytics.py
    media.py
    system.py
    desktop_observer.py
    browser_local.py

workers/
  voice/
    stt_worker.py
    tts_worker.py
  models/
    text_model_service.py
    vision_model_service.py
    embeddings_service.py
    reranker_service.py
  ingestion/
    docling_worker.py
    weaviate_worker.py
    cognee_promotion_worker.py
Best next implementation order
Add Docling and an ingestion/provenance pipeline.
Add Qwen 0.6B embedding + reranker to improve local retrieval.
Build whisper.cpp + Piper push-to-talk voice loop.
Add a GPU-aware Postgres job queue.
Add llama.cpp for grammar-constrained structured outputs and offline fallback.
Add a quantized Qwen VL 7B vision worker.
Add OmniParser + pywinauto as observe-only desktop perception.
Add supervised desktop actions only after approval/audit UI is mature.
The best optimization is not “run the largest model possible.” It is a set of specialized local workers with Eve routing between them: Qwen for reasoning, a VLM for sight, embedding/reranking for recall, Docling for documents, Whisper/Piper for voice, DuckDB/Polars for analysis, and constrained FastMCP tools for action.



i currently have nomic as the embedding model, using ollama for model loading, so options need to be supported via ollama. I can rerun current files through another embedding model for cognee if recommended. write me a full manifest for expanding and maximizing this project. consider all models, tools, etc that fit my hardware and stack profile. links to repos, ollama models, etc would be helpful. i plan to share this with cursor to help build it, so anything you can do to make it easier for it to understand and process the better. it already has the directives set, so it will understand if what is requested is not possible. make it as clear as possible. do deep research first, then build manifest


Deep-research plan
I’ll produce a Cursor-ready expansion manifest scoped to your actual constraints:

Eve is the primary agent brain
Ollama is the only model-loading/runtime path
RTX 5080-class 16 GB VRAM + 64 GB RAM
Nomic is the current embedding model
Cognee, Weaviate Wikipedia, PocketBase, PostgreSQL, FastMCP, and GUI already exist
Offline-capable/local-first behavior is required
I’ll verify exact Ollama model availability and capabilities first—especially embeddings, rerankers, text reasoning, vision, speech/voice support, and practical memory fit—then evaluate which earlier repo tools complement rather than duplicate your current stack. I will not modify workspace files while you are in Plan mode.