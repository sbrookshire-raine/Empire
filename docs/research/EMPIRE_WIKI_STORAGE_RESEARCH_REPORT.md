# EMPIRE Local Wikipedia Storage & Retrieval Research Verdict

## Executive verdict — 10 lines
1. Keep the 7.1M-file Markdown corpus as the authoritative **library** until measured section I/O proves it violates the latency budget.
2. Keep SQLite `pages` and `aliases` as the **phone book**; exact title resolution is not the cause of current structured-extract failures.
3. Split the 188M-edge `links` **roads** from the phone-book file only if a controlled benchmark proves material hop-ranking latency or operational contention.
4. Build one deterministic `wiki_extract` layer before changing storage: structure first, selection second, prose synthesis last.
5. Replace raw lead/section injection with a versioned JSON evidence envelope containing fields, tables, lists, provenance, warnings, and an explicit empty state.
6. Make empty or unsupported extraction a hard refusal condition; no storage engine can prevent invention if the answer contract permits parametric completion.
7. Put MCP in front of resolve/extract/remember contracts, but keep Cognee behind `remember` and `recall`, never behind encyclopedia existence.
8. Move a DuckDB/Parquet **roads-only benchmark** now; do not migrate the phone book and do not claim it improves extraction.
9. Keep ZIM, GBNF, and SetFit gated: their manifest kill criteria have not yet been demonstrated by measurements.
10. Judge progress on reusable table/infobox/list/scalar extracts with Weaviate off—not on cast-trivia demonstrations.

## A. Layer verdict matrix

The verdict refers to each layer’s role in the active architecture, not necessarily immediate deletion of historical backup data.

| # | Layer | Verdict | Why | Risk if wrong |
|---:|---|---|---|---|
| 1 | Markdown library (`D:\wiki_md\{year}`) | **Keep** | It is the complete, offline, citeable article source; no evidence yet shows random section I/O is outside budget. | File-count overhead may cap latency or operability; test before adopting ZIM or another blob format. |
| 2 | Title DNS: SQLite `pages`/`aliases` | **Keep** | Point lookup and alias resolution largely work, and replacing them cannot parse tables or enforce refusal. | Unmeasured lock/cache contention from co-resident links could be misattributed to SQLite itself. |
| 3 | Link web: SQLite `links`/`link_progress` | **Split** | Keep the logical roads, but benchmark a separate Parquet/DuckDB read model because 188M-edge analytics is a different workload from title OLTP. | A premature split adds export, freshness, dual-version, and rollback costs without user-visible gain. |
| 4 | Wiki reports/catalogs | **Keep** | Build manifests, redirects, disambiguation, and status artifacts are useful provenance and rebuild inputs. | Unversioned or stale reports can silently disagree with the selected wiki year. |
| 5 | Remembered-title ledger | **Keep** | A small idempotency ledger remains useful, but key future entries by structured-extract hash rather than title alone. | Title-only suppression may prevent remembering a newer year or materially changed extract. |
| 6 | Weaviate archive | **Keep** | Preserve only as an opt-in Truth Drift/year-comparison subsystem, isolated from existence and normal extraction. | Accidental fallback can reintroduce false-friend existence and availability failures. |
| 7 | Weaviate staging export | **Delete** | Remove it from the active design; retain only a labeled cold archive if audit/recovery value is proven. | Deleting the only reproducible export would make historical comparison recovery expensive. |
| 8 | `wiki_cache` triage | **Keep** | A small, inspectable compare/promote buffer has a distinct human-review job. | It can become an uncatalogued shadow source if answers read it without year/source labels. |
| 9 | Session scratchpad | **Keep** | Ephemeral bridging facts belong outside durable Cognee and support bounded multi-hop work. | Stale session facts can leak across subjects unless session IDs and TTL/cleanup are enforced. |
| 10 | Error Book | **Keep** | Persistent typed misses are essential for LOCATE/EXTRACT/ANSWER diagnosis and regression sampling. | Free-text-only logs create anecdotes rather than measurable failure classes. |
| 11 | LOOKUP lock | **Keep** | It is a useful guard against redundant scouting, but must accompany—not substitute for—an evidence-state contract. | Treating the lock as proof of obedience leaves parametric override untouched. |
| 12 | Historical ingest ops controls | **Delete** | Retire full-Cognee-ingest checkpoint/priority controls from the active wiki path; the underlying bulk-ingest strategy is closed. | Generic abort/checkpoint utilities may be lost if other bounded jobs still depend on them; inventory callers first. |
| 13 | Cognee graph memory | **Keep** | Sparse, explicit, post-extract constellations are a valid REMEMBER layer on the NTFS VHDX. | Schema-free remembers may accumulate unciteable or duplicate claims and later masquerade as source truth. |
| 14 | Cognee lock | **Keep** | Serializing Cognee MCP/CLI access protects the known single local memory substrate. | Coarse locking may become a latency bottleneck; instrument wait time before redesigning. |
| 15 | PocketBase | **Keep** | Keep it for tasks/jobs and source logging, explicitly outside title DNS and article truth. | Scope creep creates a second phone book with synchronization and authority ambiguity. |
| 16 | Ollama | **Keep** | Local synthesis is required, but it should verbalize validated extracts rather than create evidence. | Model behavior can still override evidence unless the server blocks unsupported answer paths. |

