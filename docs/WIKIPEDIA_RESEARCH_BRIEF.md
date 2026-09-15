# EMPIRE Wikipedia research brief

Local encyclopedia for Eve — what we built, what broke, what still needs research.  
Snapshot after Title DNS + link-web work (Sep 2026).

| Metric | Value |
|--------|--------|
| Title DNS pages | ~7.1 million |
| Title→title links | ~188 million |
| SQLite index | ~31 GB on `I:\EMPIRE_DATA\wiki-reports\2026\title-index.sqlite` |
| Markdown corpus | `D:\wiki_md\{year}` |

## North-star constraint

Do **not** dump full Wikipedia into Cognee. Cognee is for sparse “constellations” you explicitly remember. Wikipedia is a **library + phone book + roads** — not memory fuel.

## Current stack (intended roles)

| Layer | Role | Status |
|--------|------|--------|
| `D:\wiki_md\{year}` | Full article markdown + frontmatter `outgoing_links` (library) | Built for 2026 |
| Title DNS SQLite | Exact/alias existence: title → path (phone book) | Live — `I:\EMPIRE_DATA\wiki-reports\2026\title-index.sqlite` |
| Links table | Title → linked titles from `outgoing_links` (roads) | Live — ~188M edges; ranked + 1-hop lead injection |
| Weaviate `:8091` | Truth Drift / `compare_years` only (similarity across snapshots) | Opt-in; **not** required for who/what/cast |
| Cognee | Explicit remember of leads/primitives only | `remember_wiki_lead` tool; no bulk wiki ingest |
| Eve / Workbench | Inject `[[EMPIRE_WIKI_LOOKUP]]` before chat; Wiki Local toolbelt | DNS-first; model still sometimes calls tools anyway |

## Query path (freeway model)

Resolve title in DNS → optional ranked 1-hop neighbors → read lead from markdown → inject evidence. Cognee only when the Architect says remember / names a primitive / Truth Drift cluster.

| Piece | Meaning |
|--------|---------|
| **Phone book** | Exact title, aliases, programmatic suffixes like `(TV series)`, TV false-friend rejection (`Cult following` ≠ `The Following`) |
| **Roads** | Rank links by question intent (cast / song / cheddar). Open one neighbor lead when the landing page is not the answer (e.g. *Running Up That Hill*) |
| **Glasses** | Server injects mandatory evidence into Eve’s turn. Contract: answer only from evidence; no Weaviate boot speeches for simple facts |

## Difficulties encountered

| Problem | Symptom | Root cause |
|---------|---------|------------|
| Weaviate as existence gate | *The Following* → *Cult following* / no page | BM25/hybrid false friends; similarity ≠ “does the page exist?” |
| Endless routing patches | Each new phrasing needed another regex | Treating conversational NLP as the encyclopedia index |
| Song questions land on wrong page | *Music of Stranger Things* without “Running Up That Hill” | Alphabetical related titles; special-cased interpreter topics |
| Single-letter / quoted titles | `'V'` miss; `I'm interested…` broke lookup | Quote regex ate contractions; bare `V` hit letter page |
| Decade years | `1980s` treated as year `1980` | Year extractor matched `1980` inside `1980s` |
| Eve ignores injection | Slow fail → “boot Weaviate on 8091” | Skill still pushed `wiki_scout_search`; tool waited on dead Weaviate |
| Ambiguous follow-ups | 1984 vs miniseries → Weaviate again | Clarifications not mapped back onto last DNS candidates |
| VRAM / Deep model | 16 GB cannot hold Fast + Deep | 27B GSQ (~12 GB) is Deep-only; keep 8k ctx |

## Solutions tried (keep / drop)

| Approach | Verdict | Why |
|----------|---------|-----|
| Full Wikipedia → Cognee | **Rejected** | Scale, cost, and “what do I save?” paralysis; wrong job for graph memory |
| Weaviate hybrid for every lookup | **Narrowed** | Keep for Truth Drift only; bad existence gate |
| More regex / calibrate patches | **Partial** | Useful for triggers; not a substitute for title resolution |
| Title DNS SQLite | **Keep / expand** | Exact hit for *The Following*, *Stranger Things*, *V (1983 miniseries)* |
| Link web + question ranking + 1-hop | **Keep / refine** | Fixes song/cast/cheddar hops without embeddings |
| DNS-first `wiki_scout_search` | **Keep** | Even if Eve calls the tool, Weaviate need not be up |
| Session last-ambiguous follow-ups | **Keep / harden** | “the 1984 one” / “the miniseries?” after a fork |
| Qwen3.8 27B as Deep | **Optional** | Thinking quality; does not fix encyclopedia routing |

## Open research questions

Highest leverage unknowns (roadmap in [`WIKI_WORKBENCH_EVAL.md`](WIKI_WORKBENCH_EVAL.md) / Workbench plan):

1. **Multi-hop scratchpad quality** — Does Eve reliably upsert bridging facts during live briefs, or only when tools are forced?
2. **Full MediaWiki redirect SQL** — How much do dump-scale aliases beat curated `seed-common-aliases` on RedirectQA?
3. **ZIM / GBNF** — Deferred until section I/O or tool-lock kill criteria trip (see [`WIKI_SCOUT.md`](WIKI_SCOUT.md)).
4. **SetFit follow-ups** — Only if One-Letter Fork regresses after rule-based disambiguation.

## What “good” looks like

**Happy path (must work offline):** Who/what/cast with Wiki Local on, Weaviate off: sub-second Title DNS, correct page, answer from lead + ranked links, no Docker speech.

**Truth Drift only (opt-in):** Explicit compare 2017/2021/2026 → Weaviate. Never auto-promoted into Cognee; promote/remember is Architect-gated.

## Proven examples

| Ask | Expected landing |
|-----|------------------|
| Actors in *The Following* (TV) | *The Following* (exact) |
| 80s song / *Stranger Things* | Show + hop *Running Up That Hill* |
| Kate Bush revival song | *Kate Bush* + hop *Running Up That Hill* |
| 1980s miniseries `'V'` | *V (1983 miniseries)* |
| 1984 TV series `'V'` | *V (1984 TV series)* |
| Cheddar in cheese | *Cheese* + hop *Cheddar cheese* |

## Key paths

- `pipeline/wiki_title_dns.py` — Title DNS + links build/query  
- `pipeline/wiki_link_rank.py` — Question-ranked neighbors + hop selection  
- `frontend/wiki_drift_api.py` — Chat glasses / evidence injection  
- `docs/WIKI_SCOUT.md` — Ops and Weaviate opt-in  
- `docs/RESEARCH_CLOSURE.md` — Research phase boundaries  
- `I:\EMPIRE_DATA\wiki-reports\2026\` — Index + logs  
- Build links: `.\scripts\build-wiki-title-index.ps1` / `-Links`

## Related Cursor canvas

A live Canvas copy (not in git) may also exist at:

`C:\Users\m69nr\.cursor\projects\c-EMPIRE\canvases\wikipedia-research-brief.canvas.tsx`
