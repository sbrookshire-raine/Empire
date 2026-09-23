# EMPIRE Progress Report — Eve Tool-Loop & Context Fix

**Branch:** `cursor/eve-context-and-routing-fix`
**Date:** 2026-09-23
**Predecessor:** `cursor/empire-full-checkpoint` (7fe21ac)

---

## 1. Executive summary

Three separate, compounding defects were found and fixed in Eve's (the local agent's)
conversation loop. The headline finding is a **single root cause that had been masking
itself as several different bugs**:

> Ollama's **OpenAI-compatible** endpoint (`/v1/chat/completions`) **silently ignores
> `options.num_ctx`**. Because Eve connects through that endpoint, the chat model was
> loading at its **default 4096-token context** instead of 8192. Eve's assembled prompt is
> ~9,000 tokens, so **Ollama truncated it**, and the model never saw the full system
> prompt or the user's question. It then emitted an empty response, which the framework
> reported as `empty model response; reissuing the model call once`, and Eve answered with
> a hallucinated refusal ("I don't have direct access to local tools").

After the fix, **all three diagnostic tests pass**, including real tool calls.

| Diagnostic test | Before | After |
|---|---|---|
| 1. Catalog Discovery | ❌ "no specific question was provided" | ✅ `search_catalog({"query":"minimax","limit":1})` → `local/scenario-regret` |
| 2. Wikipedia RAG & Lock | ✅ (already worked) | ✅ Jevons paradox lead + evidence cited |
| 3. Local Evidence & Artifact | ❌ "I don't have direct access to local tools" | ✅ `check_workbench_health({})` → 291.94 GB free, 118 Active Tools |

---

## 2. Root cause detail (the important one)

### Symptom

`POST /api/eve/session` returned HTTP 202 and streamed normally, but the model called no
tools. The agent log showed:

```
[eve:harness.tool-loop] empty model response; reissuing the model call once
```

### Investigation path

Raw request/response logging was added to the AI SDK `fetch` wrapper in `agent/agent.ts`
(written to `tmp/eve-ollama-debug.log`, later removed). Findings:

1. **Tool visibility was never the problem.** The exact `tools` array sent to Ollama
   (32 tools, ~19 KB of JSON) contained both `search_catalog` and
   `check_workbench_health`, with `tool_choice: "auto"`.
2. **Not model-specific.** A/B against `llama3.1:latest` (via the designed
   `ollama-fast-ab.json` switch) also produced **no** native `tool_calls` — it emitted
   tool invocations as Markdown prose instead. Both models *are* tool-capable per
   `/api/tags`.
3. **Not the schema.** In isolation, `qwen2.5:14b-instruct` on the native `/api/chat`
   endpoint with the same 32 tools emitted **correct** `tool_calls`.
4. **`tool_choice` exonerated.** `auto` / `none` / `required` / explicit object all
   returned tool calls in isolation.

### The decisive measurement

Replaying Eve's **exact** request body against Ollama returned:

```
prompt_tokens : 2050
completion    : 20
finish_reason : "stop"
content       : (empty)
tool_calls    : (absent)
```

A 21,863-character body (system 19,089 + user 2,774 + tool schemas) **cannot** be 2,050
tokens. Proof of the mechanism:

```
~50k-char prompt -> OpenAI endpoint + options.num_ctx=8192
      prompt_tokens = 2050      /api/ps context_length = 4096   <-- IGNORED
~50k-char prompt -> native endpoint + options.num_ctx=8192
      /api/ps context_length = 8192                             <-- HONORED
```

`injectOllamaChatOptions()` in `agent/lib/ollama-config.ts` places `num_ctx` inside
`options`. The **native** endpoint honors it; the **OpenAI-compat** endpoint drops it.

### The fix

`scripts/ensure-ollama-parallel.ps1` now takes `-ContextLength` (default `8192`) and
starts the server with `OLLAMA_CONTEXT_LENGTH=8192` — a **server-wide default**, the same
mechanism already used for `OLLAMA_NUM_PARALLEL`. This makes the OpenAI-compat endpoint
load models at 8192 regardless of the ignored per-request option.

Verified: `/api/ps` reports `context_length` **4096 → 8192**.

> **VRAM note:** 16 GB is the hard ceiling on this machine. `SHARED_NUM_CTX` stays at 8192;
> no change to 32k was made or is recommended.

---

## 3. Other defects fixed in this branch