**New logical layer proposed:** `wiki_extract` between layers 1–3 and layers 11/16. It is not a new corpus DB. It deterministically parses stored page structure into a versioned evidence envelope.

## B. Ranked experiment list (maximum 8)

### 1. Generic extract-and-refusal evaluation gate

| Field | Plan |
|---|---|
| **Hypothesis** | A stratified, provenance-labeled suite will show that most current failures occur after successful LOCATE and will prevent storage substitutions from receiving false credit. |
| **Touches layers** | 1, 2, 3, 10, 11, 16; proposed `wiki_extract` |
| **Effort** | **M** — 1–3 days for an initial 60-case gold set and runner |
| **Prerequisite data** | Sample local 2026 pages: 12 infobox, 12 table, 12 list, 12 scalar/date/number, and 12 empty/missing/ambiguous cases; expected fields/cells plus page/section provenance. |
| **Metric** | Report LOCATE accuracy, extract field F1, table cell F1, list item F1, provenance coverage, p50/p95 latency, and unsupported-claim rate separately. Baseline and every later experiment run with Weaviate off. |
| **Kill criterion** | Kill any proposed change that cannot move its named metric by at least 10 percentage points or 20% latency without regressing exact-title accuracy or empty-case refusal. Expand to ≥200 cases before an architectural migration. |
| **Does not solve** | It does not parse pages, rank roads, or make Eve obey; it makes those failures distinguishable. |

### 2. Deterministic structure extractor spike

| Field | Plan |
|---|---|
| **Hypothesis** | Parsing infobox templates, MediaWiki tables, headings, and lists before LLM use will produce reusable structured candidates with ≥0.90 field/cell F1 on supported constructs and no raw `{|` injection. |
| **Touches layers** | 1, 2, 11, 16; proposed `wiki_extract` |
| **Effort** | **M** — 2–5 days |
| **Prerequisite data** | Experiment 1 fixtures; preserve original article bytes/lines. On Windows-local Python, spike `wikitextparser` or `mwparserfromhell` for templates plus a deterministic table normalizer; emit JSON Schema v1. |
| **Metric** | Field F1, table cell F1 after rowspan/colspan normalization, list item F1, 100% source title/year/section attribution, zero raw wikitable payloads, p95 parse time ≤150 ms after page read. |
| **Kill criterion** | Stop the chosen parser if supported-construct F1 is <0.80 after two bounded fixes, if it requires per-topic handlers, or if p95 parsing exceeds 500 ms. Compare another parser before abandoning deterministic extraction. |
| **Does not solve** | It does not infer arbitrary facts absent from explicit structure, resolve ambiguous titles, rank multi-hop links, or guarantee model obedience. |

