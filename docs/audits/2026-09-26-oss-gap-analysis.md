# Open-source gap analysis — 2026-09-26

Method: each *measured* open problem in `docs/GEMINI_RESEARCH_BRIEF.md` §2 was turned into a targeted
repository query (not a capability query), run through an authenticated `gh search repos` on this machine.
Every candidate below records stars / last push / licence as observed **2026-09-26** — those numbers age,
re-check before acting. Unauthenticated `api.github.com` search was rate-limited after five queries, which
is why `gh` was used; noting it so the method is reproducible.

Scope: solutions only for gaps we have evidence for. No proposal from the Gemini document is re-litigated
here except where a gap overlaps it.

## G1 — Memory content quality (`eve_core`: 8 registered / 37 reference / 21 forbidden / 9 unregistered of 75)

Our defect is three separate things, and they need three different instruments:
(a) a **scoring bug** in `scripts/optimize_eve_memory.py` (`nlm*` +55, no duplicate guard) — that is our
code, no OSS applies; (b) **exact duplicates** (`_1.md`, `X.md.md` twins); (c) **near-duplicates and
harvest residue** across a 14,652-file vault.

| Candidate | Evidence | Fit |
|---|---|---|
| `qarmin/czkawka` | 33,742★, pushed 2026-09-16, licence NOASSERTION (re-check — repo is dual-licence) | **Strongest for (b) and vault hygiene**: cross-platform duplicate finder with CLI, handles images/audio too. No ports, no network, CLI-only → wraps as a script, not a brick |
| `sahib/rmlint` | 2,430★, pushed 2026-09-19, GPL-3.0 | Fast, scriptable duplicate *removal* with a review step. Note GPL-3.0 — fine as a locally-run tool, a licence consideration if ever bundled |
| `jbruchon/jdupes` | canonical source is **Codeberg** (GitHub `h2oai/jdupes` fork: 66★, MIT, pushed 2026-07-28) | Minimal, fast exact-dup CLI. Ceiling is low-tech, which is a virtue here |
| `ChenghaoMou/text-dedup` | 762★, pushed 2026-03-09, Apache-2.0 | **For (c):** MinHash/LSH near-duplicate detection on text. This is the instrument we lack — our duplicates were found by *filename pattern*, not by content similarity |
| `huggingface/datatrove` | 3,357★, pushed 2026-09-24, Apache-2.0 | Corpus-scale filter/dedupe pipelines. Idea source for a curation pipeline; likely heavier than our 14.6k files justify |
| `google-research/deduplicate-text-datasets` | 1,270★, last pushed **2024-07-30**, Apache-2.0 | Exact-substring dedup via suffix arrays. Stale; skip |

**Verdict:** adopt `czkawka` (or `jdupes`/`rmlint`) as a **script-level** vault-duplicate instrument, and
`text-dedup` if near-duplicate measurement is wanted. The *scoring* defect still has to be fixed in our own
file — no OSS solution exists for a wrong local heuristic.

## G2 — Batch transcription of the ~900 MB audio bank (~88 files)

Realtime already works (Speaches on :8000, faster-whisper based). The gap is file-level batch.

| Candidate | Evidence | Fit |
|---|---|---|
| `SYSTRAN/faster-whisper` | 25,587★, pushed 2025-11-19, MIT | This is what Speaches already wraps — adding it direct is a **second ASR stack**; reject |
| `m-bain/whisperX` | 24,253★, pushed 2026-08-30, BSD-2 | **Only if diarization/word timestamps are wanted** (speaker-labelled captures). Adds a Python/torch stack → VRAM `extract` tenant. Justify with a measurement first |
| `Purfview/whisper-standalone-win` | 3,194★, pushed 2025-11-07, no licence declared | Zero-Python Windows executables. Useful as a **fallback when Speaches is down**, nothing more |
| `Zackriya-Solutions/meetily` | 31,125★, pushed 2026-09-15, MIT | Live meeting assistant app — a product, not a component; reject |

**Verdict:** write the batch script against the **Speaches endpoint we already run** (our §2.2). Reach for
whisperX only if a real transcript needs speaker separation.

## G3 — Container mount path containment (CWE-22)

| Candidate | Evidence | Fit |
|---|---|---|
| Python stdlib | `pathlib.Path.resolve().is_relative_to(root)` (3.9+) | **Sufficient.** Three lines; no dependency. This is the whole guard |