| # | Area | Defect | Fix |
|---|------|--------|-----|
| 1 | `frontend/serve.py` | `_resource_guard_context()` referenced an **undefined** `RESOURCE_BLOCK_RE` → `NameError` escaped the request handler before any response was written → clients saw `Remote end closed connection without response`. Session creation was fatally broken. | Defined the regex (requires both a coercive verb *and* a heavy-resource noun, order-independent) **and** wrapped the context builders in `try/except` so a builder failure can never abort session creation. |
| 2 | `frontend/serve.py` | `[AUTHORITATIVE LOCAL CATALOG CONTEXT]` was prepended *above* the ~1.3 KB companion preamble, far from the ask, so the model ignored it and called `wiki_scout_search` instead. | New `_attach_server_context()` inserts context immediately before `\n\nUser message:\n` (mirroring `workbench_ui_api` / `memory_api`). Added `_catalog_directive()`, which **explicitly forbids** wiki tools for catalog-only asks and softens automatically when a prompt legitimately targets both. |
| 3 | `frontend/wiki_drift_api.py` | `WIKI_LOOKUP_RE` contained a **bare** `tell me` alternative, so local tool prompts ("…then tell me how much free disk space is available") were misclassified as Wikipedia lookups. | Narrowed to `tell me about`, requiring an encyclopedia object. Verified `tell me about black holes` still matches; the local-tool prompt no longer does. |
| 4 | `agents/…/agent/instructions.ts` | The routing prompt was resolved as `join(agentDir, "empire-routing.md")`, where `agentDir` is the **bundle** directory. In production that file is absent, so `readFileSync` threw and was silently swallowed → **17,344 chars of routing table were dropped from the production system prompt.** | Added `ROUTING_CANDIDATES` with a fallback to the source tree, plus a `console.warn` so this can never fail silently again. |
| 5 | `frontend/eve_toolbelt.py` | `int(version or 0)` on `defaults_version` would raise `ValueError` on a legacy/string value (e.g. `"1.0"`), which — before fix #1 — would have crashed session creation. | Added `_version_number()` safe-cast helper (bool/int/float/numeric-string → int; junk → 0). |
| 6 | Runtime config | A prior diagnostic run silently stripped `voice_presence` (push-to-talk) from the operator toolbelt by posting `active_tools` verbatim. | Restored via the canonical writer; removed `active_tools` from `scripts/diagnostic.py` so it no longer mutates operator config. |
| 7 | Test | `test_explicit_catalog_intent_injects_results` asserted an undocumented string (`SYSTEM NOTE: Catalog search returned`) that the implementation never emitted. | Aligned to the documented `[AUTHORITATIVE LOCAL CATALOG CONTEXT]` marker. |

---

## 4. Progressive disclosure (context budget work)

The 8,192-token window is a hard constraint. Reducing the fixed prompt cost was necessary
to leave room for the conversation.

### Tools now gated per session (`defineDynamic`, resolved at `turn.started`)

Eve had **86** statically-registered tools; every schema was advertised to the model on
every call. Tools are now registered only when their Toolbelt limb is active.

| Category | Tools gated |
|---|---|
| `container_scout` | `container_scout_search`, `_detail`, `_docker_status` |
| `github_scout` | `github_scout_search`, `_readme` |
| `web_scout` / `web_research` | `web_scout`, `research_orchestrate` |
| `wiki_local` | `promote_wiki_cache` |
| evidence | `workspace_search`, `query_data`, `read_document` |
| artifact | `create_spreadsheet`, `author_code`, `python_verify` |
| `switchboard` | `switchboard_status`, `_ensure`, `_release`, `_tenant` |
| **`system_ops`** *(new)* | `get_model_suite`, `list_models`, `ollama_health`, `architect_now_update` |
| **`file_ops`** *(new)* | `workbench_list_dir`, `workbench_read_file`, `docling_convert`, `draft_work_order`, `propose_remember`, `list_staging`, `confirm_remember`, `drop_staging` |

**30 tools converted** (18 + 12). Two new Toolbelt categories (`system_ops`, `file_ops`)
were added to **both** `frontend/eve_toolbelt.py` and
`agents/…/agent/lib/toolbelt.ts`, both defaulting **OFF**.

### Instructions trimmed

| Item | Before | After |
|---|---|---|
| `eve_instructions.md` | 3,602 chars | ~1,700 chars |
| `empire-routing.md` | 17,345 chars | 10,441 chars |
| System prompt (measured, real Qwen tokenizer) | 5,144 tok | **2,919 tok** |
| System + 20 advertised schemas | ~11,900 tok | **4,940 tok** |
| Headroom of 8,192 | ~1,400 | **3,252** |

The 8,830-char routing table moved to an on-demand skill
`agents/empire-task-agent/agent/skills/empire-routing-detail.md` (no content lost); a
compact index plus a **"Missing tool path"** section (call `request_capability` /
`admit_for_goal`, then use the tool next turn) stays in the prompt.

> **Note:** These reductions alone did **not** fix the failures — the context was still
> being truncated at the Ollama layer. They remain valuable (real headroom), but the
> context-length fix was the actual cure. Recording this so the two are not conflated.

---

## 5. Operational fixes

- **Stale workflow queue purged.** Eve's local durable world
  (`agents/empire-task-agent/.eve/.workflow-data/runs`) held runs stuck in `running` with
  no `completedAt`, causing `[world-local] Re-enqueued N active run(s) on startup` plus a
  flood of `TypeError: fetch failed` retries. Marked stale runs terminal
  (`status: failed`, `errorCode: PURGED_STALE`, `completedAt` set). Backups under `tmp/`.
