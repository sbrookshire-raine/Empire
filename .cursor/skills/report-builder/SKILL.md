---
name: report-builder
description: Generates PDF/DOCX/HTML reports and delivers them via email or Slack, and assembles end-to-end reporting pipelines (digests, standups, security alerts). Activate for "generate a report", "create a PDF", "send this digest", "email the results", "post to Slack". Touches FastMCP (exposes report functions as tools) and Local Ollama (drafts narrative/summary text locally instead of a cloud LLM).
icon: file-text
color: Green
---

# Report Builder (Build1 edition)

## Activate when
- "Generate a report" / "Create a PDF or DOCX"
- "Send this to Slack / email"
- "Build a daily digest / standup / security alert"
- "Notify me when X happens"

## Capabilities → module

| Module | Purpose |
|---|---|
| `documents` | Write PDF, DOCX, convert Markdown → HTML |
| `template_tools` | Jinja2 rendering, built-in report templates |
| `gmail` | Send email, search, reply |
| `slack` | Post messages, upload files |
| `notification_tools` | Slack, Discord, Teams, SMS, webhook fan-out |
| `pipeline_tools` | End-to-end pipelines: research→report, security audit |
| `news_digest` | Build a filtered news digest |
| `standup_generator` | Turn activity logs into a standup post |

## Quick start — register as FastMCP tools

```python
from fastmcp import FastMCP
from documents import write_pdf, write_docx
from template_tools import render, render_security_alert
from notification_tools import send_notification

mcp = FastMCP("report-builder")

@mcp.tool()
def build_report(data: dict, template: str = "default") -> dict:
    """Render `data` through `template` and write a PDF."""
    html = render(template, data)
    path = write_pdf(html, "report.pdf")
    return {"ok": True, "result": path}
```

## Local summarization instead of a cloud LLM

Any pipeline step that drafts narrative text (executive summary, digest blurb, standup wording) should call **local Ollama**, not a hosted LLM API:

```python
import requests

def draft_summary(text: str, model: str = "llama3.1") -> str:
    r = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": model, "prompt": f"Summarize the following:\n\n{text}", "stream": False},
    )
    r.raise_for_status()
    return r.json()["response"]
```

## Build1 Integration

- Expose `build_report`, `send_notification`, and pipeline entry points as `@mcp.tool()` functions on the Build1 FastMCP server so the agent loop can trigger reports on demand.
- Pull the underlying data from PocketBase records (query via its REST API) rather than a separate database.
- Route any generative-text step (summaries, digests, alert wording) through local Ollama as shown above — never wire it to a cloud model provider.
- If the report should be viewable in-app rather than emailed/posted, render it as an HTMX-swapped HTML partial styled with Alpine.js instead of (or in addition to) a static PDF/DOCX file.
