# EMPIRE Research Handoff for Cursor

## Read first

1. `docs/EMPIRE_LOCAL_UPGRADE_RESEARCH.md`
2. `1. EMPIRE_RESEARCH_SNAPSHOT.md`
3. `docs/local-no-account-tools.yaml`
4. `EMPIRE_IDEA_QUEUE.md`
5. `docs/EVE_OLLAMA_EXPANSION_MANIFEST.md`
6. `docs/LOCAL_NO_ACCOUNT_MCP_CATALOG.md`
7. `EMPIRE_MANIFESTO.md`
8. `last_communication.md`

## Authority and boundaries

- The research snapshot is implementation truth.
- The upgrade research brief is the recommendation and model-acquisition guide.
- The YAML catalog contains existing tools and schema; avoid duplicates.
- The manifesto describes vision, not proof of implementation.
- Online resources, cloud APIs, hosted benchmarks, and frontier models may be used during construction when they have a documented local exit path.
- Operational Eve should remain local: Ollama, Cognee, PocketBase, FastMCP, localhost-bound services, and explicit memory promotion.
- No new memberships, subscriptions, recurring fees, or accounts by default.
- Do not expose generic shell, filesystem, Docker, browser, model-pull, or arbitrary database control to Eve.
- Do not install or forge every candidate at once.

## First implementation task

Create a small Work Order for the operational foundation:

1. Versioned model/runtime release manifest.
2. Golden evaluation fixture and acceptance record.
3. GPU/RAM/disk admission evidence.
4. Typed artifact lineage envelope.
5. One-step rollback for a single structured-extraction worker.

The first worker should be narrow and reversible. A suitable candidate is an official Qwen3-14B GGUF served by `llama.cpp` for schema-constrained extraction, while Ollama remains Eve's interactive runtime.

## Required Work Order behavior

Before changing the canonical repository:

- Read the relevant source files on the other computer.
- Verify whether the capability already exists.
- State the exact files to change.
- Pin model/runtime/version/license information.
- Define CPU, RAM, VRAM, disk, and network behavior.
- Add a canonical-machine smoke test and rejection condition.
- Keep new limbs default-OFF unless clearly core and approved.
- Do not auto-promote scout or generated artifacts into Cognee.
- Rebuild Eve only when TypeScript changes require it.

## Deliverable

Produce a Work Order first. Do not treat this research package as permission to implement every recommendation.
