# Web Scout

On-demand public URL → markdown cache under
`C:\Empire_Workbench\04_Thought_Experiments\web_cache\`.

Same Truth Drift contract as Wiki Local: **scratch only**, never auto-`cognee_remember`.

## Use

1. Start EMPIRE stack.
2. Enable Toolbelt **Web Scout**.
3. Ask Eve to scout a URL, or MCP `web_scout_url`, or:

```powershell
$env:PYTHONPATH="C:\EMPIRE"
.\venv\Scripts\python.exe -m pipeline.web_scout "https://example.com"
```

## Rules

- http(s) only
- Local HTTP fetch (no paid search APIs)
- Provenance front-matter + footer via `pipeline/provenance.py`
- Promote later with `cognee_remember` after triage

## Related

- Wiki Local: [WIKI_SCOUT.md](WIKI_SCOUT.md)
- Idea Queue: [EMPIRE_IDEA_QUEUE.md](EMPIRE_IDEA_QUEUE.md)