### 3. Evidence envelope plus server-side fail-closed gate

| Field | Plan |
|---|---|
| **Hypothesis** | A typed evidence state (`ok`, `empty`, `ambiguous`, `unsupported`, `error`) enforced before Ollama will reduce invented answers on empty evidence to zero. |
| **Touches layers** | 10, 11, 16; proposed `wiki_extract` |
| **Effort** | **S** — hours to 2 days |
| **Prerequisite data** | JSON Schema v1 from experiment 2 and at least 30 empty/unsupported/adversarial prompts. |
| **Metric** | 0/30 answers containing factual claims when state is not `ok`; 100% machine-readable refusal reason; supported-answer citation coverage ≥99%; no lead fallback after an empty extract. |
| **Kill criterion** | Reject prompt-only enforcement if any unsupported factual answer occurs; move the block to server/application control. Stop adding prose instructions once a deterministic gate is available. |
| **Does not solve** | It does not improve extraction recall or recover facts that the parser missed. |

### 4. MCP contract: resolve → extract → remember

| Field | Plan |
|---|---|
| **Hypothesis** | Three narrow, typed MCP tools will remove lead dumping and prevent Cognee from becoming an implicit encyclopedia while preserving explicit remembrance. |
| **Touches layers** | 1, 2, 3, 5, 9, 11, 13, 14, 16; proposed `wiki_extract` |
| **Effort** | **M** — 2–4 days including Eve mirror tests |
| **Prerequisite data** | Stable evidence schema, content hashes, and idempotency keys; no bulk Cognee job. |
| **Metric** | 100% schema-valid tool responses across the suite; zero Cognee calls during resolve/extract; zero remembers for non-`ok` extracts; duplicate remember rate 0; tool-loop rate <1%; p95 orchestration overhead ≤100 ms excluding page read/model. |
| **Kill criterion** | Stop if the façade hides raw prose under nominal JSON, lets recall decide article existence, or cannot enforce extract provenance/idempotency. Keep direct internal functions and revise the contract. |
| **Does not solve** | MCP is an interface boundary, not a parser, graph engine, or grounding guarantee by itself. |

### 5. Roads-only SQLite versus Parquet/DuckDB benchmark

| Field | Plan |
|---|---|
| **Hypothesis** | A read-only Parquet/DuckDB copy of `links` will materially improve neighbor scans and intent ranking while SQLite remains faster/simpler for `pages` and `aliases`. |
| **Touches layers** | 2, 3, 4 |
| **Effort** | **M/L** — 2–5 days depending on one-time 188M-edge export |
| **Prerequisite data** | Export only `links` to year/version-partitioned Parquet, sorted/clustered by `from_norm`; keep SQLite authoritative and record build hash. |
| **Metric** | On ≥10,000 sampled subjects: cold/warm p50/p95/p99 1-hop lookup and full rank latency, throughput, peak RAM, disk size, export duration, and result parity. |
| **Kill criterion** | **Existing gate is not yet met** because no bottleneck measurement is supplied. Do not split unless SQLite rank p95 exceeds the product budget (provisionally 500 ms) **and** DuckDB gives ≥3× p95 improvement with exact parity, tolerable RAM, and a reproducible one-way rebuild. Never dual-write initially. |
| **Does not solve** | It cannot parse infoboxes/tables, prevent invention, or improve exact-title semantics. It is a LOCATE-hop performance experiment only. |

### 6. Redirect/alias completeness delta