- **Rebuild lock pitfall documented.** `npm run build` fails with `EPERM` while Eve is
  running, because the builder renames `.output`. Stop the process on :2000 first.
- **`.gitignore` hardened** for runtime artifacts (see §6).

---

## 6. Repository hygiene changes in this branch

Added to `.gitignore` (these were previously untracked noise or risked being committed):

- `/tmp/` — debug logs + edit backups (~6.9 MB, 834 files)
- `/eve-audit/` — runtime chat transcript (privacy-sensitive)
- `*.db-shm`, `*.db-wal` — SQLite live sidecars
- `data/eval/*_stdout.txt`, `data/eval/*_stderr.txt` — runtime capture logs
- `frontend/verify-stack.json` — regenerated integration report

---

## 7. Verification status

| Gate | Result |
|---|---|
| Full unit suite | **391 tests, fail=0, err=0** |
| `scripts/diagnostic.py` (3 tests) | **3/3 pass** with real tool calls |
| Ollama context | `/api/ps` → `context_length: 8192` ✅ |
| Toolbelt integrity | `["voice_presence", "wiki_local"]` (push-to-talk intact) ✅ |

---

## 8. Open items / what to investigate next

### 8.1 Startup sweep for stale runs — **NOT IMPLEMENTED** (interrupted)

A `scripts/cleanup-stale-runs.ps1` was requested to sweep
`.eve/.workflow-data/runs` at startup and mark `status: "running"` runs as failed, hooked
into `scripts/start-stack.ps1` before the Eve launch. **This was not completed** — the
working session was interrupted mid-task and the file does not exist.

The queue was purged manually (three times) during debugging, but **it re-accumulates**
(~27–30 runs per diagnostic cycle) because the harness leaves sessions non-terminal. Until
the sweep exists, expect the `Re-enqueued N active run(s)` message to return.

### 8.2 `injectOllamaChatOptions` is now redundant

It still writes `options.num_ctx`, which the OpenAI-compat endpoint ignores. The real fix
is the server-level `OLLAMA_CONTEXT_LENGTH`. Options: (a) leave as harmless
belt-and-braces, (b) remove it to avoid implying it works, or (c) route Eve through the
native endpoint so per-request `num_ctx` is honored.

### 8.3 Deep / Librarian modes unverified

`SHARED_NUM_CTX = 8192` applies to all three chat modes. Verify that **Deep**
(`logicbeat/qwen3.8-27B_GSQ_RCO`, ~12 GB) actually loads at 8192 under the new server
default, and confirm VRAM headroom on 16 GB. These modes were not exercised in this work.

### 8.4 Queue retention policy

`.eve/.workflow-data` held **800** run files (433 completed, 3 failed, 304 purged) plus
12k event files and 51k stream files. There is no retention/pruning policy — these grow
without bound. Worth defining a retention window.

### 8.5 Tracked runtime state files

`backend/pocketbase/pb_public/dashboard/status.json` and `frontend/verify-stack.json` are
tracked but regenerated at runtime, producing diff noise on every run. Consider untracking
them (they are already listed in `.gitignore`; `git rm --cached` is still needed).

### 8.6 Stray scratch files in `tests/`

`tests/routing.ps` and `tests/routing,ps` (note the comma — likely a bad redirect) are
ad-hoc probe scripts, not part of the test suite. Neither is collected by
`unittest discover`. Candidate for deletion or relocation.

### 8.7 Wiki Local (Weaviate) is not running by default

`weaviate:8091` is opt-in (`start-weaviate.ps1`, `-Weaviate` flag). Wiki tooling is gated
behind `wiki_local`, and the diagnostic's Wikipedia test passes via server-injected
evidence rather than a tool call. Confirm intended behavior for the operational phase.

### 8.8 Model tool-choice reliability

With correct context, `qwen2.5:14b-instruct` now selects the right tool on the diagnostic
prompts. However, it occasionally chose a plausible-but-wrong tool in earlier runs
(e.g. `resource_pulse` alongside `check_workbench_health`). Worth a broader routing
regression battery now that the blocking defect is gone.

---

## 9. Changed files (this branch)

**Backend / frontend**
`frontend/serve.py`, `frontend/wiki_drift_api.py`, `frontend/eve_toolbelt.py`,
`pipeline/discovery_catalog.py`

**Eve agent**
`agents/empire-task-agent/agent/instructions.ts`,
`agents/empire-task-agent/agent/empire-routing.md`,
`agents/empire-task-agent/agent/lib/toolbelt.ts`,
`agents/empire-task-agent/agent/skills/empire-routing-detail.md` *(new)*,
30 × `agents/empire-task-agent/agent/tools/*.ts`

**Scripts / config / docs**
`scripts/ensure-ollama-parallel.ps1`, `scripts/diagnostic.py` *(new)*,
`eve_instructions.md`, `.gitignore`

**Tests**
`tests/frontend/test_catalog_pre_router.py`, `tests/frontend/test_eve_toolbelt.py`,
`tests/frontend/test_wiki_drift_api.py`, `tests/pipeline/test_discovery_catalog.py`
