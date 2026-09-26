# Wiki layer audit (measured 2026-09-26)

What this layer is, what it costs, and what is worth optimizing **for Eve specifically**.
Read this before touching anything under `pipeline/wiki_*`, `pipeline/weaviate_*`, or `D:\wiki_md`.

## 1. The corpus

| Fact | Value |
|---|---|
| Markdown corpus | `D:\wiki_md\2017` — **5,347,264 files, 20.41 GB** (~4 KB per file) |
| Producer | `pipeline/wiki_xml_convert.py` (376 lines) — MediaWiki `pages-articles` XML (`.bz2`) → Markdown with YAML frontmatter |
| Invocation | one-shot, human-run: `python -m pipeline.wiki_xml_convert --input …\enwiki-20170301-pages-articles.xml.bz2 --out-dir D:\wiki_md\2017 --snapshot-id 20170301` |
| Paths | `pipeline/wiki_ops_paths.py` — `DEFAULT_WIKI_MD_ROOT` (`WIKI_ROOT` env, default `D:\wiki_md`), reports `I:\EMPIRE_DATA\wiki-reports`, logs `I:\EMPIRE_DATA\logs` |

**`wiki_xml_convert.py` is not dead code.** A stem-based reference scan over the repo flags it as
the only unreferenced wiki module, because nothing imports it — it is the *recipe* that built 20 GB
of corpus. Deleting it deletes the ability to rebuild. If you are about to "clean up unreferenced
files", this is the one to leave alone (and the one that most looks like junk).

## 2. What Eve actually reads

`pipeline/wiki_read_lead.py` — after an entity/title match, she gets:

- lead capped at **1800 chars** (`DEFAULT_LEAD_MAX_CHARS`)
- one section capped at **1400 chars** (`DEFAULT_SECTION_MAX_CHARS`), chosen by `prefer_section_for_question`
- infobox noise stripped (`_strip_infobox_noise`), lookup via ripgrep

So her sustained read is **~3 KB per article** out of a 4 KB file in a 20 GB corpus. The corpus is
not the problem; *finding and opening* the right file among 5.3 M is.

## 3. Weaviate: do not optimize it

`pipeline/weaviate_export.py` documents the v2 archive at `D:\weaviate_v2_archive` as a raw binary DB
and its own job as a **one-time, read-only export** of `wikichunk` collections into Markdown staging,
which then flows through the normal ingest path (`wiki_ingest --export-dir …`). Its docstring states
Weaviate is shut down permanently. `scripts/start-weaviate.ps1` / `stop-weaviate.ps1` remain for the
migration window.

**Conclusion:** Weaviate is a source to drain, not a runtime dependency. Optimizing its structure buys
nothing; finishing the drain does.

## 4. Module census (34 wiki/weaviate modules)

33 of 34 are referenced by stem from code, scripts, or docs. The one exception is the converter above.
Largest: `wiki_scout.py` (1518), `wiki_interpreter.py` (1492), `wiki_title_dns.py` (1411),
`wiki_extract.py` (832), `wiki_ingest.py` (644), `web_scout.py` (486), `wiki_read_lead.py` (459).

Title resolution alone is spread across `wiki_title_dns.py`, `wiki_title_matcher.py`,
`wiki_titles_by_letter.py`, and `scripts/build-wiki-title-index.ps1` — four places to resolve one
title. That is the likeliest consolidation win, but **measure overlap before merging** (see §5).

## 5. What is worth doing, in order

1. **Lead/section sidecar index.** Precompute exactly what `wiki_read_lead` returns (~3 KB/article)
   into one indexed store so Eve's reads never open 5.3 M files. The corpus stays as the rebuild source.
2. **One title-resolution path** instead of four.
3. **Measure `wiki_extract` vs `wiki_scout` overlap** before rewriting either.

What is *not* worth doing: converting the corpus to another format for its own sake, or reviving
Weaviate. Both change storage without changing what Eve reads.

## 6. Method note

Overlap checks here compare normalised line sets (`len(line) > 25`, punctuation stripped). That is how
the routing pair was cleared: `agent/empire-routing.md` and `agent/skills/empire-routing-detail.md`
share **0** lines — the compact/detail split is deliberate (the compact file delegates to the loadable
skill), so merging them would *inflate* the always-on prompt. Same method applies to any "these two
look alike" instinct here.