| Field | Plan |
|---|---|
| **Hypothesis** | Importing the matching-year MediaWiki redirect relation will improve genuine LOCATE misses more cheaply and safely than replacing Title DNS. |
| **Touches layers** | 2, 4, 10 |
| **Effort** | **M** — 1–3 days |
| **Prerequisite data** | Matching-year redirect SQL/TSV, normalized with the existing title rules; 200+ Error Book misses labeled alias/ambiguous/absent. |
| **Metric** | Alias-miss recall improvement, exact-title regression rate 0, ambiguity rate, added rows, and p95 lookup latency. |
| **Kill criterion** | Stop if fewer than 5% of labeled LOCATE misses are recovered, normalization creates >0.5% wrong canonical mappings, or year provenance cannot be maintained. |
| **Does not solve** | It does not improve extraction after the correct page is found. |

### 7. Markdown random-section I/O benchmark; ZIM gate

| Field | Plan |
|---|---|
| **Hypothesis** | Page parsing and answer handling—not filesystem access—dominate current latency, so repacking 7.1M pages into ZIM is premature. |
| **Touches layers** | 1, 4 |
| **Effort** | **S/M** — 1–2 days |
| **Prerequisite data** | 10,000 reproducibly sampled page paths across directory sizes and article sizes; cold-ish and warm-cache runs on the actual Windows volumes. A representative ZIM subset only if the first gate trips. |
| **Metric** | Open/read/H2-scan p50/p95/p99, errors, throughput, cache sensitivity, and end-to-end share of extract latency. |
| **Kill criterion** | **Existing ZIM criterion is not yet met.** Advance ZIM only if Markdown section I/O p95 is >200 ms or >30% of end-to-end extract latency, or a measured operational requirement mandates a single file; adopt only if a same-content ZIM prototype gives ≥3× p95 improvement without losing stable title/year/section provenance. |
| **Does not solve** | ZIM does not create structured fields, rank roads, or enforce refusal; `openzim-mcp` would only change library access. |

### 8. Post-contract router/grammar gate: GBNF and SetFit

| Field | Plan |
|---|---|
| **Hypothesis** | After deterministic extraction and server-side gating, neither a learned intent router nor grammar-constrained generation is necessary for the core extract path; residual failures can be measured before adding either. |
| **Touches layers** | 10, 11, 16; proposed `wiki_extract` |
| **Effort** | **S** to measure; **M** only if a gate trips |
| **Prerequisite data** | ≥200 paraphrases spanning resolve/extract/compare/remember plus one-letter, quoted-title, ambiguous, and empty cases; tool-call traces and schema-validity logs. |
| **Metric** | Intent accuracy, repeated-tool-call rate, invalid-JSON rate, extract F1, and unsupported-claim rate after experiments 2–4. |
| **Kill criterion** | **Current GBNF gate is not met:** trial it only if invalid structured model output remains >0.5% or repeated tool loops remain >1% after lock, typed MCP, and server gate; kill if it does not halve that residual without recall loss. **Current SetFit gate is not met:** trial it only if rule routing is <95% accurate and ≥5% of all failures are true intent errors, including the One-Letter Fork; kill if macro-F1 is <0.97, it adds >50 ms p95, or errors remain extraction failures. |
| **Does not solve** | GBNF cannot find missing evidence; SetFit cannot parse page structures or replace Title DNS. Neither is a storage fix. |

## C. Direct answers to the five Architect questions

### 1. Would a different DB for the phone book + links fix extract failures?

**No.** Moving `pages`/`aliases` does not turn wikitables or infoboxes into fields, shorten lead dumps, or stop unsupported completion. That is an **EXTRACT/ANSWER-contract** failure after LOCATE succeeded. Moving **links only** may improve road scans, hop ranking, and operational isolation if experiment 5 trips its latency gate. Keep the phone book in SQLite unless point-lookup measurements—not intuition—show a separate defect.

### 2. Is MCP in front of Cognee sound, and what is the contract?

**Yes, only as a boundary around sparse post-extract memory; no, if it makes Cognee the read path for article existence.** The façade should separate jobs:

