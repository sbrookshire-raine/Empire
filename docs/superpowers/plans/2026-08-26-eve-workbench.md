# Eve Workbench Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a single local browser window where the user uploads files into Cognee memory, receives clear progress/results, and holds a streaming conversation with Eve that can use PocketBase and future tools.

**Architecture:** Extend the existing zero-build Python/Alpine frontend on port 8080. The Python server owns upload validation, bounded background jobs, and a same-origin proxy to Eve’s NDJSON API; a focused incremental pipeline ingests only explicit files into Cognee. The browser renders plain-language upload states, dialogue bubbles, tool activity, and approvals without exposing transport details.

**Tech Stack:** Python 3.11 standard library HTTP server, Cognee 1.4, local Docling, PocketBase REST, Eve 0.25 NDJSON API, Alpine.js, Pico CSS, vanilla JavaScript.

## Global Constraints

- Bind all HTTP services to `127.0.0.1`; no cloud APIs.
- Keep PocketBase as Eve’s task backend and optional ingestion-job mirror.
- Keep the frontend zero-build; do not add React, npm, or a bundler.
- Normal use stays in `http://127.0.0.1:8080/eve.html`.
- Support `.md`, `.txt`, and `.pdf`, maximum 50 MiB each and 20 files per batch.
- Default dataset is `eve_memory`; full graph extraction is opt-in.
- Never ingest `SYSTEM.md`, `LENS_*`, or a `directives` path.
- Never render Eve reasoning events or raw unescaped HTML.
- Place imports at module top level.

---

## File Structure

- `pipeline/ingest_files.py` — validate datasets, normalize explicit documents, hash/idempotency metadata, convert PDFs, and ingest one upload batch.
- `frontend/memory_api.py` — safe upload persistence, job store, executor, status projection, and PocketBase job mirroring.
- `frontend/eve_proxy.py` — typed local Eve HTTP forwarding and NDJSON response streaming helpers.
- `frontend/serve.py` — route multipart memory requests and same-origin Eve requests.
- `frontend/eve.html` — semantic single-page Workbench shell.
- `frontend/eve-workbench.js` — upload queue, job polling, chat session state, NDJSON parser, event projection, and user actions.
- `frontend/eve-workbench.css` — responsive two-column layout and clear state styling.
- `frontend/empire-nav.js` — add the Eve navigation item.
- `agents/empire-task-agent/agent/instructions.md` — prefer `eve_memory` for Workbench uploads while retaining explicit dataset requests.
- `tests/pipeline/test_ingest_files.py` — ingestion validation/idempotency tests.
- `tests/pipeline/test_cognee_dataset_filter.py` — regression tests for filtered recall.
- `tests/frontend/test_memory_api.py` — upload/job state tests.
- `tests/frontend/test_eve_proxy.py` — HTTP forwarding and NDJSON tests.
- `tests/frontend/test_eve_workbench_static.py` — acceptance-copy and safe-rendering checks.
- `scripts/verify-eve-workbench.py` — live end-to-end verifier.

---

### Task 1: Repair filtered Cognee recall and moved-root residue

**Files:**
- Modify: `pipeline/cognee_client.py:696-802`
- Modify: `pipeline/cognee_worker.py`
- Create: `tests/pipeline/test_cognee_dataset_filter.py`
- Modify: `docs/WIKI_INGEST_OVERNIGHT.md`
- Modify: `docs/WEAVIATE_HEIST.md`
- Modify: `docs/reference/MCP_WIRING_DEFERRED.md`

**Interfaces:**
- Consumes: Cognee CHUNKS hits and `_dataset_document_keys(dataset)`.
- Produces: `_filter_hits_for_dataset(...) -> list` with normalized UUID/name matching and deterministic marker fallback.

- [ ] **Step 1: Write failing filter tests**

