---
name: api-tester
description: Fuzzes OpenAPI/GraphQL APIs, runs property-based tests, and generates JUnit XML reports. Activate for "fuzz this API", "test these endpoints", "OpenAPI spec testing", "generate test suite", "GraphQL testing". Touches FastMCP (the primary Build1 API surface to fuzz) and PocketBase (its REST API can also be fuzz-tested); target only localhost endpoints, never a cloud service.
icon: zap
color: Orange
---

# API Tester (Build1 edition)

## Activate when
"fuzz this API" · "test these endpoints" · "OpenAPI/Swagger testing" · "GraphQL testing" · "property-based tests" · "generate JUnit report"

## Capabilities → module

| Module | Use for |
|---|---|
| `api_fuzzer` | `analyze_spec`, `run_schemathesis_fuzz`, `full_fuzz_pipeline`, `write_junit_xml_report` |
| `rest_client` | `graphql_query`, `graphql_introspect`, `ws_connect`, `paginate` |

## Quick start

```python
from api_fuzzer import analyze_spec, full_fuzz_pipeline

spec = analyze_spec("fastmcp_openapi.yaml")["result"]
result = full_fuzz_pipeline(
    "fastmcp_openapi.yaml",
    "http://localhost:8000",   # target the local FastMCP server, not a hosted URL
    dry_run=False,
)
```

## Build1 Integration

- **FastMCP**: if the Build1 FastMCP server exposes an OpenAPI schema for its tool endpoints, export that spec and fuzz it against the running local server (default `http://localhost:8000` or your configured port). This catches schema violations before the local-Ollama-driven agent trusts those tools.
- **PocketBase**: its REST API is also documented/introspectable (typically `http://localhost:8090`) and can be fuzz-tested the same way to validate custom collection rules/hooks.
- Always point `full_fuzz_pipeline`/`rest_client` at a `localhost`/LAN target — never at an external or cloud endpoint, since Build1's whole point is that these services run locally.
- Emit `write_junit_xml_report` output so results can be picked up by whatever CI/local test runner the user already has, or attached via the `report-builder` skill.
