# EMPIRE Local Wikipedia Data Architecture Strategy

**Research date:** 2026-09-15  
**Primary source:** `EMPIRE_WIKI_STORAGE_RESEARCH_REPORT.md` supplied in this conversation  
**Scope:** Windows-local, offline-first Wikipedia location, deterministic extraction, evidence-grounded answering, and sparse remembrance

## Evidence labels used

- **[VF] Verified fact:** supported by the supplied report or a cited primary source.
- **[RI] Reasonable inference:** follows from verified facts but still needs EMPIRE measurement.
- **[A] Assumption:** required because the report does not provide the information.
- **[O] Opinion:** architectural judgment, not an externally provable fact.
- **[EXTENSION]** Recommendation beyond the supplied report. It must pass its own acceptance gate and does not override the report.

To reduce visual noise, technical statements carrying an inline primary-source citation are **[VF]** even when the label is not repeated. Uncited design recommendations are **[RI]** or **[O]** according to context; unresolved premises are explicitly tagged **[A]**.

---

## 1. Executive summary

The report’s diagnosis is sound: EMPIRE’s dominant problem is **EXTRACT and ANSWER/REFUSE**, not **LOCATE**. Exact title resolution mostly works; changing the phone-book database cannot convert raw wikitables into rows or prevent an LLM from inventing facts after an empty read. The highest-leverage action is therefore a deterministic, versioned `wiki_extract` boundary that emits typed fields, tables, lists, scalars, provenance, warnings, and explicit non-success states.

The recommended target is intentionally conservative:

1. Keep `D:\wiki_md\{year}` as the authoritative **library**.
2. Keep SQLite `pages` and `aliases` as the authoritative **phone book**.
3. Keep SQLite roads initially; benchmark a read-only Parquet/DuckDB projection of `links` only after establishing the current p95.
4. Add a source-fidelity gate before choosing a parser: confirm whether the Markdown retains original wikitext structures, revision/dump identity, and stable evidence offsets.
5. Implement `wiki_resolve`, `wiki_extract`, `wiki_remember`, and `wiki_recall` as separate typed MCP contracts. Cognee remains sparse post-extract memory.
6. Enforce `ok | no_evidence | ambiguous | unsupported | source_error` in application code before Ollama; prompt instructions are not the control boundary.
7. **[EXTENSION]** Add a minimal source/run control plane: Git-versioned JSON manifests, JSON Schema, one small SQLite ledger, JSONL logs, and content hashes. This supplies lineage and reproducibility without a catalog platform.
8. **[EXTENSION]** Start with Windows Task Scheduler and a thin Python/PowerShell runner. Add Prefect only after measured retry/backfill complexity; do not add DataHub, OpenMetadata, dbt, or an observability stack now.
9. **[EXTENSION]** Use application-consistent SQLite snapshots and one encrypted backup tool, preferably restic if no equivalent exists; test restoration rather than equating file copy with recovery.
10. Treat ZIM, GBNF, SetFit, graph databases, lakehouse formats, document stores, time-series stores, and new vector databases as gated alternatives—not default components.

**Primary decision:** build and test the evidence contract first. Storage migration is explicitly downstream of measured LOCATE or I/O failures.

---

## 2. Interpretation of the report

### Objectives

The report seeks a reusable local data-extraction substrate for automation, not a better trivia demo.

- **LOCATE:** resolve an exact or aliased Wikipedia entity to the correct local year-scoped page.
- **EXTRACT:** transform arbitrary explicit page structures—infobox fields, table rows, lists, dates, numbers, and named values—into machine-usable records.
- **ANSWER/REFUSE:** answer only from validated evidence; empty, ambiguous, unsupported, or invalid evidence must fail closed.
- **REMEMBER:** optionally store a small successful extract constellation in Cognee after explicit approval; never ingest the encyclopedia wholesale.
- Preserve citeability, year identity, offline operation, and applicability to unattended automation.

### Governing rules

1. Do not conflate LOCATE, EXTRACT, ANSWER/REFUSE, and REMEMBER failures.
2. Do not bulk-load Wikipedia into Cognee, build GraphRAG over all pages, or embed the corpus.
3. Do not use Weaviate or any vector database as the primary existence gate; Weaviate remains Truth Drift/year comparison only.
4. Do not patch individual genres such as cast or song questions.
5. Prefer deterministic parsers and falsifiable experiments over architecture replacement.
6. Keep SQLite Title DNS unless point-lookup evidence demonstrates a fault.
7. Consider DuckDB only for the 188M-edge roads workload and only against the report’s measured kill criterion.
8. Keep ZIM, GBNF, and SetFit gated until their stated thresholds trip.
9. Keep runtime local-first on Windows 11 with Ollama; no paid cloud LLM in application code.
10. MCP is a typed interface, not a parser, database, or truth mechanism.

### Constraints and assumptions

**Verified from the report**

- About 7.1M Markdown pages exist under `D:\wiki_md`.
- A roughly 31 GB SQLite file contains `pages`, `aliases`, and about 188M `links` edges.
- Weaviate on `:8091` is optional and limited to Truth Drift.
- Cognee resides on an NTFS VHDX and is used only for explicit sparse memories.
- Current failures include raw wikitable injection, lead dumping, empty-evidence invention, and question-specific patches.
- Available GPU/VRAM is constrained; a larger always-resident model is not an architectural assumption.

**Assumptions requiring validation**

- **[A1]** The Markdown corpus is complete and maps unambiguously to a Wikimedia dump date/year.
- **[A2]** Its page bodies retain enough original wikitext structure for a deterministic parser. If conversion destroyed templates, spans, or offsets, extraction must target the retained syntax or reacquire source wikitext.
- **[A3]** Title and link data are predominantly read-only between year snapshots.
- **[A4]** One host or one coordinated writer publishes each dataset version.
- **[A5]** Provisional p95 gates in the report are acceptable product SLO candidates, not approved SLOs.
- **[A6]** EMPIRE may distribute software externally; therefore GPL dependencies require a project-specific license review. This report is not legal advice.

### Required outputs inherited from the report

