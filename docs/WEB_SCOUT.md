# Web Scout

On-demand public **URL** → markdown cache under
`C:\Empire_Workbench\04_Thought_Experiments\web_cache\`.

Same Truth Drift contract as Wiki Local: **scratch only**, never auto-`cognee_remember`.

**Not a search engine.** You (or Eve) must supply a concrete `http(s)` page URL.

## Use

1. Start EMPIRE stack.
2. Enable Toolbelt **Web Scout**.
3. Ask Eve to scout a URL, or MCP `web_scout_url`, or:

```powershell
$env:PYTHONPATH="C:\EMPIRE"
.\venv\Scripts\python.exe -m pipeline.web_scout "https://example.com"
```

## Behavior

- http(s) only (bare domains like `example.com` get `https://` prefixed)
- Local HTTP fetch with browser-like headers
- Prefers **Trafilatura** extraction when installed; falls back to HTML text strip
- Provenance front-matter + footer via `pipeline/provenance.py`
- Promote later with `cognee_remember` after triage

## Common failures

| Symptom | Likely cause |
|---------|----------------|
| HTTP 404 | Bad or moved URL |
| HTTP 403 / 429 | Site bot wall — tool may try `/feed` on homepage URLs |
| Empty extract | JS-only app; need a static docs URL |
| Eve “searches” without a link | Web Scout is fetch-only — give a URL |
| Eve says she’ll “check manually” | Hallucination — she has no browser; report as bug if it happens |

Product Hunt homepage often returns 403; `https://www.producthunt.com/feed` (or homepage with feed fallback) works for a ranked Atom list.


## Related

- Wiki Local: [WIKI_SCOUT.md](WIKI_SCOUT.md)
- Idea Queue: [EMPIRE_IDEA_QUEUE.md](EMPIRE_IDEA_QUEUE.md)
