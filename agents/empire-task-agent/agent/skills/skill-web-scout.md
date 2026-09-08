# skill-web-scout

When the Architect wants a **specific public page** captured for triage:

1. Ensure Toolbelt **Web Scout** is on.
2. Call `web_scout` with a concrete **http(s) URL** (not a search phrase).
3. Summarize from the returned `summary` / `path` / feed list — never invent page content.
4. Never call `cognee_remember` unless they explicitly ask to promote.

## Important limits

- **Web Scout = fetch one URL.** It is **not** Google / DuckDuckGo. If they say “search the web for X” without a URL, ask for a URL — do **not** invent results.
- If the tool returns `ok: false` (404, bot wall, empty JS page), report that failure briefly and **stop**.
- **Forbidden after a failed or blocked fetch:**
  - Do **not** say you will “manually review,” “check the site yourself,” “browse,” or “give me a moment to look it up.”
  - You have no interactive browser. Pretending you do breaks trust.
  - Offer real next steps only: try a public `/feed` URL, ask the Architect to paste/screenshot, or wait until a static URL works.
- Some homepages (e.g. Product Hunt) return HTTP 403 to bots. The tool may auto-fall back to `/feed` and return ranked feed entries — use that list; say it came from the **public feed** and that feed order is **not** the same as official upvote #1 unless vote counts are present.
- Prefer one short answer after the tool returns. No “I’m going to look…” preamble.

## Good

- “Scout https://docs.python.org/3/tutorial/”
- “Fetch https://www.producthunt.com/” (tool may use `/feed` if homepage is blocked)

## Bad

- Calling `web_scout` with query text like “weaviate vector database”
- Inventing a summary after HTTP 403/404
- “Give me a moment to check the site manually…”
