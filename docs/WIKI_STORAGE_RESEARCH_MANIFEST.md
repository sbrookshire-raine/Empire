# EMPIRE Wikipedia Storage Research Manifest

**Date:** 2026-09-15  
**Audience:** Outside research agents (Gumloop / Cursor / independent reviewers) and the Architect  
**Status:** Open research brief — discovery welcome **only** inside the constraints below  
**Repo:** https://github.com/sbrookshire-raine/Empire  
**Canonical local root:** `C:\EMPIRE`

---

## 0. Why this document exists

We keep circling the same wall:

- Title resolution (the “phone book”) largely **works**.
- Live answers for **basic data extracts** still **fail** or feel parametric.
- Each failed demo prompt tempts a **one-off patch** (cast tables, song hops, another regex). Those patches do not raise the ceiling for automation.
- Storage ideas keep resurfacing (“different DB,” “put it in Cognee,” “MCP in front”) without a clean map of **what each store already does** and **what has already been rejected**.

This manifest is the **single briefing packet** for an outside perspective. It lists every storage layer, what is broken, what was tried, hard constraints, and a **specific request list** of experiments / recommendations we want back.

**Do not** treat celebrity trivia or cast lists as the product. They were only probes.

---

## 1. Desired end result (Architect north star)

Eve (and later unattended automation) must be able to:

1. **Locate** the right local Wikipedia page offline (exact entity resolution).
2. **Extract** usable structured facts from that page for *arbitrary* needs — dates, numbers, tables, lists, named fields — not one genre of question.
3. **Answer or refuse** from that extract (citeable, year-scoped). Empty extract ⇒ fail closed; **do not invent**.
4. Optionally **remember** a small constellation into Cognee after a successful extract — never the whole encyclopedia.

**Success looks like:** “Pull release dates / population / table rows / section lists from local wiki without Weaviate, without rewriting prompts per question type, without dumping 7M pages into graph memory.”

**Failure looks like:** Lead dumps, invented cast names, “boot Weaviate” speeches, regex limbs per demo, or “just put Wikipedia in Cognee.”

Stack constraints (immutable for this research):

- Local-first: Windows 11, Ollama, no paid cloud LLM in app code.
- Frontend: HTMX/Alpine only (no React/SPA for core UI).
- Cognee = sparse explicit memory only.
- Weaviate = Truth Drift / year compare only (not chat existence).

---

## 2. Inventory — every storage / DB / corpus layer

Think in metaphors used in-repo: **library** (text), **phone book** (title → path), **roads** (title → title links), **glasses** (server injects evidence), **memory** (Cognee constellations).

| # | Layer | Concrete path / endpoint | Engine / format | Approx scale | Intended job | Status |
|---|--------|--------------------------|-----------------|--------------|--------------|--------|
| 1 | Markdown library | `D:\wiki_md\{year}\` (`WIKI_ROOT`) | Millions of `.md` files + YAML frontmatter (`outgoing_links`) | 2017 ~5.35M; 2021 ~6.3M; 2026 ~**7.1M** pages | Full article body for lead/section/extract | Built (2026 primary) |
| 2 | Title DNS (phone book) | `I:\EMPIRE_DATA\wiki-reports\{year}\title-index.sqlite` | **SQLite** tables `pages`, `aliases`, (+ indexes) | ~**31 GB** (2026); ~7.1M titles | Exact / alias existence → filesystem path | **Live — keep** |
| 3 | Link web (roads) | **Same** SQLite file, table `links` (+ `link_progress`) | SQLite edge list `(from_norm, to_norm, to_title)` | ~**188 million** edges | 1-hop neighbors; question-intent ranking | **Live — awkward fit** |
| 4 | Wiki reports / catalogs | `I:\EMPIRE_DATA\wiki-reports\{year}\` | JSONL/JSON/TSV | Supporting | `titles.jsonl`, status, redirects.tsv, disambig TSV, logs | Live |
| 5 | Remembered-title ledger | `…\remembered-titles.jsonl` | JSONL | Small | Skip duplicate `remember_wiki_lead` | Live |
| 6 | Weaviate archive | `I:\weaviate_v2_archive\weaviate` (legacy `D:\…`); API `http://127.0.0.1:8091` | **Weaviate** WikiChunk collections (nomic-encoded; vectorizer none in container) | Multi-year chunks | **Truth Drift / `compare_years` only** | Opt-in Docker; **not** chat gate |
| 7 | Weaviate staging export | `I:\EMPIRE_DATA\weaviate_dump\` | Markdown export | Partial | Historical heist/export | Pilot / stopped |
| 8 | wiki_cache | `C:\Empire_Workbench\04_Thought_Experiments\wiki_cache\` | Markdown triage files | Small | Scout/compare learn-from cache before promote | Live |
| 9 | Scratchpad | `C:\Empire_Workbench\04_Thought_Experiments\wiki_scratch\{session}.json` | JSON | Per session | Multi-hop bridging facts (**not** Cognee) | Live |
| 10 | Error Book | `%LOCALAPPDATA%\EMPIRE\wiki-error-book.jsonl` | JSONL | Small | Persistent miss log | Live |
| 11 | LOOKUP lock | `%LOCALAPPDATA%\EMPIRE\eve-wiki-lookup-lock.json` | JSON | Tiny | Hide scout tools when glasses inject LOOKUP | Live |
| 12 | Ingest ops control | `%LOCALAPPDATA%\EMPIRE\wiki-checkpoint.json`, `priority_subjects.json`, `wiki-abort.flag` | JSON | Tiny | Overnight resume / Wiki Ops | Historical for full Cognee dump |
| 13 | Cognee graph memory | `V:\Cognee` on VHDX `I:\EMPIRE_VHDX\empire_cognee.vhdx` (NTFS) | Cognee 1.x + Docker **Postgres** `:5432` | Grows with remembers | Sparse constellations (`eve_memory`, `truth_drift`, primitives) | Live for explicit remember only |
| 14 | Cognee lock | `%LOCALAPPDATA%\EMPIRE\cognee.lock` | File lock | — | Serialize MCP + CLI Cognee access | Live |
| 15 | PocketBase | `http://127.0.0.1:8090` | SQLite app DB | App scale | Tasks / jobs; wiki `source_type` logging only — **not** Title DNS | Live; wiki priorities stay file-based |
| 16 | Ollama | `http://localhost:11434` | Local LLM + `nomic-embed-text` | GPU/VRAM limited (16 GB class) | Chat synthesis + Weaviate query embeds | Live |