```text
wiki_resolve(subject, year)
  -> {state: exact|alias|ambiguous|missing, canonical_title, candidates[], year, source_id}

wiki_extract(subject, year, need_hint?, section?)
  -> {state: ok|empty|ambiguous|unsupported|error,
      extract_id, schema_version, canonical_title, year, source_hash,
      fields[], tables[], lists[], provenance[], warnings[], refusal_reason?}

wiki_remember(extract_id, namespace="eve_memory", tags=[], note?)
  -> {state: stored|duplicate|rejected, memory_id?, source_hash, reason?}

wiki_recall(query, namespace="eve_memory", filters?)
  -> {memory_hits[], provenance[], authority: "remembered-not-encyclopedia"}
```

`need_hint` narrows or ranks already-extracted structures; it must not be a growing genre router. `wiki_remember` accepts only a previously issued successful `extract_id`, verifies its content hash/provenance, is idempotent, and never accepts a full article by convenience. `wiki_recall` is explicitly labeled memory and cannot answer “does this Wikipedia page exist?” Cognee lock wait time should be logged.

### 3. Smallest change that unlocks table/infobox → fields without a new NLP router?

Add a deterministic structural parser to the existing section-read path and change the injected payload—not the title store and not the conversational router. Parse every located page into generic containers:

- `fields`: normalized infobox key/value pairs, preserving raw key/value and source offsets;
- `tables`: caption, headers, normalized rows/cells, with rowspan/colspan warnings;
- `lists`: section path and item text;
- `provenance`: title, year, section, byte/line/cell location, source hash.

Then use `need_hint` only for lexical column/key/section ranking. If no candidate clears a conservative threshold, return `unsupported` or the full bounded structured candidates—not invented prose. This is the smallest ceiling-raising change because it converts page syntax into reusable data independently of question genre.

### 4. Which deferred technology moves now?

| Technology | Move now? | Is the manifest gate already met? | Measurement that trips the gate |
|---|---|---|---|
| **DuckDB/Parquet** | **Benchmark now, links only; do not migrate yet.** | **No evidence yet.** The corpus shape makes the experiment plausible, not justified. | Real SQLite road-ranking p95 >500 ms (or agreed product budget) and DuckDB ≥3× faster with parity, acceptable RAM, and reproducible rebuild. |
| **ZIM** | **Stay gated. Run only the Markdown I/O benchmark now.** | **No.** “Millions of files” is a concern, not an observed latency failure. | Random H2 I/O p95 >200 ms or >30% of extract latency/single-file operational requirement, followed by ≥3× ZIM prototype gain without provenance loss. |
| **GBNF** | **Stay gated.** Use deterministic application serialization and server refusal first. | **No.** Residual loops/invalid output after lock + scratchpad + typed contract have not been measured. | Invalid JSON >0.5% or repeated tool calls >1% on ≥200 cases after experiments 2–4; retain only if grammar halves the residual without recall loss. |
| **SetFit** | **Stay gated.** | **No.** The One-Letter Fork/rule-router post-fix failure rate is not established. | Rule intent accuracy <95% and true intent errors ≥5% of all failures on ≥200 paraphrases; require SetFit macro-F1 ≥0.97 and <50 ms p95 overhead. |

Thus **DuckDB earns a spike, not adoption**. ZIM earns an I/O measurement, not repacking. GBNF and SetFit do not move until failures remain after the extract and refusal contracts.

### 5. What would an outside team not try?

A disciplined outside team would not change the storage substrate before producing a failure ledger showing which user-visible failures are LOCATE, EXTRACT, ANSWER/REFUSE, or REMEMBER. It would specifically avoid: full-wiki Cognee/GraphRAG, vector similarity as existence, phone-book migration without point-lookup evidence, ZIM repacking without I/O data, and router/model complexity for failures caused by raw unparsed structures. It would freeze cast/song demos as regression curiosities and fund only changes that improve the generic extract suite.

