# Review — Gemini's "EMPIRE System Brick Additions" (4 proposed bricks)

Date: 2026-09-26 · Reviewer: Cursor (mechanic) · Status: **review only — nothing acted on.**
Source: an externally generated proposal (4 bricks + a FastMCP integration appendix), supplied by the
Architect for assessment against the running stack.

Purpose: decide, per proposal, whether it names a real gap *in this system* or duplicates something
already built, and put genuine items on the focus list with the evidence that would justify acting.
Read for content only: no proposal implemented, no dependency added, no config or registry changed.

## What the document got right about us

It read a real version of our contract: the four required components per brick (server engine, thin client
adapter, playbook documentation, integrity/error handling) and the GPU tenancy taxonomy
(`none / chat / extract / vision / ops`) both match `docs/LEGO_CONTRACT.md`. It correctly identifies our
transport (stdio, newline-delimited JSON-RPC), our framework (FastMCP), and our error contract
(`{ok: false, error}`, no stack traces into the prompt).

## What it got wrong, or is behind us

| Claim / premise | Reality in our stack |
|---|---|
| Cites `EMPIRE_LEGO_BLUEPRINT.MD` | We have `docs/LEGO_CONTRACT.md` + `docs/LEGO_PROMPT.md`. No such file — provenance is partial, so treat its contract details as inferred |
| "Zero ports" as an architectural law for MCP | True for MCP servers (all stdio). False as a system claim: Postgres 5432, PocketBase 8090, frontend 8080, Ollama 11434, Speaches 8000 are **declared services** with documented ports (AGENTS.md) |
| Proposes semantic memory as something we lack | We run Cognee + Postgres + pgvector with Ollama `nomic-embed-text` (768d, batch 512), plus `eve_core`/`eve_memory` tiering |
| Proposes container execution as something we lack | We run Eve sandbox containers already, with `scripts/prune-sandbox-containers.ps1` (578 exited containers reaped 2026-09-26) and declared `ops` tenancy |
| Proposes offline audio transcription as something we lack | We run Speaches (`ghcr.io/speaches-ai/speaches:latest-cpu`) on :8000 for push-to-talk STT/TTS — it is faster-whisper-based. A separate faster-whisper brick would be a **third** ASR path (Speaches + Superwhisper already exist) |
| Recommends `default_on: false` + explicit tenancy | Already our model: `resource_pulse` / `admit_for_goal`, playbook limbs loaded on demand |

## Per-proposal verdicts

### 1. Semantic Memory (FastEmbed + sqlite-vec) — reject the component, one idea worth measuring
We already have semantic memory, and today's work is the reason to resist this: the measured bottleneck is
memory **content**, not the retrieval engine (first Foundation measurement of `eve_core`: 8 registered /
37 reference / 21 forbidden / 9 unregistered of 75). A second vector store would mean two memory systems to
curate — sqlite-vec plus our Postgres/pgvector store.
The one idea with merit: **CPU/ONNX embeddings to free VRAM during bulk ingest.** Evidence to settle it:
we measured idle VRAM 0 and 10.5 GB loaded at 24k context on a 16 GB card, so headroom exists today.
The blocker is cost — a different embedding model is a different vector space, so all 10,383 existing
vectors would need re-embedding. Verdict: defer; revisit only if a real ingest measures contention.

### 2. Code Intelligence (tree-sitter AST) — defer, with a precondition
Structural code navigation is the only capability here we do not already have in some form (our code reach
is `read_active_tool` + `LEGO_INDEX.md`, i.e. text-level). The precondition is stack-specific and currently
fails: our harvested codebases in `03_Active_Tools` are **flattened** representations, and tree-sitter needs
real source trees — parsing a flattened dump yields no useful AST. Also worth keeping from this section: the
FastMCP hazard that a root-level `$ref` in a declared `outputSchema` violates MCP (recursive structures
trigger it). We declare no `outputSchema` today, so it does not bite — record it for whenever a brick does.
Verdict: defer until we can point at parseable source; then it is a genuine, bounded brick.


