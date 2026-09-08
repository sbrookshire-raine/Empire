# skill-structured-extract

When the Architect wants structured document metadata (title, author, date, tags, summary) from local text:

1. Ensure Toolbelt **Structured Extract** is on.
2. Prefer worker up: `scripts/start-structured-extract.ps1` (Architect may have started it).
3. Call `structured_extract` with the text (or ask them for a file path and use MCP/file path via pipeline if exposed).
4. Answer only from returned `metadata` / lineage — never invent fields.
5. Never call `cognee_remember` unless they explicitly ask to promote.
6. Ollama remains chat; this worker is extraction-only.