The supplied report required and delivered: a 16-layer verdict matrix; no more than eight falsifiable experiments; direct answers to five Architect questions; a five-item anti-circle checklist; optional mapped reference architectures; a ten-line executive verdict; and no more than three next-week actions. This strategy preserves those decisions and adds implementation/governance detail only where marked **[EXTENSION]**.

### Desired result and success criteria

A successful request follows this invariant:

```text
resolved source + validated evidence records + verified provenance
    -> bounded answer
anything else
    -> disambiguation or machine-readable refusal
```

Minimum acceptance measures from the report:

- LOCATE accuracy reported separately from extract quality.
- Field F1, table-cell F1, list-item F1, provenance coverage, and p50/p95 latency measured on a generic gold set with Weaviate off.
- Zero factual answers on empty/unsupported evidence in the refusal test set.
- No raw `{|` wikitable payload reaches the answer model.
- Exact-title behavior does not regress.
- No successful `remember` occurs without a provenance-bearing successful extract.
- Any architecture migration must improve its named metric by at least 10 percentage points or latency by 20%; the roads split has the stricter report gate of SQLite p95 over budget and at least 3× DuckDB improvement with parity.

---

## 3. Gaps, risks, ambiguities, or potential weaknesses in the report

| Gap or risk | Type | Why it matters | Required resolution |
|---|---|---|---|
| Source-fidelity is unknown | **[A]** | Wikitext parsers cannot reconstruct templates, rowspans, revision IDs, or source offsets discarded during Markdown conversion. | Inspect 50–100 representative files against original dump/source records before selecting the parser. |
| “Canonical” source is underspecified | **[RI]** | Markdown, reports, SQLite, and possible dumps may disagree by year/build. | **[EXTENSION]** Register a dataset version with dump date, source checksum, build commit, artifact hashes, and atomic active/superseded status. |
| Evidence coordinates are not finalized | **[RI]** | Line numbers shift after normalization; paths can move; table cells may be synthesized from spans. | Define byte offsets against immutable source bytes plus section/table coordinates and fragment hashes. |
| SLOs are provisional | **[VF]** | The report uses provisional values such as 500 ms road p95 and 200 ms section I/O p95. | Architect approves end-to-end, stage, warm/cold, and batch SLOs before migration decisions. |
| Gold-set size is small | **[RI]** | Sixty cases can prove plumbing but not broad encyclopedia robustness. | Use 60 for POC; stratify and expand to at least 200 before architecture migration, then sample by markup construct and article size. |
| Normalization policy is absent | **[RI]** | Dates, units, footnotes, merged cells, repeated keys, and links can be normalized incorrectly while schema-valid. | Preserve raw and normalized values; version each deterministic normalizer and record warnings. |
| Unsupported syntax policy is incomplete | **[RI]** | Template/Lua expansion and extension tags exceed simple parser behavior. | Literal parser first; return `unsupported`; escalate selected fixtures to Parsoid only if measured value justifies it. |
| Update/synchronization model is unspecified | **[A]** | Dual writes or partial year swaps can create mixed truth. | Publish immutable versions, verify them, then atomically switch an active manifest pointer. No mutable dual truth. |
| Backup and recovery objectives are absent | **[A]** | Seven million files and VHDX/Cognee state have different rebuild and recovery costs. | Define RPO/RTO by data class and perform timed restore drills. |
| Trust boundary is incomplete | **[RI]** | Local source text can still contain malicious instructions; MCP tool output may be malformed; paths can escape roots. | Treat source text as data, validate all tool I/O, enforce path containment and least-privilege ACLs, and never execute page content. |
| License obligations need source-level review | **[A]** | Parser and corpus licenses differ; wikitextparser is GPL-3.0 while alternatives are MIT; Wikipedia content attribution/share-alike duties may apply. | Record source/tool licenses in manifests and obtain counsel for distribution strategy. |
| Cognee consistency/restore semantics are not evaluated | **[RI]** | Sparse memory is allowed but could still hold stale or unciteable claims. | Require extract IDs, source hashes, namespace, explicit authority label, idempotency key, and tested VHDX/database restore. |

These gaps do not invalidate the report. They mostly reinforce its demand to validate evidence before adding infrastructure.

---

## 4. Research findings

### Relevant strategies and architectural patterns

#### 4.1 Separate authoritative stores from reproducible projections

**[RI] Recommended.** Keep one authority per job:

- Markdown/source bytes: article content authority.
- SQLite `pages`/`aliases`: entity existence and path authority.
- SQLite roads: initial adjacency authority.
- Evidence JSON: request-level validated extract authority.
- Parquet: optional immutable batch/analytics projection.
- Cognee: explicitly remembered derived claims, labeled non-encyclopedic memory.

Every projection records input artifact IDs, hashes, schema/extractor versions, and run ID. This avoids the common hybrid-system failure in which several engines silently become competing truth stores.

#### 4.2 Medallion-like layers without a lakehouse product

**[EXTENSION]** Use the useful separation—landing, validated, normalized, serving, archive—but implement it with directories, manifests, SQLite, JSON/Parquet, and atomic publication. Iceberg/Delta/Hudi are unnecessary for one coordinated local writer because their distributed transaction/catalog machinery solves a problem not in evidence.

#### 4.3 Contract-first and fail-closed serving

