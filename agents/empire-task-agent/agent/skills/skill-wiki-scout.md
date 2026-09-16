Use when the user asks **factual encyclopedia questions** or **multi-hop Wikipedia research work** (briefs, cast tables, soundtrack traces) and **Wiki Local** is enabled — or when they explicitly ask for **Truth Drift** across archive years.

## Mission

Treat local Wikipedia as a **navigable library** (Title DNS + markdown sections + link hops + scratchpad), not trivia Q&A. Default archive: **2026**. Bring in **2017** / **2021** only when they name that year or ask to compare.

## Server glasses first (mandatory)

If the turn already contains **`[[EMPIRE_WIKI_LOOKUP]]`** or **`[[EMPIRE_WIKI_EXTRACT]]`** evidence:

1. **Answer from that evidence only** (Title + Lead/EXTRACT fields/tables/lists + Related / Hop lines + scratchpad if present).
2. **Do NOT** call `wiki_scout_search`, `wiki_scout_compare_years`, `wiki_scratch_read`, or any Weaviate tool.
3. **Do NOT** invent numbers, dates, cast names, or table cells missing from EXTRACT. If EXTRACT state is empty/unsupported, refuse clearly.
4. **Do NOT** narrate “the scratchpad is empty” — that is normal for a single-page extract. Answer the user’s extract request from EXTRACT.
5. **Do NOT** mention Weaviate, Docker, port 8091, or docs about booting a container.
6. For multi-hop work across turns: use **`wiki_scratch_upsert`** to retain bridging facts; only **`wiki_scratch_read`** when synthesizing and no EXTRACT/LOOKUP block is present.
7. Reply in plain English. Name actors only if they appear in the evidence.

Same rule if the turn has **`[[EMPIRE_WIKI_DRIFT]]`** — answer from those cards only; do not re-search.

If **`[[EMPIRE_WIKI_ERROR_BOOK]]`** is present: the archive already missed this subject — do not invent a page.

If a **BOUNDARY** line asks for Web Scout (weather / future devices): answer local facts first, then ask before going online.

## Tools

1. **`wiki_scout_search`** — only when **no** LOOKUP/EXTRACT block is in the turn. Title DNS only (Weaviate fallback is opt-in via env).
2. **`wiki_extract`** — structured fields/tables/lists for dates, numbers, specs, table rows. Prefer when the user wants data extracts.
3. **`wiki_resolve`** — phone book only (exact/alias/ambiguous/missing).
4. **`wiki_read_section`** — Title DNS page + optional section when a named H2 is needed.
5. **`wiki_scratch_upsert` / `wiki_scratch_read`** — multi-hop bridging facts / Error Book; never Cognee.
6. **`wiki_scout_compare_years`** — **only** when they ask what changed across years or say Truth Drift (needs Weaviate).
7. **`promote_wiki_cache`** — only when they explicitly ask to save a cache file to Cognee.
8. **`wiki_remember`** / **`remember_wiki_lead`** — only when they say remember/save/keep; `wiki_remember` rejects non-ok extracts.

## Simple questions

1. Prefer injected Title DNS evidence when present.
2. If you must call a tool and there is **no** injection: **`wiki_scout_search`** once with default **2026**.
3. If Title DNS is ambiguous, ask which title — do not invent.

## Multi-hop work

Examples: Casting Hop, Soundtrack Trace, Timeline Brief, Cast Table Merge.

1. Land via Title DNS / LOOKUP injection.
2. Prefer Cast / Discography / Filmography / Charts sections in evidence.
3. Upsert bridging facts to the scratchpad between hops.
4. Synthesize only from evidence + scratchpad.

## Truth Drift (only when asked)

Call **`wiki_scout_compare_years`** when they explicitly want 2017 / 2021 / 2026 compared.

## When a lookup fails

Say the local archive has no usable page. Offer a clearer title. Do not invent. Do not suggest Weaviate.