**There is no `wiki_extract` module yet.** Extract today ≈ read lead / H2 section as prose (or raw wikitable markup), inject into chat.

### Schema sketch (Title DNS SQLite)

Defined in `pipeline/wiki_title_dns.py`:

- `pages(title, title_norm, path, …)` — canonical titles → markdown path  
- `aliases(alias_norm → title)` — redirects / curated / parenthetical seeds  
- `links(from_norm, to_norm, to_title)` — roads  
- `link_progress` — resumable link build  

Build: `.\scripts\build-wiki-title-index.ps1` and `-Links`.

### MCP / tool front door (already exists; incomplete for extracts)

| Server | File | Notable tools |
|--------|------|----------------|
| `empire-wiki-scout` | `mcp/wiki_scout_mcp.py` | `wiki_scout_search`, `wiki_scout_compare_years`, `wiki_read_section`, `remember_wiki_lead`, `promote_wiki_cache`, scratchpad tools |
| `empire-wiki` | `mcp/wiki_mcp.py` | Ingest/export/status — **overnight Cognee dump halted** |
| `empire-cognee` | `mcp/cognee_mcp.py` | `cognee_remember` / `recall` / `improve` / `forget` |

Eve mirrors live under `agents/empire-task-agent/agent/tools/`. Chat glasses: `frontend/wiki_drift_api.py`.

---

## 3. Intended happy path (as designed today)

```text
User ask (Wiki Local ON, Weaviate OFF)
  → Title DNS resolve (SQLite pages/aliases)
  → optional rank 1-hop links (same SQLite) by question heuristics
  → read lead / preferred H2 from D:\wiki_md
  → Workbench injects [[EMPIRE_WIKI_LOOKUP]] + LOOKUP lock
  → Eve answers ONLY from evidence
  → optional remember_wiki_lead → Cognee (Architect/tool gated)
```

Truth Drift fork: boot Weaviate → compare years → `wiki_cache` → optional promote to dataset `truth_drift`.

**Cognee is not on the read path for encyclopedia existence.**

---

## 4. What is failing (symptoms → diagnosis)

### 4.1 Product / automation failures (current pain)

| Symptom | What we think is wrong | Why “another DB for titles” may not fix it |
|---------|------------------------|--------------------------------------------|
| Section returns `{|` wikitable junk | **Tables are not prose**; no general table→rows extractor | Phone book already found the page |
| Eve pastes long lead / ignores hops | **Lead dump ≠ extract**; wrong default injection for “pull X” | Resolve worked; synthesis/contract failed |
| Invented names / facts when section empty | **Empty extract does not fail closed**; parametric fill | Memory DB won’t stop invention |
| Per-demo regex / cast-only patches | Optimizing for **one question shape** | Ceiling unchanged for next ask genre |
| Feeling of going in circles | Mixing **locate** problems with **extract** and **store** problems | Need substrate clarity (this doc) |

