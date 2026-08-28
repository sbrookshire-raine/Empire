# Eve Workbench Design

## Goal

Make Eve experimentation browser-first. A local user can drag files into memory,
watch ingestion progress, chat with Eve, approve tool actions, and use PocketBase
through Eve without opening a terminal.

## Scope

The first release adds a dedicated `frontend/eve.html` page served at
`http://127.0.0.1:8080/eve.html`.

It supports:

- Drag-and-drop and file-picker upload for `.md`, `.txt`, and `.pdf`.
- Local PDF-to-Markdown conversion before ingestion.
- Incremental ingestion into a user-selected dataset, default `eve_memory`.
- Durable Eve chat sessions with streaming responses and follow-up turns.
- Generic tool activity cards and human-input approval buttons.
- Recent file/job status stored in PocketBase.
- Service health and a single start/repair action.

It does not resume Wikipedia ingestion, expose services beyond localhost, replace
PocketBase, or introduce a JavaScript build system.

## Architecture

Keep the existing zero-build stack:

- `frontend/eve.html`: Alpine.js browser application and Pico CSS presentation.
- `frontend/serve.py`: same-origin HTTP boundary on `127.0.0.1:8080`.
- `frontend/memory_api.py`: upload validation, safe file persistence, conversion,
  ingestion job lifecycle, and memory status.
- `frontend/eve_proxy.py`: Eve request forwarding and NDJSON stream proxying.
- `pipeline/ingest_files.py`: incremental ingestion of explicit files into an
  explicit dataset.
- Eve on `127.0.0.1:2000`: conversations, PocketBase tools, Cognee tools, and
  future tool integrations.
- PocketBase on `127.0.0.1:8090`: task records and ingestion job/source metadata.
- Cognee Postgres on `127.0.0.1:5432`: graph/vector memory.

The browser never calls Eve, PocketBase administration, or Cognee directly for
Workbench operations. The Python frontend proxies those local services, avoiding
CORS and centralizing validation.

## User Experience

### Page shell

The shared EMPIRE navigation gains an **Eve** item. All primary interaction stays
inside this single page and browser window. Uploading a file must never send the
user to Primitives, PocketBase, a terminal, or another tab.

The page has:

1. A compact health strip for Eve, memory, PocketBase, and Ollama.
2. A clearly labeled **Add files to Eve's memory** area with a large drop zone,
   **Choose files** button, selected-file list, and one primary **Add to memory**
   button.
3. A clearly labeled **Chat with Eve** area with familiar message bubbles,
   persistent conversation history, a large composer, Send, Stop, and New Chat.

Desktop uses a two-column layout with memory on the left and chat on the right.
Mobile stacks memory above chat.

The default view hides datasets, ingest modes, models, graph terminology, and
other implementation details. An **Advanced options** disclosure contains the
dataset and full-graph controls for users who intentionally want them.

### Clarity requirements

- There is exactly one primary upload action: **Add to memory**.
- There is exactly one primary chat action: **Send**.
- File selection immediately displays filenames and sizes.
- Upload response is plain language and visible beside the file:
  **Uploading**, **Reading PDF**, **Learning**, **Ready**, or **Failed**.
- Successful completion says **“Eve can now use this file in chat.”**
- Failed completion states the cause and provides a visible **Try again** button.
- A successful upload offers **Ask Eve about these files**, which inserts and
  sends a natural-language prompt in the same chat panel.
- Chat renders user and Eve messages as visually distinct dialogue bubbles.
- Streaming text appears inside Eve's current bubble; technical NDJSON events
  never appear in the conversation.
- Tool activity is collapsed to short human language such as **Searching
  memory…** or **Creating a PocketBase task…**.
- No normal workflow requires copying a path, dataset name, command, token, or
  JSON.

### Upload workflow

1. User drops one or more supported files.
2. UI immediately shows filenames, sizes, and local validation results.
3. User presses **Add to memory**.
4. Server sanitizes filenames, enforces size/type limits, and stores each file
   under `data/eve_memory/uploads/<job-id>/`.
5. Markdown/text files enter ingestion directly.
6. PDFs convert locally with the installed Docling pipeline; generated Markdown
   is saved beside the source.
7. The job ingests only the uploaded files, not the entire curated folder.
8. UI polls job status and translates internal stages into the plain-language
   statuses defined above.
9. Successful jobs can seed a chat prompt such as “Summarize the files I just
   added from dataset eve_memory.”

Defaults:

- Dataset: `eve_memory`
- Mode: remember + embed
- Full graph extraction: opt-in
- Maximum file size: 50 MiB per file
- Maximum batch: 20 files

Directive-looking files (`SYSTEM.md`, `LENS_*`) are rejected from memory fuel.

### Chat workflow

