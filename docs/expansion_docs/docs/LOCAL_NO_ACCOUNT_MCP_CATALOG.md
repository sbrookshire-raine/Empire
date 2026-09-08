# Local-Only, No-Account MCP / CLI Tool Catalog

**Scope:** tools an agent can use after local installation without a vendor login, account, OAuth flow, API key, cloud plan, or normal-operation internet access. Network-capable tools are included only where they can be bound to `localhost` or an approved LAN allowlist.

**Catalog data:** [`local-no-account-tools.yaml`](local-no-account-tools.yaml). The YAML is the machine-readable source of truth for FastMCP adoption planning.

## Selection rules

An entry qualifies only when its core function can run from the machine or LAN:

- **Native MCP** means it already speaks Model Context Protocol.
- **CLI wrapper** means FastMCP calls a tightly constrained local command.
- **Library wrapper** means FastMCP exposes typed Python functions instead of executing arbitrary code.
- **Local API wrapper** means FastMCP talks only to a service running on `localhost` or an allowlisted LAN host.
- Downloading installers, packages, browser binaries, language data, or model weights is an installation-time concern. A tool must not need an account after it is installed.

Excluded: GitHub/GitLab cloud, Google/Microsoft/Slack/Notion integrations, hosted LLMs, hosted vector databases, SaaS automation, public web search/fetching, and any integration that needs a token—even if its source code is open.

## Recommended initial bundle

Adopt these first. They cover persistent local state, comparative data analysis, documents, and tightly scoped workstation inspection without giving an agent unrestricted command execution.

| Priority | Component | FastMCP surface to expose | Default privilege |
|---|---|---|---|
| P0 | Official MCP filesystem server | Mounted server constrained to approved workspace roots | Read-only |
| P0 | Official MCP Git server | Local repository status, diff, log, and read operations | Read-only |
| P0 | DuckDB + Polars | Dataset profile, schema, comparison, aggregate, and chart-data tools | Read-only |
| P0 | SQLite | Structured agent state and local task/audit data | Read-only except dedicated state namespace |
| P0 | Qdrant + local embeddings | `remember`, `search_memory`, `forget_memory` with per-user/project namespaces | Scoped write |
| P0 | Tesseract + OCRmyPDF + pypdf | OCR, extract, inspect, and render documents under allowed roots | Read-only output artifacts |
| P1 | Pandoc + LibreOffice headless | Convert office/document files within a sandbox directory | Writes only to output directory |
| P1 | FFmpeg + ImageMagick | Inspect and transform local media to a sandbox output directory | Writes only to output directory |
| P1 | Ollama or llama.cpp | Narrow local-model tasks, bound to localhost | No model-management tools by default |
| P2 | Playwright | Browser actions only against explicitly allowlisted local/LAN origins | Confirmation before form submit/download |
| P2 | pywinauto + PyAutoGUI | Window inspection and supervised desktop actions | Confirmation before input events |

## Capability catalog

The catalog deliberately favors mature, direct building blocks over random MCP wrappers. Wrapping these tools in your own FastMCP server keeps tool names, schemas, authorization, paths, logging, and confirmation behavior under your control.

### Native local MCP servers

