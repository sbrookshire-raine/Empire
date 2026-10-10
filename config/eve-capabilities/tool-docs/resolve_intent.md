---
name: resolve_intent
toolbelt: always
one_line: Map plain English verbs to intents, local-first tools, and playbook
---

# resolve_intent

Turn **everyday words** into an **intent route** (codex vocabulary).

## When to use

- User says **scrape**, **research**, **lookup**, **remember**, **find**, **compare**, etc. without naming a tool.
- Before refusing or answering from general knowledge when **local_first** applies.

## Parameters

- `message` — User's ask or the operative sentence (required).
- `limit` — Max intents returned (default 3).

## After resolve

1. Call **`local_tools`** in order when `local_first` is true.
2. **`resource_pulse` / `admit_for_goal`** for listed **limbs** before online tools.
3. **`playbook(area)`** for worked examples; **`tool_docs(tool)`** for parameters.

Codex file: `config/eve-capabilities/intent-codex.json` — Mechanic-editable.