1. First message creates an Eve session through the same-origin proxy.
2. The browser reads Eve’s NDJSON stream with `fetch()` and `ReadableStream`.
3. `message.appended` updates the active assistant message incrementally.
4. `actions.requested` and `action.result` render compact activity cards.
5. `input.requested` renders choices or Approve/Deny controls.
6. `session.waiting` stores the newest continuation token.
7. Follow-up messages reuse the session and current continuation token.
8. Stop calls Eve’s cancellation endpoint.
9. New Chat clears browser session state and starts fresh.

Reasoning events are not shown. Tool arguments are summarized and secrets are
never rendered.

### PocketBase and future tools

PocketBase remains Eve’s task backend. The user can ask Eve to list, create,
update, search, or delete tasks in normal chat. Delete approval appears in the
Workbench.

The UI treats tool events generically. Adding a future Eve tool produces an
activity card without requiring a new page. Tool-specific rich controls are
added only when a real workflow requires them.

## HTTP Interfaces

### Memory

- `GET /api/memory/status`
  - Returns service readiness, recent jobs, datasets, and upload constraints.
- `POST /api/memory/upload`
  - Multipart request with `files`, `dataset`, and `full_graph`.
  - Returns `202` with a job ID and accepted file metadata.
- `GET /api/memory/jobs/<job-id>`
  - Returns current stage, file progress, result counts, timestamps, and error.
- `POST /api/memory/jobs/<job-id>/retry`
  - Retries a failed job without creating duplicate successful records.

### Eve proxy

- `GET /api/eve/info`
- `POST /api/eve/session`
- `POST /api/eve/session/<session-id>`
- `GET /api/eve/session/<session-id>/stream?startIndex=<n>`
- `POST /api/eve/session/<session-id>/cancel`

Request and response bodies preserve Eve’s contract. Stream responses preserve
NDJSON boundaries and flush each event line.

## Ingestion and Dataset Repair

The existing `primitives_test` recall failure is repaired before GUI delivery.
Dataset filtering must compare normalized Cognee document IDs/names against
dataset membership and retain stamped dataset/fuel markers. A regression test
uses the two existing primitives documents and verifies a focused query returns
at least one filtered hit.

The new incremental pipeline accepts explicit file paths and dataset names.
Dataset names are restricted to letters, numbers, `_`, and `-`, with length
1–64. It stamps each document with source filename, dataset, content hash, and
upload job ID. Re-uploading unchanged content to the same dataset is idempotent.

## Background Jobs

Uploads return before conversion/embedding completes. A bounded in-process
executor runs one ingestion job at a time because Cognee already serializes
writes and Ollama/Docling are resource-heavy.

Job state is written atomically under `%LOCALAPPDATA%\EMPIRE\memory-jobs\` and
mirrored to PocketBase `ingestion_jobs` when PocketBase is available. Local job
state remains authoritative for the UI if PocketBase is temporarily unavailable.

An interrupted `running` job is marked `failed` with an interruption message on
frontend startup. The user may retry it.

## Security and Failure Handling

- Bind to `127.0.0.1` only.
- Reject path traversal, absolute names, unsupported extensions, empty files,
  directive files, oversized files, and oversized batches.
- Never execute uploaded content.
- Escape all rendered text; no raw HTML from Eve or files.
- Use finite proxy/connect/read timeouts except for active NDJSON streaming.
- Convert backend exceptions into concise user-facing errors plus local logs.
- Keep original uploads local; no cloud APIs are introduced.
- If a dependency is down, show exactly which service and expose Start/Repair.

## Testing

### Unit

- Upload filename, extension, size, batch, directive, and dataset validation.
- Job state transitions and interrupted-job recovery.
- Incremental document stamping and content-hash idempotency.
- Dataset-filter matching for dictionary and string hits.
- Eve NDJSON line forwarding and event projection.

### Integration

- Upload `.txt` and `.md`, wait for ready, and recall unique fixture text.
- Convert and ingest a small PDF fixture.
- Create an Eve session, consume streamed text, send a continuation, and cancel.
- Ask Eve to list and create a PocketBase task.
- Stop one dependency and verify the health strip/error response identifies it.

### Browser

- Drag/drop and file-picker flows.
- Responsive two-column/stacked layout.
- Streaming assistant message.
- Tool activity and approval controls.
- Retry failed ingestion and start a new chat.

## Operational Flow

Cold start remains:

```powershell
cd C:\EMPIRE
.\scripts\start-stack.ps1
```

Normal use is entirely through:

`http://127.0.0.1:8080/eve.html`

## Acceptance Criteria

The feature is accepted only when a user can complete this uninterrupted flow in
one browser window:

1. Open Eve.
2. Click **Choose files** and select a text or PDF file.
3. See the selected filename.
4. Click **Add to memory**.
5. See progress and the final response **“Eve can now use this file in chat.”**
6. Click **Ask Eve about these files**.
7. See the question and Eve's streaming answer as clear dialogue bubbles.
8. Send a follow-up question in the same conversation.
9. Ask Eve to create or list a PocketBase task and see a plain-language tool
   activity response.

No step opens a terminal, another page, another browser tab, PocketBase admin,
or raw API output.