## D. Anti-circle checklist

- [ ] **“Put Wikipedia in Cognee so facts are connected.”** Already tried: the overnight full ingest was halted for scale, cost, unclear retention, and wrong-layer semantics; Cognee remains sparse REMEMBER only.
- [ ] **“Use Weaviate or a new vector DB to decide whether a title exists.”** Already tried: similarity produced false friends such as *The Following* → *Cult following*; Title DNS remains the existence gate.
- [ ] **“GraphRAG/embed all pages, but with a newer embedding model.”** Already closed: corpus-scale construction is the wall, and changing embeddings does not alter the forbidden full-corpus job.
- [ ] **“Move the entire 31 GB SQLite to DuckDB/PocketBase/a graph DB.”** Recycled conflation: exact phone-book hits work; only 188M-edge road analytics has a plausible engine mismatch, and even that awaits a benchmark.
- [ ] **“Fix the next cast/song/quoted-title prompt with another regex, SetFit router, or bigger model.”** Already tried in variants: phrasing patches move one demo while raw tables, empty evidence, and unsupported synthesis remain; parse generic structures and fail closed first.

## E. Optional reference architectures mapped to EMPIRE metaphors

### E.1 Conservative architecture — recommended default

```text
LIBRARY  D:\wiki_md\{year}\*.md
   │ exact path + bytes
PHONE BOOK  SQLite pages/aliases ── REPORTS redirects/disambiguation
   │ located article
EXTRACT  deterministic AST/table/list parser → Evidence JSON v1
   │ state=ok only                       └─ state!=ok → server refusal
GLASSES  [[EMPIRE_WIKI_EXTRACT]] + LOOKUP lock
   │
OLLAMA  verbalize/cite bounded evidence
   │ explicit user/Architect action
MEMORY  MCP wiki_remember → Cognee sparse constellation
```

The **roads** remain in SQLite initially and are consulted only when direct resolution/explicit multi-hop requires them. Weaviate stays on a separate Truth Drift fork.

### E.2 Performance-split architecture — only after experiment 5 passes

```text
LIBRARY: Markdown (or ZIM only after experiment 7 passes)
PHONE BOOK: SQLite pages/aliases — authoritative, point lookup
ROADS: versioned Parquet + DuckDB — read-only analytical projection rebuilt per wiki year
EXTRACT: same deterministic Evidence JSON contract
MEMORY: same sparse Cognee contract
```

This is a one-way build, not dual-write: SQLite/report artifacts produce a year/hash-labeled roads snapshot. Failure falls back to SQLite roads. The extract contract remains unchanged, proving that storage optimization and data extraction are independent.

### E.3 Where common reference systems fit—and do not fit

- **Kiwix/ZIM** maps only to the **library container/access** job. It may reduce file-count overhead but is neither phone book semantics nor extraction.
- **MediaWiki replica SQL** is useful as a **phone-book/report input**, especially redirects and page identity; running a full MediaWiki service is unnecessary for the stated failures.
- **SQLite FTS** could be a bounded **library discovery fallback** after exact/alias miss, but never the primary existence gate and not a table parser.
- **DuckDB over Parquet** maps to **roads analytics**, not canonical title writes or agent memory.
- **MCP** is the typed doorway across resolve/extract/remember; it is not itself a database or grounding mechanism.
- **Cognee** maps only to **memory** after a successful, provenance-bearing extract.

## Do this next week

1. Build the 60-case generic extract/refusal gold set and emit a LOCATE → EXTRACT → ANSWER failure ledger with Weaviate off.
2. Spike deterministic infobox/table/list parsing and inject `Evidence JSON v1`; enforce server-side refusal for every non-`ok` state.
3. Export a representative roads partition to Parquet and benchmark SQLite versus DuckDB; authorize a full 188M-edge export only if the provisional latency gate trips.