### 4.2 Historical / still-relevant infrastructure failures

Documented in `docs/WIKIPEDIA_RESEARCH_BRIEF.md` and `docs/WIKI_SCOUT.md`:

| Problem | Symptom | Root cause |
|---------|---------|------------|
| Weaviate as existence gate | *The Following* → *Cult following* | Similarity ≠ ontological existence |
| Endless routing patches | New phrasing → new regex | Conversational NLP treated as the index |
| Wrong landing / weak hops | Song Q without *Running Up That Hill* | Alphabetical related titles; intent ranking incomplete |
| Quote / letter titles | `'V'`, contractions broken | Parser edges (partially mitigated) |
| Decade years | `1980s` → `1980` | Year extractor |
| Eve ignores injection | “Boot Weaviate on 8091” | Tool skill + dead Weaviate wait |
| Ambiguous follow-ups | 1984 vs miniseries | Session disambiguation incomplete |
| VRAM | Can’t hold Fast + Deep | Hardware bound |
| Millions of MD files | FS overhead for random section I/O | Motivates ZIM *later* — kill-criteria gated |
| Links in SQLite | Large edge scans / rank may be slow or clumsy | OLTP engine holding OLAP-shaped graph |
| Cognee on wrong FS | Corrupt / broken if not NTFS VHDX | Operational; solved via `V:\Cognee` |

`docs/RESEARCH_CLOSURE.md` (2026-09-10) already stated: what actually failed for grounding was often **parametric override, fat injection, Truth Drift hijack — not retrieval**. That diagnosis still applies to live extract demos.

---

## 5. What has been tried (verdict table)

| Approach | Verdict | Evidence / reason | Revisit? |
|----------|---------|-------------------|----------|
| Full Wikipedia → Cognee overnight ingest | **Rejected / halted** | Scale, cost, “what do I save?”, wrong job for graph memory | **No** as bulk dump |
| Weaviate hybrid for every chat lookup | **Narrowed** | False friends; keep Truth Drift only | Only with `EMPIRE_WIKI_WEAVIATE_FALLBACK=1` after miss |
| Second vector DB / Kiwix as primary retrieval | **No** | Research closure | Steal contracts only if useful |
| Full GraphRAG / embed-all wiki | **Never** for this corpus | Construction wall at scale | **No** |
| Title DNS SQLite phone book | **Keep** | Exact hits proven (*The Following*, *V (1983…)*, etc.) | Expand aliases/redirects SQL |
| Link web in same SQLite + heuristic rank | **Keep / refine** | Works without embeddings; may be wrong *engine* for analytics | DuckDB spike if bottleneck proven |
| DNS-first `wiki_scout_search` | **Keep** | Weaviate need not be up | — |
| Server glasses + LOOKUP lock | **Keep / harden** | Stops some tool loops; model still can ignore contract | Contract + extract payload |
| Regex / calibrate / interpreter topics | **Partial** | Useful triggers; not encyclopedia index | Stop genre-specific limbs |
| `remember_wiki_lead` → Cognee | **Keep (sparse)** | Lead-only constellation | Extend to **structured extracts** |
| Qwen larger Deep model | **Optional** | Thinking; does **not** fix routing/extract | Not a storage fix |
| DuckDB for link analytics | **Researched, not built** | Kill criterion in `WIKI_SCOUT.md` | **Yes — candidate experiment** |
| ZIM / openzim-mcp | **Deferred** | Kill: section I/O too slow or single-file need | Only if I/O proven |
| GBNF / schema masks | **Deferred** | Kill: tool loops after lock+scratchpad | Later |
| SetFit intent router | **Deferred** | Kill: One-Letter Fork still fails after rules | Later |
| Cast-specific / song-primary patches | **Rejected as strategy** | Architect: don’t whack-a-mole question types | General extract instead |
| PocketBase as wiki priority/title DB | **Deferred / not chosen** | File-based priorities; PB for app tasks | Unlikely |

---

## 6. Concerns (Architect + systems)

