---
area: wiki-archive
one_line: Local Wikipedia work — lookup, title hops, sections, extracts, truth drift, lead memory.
tools: wiki_scout_search, wiki_resolve, wiki_read_section, wiki_extract, wiki_scout_compare_years, remember_wiki_lead, wiki_remember, promote_wiki_cache, wiki_scratch_upsert, wiki_scratch_read
skills: skill-wiki-scout
---

# Local Wikipedia archive — worked pathways

The archive is a **phone book of exact titles** (7.1M pages, snapshot 2026 default; 2017/2021 exist).
Search the **bare title**, never the question; hop in the same turn when the lead lacks the fact.
A miss is logged automatically (Error Book) and comes back as `known_miss`.

## Local Wikipedia lookup
Use when: who/what/when questions, cast lists, briefs, "tell me about X" where X is a thing.

- **Ask:** "who were the white stripes?" → **Do:** `wiki_scout_search("The White Stripes")` → **Get:** the lead answer ("American rock duo formed in Detroit, Michigan, in 1997…") with the page named.
- **Ask:** "what is a drum kit made of?" → **Do:** `wiki_scout_search("Drum kit")` → **Get:** the components list straight from the lead.
- **Ask:** "how can I learn drums using the rules of juggling?" → **Do:** `wiki_scout_search("Juggling")` **and** `("Drum kit")` in the same turn → **Get:** two grounded leads to map between (never answer this from memory).
- **Ask:** "tell me about magnetism" → **Do:** `wiki_scout_search("Magnet")` → **Get:** the physics lead, not the band.
- **Ask:** "does the archive cover X?" → **Do:** `wiki_scout_search("<bare title>")`; if `ok=false`, retry once with the noun only → **Get:** either the card, or an honest "no page titled X" (the miss is already logged).

## Sections and extracts (the hop)
Use when: the asked fact is not in the lead — a table row, a date, a track listing, a number.

- **Ask:** "which album has Seven Nation Army?" → **Do:** `wiki_scout_search("The White Stripes")` → `wiki_read_section("Elephant")` → **Get:** the track answer from the album page.
- **Ask:** "what were the TV ratings for The Following?" → **Do:** `wiki_scout_search("The Following")` → `wiki_extract(need_hint="ratings table")` → **Get:** the table rows (or `state=empty` → refuse, do not invent).
- **Ask:** "how many episodes did season 2 have?" → **Do:** `wiki_read_section("The Following", section="Episodes")` → **Get:** the count with its table.
- **Ask:** "what did this article say about the cast?" → **Do:** `wiki_extract(title, need_hint="cast")` → **Get:** only the names that are literally present.
- **Ask:** "give me the specs from the PS2 page" → **Do:** `wiki_extract("PlayStation 2", need_hint="specifications")` → **Get:** the specs table; unsupported state ⇒ say so.

## Title resolution and ambiguity
Use when: the name could be several things, or the bare word has no page of its own.

- **Ask:** "magnetism" → **Do:** `wiki_resolve("Magnetism")` then `wiki_scout_search("Magnet")` → **Get:** the right reading named before answering (the band `The Magnets` is a different page).
- **Ask:** "the white stripes album" → **Do:** `wiki_resolve("White Blood Cells")` → **Get:** the exact page for the album rather than the band.
- **Ask:** "DRUMS" → **Do:** `wiki_resolve("DRUMS")` → **Get:** a disambiguation/spacecraft page, so say the archive reads it differently and try `Drum kit`.
- **Ask:** "series" → **Do:** `wiki_resolve("Series")` → **Get:** the disambiguation reading, then pick with the Architect instead of guessing.

## Truth drift across snapshots
Use when: they name a year (2017/2021/2026) or ask what changed.

- **Ask:** "how did the Stranger Things page change between 2017 and 2026?" → **Do:** `wiki_scout_compare_years("Stranger Things")` → **Get:** the side-by-side drift (needs Wiki Local/Weaviate up).
- **Ask:** "what did the 2017 archive say about X?" → **Do:** `wiki_scout_compare_years("X", years=["2017"])` → **Get:** that snapshot's wording only.
- **Ask:** "compare the cast tables" → **Do:** `wiki_extract` on both years then compare → **Get:** the diff, with both years labelled.

## Keeping what you found
Use when: a lead should survive the turn (bridging fact, or fuel for later recall).

- **Ask:** "remember that the archive says X" → **Do:** `remember_wiki_lead(title, text)` → **Get:** a cached lead under the workbench wiki_cache.
- **Ask:** "keep this in memory" → **Do:** `propose_remember(...)` then `confirm_remember(...)` **only after the Architect agrees** → **Get:** a Cognee entry (never auto-promote).
- **Ask:** "save this for the next hop" → **Do:** `wiki_scratch_upsert(text, session_id=...)` → **Get:** a scratchpad note; `wiki_scratch_read(include_errors=True)` reads it back with the Error Book.
- **Ask:** "what did we already try?" → **Do:** `wiki_scratch_read(session_id, include_errors=True)` → **Get:** prior bridging facts + logged misses (do not re-search a logged dead end blind).
- **Ask:** "keep that album table for later" → **Do:** `wiki_extract("Elephant", need_hint="studio albums")`, then `wiki_remember("Elephant", need_hint="studio albums")` → **Get:** the extract itself in Cognee — an extract is only stored when he explicitly asks (empty extracts are refused; `wiki_md` is never bulk-ingested).
- **Ask:** "promote this page to memory" → **Do:** `promote_wiki_cache(path, dataset="eve_memory")` → **Get:** the cached markdown ingested for recall.