### 3. Container Operations (docker-py over named pipe) — already built; keep the security check
We execute containers; the proposal's transport detail (docker-py + `npipe://`) is an implementation
alternative to whatever we use now, not a capability gap. Its one genuinely valuable contribution is the
path-traversal warning (CWE-22) on model-supplied volume mounts. Applicability was probed: no
`Mount`/`bind`/`HostConfig`/`volume` surface appears in `agent/tools/*.ts`, so there may be nothing to fix —
but that was a narrow search and the claim deserves a wider look before we call it N/A.
The cited CVEs (CVE-2025-68143, CVE-2026-57442) are **unverified** — we accept no upstream claim without
evidence. The containment check is cheap and worth doing on its own merits.
Verdict: no new brick; add the path-containment verification to the focus list.

### 4. Audio Transcription (faster-whisper) — adopt the need, reject the component
Realtime transcription exists (Speaches). The unmet need is different and real: `config/library.json`
records ~88 audio files (~900 MB) in `02_Skills_and_Prompts` with the note *"audio is a transcription job,
not a read"* — i.e. **batch** transcription was never built. The right route is the ASR service we already
run (its OpenAI-compatible `/v1/audio/transcriptions` endpoint), not a second model stack.
Verdict: build batch transcription against Speaches; do not add faster-whisper.

## The FastMCP appendix — mostly already handled

- **stdio termination / orphans**: real concern, already addressed by construction. Our consolidated
  `agent/lib/mcp-client.ts` uses the SDK's `StdioClientTransport` and closes via `client.close()` →
  `transport.close()` with ref-counted sessions — the graceful path, not a raw signal kill. Consistent with
  this session's finding that orphaned MCP python processes had accumulated historically (16 → 2) and stayed
  fixed after consolidation.
- **`ToolError` bypassing masked errors**: no `ToolError` use found in `mcp/*.py`; our error contract is
  currently satisfied by structured returns. Possible small improvement, not a defect.
- **Error payloads failing `outputSchema` validation**: not applicable — we declare no `outputSchema`.

## The point the document never addresses

Four new bricks would each add a playbook limb and tool schemas to a prompt already ~11k tokens
(instructions + routing ≈ 5.8k, tool schemas ≈ 5.3k) inside a 24,576-token window — and this session was
spent *reducing* that footprint (MCP wrappers 1,328 → 299 lines). In EMPIRE, capability is not free at
runtime: a brick must displace something or justify its tokens. The document treats additions as strictly
positive, which is the opposite of our hand-footprint rule (`OPERATING_CONTRACT.md` §4–§5).

## Focus list (candidates — none started)

| # | Item | Why | Cost | Evidence needed |
|---|---|---|---|---|
| F1 | Batch transcription of the ~900 MB audio bank **via existing Speaches** | The one real unmet need the document surfaced; library.json already flags it | Low: one script against a running service | None — need is documented |
| F2 | Verify no model-supplied host path can reach a container mount; if any exists, enforce `resolve().is_relative_to(root)` | Closes the document's only substantial security claim | Low | Wider search of the sandbox path than `agent/tools/*.ts` |
| F3 | Standing check for lingering MCP child processes (we fixed 16 → 2; keep it fixed) | Converts a one-time cleanup into a measured invariant | Low | Add to an existing audit step |
| F4 | Tree-sitter code-intelligence brick | Only genuine capability gap found | Medium–high (server + limb + tests + tokens) | Parseable source in `03_Active_Tools` (currently flattened) |
| F5 | CPU/ONNX embedding path for bulk ingest | Would free VRAM if contention is real | **High**: invalidates 10,383 vectors → full re-embed | A measured ingest showing GPU contention (headroom exists today) |
| F6 | Note: any future `outputSchema` must avoid root-level `$ref` | Cheap insurance on a documented FastMCP/MCP incompatibility | None (documentation) | — |

**Recommendation:** F1–F3 are worth doing on their own merits and are small. F4 and F5 are deferred with
preconditions stated above — both are pivots, and neither is justified by the current measurement. Nothing
here should displace the two items already open: the memory curation rebuild (sign-off pending) and the
cognee upgrade runbook.