1. **Wrong problem framing** — Replacing SQLite titles with Cognee or another “smart” DB will not parse wikitables or stop invention.
2. **Cognee misuse** — Using graph memory as an encyclopedia recreates the halted overnight ingest (VRAM, time, “what to save,” lock contention on `V:`).
3. **One file, two jobs** — 31 GB SQLite doing both point lookups and 188M-edge analytics is a known mismatch (OLTP vs OLAP); changing *without* measurement wastes rebuild days.
4. **Whack-a-mole evals** — Cast/Englund/RUTH-style live tests train the system on trivia, not automation extracts.
5. **Injection vs obedience** — Headless injection can pass while live Eve still synthesizes from weights.
6. **Dual-write / migration cost** — Rebuilding links into DuckDB/Parquet is multi-hour/day work; needs kill criteria and a rollback story.
7. **VRAM / model size** — Storage research must not assume a second 27B always resident.
8. **Going in circles** — Research agents must return **ranked experiments with pass/fail metrics**, not another architecture essay that re-proposes full-wiki RAG.

---

## 7. Hard constraints for outside researchers

**Allowed**

- Recommend alternate **local** stores for *specific* layers (e.g. roads vs phone book vs article blob).
- Propose MCP tool shapes for `resolve` / `extract` / `remember`.
- Propose deterministic parsers (wikitext AST, Rust parsers, table libraries).
- Propose eval suites for **generic extracts** (dates, numbers, tables, lists).
- Compare SQLite vs DuckDB vs Parquet vs graph DBs vs ZIM **with workload math** (point lookup vs multi-hop scan vs random section read).

**Forbidden / already closed**

- Full corpus → Cognee / GraphRAG / “embed all of Wikipedia.”
- Replacing Title DNS existence checks with dense/hybrid search as the primary gate.
- Cloud BaaS, paid LLM APIs in the runtime path.
- React/Next for core EMPIRE UI.
- “Just use a bigger model” as the storage fix.

**Must map recommendations to layers 1–16 above** (or explicitly propose a new layer with a single job).

---

## 8. Requested deliverables (what we want back)

Outside agents (Gumloop et al.) should return a report with **these exact sections**:

### A. Layer verdict matrix

For each of layers 1–16 (or your merge/split of them): **Keep / Replace / Split / Delete**, one sentence why, risk if wrong.

### B. Ranked experiment list (max 8)

Each experiment must include:

| Field | Required |
|-------|----------|
| Name | Short |
| Hypothesis | Falsifiable |
| Touches layers | Numbers from §2 |
| Effort | S / M / L (hours–days, honest) |
| Prerequisite data | e.g. export `links` to Parquet |
| Metric | How we know it worked (latency p95, extract F1 on N pages, Eve invent rate = 0 on empty, etc.) |
| Kill criterion | When to stop |
| Does **not** solve | Explicit non-claims |

Prioritize experiments that move **generic structured extract for automation**, not trivia accuracy.

### C. Explicit answers to Architect questions

1. Is “put phone book + links in a different DB” likely to fix **extract** failures, or only **hop ranking / scan** performance?  
2. Is “MCP as frontend to Cognee” sound if Cognee only stores **post-extract constellations**? What MCP tool contract?  
3. What is the smallest change that unlocks **table/infobox → fields** without a new NLP router?  
4. Which deferred tech (DuckDB, ZIM, GBNF, SetFit) should move **now** vs stay gated — with evidence?  
5. What would an outside team **not** try that EMPIRE keeps re-discussing?

### D. Anti-circle checklist

List 5 proposals that **sound** like progress but recycle rejected paths (with one-line “already tried” pointer).

### E. Optional: reference architectures

Cite offline encyclopedia / agent systems (Kiwix, MediaWiki replicas, SQLite FTS, DuckDB graphs, ZIM+MCP, etc.) **only** with how they map onto EMPIRE’s library/phone book/roads/memory split.

---

## 9. Seed list of experiments we already suspect (challenge or confirm)

Researchers may reorder, kill, or replace these — but must address them:

1. **General wikitable + infobox extractor** (deterministic) → `EXTRACT` JSON + short prose; inject `[[EMPIRE_WIKI_EXTRACT]]` instead of lead dump.  
2. **Fail-closed contract** when extract empty (no parametric fill).  
3. **DuckDB (or Parquet+DuckDB) spike for `links` only**; keep SQLite for `pages`/`aliases`; measure neighbor+rank latency vs SQLite.  
4. **MCP `wiki_extract(subject, need_hint, year)`** wrapping DNS → read → extract; Eve tool mirror.  
5. **Remember path**: promote successful *structured* extracts to Cognee (`eve_memory`), not full pages.  
6. **Eval suite**: 5–8 generic extract cases (population, release dates, table N rows, section list items, miss→refuse) with Weaviate off — retire cast-trivia as north star.  
7. **MediaWiki redirect SQL import** completeness vs curated aliases (RedirectQA delta).  
8. **Section I/O benchmark** on `D:\wiki_md` random H2 reads → only then consider ZIM.