```python
import unittest

from pipeline.cognee_client import _filter_hits_for_dataset


class DatasetFilterTests(unittest.TestCase):
    def test_keeps_hit_whose_document_id_is_dataset_member(self) -> None:
        hit = {"document_id": "ABC", "document_name": "text_x", "text": "body"}
        self.assertEqual(
            _filter_hits_for_dataset([hit], "eve_memory", allowed_ids={"abc"}),
            [hit],
        )

    def test_keeps_nested_payload_and_stamped_dataset_marker(self) -> None:
        hit = {"payload": {"text": "dataset: eve_memory\nunique fact"}}
        self.assertEqual(_filter_hits_for_dataset([hit], "eve_memory"), [hit])

    def test_keeps_curated_fuel_marker(self) -> None:
        hit = {"text": "fuel: curated_primitives\nFriction & Flow"}
        self.assertEqual(_filter_hits_for_dataset([hit], "primitives_test"), [hit])


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run the focused test and confirm RED**

Run:

```powershell
.\venv\Scripts\python.exe -m unittest tests.pipeline.test_cognee_dataset_filter -v
```

Expected: UUID case normalization and nested payload tests fail.

- [ ] **Step 3: Normalize hit fields in the filter**

Implement helpers in `pipeline/cognee_client.py`:

```python
def _normalized_key(value: object) -> str:
    return str(value or "").strip().lower()


def _hit_fields(hit: object) -> tuple[str, str, str]:
    if not isinstance(hit, dict):
        return str(hit), "", ""
    payload = hit.get("payload")
    nested = payload if isinstance(payload, dict) else {}
    text = hit.get("text") or nested.get("text") or ""
    document_name = hit.get("document_name") or nested.get("document_name") or ""
    document_id = hit.get("document_id") or nested.get("document_id") or ""
    return str(text), _normalized_key(document_name), _normalized_key(document_id)
```

Normalize `allowed_names` and `allowed_ids` once before iterating, then compare
the normalized values returned by `_hit_fields`.

- [ ] **Step 4: Close Cognee resources in the worker**

Wrap worker dispatch in `try/finally` and invoke the installed Cognee shutdown
hook when present:

```python
try:
    return await dispatch(args)
finally:
    close = getattr(cognee, "close", None)
    if callable(close):
        result = close()
        if inspect.isawaitable(result):
            await result
```

If Cognee exposes no close hook, close the configured HTTP client from the
adapter that created it. The worker must exit without `Unclosed client session`.

- [ ] **Step 5: Run tests and a live recall**

```powershell
.\venv\Scripts\python.exe -m unittest tests.pipeline.test_cognee_dataset_filter -v
$env:PYTHONPATH="C:\EMPIRE"
.\venv\Scripts\python.exe -m pipeline.cognee_worker recall --query "Friction and Flow" --dataset primitives_test
```

Expected: tests pass; live results contain at least one existing curated hit;
stderr contains no unclosed-client warning.

- [ ] **Step 6: Replace remaining operational OneDrive examples**

Replace active command examples under the three listed docs with `C:\EMPIRE`.
Do not alter historical prose that is explicitly describing the migration.

---

### Task 2: Add explicit-file incremental ingestion

**Files:**
- Create: `pipeline/ingest_files.py`
- Create: `tests/pipeline/test_ingest_files.py`

**Interfaces:**
- Produces:
  - `validate_dataset(name: str) -> str`
  - `validate_memory_file(path: Path) -> Path`
  - `prepare_document(path: Path, dataset: str, job_id: str) -> PreparedDocument`
  - `ingest_files(paths: list[Path], dataset: str, job_id: str, full_graph: bool) -> dict`

- [ ] **Step 1: Write failing validation and stamping tests**

```python
import tempfile
import unittest
from pathlib import Path

from pipeline.ingest_files import prepare_document, validate_dataset, validate_memory_file


