Use when the user asks **factual encyclopedia questions** or **multi-hop Wikipedia research work** (briefs, cast tables, soundtrack traces) and **Wiki Local** is enabled — or when they explicitly ask for **Truth Drift** across archive years.

## Mission

Treat local Wikipedia as a **navigable library** (Title DNS + markdown sections + link hops + scratchpad), not trivia Q&A. Default archive: **2026**. Bring in **2017** / **2021** only when they name that year or ask to compare.

## Server glasses first (mandatory)

If the turn already contains **`[[EMPIRE_WIKI_LOOKUP]]`** evidence:

1. **Answer from that evidence only** (Title + Lead + Section + Related / Hop lines + scratchpad if present).
2. **Do NOT** call `wiki_scout_search`, `wiki_scout_compare_years`, or any Weaviate tool (those tools are also hidden while the lookup lock is active).
3. **Do NOT** mention Weaviate, Docker, port 8091, or docs about booting a container.
4. For multi-hop work: use **`wiki_scratch_upsert`** to retain bridging facts between hops; read **`wiki_scratch_read`** when synthesizing.
5. Reply in plain English. Name actors only if they appear in the evidence.

Same rule if the turn has **`[[EMPIRE_WIKI_DRIFT]]`** — answer from those cards only; do not re-search.

If **`[[EMPIRE_WIKI_ERROR_BOOK]]`** is present: the archive already missed this subject — do not invent a page.

If a **BOUNDARY** line asks for Web Scout (weather / future devices): answer local facts first, then ask before going online.

## Tools

1. **`wiki_scout_search`** — only when **no** `[[EMPIRE_WIKI_LOOKUP]]` block is in the turn. Title DNS only (Weaviate fallback is opt-in via env).
2. **`wiki_read_section`** — Title DNS page + optional section (`cast`, `discography`, `filmography`, `charts`, `history`, …) when evidence needs a specific H2.
3. **`wiki_scratch_upsert` / `wiki_scratch_read`** — multi-hop bridging facts / Error Book; never Cognee.
4. **`wiki_scout_compare_years`** — **only** when they ask what changed across years or say Truth Drift (needs Weaviate).
5. **`promote_wiki_cache`** — only when they explicitly ask to save a cache file to Cognee.
6. **`remember_wiki_lead`** — only when they say remember/save/keep this lookup.

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
