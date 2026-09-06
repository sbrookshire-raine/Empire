Use when the user asks for encyclopedia facts, Wikipedia context, Truth Drift across years, or local research before the web — and **Wiki Local** is enabled in the Toolbelt.

## Mission

Query the local Weaviate Wikipedia index, cache markdown for triage, answer from summaries + paths. Never invent wiki facts. Never auto-promote to Cognee.

## Tools

1. `wiki_scout_search` — one year (`2017` / `2021` / `2026`, default 2021).
2. `wiki_scout_compare_years` — same topic across years (Truth Drift).

## How to answer

1. Call the tool silently first.
2. Cite what you found in plain language; mention the cache path briefly if useful for triage.
3. If Weaviate is down, say the local wiki index is offline and suggest enabling it later — do not invent articles.
4. If Wiki Local is off and the user needs wiki research, tell them to enable **Wiki Local** in the Toolbelt.
5. Promote only when the user (or triage) decides a cache file is worth keeping — then `cognee_remember` (do not do this automatically).

## Hard rules

- Local Weaviate first; do not use cloud/web search for this path.
- Do not dump full article bodies into chat — use tool summaries.
- Do not restart overnight wiki→Cognee ingest.
- PocketBase Tasks are unrelated; Work Orders are for Cursor forge work, not wiki lookup.