class IngestFilesTests(unittest.TestCase):
    def test_dataset_accepts_safe_name(self) -> None:
        self.assertEqual(validate_dataset("eve_memory-2"), "eve_memory-2")

    def test_dataset_rejects_path_characters(self) -> None:
        with self.assertRaises(ValueError):
            validate_dataset("../memory")

    def test_directive_filename_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "SYSTEM.md"
            path.write_text("do this", encoding="utf-8")
            with self.assertRaises(ValueError):
                validate_memory_file(path)

    def test_prepared_text_has_traceable_header_and_hash(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "notes.txt"
            path.write_text("unique fact", encoding="utf-8")
            doc = prepare_document(path, "eve_memory", "job-1")
            self.assertIn("dataset: eve_memory", doc.content)
            self.assertIn("upload_job_id: job-1", doc.content)
            self.assertIn("content_hash:", doc.content)
```

- [ ] **Step 2: Verify RED**

```powershell
.\venv\Scripts\python.exe -m unittest tests.pipeline.test_ingest_files -v
```

Expected: import fails because `pipeline.ingest_files` does not exist.

- [ ] **Step 3: Implement validation and prepared document type**

```python
from dataclasses import dataclass

DATASET_RE = re.compile(r"^[A-Za-z0-9_-]{1,64}$")
ALLOWED_SUFFIXES = {".md", ".txt", ".pdf"}


@dataclass(frozen=True)
class PreparedDocument:
    source_path: Path
    content: str
    content_hash: str
```

Reject unsupported extensions, empty files, directive names, and any path with
a `directives` component. Stamp source filename, dataset, job ID, and SHA-256.

- [ ] **Step 4: Implement local PDF conversion**

Expose:

```python
def convert_pdf(source: Path, output_dir: Path) -> Path:
    ...
```

Call the installed local Docling conversion API in-process. Write UTF-8 Markdown
to `output_dir / f"{source.stem}.md"`. Raise `MemoryConversionError` with a
plain-language message if conversion produces no text.

- [ ] **Step 5: Implement explicit batch ingestion**

```python
async def ingest_files_async(
    paths: list[Path],
    dataset: str,
    job_id: str,
    full_graph: bool = False,
) -> dict[str, object]:
    prepared = [prepare_document(path, dataset, job_id) for path in paths]
    await remember_many([item.content for item in prepared], dataset=dataset, mode="fast")
    await embed_dataset(dataset)
    if full_graph:
        await cognify_dataset(dataset)
    return {
        "dataset": dataset,
        "files": [item.source_path.name for item in prepared],
        "documents": len(prepared),
        "hashes": [item.content_hash for item in prepared],
    }
```

Add a synchronous `ingest_files(...)` wrapper using `asyncio.run`.

- [ ] **Step 6: Add idempotency**

Persist a small JSON hash index under
`%LOCALAPPDATA%\EMPIRE\memory-jobs\content-index.json`. Key it by
`dataset + ":" + content_hash`. Skip only hashes recorded after successful
embedding. Return `skipped` filenames in the result.

- [ ] **Step 7: Run unit tests**

```powershell
.\venv\Scripts\python.exe -m unittest tests.pipeline.test_ingest_files -v
```

Expected: all tests pass without contacting Ollama or Postgres.

---

### Task 3: Build safe upload and background job APIs

**Files:**
- Create: `frontend/memory_api.py`
- Create: `tests/frontend/test_memory_api.py`
- Modify: `frontend/serve.py`

**Interfaces:**
- Produces:
  - `UploadPolicy(max_file_bytes=52_428_800, max_files=20)`
  - `MemoryJobStore`
  - `MemoryJobRunner`
  - `save_uploads(parts, dataset, full_graph) -> MemoryJob`
  - HTTP `GET /api/memory/status`
  - HTTP `POST /api/memory/upload`
  - HTTP `GET /api/memory/jobs/<id>`
  - HTTP `POST /api/memory/jobs/<id>/retry`

- [ ] **Step 1: Write failing policy/job tests**

```python
import tempfile
import unittest
from pathlib import Path

from frontend.memory_api import MemoryJobStore, UploadPolicy, sanitize_filename


class MemoryApiTests(unittest.TestCase):
    def test_filename_drops_path_components(self) -> None:
        self.assertEqual(sanitize_filename(r"..\..\notes.txt"), "notes.txt")

    def test_policy_rejects_unsupported_extension(self) -> None:
        with self.assertRaises(ValueError):
            UploadPolicy().validate("payload.exe", 10)

    def test_interrupted_running_job_recovers_as_failed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            store = MemoryJobStore(Path(tmp))
            store.write({"id": "j1", "status": "learning"})
            store.recover_interrupted()
            self.assertEqual(store.read("j1")["status"], "failed")
```

- [ ] **Step 2: Verify RED**

```powershell
.\venv\Scripts\python.exe -m unittest tests.frontend.test_memory_api -v
```

Expected: import fails because `frontend.memory_api` does not exist.

- [ ] **Step 3: Implement upload policy and atomic job store**

Use `Path(name.replace("\\", "/")).name`, normalize whitespace, and retain only
safe filename characters. Write JSON to a sibling `.tmp`, flush, then
`Path.replace()` into place.

Internal statuses:

```python
JobStatus = Literal["queued", "converting", "embedding", "ready", "failed"]
```

User labels:

```python
STATUS_LABELS = {
    "queued": "Uploading",
    "converting": "Reading PDF",
    "embedding": "Learning",
    "ready": "Ready",
    "failed": "Failed",
}
```

- [ ] **Step 4: Implement bounded runner**

Create one `ThreadPoolExecutor(max_workers=1)`. Each transition updates local
JSON and best-effort mirrors the job to PocketBase `ingestion_jobs`. Exceptions
set `status="failed"` and a concise `error`.

- [ ] **Step 5: Add multipart parsing to `serve.py`**

Route multipart requests before `_read_json()`. Use `email.parser.BytesParser`
with a synthetic MIME header, enforce total request size before reading, and
pass only validated file parts to `memory_api`.

Return:

```json
{
  "ok": true,
  "job": {
    "id": "job-id",
    "status": "queued",
    "label": "Uploading",
    "files": [{"name": "notes.txt", "bytes": 123}]
  }
}
```

with HTTP 202.

- [ ] **Step 6: Add status and retry routes**

Unknown IDs return 404 JSON. Retry is allowed only for `failed`; ready jobs
return 409 to prevent duplicates.

- [ ] **Step 7: Run tests**

```powershell
.\venv\Scripts\python.exe -m unittest tests.frontend.test_memory_api -v
```

Expected: all tests pass.

---

### Task 4: Add same-origin Eve proxy and NDJSON projection

**Files:**
- Create: `frontend/eve_proxy.py`
- Create: `tests/frontend/test_eve_proxy.py`
- Modify: `frontend/serve.py`

**Interfaces:**
- Produces:
  - `eve_request(method, path, payload=None) -> EveResponse`
  - `iter_ndjson(stream) -> Iterator[dict]`
  - `project_event(event: dict) -> dict | None`
  - same-origin `/api/eve/*` routes.

- [ ] **Step 1: Write failing NDJSON tests**

```python
import io
import unittest

from frontend.eve_proxy import iter_ndjson, project_event


class EveProxyTests(unittest.TestCase):
    def test_ndjson_handles_split_reads(self) -> None:
        stream = io.BytesIO(b'{"type":"message.appended"}\n{"type":"session.waiting"}\n')
        self.assertEqual(len(list(iter_ndjson(stream))), 2)

    def test_reasoning_event_is_hidden(self) -> None:
        self.assertIsNone(project_event({"type": "reasoning.appended", "data": {}}))

    def test_message_event_keeps_plain_text(self) -> None:
        event = {"type": "message.appended", "data": {"delta": "Hello"}}
        self.assertEqual(project_event(event), event)
```

- [ ] **Step 2: Verify RED**

```powershell
.\venv\Scripts\python.exe -m unittest tests.frontend.test_eve_proxy -v
```

- [ ] **Step 3: Implement local request forwarding**

Use `http.client.HTTPConnection("127.0.0.1", 2000, timeout=15)`. Restrict paths
to `/eve/v1/info` and session routes. Forward JSON content type and status.

- [ ] **Step 4: Implement stream forwarding**

For stream routes, send:

```http
Content-Type: application/x-ndjson; charset=utf-8
Cache-Control: no-cache
X-Content-Type-Options: nosniff
```

Read and flush one newline-terminated event at a time. Pass projected events;
drop reasoning events. On upstream disconnect, emit:

```json
{"type":"proxy.error","data":{"message":"Eve disconnected. You can retry this message."}}
```

- [ ] **Step 5: Add routes**

Map `/api/eve/...` to `/eve/v1/...` for info, create, continuation, stream, and
cancel. Reject all other proxy paths.

- [ ] **Step 6: Run tests**

```powershell
.\venv\Scripts\python.exe -m unittest tests.frontend.test_eve_proxy -v
```

Expected: all tests pass.

---

### Task 5: Build the single-window Eve Workbench

**Files:**
- Create: `frontend/eve.html`
- Create: `frontend/eve-workbench.js`
- Create: `frontend/eve-workbench.css`
- Create: `tests/frontend/test_eve_workbench_static.py`
- Modify: `frontend/empire-nav.js`

**Interfaces:**
- Consumes: `/api/memory/*`, `/api/eve/*`, `/api/services/status`.
- Produces: one accessible page satisfying the spec acceptance flow.

- [ ] **Step 1: Write failing static acceptance tests**

```python
import unittest
from pathlib import Path


class EveWorkbenchStaticTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.html = Path("frontend/eve.html").read_text(encoding="utf-8")

    def test_primary_labels_are_clear(self) -> None:
        for text in (
            "Add files to Eve's memory",
            "Choose files",
            "Add to memory",
            "Chat with Eve",
            "Send",
        ):
            self.assertIn(text, self.html)

    def test_page_has_single_file_input_and_chat_form(self) -> None:
        self.assertEqual(self.html.count('type="file"'), 1)
        self.assertIn('id="chat-form"', self.html)
```

- [ ] **Step 2: Verify RED**

```powershell
.\venv\Scripts\python.exe -m unittest tests.frontend.test_eve_workbench_static -v
```

- [ ] **Step 3: Implement semantic HTML shell**

Create distinct `<section aria-labelledby>` regions for memory and chat. File
input accepts `.md,.txt,.pdf` and `multiple`. Advanced options live in
`<details>`. All status text uses `aria-live="polite"`.

- [ ] **Step 4: Implement memory client state**

Use Alpine state for selected files, drag state, active job, and recent jobs.
Build `FormData` with files, dataset, and full_graph. Poll every second while a
job is active and stop on ready/failed.

On ready render:

```text
Eve can now use this file in chat.
```

and an **Ask Eve about these files** button.

- [ ] **Step 5: Implement chat session and NDJSON reader**

Maintain:

```javascript
{
  sessionId: null,
  continuationToken: null,
  streamIndex: 0,
  messages: [],
  activities: [],
  pendingInput: null,
  sending: false
}
```

Create the first session with `{"message": text}`. Follow up with the current
continuation token. Parse `response.body.getReader()` chunks with a retained
line buffer. Update the current Eve bubble from cumulative text when available,
otherwise append the delta.

- [ ] **Step 6: Project tool and approval events**

Map known tools to human labels:

```javascript
const TOOL_LABELS = {
  cognee_recall: "Searching memory…",
  cognee_remember: "Saving memory…",
  list_tasks: "Reading PocketBase tasks…",
  search_tasks: "Searching PocketBase tasks…",
  create_task: "Creating a PocketBase task…",
  update_task: "Updating a PocketBase task…",
  delete_task: "Preparing to delete a PocketBase task…",
};
```

Unknown tools use `Using <display name>…`. Render input requests as buttons and
send selected text through the normal continuation route.

- [ ] **Step 7: Add Stop, New Chat, and safe rendering**

Stop posts to cancel. New Chat aborts the fetch reader and clears local state.
Render all text with Alpine `x-text`; never use `x-html`.

- [ ] **Step 8: Style for clarity**

Use a two-column grid with a narrower memory panel and flexible chat panel.
Dialogue uses high-contrast user/Eve bubbles, a sticky composer, visible focus
rings, and status badges with icon plus text (never color alone). Stack below
800px.

- [ ] **Step 9: Add navigation**

Add:

```javascript
{ id: "eve", label: "Eve", href: "http://127.0.0.1:8080/eve.html" }
```

immediately after Dashboard.

- [ ] **Step 10: Run static tests**

```powershell
.\venv\Scripts\python.exe -m unittest tests.frontend.test_eve_workbench_static -v
```

Expected: all tests pass.

---

### Task 6: Wire Eve defaults and end-to-end verification

**Files:**
- Modify: `agents/empire-task-agent/agent/instructions.md`
- Create: `scripts/verify-eve-workbench.py`
- Modify: `AGENTS.md`
- Modify: `docs/OPERATIONAL_HANDOFF.md`

**Interfaces:**
- Consumes: live Ollama, PocketBase, frontend, Eve, Postgres, and V:.
- Produces: one command that verifies the Workbench workflow.

- [ ] **Step 1: Update Eve memory guidance**

Add:

```markdown
- Workbench uploads default to Cognee dataset `eve_memory`. When the user asks
  about files they uploaded in the Eve Workbench, call `cognee_recall` with
  `dataset: "eve_memory"` unless they name another dataset.
```

Retain the existing `primitives_test` guidance for curated primitives.

- [ ] **Step 2: Write the verifier**

The verifier must:

1. Check `V:\Cognee`, Docker Postgres, Ollama, PocketBase, frontend, and Eve.
2. POST a unique `.txt` multipart fixture to `/api/memory/upload`.
3. Poll its job to `ready` with a bounded timeout.
4. Recall the unique marker through `pipeline.cognee_worker`.
5. Create an Eve session with “Reply with the word READY.”
6. Read NDJSON until `session.waiting`, asserting assistant text exists.
7. Send a continuation and assert another assistant response.
8. Query PocketBase tasks without mutating existing records.
9. Exit nonzero with the exact failed stage.

- [ ] **Step 3: Run all focused tests**

```powershell
.\venv\Scripts\python.exe -m unittest `
  tests.pipeline.test_cognee_dataset_filter `
  tests.pipeline.test_ingest_files `
  tests.frontend.test_memory_api `
  tests.frontend.test_eve_proxy `
  tests.frontend.test_eve_workbench_static -v
```

Expected: all tests pass.

- [ ] **Step 4: Run typecheck**

```powershell
Push-Location agents\empire-task-agent
npm run typecheck
Pop-Location
```

Expected: exit 0.

- [ ] **Step 5: Restart and run live verification**

```powershell
.\scripts\start-stack.ps1
.\venv\Scripts\python.exe .\scripts\verify-eve-workbench.py
```

Expected: every stage reports PASS and the command exits 0.

- [ ] **Step 6: Browser acceptance**

Open `http://127.0.0.1:8080/eve.html` and verify:

- choose/drop a text file;
- selected filename is visible;
- upload progresses to “Eve can now use this file in chat.”;
- Ask Eve about these files creates a user bubble and streaming Eve bubble;
- a follow-up stays in the same conversation;
- “List my tasks” shows PocketBase activity and a readable answer;
- Stop and New Chat work;
- no console errors occur.

- [ ] **Step 7: Update operator directions**

Make `AGENTS.md` and the operational handoff point normal users directly to
`/eve.html`. Keep command-line instructions under troubleshooting only.

