Use when the user asks **factual encyclopedia questions** or **multi-hop Wikipedia research work** (briefs, cast tables, soundtrack traces) and **Wiki Local** is enabled — or when they explicitly ask for **Truth Drift** across archive years.

## Mission

Treat local Wikipedia as a **navigable library** (Title DNS + markdown sections + link hops + scratchpad), not trivia Q&A. Default archive: **2026**. Bring in **2017** / **2021** only when they name that year or ask to compare.

## You own retrieval (autonomous contract)

Since 2026-09-23 the Workbench **no longer injects** Wikipedia evidence. **You** decide
when a lookup is needed and **you** run it with the tools below — the same way you call
every other local tool.

1. **Read the conversation first, then call a tool.** Resolve pronouns and follow-ups
   yourself: "that page", "the 1984 one", "more about it", "their discography" all mean
   the entity you were just discussing. Pass the tool a **self-contained subject** —
   never the pronoun, never "that".
2. **A lead is a landing, not an answer.** `wiki_scout_search` returns the article
   **lead**. If the asked fact (a song, album, date, number, table row) is not literally
   in what the tool returned, **hop**:
   - name the page the fact most likely lives on — the work, person, episode, or album
     the question is really about — then confirm it with **`wiki_resolve`** and read it
     with **`wiki_read_section`** / **`wiki_extract`** (`need_hint` = the fact);
   - "which song/music" traces: read the linked artist or work page. Example that works:
     *Stranger Things* lead has no song → `wiki_read_section("Running Up That Hill")` →
     the archive lead states the post-season-4 revival.
   - A hypothesis is allowed, but it must be **verified by a tool result** before you say
     it. Never answer from training memory. If the hop misses too, say the archive has
     nothing.
3. **When a tool returns nothing usable:** say the local archive has no usable page and
   offer a clearer title. Never invent, never suggest Weaviate.
4. **Answer only from tool output** (Title + Lead/EXTRACT fields/tables/lists +
   scratchpad). If an EXTRACT state is empty/unsupported, refuse.
5. **Never invent** numbers, dates, cast names, or table cells that are absent from the
   EXTRACT.
6. Do **not** claim the archive is unavailable before you have called a tool once.
7. Do **not** narrate routing ("let me check the local archive…") — look it up and answer.
8. Do **not** mention Weaviate, Docker, port 8091, or docs about booting a container.
9. For multi-hop work across turns: use **`wiki_scratch_upsert`** to retain bridging
   facts; **`wiki_scratch_read`** only when synthesizing and no fresh evidence is in hand.
10. Reply in plain English. Name actors/albums only if they appear in tool output.

### Legacy escape hatch (rare)

If a turn arrives already carrying **`[[EMPIRE_WIKI_LOOKUP]]`**,
**`[[EMPIRE_WIKI_EXTRACT]]`**, or **`[[EMPIRE_WIKI_DRIFT]]`**, the Workbench is running
the old regex middleware (`EMPIRE_WIKI_MIDDLEWARE=1`). Then:

1. Answer from that block only (Title + Lead/EXTRACT + Related / Hop lines).
2. Do **not** call any wiki tool for that turn.
3. Do **not** narrate an empty scratchpad — normal for a single-page extract.

If **`[[EMPIRE_WIKI_ERROR_BOOK]]`** is present: the archive already missed this subject — do not invent a page.

If a **BOUNDARY** line asks for Web Scout (weather / future devices): answer local facts first, then ask before going online.

## Tools

1. **`wiki_scout_search`** — default landing: Title DNS + article lead for a subject (once per subject; hop with the others below when the asked fact is not in the lead).
2. **`wiki_extract`** — structured fields/tables/lists for dates, numbers, specs, table rows. Prefer when the user wants data extracts or a cast/crew table.
3. **`wiki_resolve`** — phone book only (exact/alias/ambiguous/missing). Use when unsure whether the title exists before extracting.
4. **`wiki_read_section`** — Title DNS page + optional named H2 section (cast, discography, filmography, charts, history, reception, plot, production).
5. **`wiki_scratch_upsert` / `wiki_scratch_read`** — multi-hop bridging facts / Error Book; never Cognee.
6. **`wiki_scout_compare_years`** — **only** when they ask what changed across years or say Truth Drift (needs Weaviate).
7. **`promote_wiki_cache`** — only when they explicitly ask to save a cache file to Cognee.
8. **`wiki_remember`** / **`remember_wiki_lead`** — only when they say remember/save/keep; `wiki_remember` rejects non-ok extracts.

## Simple questions

1. Call **`wiki_scout_search`** once with the subject the user actually means (default year **2026**).
2. If Title DNS is ambiguous, ask which title — do not invent.
3. Lead too thin for the question? Escalate to **`wiki_extract`** (or
   **`wiki_read_section`** for a named section) in the same turn instead of guessing.

## Multi-hop work

Examples: Casting Hop, Soundtrack Trace, Timeline Brief, Cast Table Merge.

1. Land the subject yourself: **`wiki_scout_search`** (lead) or **`wiki_resolve`** (does the title exist?).
2. Prefer **Cast / Discography / Filmography / Charts** sections — read them with
   **`wiki_read_section`** or **`wiki_extract`** when the landing lead is not enough.
3. Upsert bridging facts to the scratchpad between hops.
4. Synthesize only from tool output + scratchpad.

## Truth Drift (only when asked)

Call **`wiki_scout_compare_years`** when they explicitly want 2017 / 2021 / 2026 compared.

## When a lookup fails

Say the local archive has no usable page. Offer a clearer title. Do not invent. Do not suggest Weaviate.
