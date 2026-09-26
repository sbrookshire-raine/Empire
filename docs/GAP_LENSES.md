# Two lenses for evaluating any addition to EMPIRE

Written 2026-09-26 because the previous candidate lists (Gemini's bricks, my OSS gap analysis) mixed two
categories that have **different owners, different evidence and different costs**:

- **Lens A — builder instruments.** What makes EMPIRE better *to build and maintain*: tools that find defects
  in our code, our data and our pipeline. Used by the Architect and the mechanic at build time. They cost
  nothing at runtime (no prompt tokens, no VRAM, no limbs).
- **Lens B — Eve's runtime capability.** What makes Eve a better orchestrator and user of resources —
  documents, memory, search, voice, code reach, resource admission. These *do* cost: prompt tokens, VRAM,
  one more thing to keep working. They are judged by whether her behaviour measurably improves.

The distinction matters because the costs are not comparable: a Lens A tool that trims 3,000 duplicate
vault files is free forever after, while a Lens B limb taxes every turn. A candidate must be labelled with
its lens before it can be ranked against anything.

**Selection rule for Lens A:** no instrument without a recorded instance of the defect class it detects. We
have been bitten by each class below at least once, so each one has evidence rather than a hunch.

## Lens A — builder instruments

| Candidate | Evidence (as of 2026-09-26) | Defect class it finds | Our recorded instance |
|---|---|---|---|
| `osprey-oss/deptry` | **1,484★ MIT**, pushed 2026-09-26 | unused / **missing** / transitive Python deps | **docling was installed but never declared in `requirements.txt`** — found by hand 2026-09-26; a fresh setup would have lost PDF conversion silently |
| `jendrikseipp/vulture` | **4,823★ MIT**, pushed 2026-09-25 | dead Python code | three separate "this looks dead" calls that were **wrong when measured** (a routing pair sharing 0 lines; three guide docs sharing 0–1; the "dead" file that was the recipe for a 20 GB corpus) |
| `boxed/mutmut` | **1,453★ BSD-3**, pushed 2026-09-12 | tests that pass but would not catch a defect | the gate is the arbiter (598 tests) and has never been measured for *strength*; a rotted harness sat unrun until 2026-09-24 |
| `qarmin/czkawka` · `sahib/rmlint` · `jbruchon/jdupes` (Codeberg canonical) | 33,742★ · 2,430★ GPL-3.0 · fork only on GitHub | duplicate files on disk | duplicates found **inside curated memory** by filename (`_1.md`, `X.md.md`); the 14,652-file vault has never been swept for content duplicates |
| `ChenghaoMou/text-dedup` · `huggingface/datatrove` | 762★ Apache-2.0 · 3,357★ Apache-2.0 | **near**-duplicate text | our duplicates were only ever detected by filename pattern — no content-similarity measurement exists |
| `lycheeverse/lychee` | exists (confirmed via a deprecated alternative pointing at it) but **I did not capture its own stats** — re-verify before citing | broken links / rotten references | 754 markdown docs, a DOC_MAP that claims to index them, and no link check has ever run |
| `microsoft/markitdown` · `datalab-to/marker` · `datalab-to/surya` | 187,150★ MIT · 39,988★ Apache-2.0 · 21,418★ Apache-2.0 | formats we cannot read (office, scanned PDF, tables) | ingest works on md/txt/pdf; **no measurement exists of what formats fail today** |
| our own `audit-empire` / `check-legos` / `check-foundation` / `vault-manifest` | in-repo, wired into `mechanic-green` | contract, capability, memory and completeness drift | this is the pattern that keeps working: an instrument per defect **class**, not per incident |


## Lens B — Eve's runtime capability, by resource

| Resource | What she has today | Candidate | Evidence | Verdict |
|---|---|---|---|---|
| **Memory quality** | Cognee + pgvector, recall pulls large candidate pools (`DEFAULT_RECALL_TOP_K` 250, fallback 2000), no reranking stage | `PrithivirajDamodaran/FlashRank` | **1,006★ Apache-2.0**, pushed 2026-07-11 — CPU/ONNX cross-encoder reranking | **Best Lens B fit found.** It is a *stage*, not a store (no second memory system), runs on CPU (`gpu_tenant: none`), and our 250–2000 candidate pools are exactly the shape a reranker needs. Must be **measured against the recall test** before adoption |
| | | `netease-youdao/BCEmbedding` 1,881★ Apache-2.0 | embedding + reranker models for RAG | Second opinion; heavier |
| | | BGE rerankers (`BAAI/bge-reranker-*`) | **not GitHub repos** — they live on HuggingFace, so the GitHub search channel was the wrong instrument here | Check HF/Ollama availability + CPU feasibility instead |
| | | idea: `getzep/graphiti` 31,178★ — **bi-temporal edges** | our recall cannot say *when* a fact stopped being true | Idea only (its store is rejected); recorded |
| **Documents** | `read_document` over md/txt/pdf via docling | `marker` (PDF→md+JSON, accuracy), `surya` (OCR/layout/tables, 90+ languages), `markitdown` (office) | see Lens A row above | **Measure first:** which formats actually fail today. A brick without that measurement is a guess |
| **Web / search** | self-hosted SearXNG + web_scout | `adbar/trafilatura` | **6,868★ Apache-2.0**, pushed 2026-09-25 — main-text + metadata extraction | High value: clean extraction means less junk in her context and better recall of what she read. Cheap, CPU, no service |
| **Chunking** (feeds memory) | Cognee defaults | `feyninc/chonkie` | **4,772★ MIT**, pushed 2026-09-18 — lightweight ingestion/chunking | Only if a recall test shows chunk-boundary loss; changing chunking re-embeds |
| **Code reach** | `read_active_tool` (text-level) | `ast-grep` + its MCP · `universal-ctags/ctags` | 16,052★ MIT · 7,289★ GPL-2.0 | Blocked by **data**: our codebases are flattened. De-flatten check comes first (Lens A work) |
| **Voice** | Speaches on :8000 (realtime) | — | — | Batch script against Speaches; whisperX only if diarization is genuinely needed |
| **Admission / ops** | `resource_pulse`, `admit_for_goal` | — | — | Orphan-process assertion (~15 lines); VRAM accounting accuracy |

## Re-sort of the earlier ranked list, by lens

| Earlier item | Lens | Why |
|---|---|---|
| Duplicate sweep (`czkawka`/`jdupes`) + near-dup (`text-dedup`) | **A** | curation-time data hygiene; frees Eve forever, costs nothing at runtime |
| Batch transcription of the audio bank | **A** producing **B**-usable material | it is a *pipeline* (builder-owned) whose output becomes documents she can read |
| Container mount containment | **B** (safety) | protects her sandbox at runtime; stdlib guard, no dependency |
| `ast-grep` brick | **B**, gated by **A** | runtime capability whose precondition is a builder data fix |
| Lingering MCP process check | **A** (ops) protecting **B** | keeps her runtime healthy; measures an invariant we already fixed once |
| `deptry`, `vulture`, `mutmut`, `lychee` | **A** | find our defects mechanically — no runtime cost at all |
| `FlashRank`, `trafilatura`, `chonkie`, OCR/marker | **B** | improve what she retrieves, reads or speaks |
| `graphiti` bi-temporal idea | **B** (idea only) | memory semantics, not a component |

## Still unsearched (the investigation continues in both directions)

**Lens A:** markdown/prose linting (`lychee` stats unverified; `vale`, `typos`), a PocketBase migration test
harness, container image **digest pinning** (we have two unpinned `:latest` images), dependency CVE auditing
(`pip-audit`), coverage-gap analysis.
**Lens B:** an actual reranker comparison on our corpus (FlashRank vs BCEmbedding vs a BGE model — measured,
not read about), MCP tool-output size management, whether the `vision` GPU tenant is used at all, TTS quality,
and consolidation passes (what Cognee's `memify` actually buys on `eve_core`).

## Recommendation, small first

**Lens A now:** (1) `deptry` into the gate — it would have caught the docling hole the day it appeared;
(2) `czkawka` sweep of the vault; (3) `vulture` + `mutmut` as *measurements* reported by the gate, not
gates themselves (a wrong "dead code" call costs more than an unmeasured one).
**Lens B now:** (1) `trafilatura` for web reading; (2) measure `FlashRank` against the recall test;
(3) the Speaches batch script; (4) code reach only after the de-flatten check.

**Rule going forward:** every proposed addition states its lens. Lens A tools are adopted when they target a
recorded defect class. Lens B limbs must show a measured behavioural improvement, because they tax every turn.