---

## 10. Key code & doc pointers (do not rediscover blindly)

| Path | Why |
|------|-----|
| `docs/WIKIPEDIA_RESEARCH_BRIEF.md` | Metrics, tried/dropped, freeway model |
| `docs/WIKI_SCOUT.md` | Ops, Weaviate opt-in, **deferred kill criteria** |
| `docs/RESEARCH_CLOSURE.md` | Discovery closed; parametric failure diagnosis |
| `docs/WIKI_WORKBENCH_EVAL.md` | Offline workbench eval rules |
| `docs/WIKI_INGEST_OVERNIGHT.md` | Halted full ingest layout |
| `docs/COGNEE_VHDX.md` | Why Cognee lives on `V:` |
| `Local Wikipedia Agent Architecture.md` | External research synthesis (SQLite vs DuckDB, ZIM, SetFit) — **proposals, not as-built** |
| `pipeline/wiki_title_dns.py` | Phone book + links build/query |
| `pipeline/wiki_link_rank.py` | Neighbor ranking |
| `pipeline/wiki_read_lead.py` | Lead/section read |
| `frontend/wiki_drift_api.py` | Glasses injection |
| `mcp/wiki_scout_mcp.py` | MCP front door today |
| `data/eval/wiki_workbench.jsonl` | Current workbench cases |

---

## 11. Copy-paste prompt for Gumloop (or any outside research agent)

Paste everything between the fences as the agent system/user research prompt. Attach this file (`docs/WIKI_STORAGE_RESEARCH_MANIFEST.md`) as the primary context document if the tool allows file upload.

````text
You are an independent systems researcher. You are NOT the EMPIRE build agent.
Your job is to break a circular debate about local Wikipedia storage and retrieval.

Read and obey the attached document:
  EMPIRE docs/WIKI_STORAGE_RESEARCH_MANIFEST.md
(If not attached, treat the following as binding: Wikipedia is a library + phone book + roads;
Cognee is sparse memory only; Weaviate is Truth Drift only; full wiki→Cognee and embed-all
are FORBIDDEN; the product goal is generic structured DATA EXTRACTS for automation, not cast trivia.)

Context in one paragraph:
EMPIRE already has ~7.1M markdown pages on D:\wiki_md, a ~31GB SQLite Title DNS
(title→path) plus ~188M links in the SAME SQLite, optional Weaviate on :8091 for year
compare, and Cognee on a VHDX for explicit remembers. Exact title lookup mostly works.
Live failures are: raw wikitables injected as junk, lead dumps instead of extracts,
model invention when evidence is empty, and temptation to patch per question type.
The Architect wonders whether a different DB for the phone book/links, or MCP as a
frontend to Cognee, would help — but does not want another loop of rejected ideas.

Deliverables (mandatory structure):
A) Layer verdict matrix for every storage layer in the manifest (Keep/Replace/Split/Delete).
B) At most 8 ranked experiments, each with hypothesis, layers touched, effort S/M/L,
   metrics, kill criterion, and explicit non-claims.
C) Direct answers to the five Architect questions in §8.C of the manifest.
D) Anti-circle checklist: 5 ideas that sound new but recycle rejected work.
E) Optional reference architectures mapped onto library / phone book / roads / memory.

Rules:
- Prefer falsifiable experiments over architecture essays.
- Distinguish LOCATE vs EXTRACT vs REMEMBER failures; do not conflate them.
- Do not recommend full Wikipedia into Cognee, GraphRAG-over-all, or Weaviate as the
  primary existence gate.
- Do not optimize for “who was in the cast” demos; optimize for reusable extract pipelines.
- If recommending DuckDB, ZIM, SetFit, or GBNF, say whether EMPIRE’s existing kill
  criteria are already met or not, and what measurement would trip them.
- Be concrete about Windows-local, offline-friendly tooling.

Output: a single markdown report. Start with a 10-line executive verdict.
End with a “Do this next week” list of ≤3 actions ordered by leverage.
````

---

## 12. How EMPIRE will use the Gumloop output

1. Architect reviews the ranked experiments against this manifest’s constraints.  
2. Build agent implements only items that survive kill criteria and do not reopen rejected paths.  
3. Eval gate: generic extract suite (Weaviate off) before any further storage migration of the phone book.  
4. Update this manifest’s §5 verdict table when an experiment ships or dies.

---

## 13. One-sentence summary

**Keep the phone book; stop dumping leads; build general extracts; optionally speed the roads with an analytics DB; use MCP to resolve/extract and Cognee only to remember the small results — and demand outside research return measurable experiments, not another circle.**