JSON Schema validates envelope shape, while a custom semantic validator recomputes source and fragment hashes, checks evidence offsets, and verifies deterministic normalization. JSON Schema’s current published dialect is 2020-12, but schema validity alone does not establish factual support ([JSON Schema specification](https://json-schema.org/specification)).

MCP tools can declare input and output schemas and structured content; the current specification also requires servers to validate inputs and advises clients to validate results before passing them to an LLM ([MCP Tools specification, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/server/tools)). EMPIRE should validate on both sides because “should” in a protocol is not an application guarantee.

#### 4.4 Immutable snapshot publication

**[EXTENSION]** Build a year/version into a temporary location, validate counts/hashes/contracts, then atomically publish a small manifest pointer. Readers pin a version for the duration of a request. Failed builds never modify the active version. This is simpler and safer than synchronizing mutable rows across SQLite, Parquet, and Cognee.

#### 4.5 Measured escalation

- Literal deterministic parser first.
- Parsoid only for failures caused by expansion semantics.
- DuckDB only for measured road analytics or cross-page extract analytics.
- Prefect only for measured scheduling/backfill pain.
- ZIM only after loose-file I/O or recovery violates an SLO.
- A graph engine only after indexed adjacency remains inadequate for required multi-hop queries.

### Candidate database structures

| Structure | Appropriate EMPIRE role | Findings and trade-off |
|---|---|---|
| Relational/embedded SQLite | Phone book, aliases, control ledger, current roads | SQLite explicitly targets device-local storage with low writer concurrency and less than about a terabyte; it is simple and serverless ([appropriate uses, updated 2025-05-31](https://sqlite.org/whentouse.html)). Keep point lookups here. |
| Columnar DuckDB + Parquet | Optional roads analytics, batch extract analytics, audits | DuckDB is in-process OLAP and directly reads/writes Parquet with multi-file queries. Its concurrency model centers read-write work in one process; multiple processes may read read-only ([concurrency](https://duckdb.org/docs/current/connect/concurrency), [Parquet](https://duckdb.org/docs/current/data/parquet/overview)). Use as a projection, not Title DNS. |
| Document database | None now | Article documents already exist as Markdown; request extracts need typed evidence, not a second schemaless copy. MongoDB would add a server and SSPL review without addressing extraction. |
| Property graph | Optional future multi-hop road serving | Cypher can simplify variable-hop queries, but loading 188M edges creates another projection and operational surface. Only benchmark an embedded, actively maintained engine after SQL/index tuning fails the SLO. |
| Time-series database | None now | Wiki data is versioned by dump/year, not high-rate telemetry. Store run metrics in the control SQLite/JSONL; revisit only if monitoring volume becomes independently material. |
| Vector database | Truth Drift only | Vector similarity is useful for semantic comparison, not ontological existence. Keep current Weaviate scope; replacing it with another vector engine does not fix the architectural mismatch. |
| Lakehouse table format | None now | Snapshot transactions, concurrent writers, and multi-engine catalogs are not required. Plain Parquet plus manifests is the simpler interoperable choice. |
| Warehouse server | None now | A Windows-local single-user analytical workload is better served by embedded DuckDB. ClickHouse/PostgreSQL become relevant only with concurrent remote users or service-level requirements. |
| Hybrid | Recommended, with strict authority boundaries | SQLite + files + optional Parquet/DuckDB + sparse Cognee is justified because each engine has one distinct job. Hybrid does not mean all engines answer every question. |

### Recommended data-layer design

| Layer | Responsibility | Physical implementation | Quality gate |
|---|---|---|---|
| 0. Source registration **[EXTENSION]** | Identify Wikimedia source, year/dump date, checksums, license, owner, status | JSON manifest + control SQLite row | Required fields, unique dataset ID, checksum and path verified |
| 1. Landing/raw | Preserve immutable source representation and build reports | Existing Markdown and wiki reports; original dump manifest retained | Counts, hashes, path containment, random open test |
| 2. Index/LOCATE | Exact title, alias, redirects, path | Existing SQLite `pages`/`aliases` | Exact/redirect suite; duplicate normalized titles; paths exist |
| 3. Roads | Adjacency and hop candidates | Existing SQLite `links`; optional immutable Parquet/DuckDB projection | Result parity, p95, row counts, build hash |
| 4. Structural extraction | Parse infoboxes, tables, lists, headings | Parser adapter over retained source syntax | Construct-level fixtures; no per-topic handlers; explicit unsupported |
| 5. Validation | Enforce envelope and evidence semantics | JSON Schema + custom verifier; Pandera only for tabular batches | Schema valid, offsets/hashes valid, no record without evidence |
| 6. Normalization | Deterministic dates, numbers, units, links | Versioned pure functions | Raw value retained; transform named; reject rather than guess |
| 7. Serving/semantic contract | Return bounded evidence for automation | `Evidence JSON v1` via MCP `structuredContent` | Typed state; size limits; provenance coverage; refusal on non-`ok` |
| 8. Answer | Verbalize validated evidence | Ollama behind server-side gate | Unsupported-claim rate zero on refusal suite; citations present |
| 9. Analytics **[EXTENSION]** | Cross-page extract/quality/road analysis | JSONL initially; Parquet/DuckDB after benchmark | Reproducible partition manifest; query parity |
| 10. Memory | Explicitly remember accepted extracts | Cognee through `wiki_remember` only | Successful extract ID required; idempotent; namespace/provenance present |
| 11. Archive/recovery **[EXTENSION]** | Retain manifests, critical state, snapshots | NTFS snapshots/directories plus restic or existing equivalent | Hash/integrity check and timed restore test |

### Data-source management approach

**[EXTENSION] Minimal registry schema**

- `datasets`: ID, role, source URI/name, language, dump date, license, owner, root, state.
- `artifacts`: dataset ID, path, format, byte/row/page count, SHA-256, schema version, producer version.
- `runs`: job, code commit, input/output artifact IDs, start/end, counts, status, error code.
- `lineage_edges`: run ID, input artifact ID, output artifact ID, transformation.
- `quality_results`: check, observed/expected, severity, pass/fail, sample path.
- `backup_runs`: snapshot, target, verification, restore-test date, measured recovery time.

**Lifecycle:** `registered → landed → validated → active → superseded → retired → purged`. Retirement requires no active manifest pointer, no dependent artifact, documented retention decision, and a recovery path if legally/operationally required.

**Synchronization:** build immutable versions; never dual-write mutable truth. An atomic active-manifest switch publishes a version. Cognee memories retain the original extract/source hash even after a source is superseded and are marked stale when their source version is retired.

**Deduplication:** titles use existing normalization/alias rules; artifacts use hashes; extraction remembers use `(extract_id, source_hash, namespace)` idempotency. Semantic similarity is not a dedup authority.

**Access control:** NTFS ACLs and a dedicated service identity. Library/index reads are read-only; publisher writes only version staging and active pointer; memory writes require explicit tool authorization. Logs should avoid storing unnecessary user prompt content.

### Relevant open-source tools

Research supports a small immediate tool set:

- **SQLite** — public-domain embedded database; retain for Title DNS and use for a compact control ledger.
- **wikitextparser** — current repository activity observed 2026-09-03; GPL-3.0; APIs cover templates, sections, tables and lists. Best feature match if retained source is wikitext and licensing is acceptable ([repository](https://github.com/5j9/wikitextparser)).
- **mwparserfromhell** — MIT; active repository observed 2026-07-28; mature AST for templates/headings/links but no equivalent first-class table grid API ([repository](https://github.com/earwig/mwparserfromhell)).
- **Parsoid** — canonical higher-fidelity wikitext/HTML route, but heavier and dependent on MediaWiki configuration/templates; escalation only ([project](https://www.mediawiki.org/wiki/Parsoid)).
- **JSON Schema 2020-12 + Python `jsonschema`** — envelope validation; bundle schemas locally and disallow network resolution.
- **Pandera** — MIT and active as of 2026-09-14; optional code-level validation when extracts become dataframe/table batches ([repository](https://github.com/unionai-oss/pandera/)).
- **DuckDB + Parquet** — MIT engine plus open columnar interchange for optional analytics; keep off the synchronous request path until justified.
- **MCP Python SDK** — MIT; typed local tool interface. It does not replace semantic validation.
- **restic** — BSD-2-Clause, single executable, Windows support, encryption, deduplication and repository verification; official site showed 0.19.1 released 2026-07-05 ([restic](https://restic.net/)).
- **Windows Task Scheduler + Python/PowerShell** — initial orchestration with no new service.
- **Prefect OSS** — Apache-2.0 and documented first-class Windows/PowerShell/UNC support; optional after orchestration tripwires ([Windows guide](https://docs.prefect.io/v3/how-to-guides/self-hosted/server-windows)).

---

## 5. Comparative analysis

### Significant architecture and storage options

| Option | Purpose | Advantages | Disadvantages/limits | Maturity & scale | Ops complexity | License | Integration | Fit |
|---|---|---|---|---|---|---|---|---|
| Markdown + NTFS | Article library | Already built, inspectable, source-like, no service | Millions of files affect enumeration/backup; source fidelity unknown | Existing 7.1M corpus proves scale, not latency | Low runtime; potentially high backup metadata cost | Corpus/tool-specific | Existing path reads | **Keep; benchmark I/O.** |
| ZIM/libzim | Compressed single/few-file library | Indexed offline archive, distribution-friendly, reduces file count | Rebuild/decompression/tooling cost; does not extract; Windows build integration is heavier | libzim repository active in 2026 | Medium | GPL-2.0-or-later for libzim | Requires new reader and provenance mapping | **Gated.** Adopt only after report I/O criterion passes. |
| SQLite | Relational phone book/control/adjacency | Embedded, reliable, transactional, native Windows, simple | Single-writer pattern; mixed OLTP/OLAP can cause cache/rebuild costs | Very mature; 31 GB is within stated device-local fit | Low | Public domain | Already integrated | **Essential/keep.** Consider physical road split, not semantic replacement. |
| PostgreSQL | Concurrent relational service | Strong SQL, concurrency, recovery/tooling | Service, upgrades, credentials, no inherent extract benefit | Very mature and scalable | Medium/high | PostgreSQL License | Rewrite deployment/query layer | **Reject now.** Revisit for concurrent remote clients/writers. |
| Parquet + DuckDB | Columnar snapshots and OLAP | Portable files, pushdown, fast scans/joins, in-process | Publication discipline; read-write concurrency centered on one process; not point-lookup authority | Mature, actively maintained | Low/medium | Apache-2.0 format; DuckDB MIT | Export links/extracts; parity harness | **Benchmark roads; optional analytics.** |
| Embedded property graph | Multi-hop road queries | Native graph model and Cypher-style traversal | Full edge copy, younger dependency, memory/import cost | Candidate-specific | Medium | Candidate-specific; review required | New exporter/query adapter | **Future gated benchmark only.** |
| Neo4j/server graph | Graph serving/tooling | Mature query ecosystem | JVM/service footprint; Community/Enterprise licensing split; duplicated truth | Mature | High for one workstation | Community GPLv3; enterprise terms differ | Service and import pipeline | **Reject now.** |
| MongoDB/document DB | Document serving | Flexible records and indexes | Duplicate article store, schemaless drift, service, SSPL review | Mature | Medium | SSPL v1 Community | New ingestion/sync | **No current role.** |
| Weaviate/vector store | Semantic/year comparison | Approximate semantic retrieval | Similarity is not existence; service/resource cost; embedding drift | Existing EMPIRE component | Medium | Verify deployed version/terms | Existing Truth Drift fork | **Keep narrowly scoped.** No new vector store. |
| Iceberg/Delta/Hudi | Lakehouse snapshots/schema evolution | Distributed transaction and multi-engine interoperability | Catalog/engine complexity exceeds single-writer need | Mature in distributed data platforms | High | Project-specific OSS | New catalog and compute stack | **Reject now.** Plain Parquet/manifests suffice. |
| ClickHouse/warehouse server | Large analytical serving | High scan/aggregation throughput | Service/container/WSL burden; duplicates DuckDB role | Mature | High relative to need | Apache-2.0 for OSS core; verify distribution | ETL and operations | **Reject now.** |
| Time-series DB | High-rate metrics | Retention, downsampling, time queries | Wrong model for wiki truth and low-volume run summaries | Mature category | Medium | Tool-specific | Telemetry agents/services | **Not applicable now.** |

### Extraction and governance options

| Option | Purpose | Advantages | Disadvantages/limits | Maintenance evidence | License | Fit/decision |
|---|---|---|---|---|---|---|
| wikitextparser | Tables/templates/lists/sections | Closest generic feature match; span-aware structures | No full MediaWiki expansion; fresh major version risk; GPL review | Repository activity 2026-09-03 | GPL-3.0 | **POC candidate if source fidelity and license gates pass.** Pin version. |
| mwparserfromhell | Wikitext AST/template fields | Mature, source-preserving, permissive license | No first-class table/list data layer; no template expansion | Repository activity 2026-07-28 | MIT | **License-friendly alternative/parser oracle.** Needs table adapter. |
| Parsoid | MediaWiki-faithful parsing/expansion path | Canonical HTML/PageBundle metadata | PHP/MediaWiki operational weight; correct template/module state needed | Active Wikimedia project | GPL-2.0-or-later | **Selective escalation**, not first component. |
| JSON Schema + semantic verifier | Contract and evidence validation | Open standard, local, deterministic, interoperable | Schema cannot prove entailment; custom verifier required | 2020-12 current published dialect | Spec/open ecosystem; Python validator MIT | **Essential.** |
| Pandera | Tabular/dataframe quality | Lightweight, code-native, supports typed checks | Additional dependency; not needed for request-level JSON alone | Active 2026-09-14 | MIT | **Optional-essential for batch tables**, after JSON contract. |
| Great Expectations | Reusable quality suites/docs | Rich validation artifacts and Data Docs | More concepts/state than current need | Active project; version must be pinned | Apache-2.0 | **Alternative to Pandera**, not companion; adopt for many shared suites. |
| Soda Core | SQL/declarative quality checks | Operator-readable SodaCL; SQL-centric | Connector packaging and another DSL | Active in 2026 per official releases | Apache-2.0 core | **Alternative** if checks become mainly SQL. |
| Task Scheduler + runner | Scheduling | Native, offline, minimal | Limited dependency/backfill UI | Windows component | OS terms + script licenses | **Default.** |
| Prefect OSS | Retries/backfills/visibility | Documented Windows support; Python-native | Server/worker/state/upgrade burden | Active 2026 | Apache-2.0 | **Optional first orchestrator** after explicit tripwire. |
| Dagster OSS | Asset/partition orchestration | Strong asset lineage/materialization model | Webserver/daemon and framework overhead | Active 2026 | Apache-2.0 | **Alternative** if asset-centric lineage becomes primary. |
| OpenLineage | Interoperable lineage events | Open event model across engines | Events need a consumer; not a catalog by itself | Active 2026 | Apache-2.0 | **Optional format only** after multi-engine consumer exists. |
| OpenMetadata/DataHub | Catalog/governance platforms | Search, ownership, lineage UI | Multi-service footprint and assigned operator required | Both active in 2026 | Apache-2.0 | **Reject now.** One host/source family does not justify them. |
| restic | Encrypted deduplicated backup | Single binary, Windows, verification, many targets | Does not create app-consistent DB snapshots by itself; secrets/restore drills required | 0.19.1, 2026-07-05 | BSD-2-Clause | **Recommended if no equivalent backup exists.** |

**License caveat:** repository licenses were verified from official project pages during this research, but compatibility with EMPIRE’s distribution model and Wikipedia content obligations requires legal review.

---

## 6. Recommended target architecture

### Proposed end-to-end architecture

```text
SOURCE REGISTRY [EXTENSION]
  dataset manifest + checksums + license + year/dump + active state
       │
LANDING / LIBRARY
  D:\wiki_md\{year} + immutable reports (+ source dump identity)
       │
LOCATE
  SQLite pages/aliases ─────── roads: SQLite links
       │                         └─ optional Parquet/DuckDB projection after benchmark
       │
STRUCTURAL EXTRACT
  parser adapter → fields/tables/lists/scalars + raw evidence spans
       │
VALIDATE / NORMALIZE
  JSON Schema → semantic evidence verifier → deterministic normalizers
       │ non-ok                         │ ok
       └──── machine refusal            ▼
SERVE
  wiki_extract MCP structuredContent + bounded evidence envelope
       │
ANSWER GATE
  application permits Ollama only for validated `ok` records
       │ explicit remember only
       ▼
MEMORY
  wiki_remember → Cognee; wiki_recall labeled remembered-not-encyclopedia

CONTROL PLANE [EXTENSION]
  control.sqlite + JSONL logs + quality fixtures + run/artifact lineage

ARCHIVE/DR [EXTENSION]
  SQLite consistent snapshots + hashes + one backup repository + restore tests
```

### Database and storage choices

- **Authoritative content:** existing Markdown, read-only by runtime.
- **Authoritative existence:** existing SQLite `pages`/`aliases`.
- **Authoritative roads:** existing SQLite initially. If experiment 5 passes, physically separate or publish a versioned Parquet/DuckDB read projection; SQLite/report artifacts remain rebuild sources.
- **Request evidence:** JSON object validated against a locally bundled immutable schema.
- **Batch extracts:** JSONL first. Move to partitioned Parquet only when cross-page analytics or throughput justifies it.
- **Control metadata [EXTENSION]:** small independent SQLite database, not PocketBase and not the Title DNS file.
- **Memory:** Cognee only through a successful extract reference.

### Data layers and responsibilities

The layer table in §4 is normative for the proposed target. No layer may silently fall back across job boundaries: Weaviate cannot answer existence; Cognee cannot substitute for Wikipedia; Ollama cannot create missing records; analytics projections cannot become mutable authority.

### Source-management and governance model

Each active request pins `dataset_id`, `year`, `source_hash`, `title_index_version`, and `extractor_version`. Each output records `run_id`, schema/normalizer versions, evidence coordinates, and warnings. Quality failures quarantine the output; they do not trigger lead fallback.

A source owner approves activation and retirement. A source version becomes active only after counts, checksums, title/path tests, generic extraction fixtures, and backup classification pass. Superseded versions remain readable for the retention window and Truth Drift use.

### Data flow and lifecycle

1. Register source/dump metadata.
2. Land or identify immutable page/report artifacts.
3. Verify hash/count/path and build Title DNS/roads.
4. Run LOCATE regression suite.
5. Parse structures and emit raw evidence records.
6. Validate schema and source-derived semantics.
7. Normalize deterministically while retaining raw values.
8. Publish validated extract or explicit refusal.
9. Optionally persist batch extracts as a versioned projection.
10. Remember only an approved successful extract.
11. Supersede atomically; mark derived memories/projections stale rather than rewriting history.
12. Retire only after lineage, retention, and recovery checks.

### Security, access, backup, monitoring, and disaster recovery

**Security**

- Dedicated Windows service account; deny ordinary runtime writes to library and active indexes.
- Allowlist roots and resolve canonical paths to prevent traversal outside `D:\wiki_md` and approved report/state locations.
- Treat all page text and tool responses as untrusted data; never execute markup, links, templates, or embedded instructions.
- Validate MCP input/output, enforce payload size/time limits, log tool usage, and require explicit authorization for memory writes.
- Bundle schemas and dependencies offline; disable network `$ref` and unapproved runtime extension downloads.
- Store backup credentials outside repositories; restrict backup/VHDX access through OS ACLs. Avoid storing full user prompts unless required.

**Backup/DR [EXTENSION]**

- Classify: irreplaceable (code, schemas, manifests, fixtures, memory), rebuild-expensive (Title DNS, roads, control DB, extracts), re-downloadable (source dumps with checksums), ephemeral (cache/temp).
- Create consistent SQLite copies with the Online Backup API or `VACUUM INTO`, then run `quick_check`; the official Backup API is designed to snapshot a running database ([SQLite Backup API, updated 2025-11-13](https://www.sqlite.org/backup.html)). Do not copy only a live WAL main file.
- Back up completed snapshots with exactly one engine such as restic, verify the repository, and restore monthly to another directory.
- Test representative title/road/control queries after restore. Test Cognee/VHDX restore separately.
- **[A]** Architect must set RPO/RTO. Until then, no claim that the backup design is sufficient is valid.

**Monitoring [EXTENSION]**

Use JSONL plus a daily local health command before adding a stack. Required fields: timestamp, run ID, stage, dataset/artifact IDs, duration, counts in/out/rejected, typed error, code/extractor version. Alert/nonzero exit on stale required run, hash/count mismatch, SQLite check failure, stale backup verification, schema-invalid output, or any factual response on a refusal fixture.

---

## 7. Recommended open-source stack

### Essential now

| Tool/component | What it does | Why recommended and fit | Alternatives/limits |
|---|---|---|---|
| Existing Markdown/NTFS | Authoritative library | Already complete and offline; no migration evidence | ZIM only after I/O/recovery gate trips |
| SQLite | Title DNS and compact control metadata | Lowest complexity for local read-mostly point lookups; public domain | PostgreSQL only for demonstrated concurrency/service need |
| One parser adapter | Deterministic page structures | Directly attacks EXTRACT failures | `wikitextparser` if fidelity/license pass; `mwparserfromhell` + table adapter if permissive license is required; Parsoid only selectively |
| JSON Schema 2020-12 + Python `jsonschema` | Evidence envelope validation | Standard, local, language-neutral contract | Must be paired with custom semantic evidence verifier |
| Custom evidence verifier | Recomputes hashes/offsets and validates derivation | Prevents schema-valid fabrication | No off-the-shelf schema tool replaces it |
| MCP Python SDK | Typed resolve/extract/remember boundary | Matches report; local stdio possible | Direct function API remains useful for tests; MCP is not truth |
| Python/PowerShell + Task Scheduler | Jobs and health checks | No new service; Windows-native | Prefect after retry/backfill tripwire |
| Git + JSON manifests + control SQLite **[EXTENSION]** | Source, artifact, run, quality, lineage registry | Reproducibility without catalog sprawl | OpenLineage only with a real consumer |

### Optional after measured gates

| Tool | Add only when | Fit and alternative |
|---|---|---|
| Pandera | Extracts are handled as dataframes/batches and schema checks need code-native column/cross-field validation | Prefer over deploying a quality platform; Great Expectations or Soda Core are alternatives, not companions. |
| DuckDB + Parquet | Roads benchmark passes or cross-page extract analytics is required | Keep read projection immutable; no Title DNS migration. |
| restic | No equivalent encrypted, versioned, verifiable backup exists | Choose restic or Kopia, not both; benchmark seven-million-file scan and restore. |
| Prefect OSS | ≥5 dependent jobs, >2 manual recovery incidents/month, >60 min/week orchestration handling, or brittle backfills | Best documented Windows option among compared orchestrators; Dagster if asset lineage/partitions dominate. |
| Parsoid | Literal parser failures are specifically caused by template/Lua expansion and enough gold cases require fidelity | Operate only for selected pages or an offline expansion stage. |
| OpenLineage | Multiple languages/orchestrators need lineage interchange and an approved consumer exists | Continue control SQLite as local operational source. |
| GBNF/llama.cpp | Post-contract invalid output >0.5% or repeated tool calls >1% on ≥200 cases | Must halve residual without recall loss; semantic verifier remains mandatory. |
| SetFit | Rule intent accuracy <95% and true intent errors are ≥5% of failures | Require macro-F1 ≥0.97 and <50 ms p95 overhead. |
| ZIM/libzim | Markdown random H2 I/O >200 ms p95, >30% of end-to-end latency, or single-file operation is required | Require ≥3× p95 gain and provenance fidelity. |

### Explicitly not recommended now

OpenMetadata, DataHub, dbt, a second vector store, MongoDB, a graph server, ClickHouse, a time-series database, Iceberg/Delta/Hudi, Kubernetes, or multiple validation/orchestration tools. None addresses the present failure more directly than a parser, contract, and refusal gate.

---

## 8. Implementation roadmap

### Phase 0 — Source and acceptance clarification (2–3 days)

**Dependencies:** access to representative pages, their source/dump identity, current query code, and Architect SLO approval.

**Actions**

1. Inspect 50–100 pages across infobox, wikitable, list, scalar, template-generated, malformed, and empty cases.
2. Determine retained syntax, encoding, offsets, frontmatter, revision/dump metadata, and comparison source.
3. Freeze `Evidence JSON v1`, state machine, evidence coordinate rules, and generic 60-case gold set.
4. **[EXTENSION]** Define dataset/artifact/run IDs and a minimal manifest schema.

**Milestone:** signed source-fidelity note and schema.  
**Acceptance:** every fixture is classified as literal-parseable, expansion-required, already-lossy, or absent; no parser choice is made on an unknown representation.

### Phase 1 — Proof of concept (1 week)

**Actions**

1. Implement parser adapters for infobox fields, tables, lists, and section-scoped scalars without topic-specific rules.
2. Validate with JSON Schema and a semantic verifier; preserve raw and normalized values.
3. Implement application-level non-`ok` refusal before Ollama.
4. Produce stage metrics with Weaviate off.

**Risks:** parser licensing, discarded source semantics, merged-cell handling, normalization overreach.  
**Acceptance:** no raw `{|`; ≥0.90 F1 target on supported POC constructs, stop/reconsider below the report’s 0.80 floor after two bounded fixes; 100% provenance on successful records; zero factual output across at least 30 non-`ok` cases; p95 parser time ≤150 ms target and ≤500 ms hard stop after page read.

### Phase 2 — Initial production release (1–2 weeks)

**Dependencies:** Phase 1 acceptance and Eve integration access.

**Actions**

1. Implement typed `wiki_resolve`, `wiki_extract`, `wiki_remember`, and `wiki_recall` MCP tools plus direct test functions.
2. Enforce size/time/path/authorization limits and idempotent remember.
3. **[EXTENSION]** Add control SQLite, versioned manifests, JSONL run logs, and atomic version publication.
4. Run the generic suite end-to-end; retain lead/section read only as diagnostic output, never answer fallback.

**Milestone:** one year-scoped local release serving typed extracts.  
**Acceptance:** 100% schema-valid tool results; zero Cognee calls during resolve/extract; zero remembers for non-`ok`; duplicate remember rate zero; exact-title suite unchanged; unsupported-claim rate zero on refusal suite; p95 orchestration overhead ≤100 ms excluding read/model as the report proposes.

### Phase 3 — Hardening and recovery (1–2 weeks)

**Actions**

1. Expand to ≥200 stratified cases, including adversarial source text and ambiguous titles.
2. Add deterministic redirect completeness evaluation and error-book taxonomy.
3. **[EXTENSION]** Create consistent DB snapshots, hashes, backup classification, health command, and timed restore drill.
4. Pin dependency versions and hashes; generate an SBOM if EMPIRE is distributed.

**Acceptance:** quality results reproducible from pinned source/code; daily health detects seeded failures; restored SQLite passes integrity and representative queries; Cognee restore tested; approved RPO/RTO met or gap documented.

### Phase 4 — Performance decisions (only after baselines)

**Actions**

1. Benchmark SQLite roads versus representative Parquet/DuckDB using identical 10,000-subject workloads.
2. Benchmark cold/warm Markdown H2 reads on actual Windows volumes.
3. Measure orchestration effort and residual routing/grammar failures.

**Acceptance:** adopt only under existing report gates. DuckDB requires over-budget SQLite p95 plus ≥3× p95 improvement, exact parity, acceptable RAM, and reproducible one-way rebuild. ZIM, GBNF, and SetFit use the report’s stated gates. A graph engine requires a new Architect-approved experiment and cannot become existence authority.

### Phase 5 — Future scale

Potential triggers—not current recommendations:

- Multiple remote users/writers → evaluate PostgreSQL/service deployment.
- Frequent multi-engine analytical publication → evaluate a catalog/table format.
- Many heterogeneous sources and governance users → evaluate OpenMetadata/DataHub.
- Large job DAGs/backfills → evaluate Prefect or Dagster.
- Proven multi-hop road bottleneck → benchmark an embedded property graph.

Every trigger requires workload measurements, an operator, rollback, license review, and a clear system-of-record boundary.

---

## 9. Decision log

| Decision | Status | Alternatives rejected/deferred | Reason |
|---|---|---|---|
| Keep Markdown library | **Adopt** | ZIM now, document DB copy | No measured I/O failure; migration does not improve EXTRACT. |
| Keep SQLite phone book | **Adopt** | DuckDB/PostgreSQL/graph/vector existence | Exact lookup works; SQLite matches local low-writer point lookup. |
| Add deterministic extract boundary | **Adopt** | Lead dumping, topic regexes, model-only extraction | Directly addresses tables/infoboxes/lists and is testable. |
| Add schema + semantic validation | **Adopt** | Prompt-only obedience, GBNF now | Application enforcement can fail closed; grammar cannot prove evidence. |
| Use MCP for typed boundaries | **Adopt** | Cognee as universal front door | Preserves resolve/extract/remember separation. |
| Keep Cognee sparse | **Adopt** | Full-wiki Cognee/GraphRAG | Explicit report prohibition and wrong scale/job. |
| Benchmark DuckDB roads only | **Conditional** | Full SQLite migration, graph server | OLAP shape is plausible; adoption still requires report’s ≥3× gate. |
| Minimal source/run ledger **[EXTENSION]** | **Adopt experimentally** | DataHub/OpenMetadata/OpenLineage backend | Supplies lineage and quality with one embedded DB and manifests. |
| Task Scheduler first **[EXTENSION]** | **Adopt** | Prefect/Dagster now | Current job complexity has not justified a service. |
| restic if backup gap exists **[EXTENSION]** | **Conditional** | Kopia, raw live-file copy | Single executable, Windows, encryption/verification; app-consistent snapshots still required. |
| ZIM/GBNF/SetFit | **Defer** | Immediate adoption | Existing report gates are not met. |
| Graph/document/time-series/lakehouse/warehouse | **Reject now** | Category-specific tools | No current workload requires them; each adds a second truth or service. |

---

## 10. Open questions and information needed before implementation

1. Does `D:\wiki_md` contain original wikitext, rendered Markdown, or a hybrid? Which constructs and offsets survive conversion?
2. What exact Wikimedia dump/revision and content license correspond to each year? Are original dumps/checksums retained?
3. What are approved p50/p95/p99 budgets for title lookup, road ranking, page read, extraction, and end-to-end response—cold and warm?
4. Is EMPIRE distributed externally? If yes, what dependency-license policy applies to GPL-3.0 parser code and content attribution/share-alike?
5. What table semantics are in scope for v1: rowspan/colspan, sortable tables, nested templates, footnotes, hidden cells, generated tables?
6. What does “arbitrary needs” mean operationally: return all bounded structures, lexical `need_hint` ranking, or typed user-request schemas?
7. How are dates, units, ranges, citations, and repeated infobox keys normalized, and which transformations are reversible?
8. How many concurrent readers/writers exist, and do multiple processes currently touch SQLite/Cognee?
9. What are the actual current SQLite title/road latency distributions, cache settings, indexes, query plans, and lock waits?
10. What are the RPO/RTO, retention, storage budget, and approved backup destinations for Markdown, SQLite, Cognee/VHDX, and extracts?
11. Which data is sensitive: user prompts, scratchpad, memory, logs? What retention and deletion obligations apply?
12. Who owns source activation, schema changes, quality waivers, dependency upgrades, and retirement decisions?
13. Is the report’s 60-case suite already available, or must it be authored and reviewed from scratch?
14. What constitutes an acceptable refusal UX for unattended automation versus interactive chat?

Conclusions about parser selection, ZIM, DuckDB adoption, backup sufficiency, and licensing remain conditional until these questions are answered.

---

## 11. Sources and evidence

Primary sources were preferred. Access dates are 2026-09-15 unless a release/update date is stated.

1. **Supplied EMPIRE report — `EMPIRE_WIKI_STORAGE_RESEARCH_REPORT.md` (2026-09-15).** Primary authority for objectives, constraints, layer decisions, experiments, and gates.
2. [SQLite: Appropriate Uses](https://sqlite.org/whentouse.html) — updated 2025-05-31. Supports SQLite’s fit for device-local, low-writer-concurrency, sub-terabyte storage and the distinction from client/server databases.
3. [SQLite: Online Backup API](https://www.sqlite.org/backup.html) — updated 2025-11-13. Supports consistent snapshots of running databases and the recommended snapshot-before-repository-backup pattern.
4. [SQLite: Copyright/Public Domain](https://sqlite.org/copyright.html). Supports licensing statement.
5. [DuckDB: Concurrency](https://duckdb.org/docs/current/connect/concurrency). Supports one-process read-write and multiple-process read-only limitations.
6. [DuckDB: Reading and Writing Parquet](https://duckdb.org/docs/current/data/parquet/overview). Supports direct Parquet scans, multi-file reads, and projection/filter pushdown use.
7. [DuckDB repository](https://github.com/duckdb/duckdb) — official repository; research observed current 1.5.5 and MIT licensing. Supports maintenance/license assessment.
8. [Apache Parquet project](https://parquet.apache.org/). Supports Parquet as an interoperable open columnar format.
9. [wikitextparser repository](https://github.com/5j9/wikitextparser) — activity observed 2026-09-03; GPL-3.0. Supports parser capability/maintenance/license assessment.
10. [wikitextparser documentation](https://wikitextparser.readthedocs.io/en/latest/README.html). Supports template, table, section, and list API claims and known parser limitations.
11. [mwparserfromhell repository](https://github.com/earwig/mwparserfromhell) — activity observed 2026-07-28; MIT. Supports maintenance/license assessment.
12. [mwparserfromhell limitations](https://mwparserfromhell.readthedocs.io/en/latest/limitations.html). Supports the warning that offline AST parsing does not reproduce all MediaWiki semantics.
13. [Wikimedia Parsoid project](https://www.mediawiki.org/wiki/Parsoid). Supports Parsoid’s canonical wikitext/HTML role and heavier MediaWiki integration requirements.
14. [JSON Schema specification](https://json-schema.org/specification) — current published dialect 2020-12. Supports the contract format recommendation.
15. [Python `jsonschema` repository](https://github.com/python-jsonschema/jsonschema) — MIT; research observed v4.26.0 released 2026-01-07. Supports local Python validation implementation.
16. [MCP Tools specification](https://modelcontextprotocol.io/specification/2026-07-28/server/tools) — 2026-07-28. Supports typed input/output schemas, structured content, server input validation, and client result-validation guidance.
17. [MCP Python SDK repository](https://github.com/modelcontextprotocol/python-sdk) — MIT; research observed v2.2.0 released 2026-09-07. Supports Python implementation choice.
18. [Pandera repository](https://github.com/unionai-oss/pandera/) — activity observed 2026-09-14; MIT. Supports optional dataframe validation recommendation.
19. [OpenZIM ZIM format](https://openzim.org/wiki/ZIM_file_format) and [libzim repository](https://github.com/openzim/libzim) — active on 2026-09-15; GPL-2.0-or-later. Support ZIM’s offline indexed archive role and licensing caution.
20. [restic official site](https://restic.net/) — lists Windows support, single-executable operation, cryptography, verification, BSD-2-Clause, and 0.19.1 released 2026-07-05. Supports conditional backup recommendation.
21. [Prefect: Run on Windows](https://docs.prefect.io/v3/how-to-guides/self-hosted/server-windows). Supports first-class PowerShell, Windows paths, and UNC-path claims; it does not remove server/worker operational cost.
22. [OpenLineage project](https://openlineage.io/). Supports optional open lineage-event interoperability; no consumer is currently established for EMPIRE.
23. [OpenMetadata repository](https://github.com/open-metadata/OpenMetadata) and [DataHub documentation](https://docs.datahub.com/docs/quickstart). Support that both are active metadata platforms but require substantially more service infrastructure than the proposed local ledger.
24. [llama.cpp grammar documentation](https://github.com/ggml-org/llama.cpp/blob/master/grammars/README.md). Supports the distinction between syntactic constraint and evidence correctness; GBNF remains report-gated.
25. [Weaviate releases](https://github.com/weaviate/weaviate/releases). Supports active maintenance only; EMPIRE’s allowed Truth Drift scope comes from the supplied report, not from Weaviate documentation.

### Verification limitations

- Repository activity, release versions, and licenses were checked against official project pages during the research session. They can change; pin and re-verify before procurement or release.
- No EMPIRE runtime, source corpus, schema, benchmarks, query plans, or backup system was available to inspect. All performance and acceptance thresholds therefore come from the supplied report or are explicitly labeled assumptions/extensions.
- No legal conclusion is offered. Licenses are factual metadata; compatibility and content obligations require counsel.

---

## Prioritized recommendation

1. **First: validate source fidelity and implement `Evidence JSON v1` with deterministic extraction plus server-side refusal.** This directly addresses the reported failures and creates the measurement boundary every later decision needs.
2. **Second: add the typed MCP tools and a minimal manifest/control ledger.** This makes provenance, idempotency, lineage, and safe sparse remembrance enforceable without adding a platform.
3. **Third: benchmark—not migrate—the roads and library.** Move links to Parquet/DuckDB or pages to ZIM only if the existing report gates trip. Until then, another database would increase complexity without improving the desired result.