**Verdict:** no OSS needed. Note the search itself is still open — no `Mount`/`bind`/`HostConfig` surface was
found in `agent/tools/*.ts`, so we may have nothing to guard; verify wider before writing code.


## G4 — Structural code navigation (the only genuine capability gap)

Our reach is text-level (`read_active_tool` + `LEGO_INDEX.md`). The precondition recorded earlier still
stands: harvested codebases are **flattened**, and an AST needs real source trees.

| Candidate | Evidence | Fit |
|---|---|---|
| `ast-grep/ast-grep` | **16,052★, pushed 2026-09-25, MIT** — Rust CLI, structural search/lint/rewrite | **Best fit found.** Single binary, no ports, no daemon, `gpu_tenant: none`, no Python/torch. Structural queries without an AST-in-the-prompt |
| `ast-grep/ast-grep-mcp` | **468★, pushed 2026-09-24, MIT** — the maintainer's own MCP server | A brick could be a **thin wrapper over an existing, maintained server** rather than a new implementation — unusual leverage, worth an explicit look |
| `DeusData/codebase-memory-mcp` | 44,979★, pushed 2026-09-26, MIT — "code intelligence MCP server … persistent knowledge graph" | **Tempting, and a trap:** it wants to be a memory layer. Our rule is one store. Read the indexing approach as an idea; do not adopt the store |
| `Aider-AI/aider` | 49,203★, pushed 2026-05-22, Apache-2.0 | Its RepoMap (tree-sitter + graph ranking) is the best *idea* for ranking what to show a model — idea source, not a component |
| `yamadashy/repomix` 28,500★ MIT · `coderamp-labs/gitingest` 15,643★ MIT · `mufeedvh/code2prompt` 7,698★ MIT (all pushed 2026-09-25/26) | | These **flatten** — the direction Tool Forge already goes. Relevant only for re-harvesting real trees from the originating repos |

**Verdict:** the honest blocker is data, not tooling. De-flattening (or re-cloning from the URLs recorded in
`LEGO_INDEX.md`) has to come first; then `ast-grep` is a small, contract-shaped brick. **Precondition test:**
does `03_Active_Tools` contain any parseable tree today? If not, stop at the question.

## G5 / G6 / G7 — no OSS applies

- **G5 legacy 2.6 GB store on `V:\Cognee`** — a keep-or-reclaim decision, not a software gap.
- **G6 version debt** — the solutions are the upstream projects we already track (`topoteretes/cognee`,
  PocketBase 0.40.4). Runbook exists.
- **G7 lingering MCP child processes** — a ~15-line `psutil` (or `Get-Process`) assertion. No project to adopt.

## Adjacent find worth recording (not in our gap list)

`microsoft/markitdown` — **187,150★, pushed 2026-09-21, MIT** — converts files/Office docs to Markdown. We
convert with docling; markitdown covers `.docx`/`.xlsx`/`.pptx`/`.msg` more cheaply. Not a measured gap, so
it is **not** a recommendation: it becomes one the moment a real ingest fails on a format docling mishandles.

## Cross-cutting pattern: the "second store" trap

Three of the highest-starred candidates (`codebase-memory-mcp`, `getzep/graphiti` 31,178★ Apache-2.0,
`mem0ai/mem0` 66,025★ Apache-2.0) are memory layers. Under our §2/§3 rules they are all rejected as
components — a second store means two things to curate, and we have direct evidence of what under-curated
memory costs. One idea is worth stealing from that space regardless: `graphiti`'s **bi-temporal edges**
(valid-from/valid-to) address a real weakness of ours — recall cannot say *when* a fact stopped being true.
Idea-level only; recorded, not proposed.

## Ranked result

| Rank | Action | Shape | Why now |
|---|---|---|---|
| 1 | `czkawka`/`jdupes` duplicate sweep of the vault + `text-dedup` near-dup measurement | script | Evidence already exists that duplicates are inside curated memory; the vault is 14,652 files and unchecked |
| 2 | Batch transcription script against **Speaches** | script | Documented unmet need; no new stack |
| 3 | Wider verification of the container mount surface, then stdlib containment guard | check | Cheapest unresolved security question we have |
| 4 | De-flattening feasibility check for `03_Active_Tools` | measurement | Gates the only real capability gap (G4) |
| 5 | `ast-grep` brick | brick | Only after rank 4 answers yes |
| — | `whisperX`, `graphiti`, `mem0`, `codebase-memory-mcp`, `markitdown` | — | **Not now** — each is a second stack/store, or belongs to a gap we have not measured |
