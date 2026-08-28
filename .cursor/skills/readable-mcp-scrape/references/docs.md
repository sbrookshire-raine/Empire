# readable-mcp — EMPIRE reference pointers

## Upstream

- Repo: https://github.com/tommypj/readable-mcp
- Stack: FastMCP, Python, Trafilatura, SSRF-conscious fetch
- Job: single URL → clean Markdown (local, no paid LLM)

## EMPIRE handoff

1. Convert URL → `.md`
2. Stage in `mock_data_ingest/` (or wiki staging)
3. Ingest: `.\scripts\ingest-mock.ps1 <file>` or `empire-cognee` / `cognee_ingest_mock_file`
4. Overnight wiki corpus on `D:\wiki_md` remains separate (bulk MD already local)

## Redundancy winners

| Competitor | Verdict |
|---|---|
| `docs-guide-scraper` | Winner for full docs sites / llms.txt / sitemap |
| `web-researcher` | Winner for multi-round research + Ollama synthesize |
| `modelcontextprotocol/servers` fetch | Bin 3 — Node; prefer this FastMCP path |
| Official filesystem MCP | Bin 3 — Desktop Commander wins FS |

## Related docs

- `docs/reference/Deep Research Resource URL Report.md`
- `docs/reference/MASTER_INTEGRATION_MATRIX.md`
- Cognee MCP: `mcp/cognee_mcp.py`
