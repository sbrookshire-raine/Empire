# Capability route index (Eve self-discovery)

Eve already had three partial layers; they did not form one ladder:

| Layer | Tool | What it actually searches |
|-------|------|---------------------------|
| Playbook | `playbook(topic)` | Worked examples by area / tool name |
| Syntax | `tool_docs(name)` | One tool's parameters |
| OSS catalog | `search_catalog(query)` | **`catalog.db`** — external repos/MCP rows, not her 80+ agent tools |

**`capability_route(query)`** closes the gap: a **keyword index** over her own tools, Toolbelt
limbs, and playbook areas, with **load hints** (GPU, network, auto-enable) so she can choose a
path without loading every schema or admitting heavy limbs blindly.

**`resolve_intent(message)`** is the **verb codex** layer: scrape → gather web, research → local
then desk/web, lookup → files/memory/wiki — see [`INTENT_CODEX.md`](INTENT_CODEX.md).

## Protocol (routing contract)

0. **`resolve_intent(message)`** — everyday verbs → intent policy (`intent-codex.json`).
1. **`capability_route(query)`** — pick tool, limb, or playbook area; read `next_steps` and `load`.
2. **`playbook(area)`** — reuse ask → tool → artefact examples.
3. **`tool_docs(tool)`** — parameters before calling.
4. **`resource_pulse()`** / **`admit_for_goal(category)`** — before session limbs that are off (REA, vision, stems, …).

Use **`search_catalog`** only when the ask is about an **external** capability row (MCP server, GitHub repo in the intake catalog).

## Sources (auto-rebuilt, cached)

- `config/eve-capabilities/tool-docs/*.md` — tool names and one-liners
- `config/eve-capabilities/playbook/*.md` — areas and tool lists
- `config/capability-manifest.json` — limb admission / GPU / network
- `config/eve-capabilities/route-synonyms.json` — manual phrase boosts (Mechanic-editable)

Implementation: `pipeline/capability_index.py`.

## Mechanic commands

```powershell
.\venv\Scripts\python.exe -m pipeline.capability_index "reverse engineer electron" --limit 5
.\venv\Scripts\python.exe -m pipeline.capability_index --list
```

## Related

- [`docs/PLAYBOOK.md`](PLAYBOOK.md) — worked examples
- [`docs/REFACTOR_PLAN.md`](REFACTOR_PLAN.md) — R-06 intent groups (future: ≤3 active limbs)
- [`docs/REA_LIMB.md`](REA_LIMB.md) — example limb admitted on demand
