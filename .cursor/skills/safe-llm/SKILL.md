---
name: safe-llm
description: Routes LLM calls with local Ollama as the default provider (hosted providers optional fallback only), extracts typed structured data, and applies safety guardrails (hallucination, PII, prompt-injection checks). Activate for "add fallback providers", "extract structured data from LLM", "check for hallucinations", "validate LLM output", or "safe pipeline". Touches Build1's Inference layer (Local Ollama) and can be exposed via FastMCP.
icon: shield-check
color: Violet
---

# Safe LLM

## Activate when
"add provider fallback" · "use multiple LLMs" · "extract structured data" · "validate LLM output" · "check for hallucinations" · "redact PII from response" · "safe pipeline"

## Scripts (keep in a `scripts/` subdirectory)

| Script | Use for |
|---|---|
| `scripts/llm_provider_router.py` | `detect_available_providers`, `fallback_completion`, `estimate_cost` — default provider list should start with local Ollama models; only add hosted providers (gpt-4o, claude, etc.) if the user opts in |
| `scripts/structured_llm_extractor.py` | `extract_structured(model, msgs, PydanticSchema)` with retry, run against the local model first |
| `scripts/llm_guardrails.py` | `check_hallucination`, `check_pii(redact=True)`, `check_prompt_injection`, `run_all_checks` |

## Recommended chain
```python
from scripts.llm_provider_router import fallback_completion, detect_available_providers
from scripts.structured_llm_extractor import extract_structured
from scripts.llm_guardrails import run_all_checks, check_pii

providers = detect_available_providers()["result"]  # local Ollama models listed first
result = fallback_completion(["ollama/llama3", "ollama/mistral"], messages)  # local-only fallback chain
checks = run_all_checks(result["result"]["text"])
```

## Build1 Integration
- **Inference**: the fallback chain should be Ollama-model-to-Ollama-model (e.g. try `llama3`, fall back to `mistral`) by default; only append a hosted model to the chain if the user explicitly asks for cloud fallback, and note that this breaks the zero-cloud guarantee.
- **Nervous System**: wrap `fallback_completion`, `extract_structured`, and `run_all_checks` as FastMCP tools so any Build1 agent can call a guardrailed, local-first LLM pipeline.
- **Memory/RAG**: guardrail-checked structured extractions can be written into Cognee's graph for downstream retrieval.