| Tool | Repository | Core local capability | FastMCP adoption |
|---|---|---|---|
| Filesystem | [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | Directory-scoped local file operations | Mount/proxy it; configure only approved roots. |
| Git | [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | Local Git repository inspection and operations | Mount/proxy it; split read from commit/branch mutation. |
| SQLite | [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | SQLite queries and analysis | Use read-only DB connections for agent-provided SQL. |
| PostgreSQL | [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | Self-hosted local/LAN PostgreSQL | Use an agent-specific read-only role. |
| Memory | [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | Demonstration knowledge graph memory | Use only as a reference; prefer Qdrant/Kùzu/SQLite for production persistence. |

The official repository says these are reference implementations, not automatically production-ready; its top-level license has mixed historical terms. Review each package before vendoring or redistribution.

### Local data, memory, and analysis

| Tool | License | Interface | Use through FastMCP |
|---|---:|---|---|
| [DuckDB](https://github.com/duckdb/duckdb) | MIT | CLI, Python API | Profile and compare CSV, Parquet, JSON, and SQLite data using parameterized, read-only SQL. |
| [Polars](https://github.com/pola-rs/polars) | MIT | Python/Rust API | Typed DataFrame operations: join, group, compare, missing-value and duplicate detection. |
| [pandas](https://github.com/pandas-dev/pandas) | BSD-3-Clause | Python API | Broad compatibility for spreadsheets and local data formats. |
| [SQLite](https://github.com/sqlite/sqlite) | Public domain | CLI, embedded library | Durable local state, audit logs, and structured agent memory. |
| [PostgreSQL](https://github.com/postgres/postgres) | PostgreSQL License | Local/LAN server, CLI | Multi-process structured data with a local role-based boundary. |
| [Qdrant](https://github.com/qdrant/qdrant) | Apache-2.0 | Local HTTP/gRPC | Vector retrieval; bind to loopback and use namespaced collections. |
| [Chroma](https://github.com/chroma-core/chroma) | Apache-2.0 | Python, local HTTP | Simpler local vector store for prototypes. |
| [Kùzu](https://github.com/kuzudb/kuzu) | MIT | Embedded database, Python API | Local graph memory and relationship traversal without a server. |
| [Neo4j Community](https://github.com/neo4j/neo4j) | GPL-3.0 | Local/LAN database | Graph memory when Cypher and a server are desired; assess copyleft obligations. |
| [sentence-transformers](https://github.com/UKPLab/sentence-transformers) | Apache-2.0 | Python API | Generate embeddings locally; model weights have separate licenses. |

### Documents, OCR, office files, and media

| Tool | License | Interface | Use through FastMCP |
|---|---:|---|---|
| [Tesseract](https://github.com/tesseract-ocr/tesseract) | Apache-2.0 | CLI/library | Offline OCR for images and rendered pages. |
| [OCRmyPDF](https://github.com/ocrmypdf/OCRmyPDF) | MPL-2.0 | CLI | Create searchable local PDFs; write only into a controlled output root. |
| [pypdf](https://github.com/py-pdf/pypdf) | BSD-3-Clause | Python API | Extract, merge, split, rotate, and inspect PDFs. |
| [PyMuPDF](https://github.com/pymupdf/PyMuPDF) | AGPL-3.0/commercial | Python API | Rendering/extraction option; do not adopt without accepting its license model. |
| [Pandoc](https://github.com/jgm/pandoc) | GPL-2.0-or-later | CLI | Sandboxed document conversion. |
| [LibreOffice](https://github.com/LibreOffice/core) | MPL-2.0 | Headless CLI, UNO API | Spreadsheet/document conversion and recalculation. |
| [ImageMagick](https://github.com/ImageMagick/ImageMagick) | ImageMagick License | CLI/library | Inspect, resize, convert, and annotate local images. |
| [FFmpeg](https://github.com/FFmpeg/FFmpeg) | LGPL-2.1-or-later/GPL depending on build | CLI/library | Inspect/transcode/clip local audio and video; choose build options deliberately. |
| [librosa](https://github.com/librosa/librosa) | ISC | Python API | Local audio features, segmentation, and comparisons. |

### Local models, speech, and vision

| Tool | License | Interface | Use through FastMCP |
|---|---:|---|---|
| [Ollama](https://github.com/ollama/ollama) | MIT | Local CLI/HTTP API | Connect only to loopback; expose task-specific inference tools, not raw unrestricted prompts. |
| [llama.cpp](https://github.com/ggml-org/llama.cpp) | MIT | CLI/local HTTP server | Portable local GGUF inference and embeddings. |
| [vLLM](https://github.com/vllm-project/vllm) | Apache-2.0 | Local HTTP API | High-throughput GPU serving if hardware supports it. |
| [whisper.cpp](https://github.com/ggml-org/whisper.cpp) | MIT | CLI/local server | Offline audio transcription. |
| [faster-whisper](https://github.com/SYSTRAN/faster-whisper) | MIT | Python API | High-performance local transcription. |
| [Piper](https://github.com/OHF-Voice/piper1-gpl) | GPL-3.0 | CLI/library | Offline TTS; assess GPL requirements and selected voice-model terms. |
| [Coqui TTS](https://github.com/coqui-ai/TTS) | MPL-2.0 | Python/CLI | Local TTS, multi-speaker synthesis, and fine-tuning; voice/model terms and consent apply. |
| [OmniParser](https://github.com/microsoft/OmniParser) | CC-BY-4.0 repository; components vary | Python/model API | Parse screenshots into UI elements; review each detector/caption model license. |

### Desktop, browser, system, and workflow automation

| Tool | License | Interface | Use through FastMCP |
|---|---:|---|---|
| [Playwright](https://github.com/microsoft/playwright) | Apache-2.0 | Python/Node API, CLI | Local/LAN browser automation with an origin allowlist and confirmation for submits/downloads. |
| [pywinauto](https://github.com/pywinauto/pywinauto) | BSD-3-Clause | Python API | Windows UI Automation/Win32 control; prefer semantic controls to screen coordinates. |
| [PyAutoGUI](https://github.com/asweigart/pyautogui) | BSD-3-Clause | Python API | Screenshots and mouse/keyboard input; require confirmation before every input sequence. |
| [OpenAdapt](https://github.com/OpenAdaptAI/OpenAdapt) | MIT | Local app/API | Record/replay desktop demonstrations; normalize actions into stable selectors before reuse. |
| [psutil](https://github.com/giampaolo/psutil) | BSD-3-Clause | Python API | Read-only process, CPU, memory, disk, and network inspection. |
| [APScheduler](https://github.com/agronholm/apscheduler) | MIT | Python API | Local recurring jobs and maintenance schedules. |
| [Node-RED](https://github.com/node-red/node-red) | Apache-2.0 | Self-hosted local/LAN API/UI | Local visual workflows; bind/admin-protect the editor on LAN. |
| [Docker CLI](https://github.com/docker/cli) | Apache-2.0 | CLI | Local container operations; isolate as high-risk and never expose generic command execution. |
| [jc](https://github.com/kellyjonbrazil/jc) | MIT | CLI | Parse allowlisted local command output into JSON. |

## FastMCP adapter patterns

### 1. Wrap a library, not a shell command

Use a library wrapper for DuckDB, Polars, pypdf, psutil, pywinauto, Qdrant clients, and local model clients. Typed input models and narrow return data provide validation and auditability.

For example, model the data-analysis surface as separate `profile_dataset`, `compare_datasets`, `summarize_column`, and `create_chart_data` tools. Each tool should accept a cataloged dataset identifier—not an unrestricted filesystem path—and use fixed operation parameters. Return bounded JSON results or an artifact reference, never an arbitrary DataFrame serialization or generic SQL execution result.

### 2. Wrap a CLI with a fixed argument schema

For Tesseract, Pandoc, FFmpeg, ImageMagick, and LibreOffice, build each tool around a fixed command template. Resolve inputs under an allowlisted root, use argument arrays instead of a shell, set timeouts and resource limits, and force outputs into an agent artifact directory.

Never expose a tool such as `run_command(command: str)`.

### 3. Connect only to local services

For Ollama, Qdrant, Chroma, PostgreSQL, Node-RED, or a local Playwright endpoint:

- default to `127.0.0.1`;
- reject public addresses and DNS names;
- permit LAN hosts only from a static allowlist;
- use separate local database users/credentials even when no vendor account is involved;
- make destructive actions distinct tools with explicit confirmation.

### 4. Mount existing MCP servers selectively

The official filesystem, Git, SQLite, and PostgreSQL MCP servers can be mounted or proxied behind your FastMCP gateway. Do not blindly aggregate every tool: preserve directory, repository, database-role, and audit boundaries.

## Mandatory controls

1. **Allowed roots:** canonicalize paths and reject traversal, symlink escapes, and UNC paths unless explicitly approved.
2. **Read first:** filesystem, Git, SQL, process, document, and analytics tools must be read-only by default.
3. **Separate mutation:** use individually named `write_*`, `delete_*`, `commit_*`, `click_*`, `type_*`, and `submit_*` tools; require an approval token for each.
4. **No generic shell:** no arbitrary command, PowerShell, Python, Docker, SQL, or browser-JavaScript execution tool for the model.
5. **Desktop supervision:** screenshots are sensitive; never automatically type secrets, submit forms, send messages, delete items, or approve purchases.
6. **Local model license review:** application code can be permissively licensed while downloaded model weights may be restricted. Track weights separately.
7. **Audit logs:** record tool name, validated inputs, user approval, result summary, artifacts, duration, and failure—not secrets or full sensitive document contents.

## Maintenance process

This is a curated adoption list, not an assertion that every GitHub repository is safe. Before enabling an entry, pin a release/version, verify its license and transitive/model terms, scan dependencies, test inside a low-privilege account or VM, and review upstream release/security activity. Re-check the catalog on a regular release cadence.