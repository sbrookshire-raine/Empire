# LEGO prompt — how to ask an outside model for pieces that fit

This is your part-A artifact: hand this file (or paste §2) to any external model — Gemini, Composer,
DeepSeek, whatever — and it will know **what attaches to EMPIRE and what does not**, in EMPIRE's own
vocabulary, with an output format that a machine can check.

The rules it references are enforced: `scripts/check-legos.py` runs inside `mechanic-green` and fails
the build on a non-conforming brick. Full standard: `docs/LEGO_CONTRACT.md`.

---

## 1. Copy-paste prompt

> **Context.** EMPIRE is a local-first, meter-free AI workspace: a Windows host running Python, Node,
> PowerShell, Docker and Ollama. Everything runs on this machine — there are no cloud API calls at
> runtime, no API keys, no telemetry. A local agent ("Eve") uses a fixed set of **limbs**; each limb is
> a Python MCP server plus a thin TypeScript adapter, described by a playbook page and registered in a
> brick catalog.
>
> **Task.** Propose one or more **bricks**: self-contained capabilities that attach to this system
> without modifying its core.
>
> **What a brick is.** Four parts, all required:
> 1. `mcp/<name>_mcp.py` — FastMCP tools over stdio. Reads/writes only inside roots declared in its env.
> 2. `agent/lib/<name>-mcp.ts` — a `createEmpireMcpClient({ label, clientName, script, env })` config
>    plus one thin function per tool. **Do not** import the MCP SDK, manage process lifetime, or parse
>    MCP JSON yourself; a shared client does all of that.
> 3. `config/eve-capabilities/playbook/<limb>.md` — frontmatter (`area`, `one_line`, `tools`, `skills`)
>    and "ask → do → get" pathways. This is how the agent learns to use it, read on demand.
> 4. A brick entry (see §3) — `default_on: false` unless it is core, honest `gpu_tenant`, declared
>    `ports`, and the actual tool names.
>
> **Never propose** (these are automatic rejections):
> - a cloud API, an API key, or any hosted service in the runtime path;
> - a new service or port without an admission entry and start-script wiring;
> - a tool that reads or writes outside its declared roots;
> - embedding manuals/guides/transcripts into memory (reference material is reached by name, never
>   embedded);
> - a new always-on prompt rule (agent guidance goes in a skill or playbook page, where it costs no
>   context budget);
> - a second copy of something that already exists; or anything requiring changes to the shared client
>   or the playbook format to bolt on.
>
> **Requirements the system cares about:** declared GPU tenancy (one GPU tenant at a time — `none`,
> `chat`, `extract`, `vision`, `ops`); declared network use; errors returned as
> `{ ok: false, error }` naming the failing server; no secrets in memory in any tier.
>
> **Deliverable.** For each brick: the brick JSON (§3), the tool list with one-line purposes, what it
> needs (GPU tenant, network, services, disk), the playbook pathways, and a short **fit argument**
> answering §4's checklist. State plainly any assumption you made. If nothing you can propose fits,
> say that — a clean "does not fit" is a better answer than a stretch.

## 2. Required output format per brick

```json
{
  "id": "short-stable-name",
  "label": "Human Label",
  "toolbelt": "limb_name_or_null",
  "default_on": false,
  "gpu_tenant": "none",
  "ports": { "in": ["text"], "out": ["text"] },
  "tools": ["tool_one", "tool_two"],
  "note": "One sentence: what it does and why it exists."
}
```

Plus, in prose: the tool list with purposes, the declarations (GPU / network / services / disk), the
playbook pathways, and the fit argument.

## 3. Self-check before submitting

| Question | Must be true |
|---|---|
| All four parts present? | server + adapter + playbook page + brick entry |
| Does it declare what it needs? | `gpu_tenant`, `ports`, `network`, `requires_services`, disk |
| Is it local-only? | no cloud endpoints, no keys |
| Is it thin? | no SDK/lifetime/parsing code in the adapter |
| Does it stay out of the always-on prompt? | usage taught via a playbook page |
| Is its data honest? | reference → a registry line, never an embedding |
| Would it pass the gate? | conforming to `docs/LEGO_CONTRACT.md` |

## 4. What happens to a submission

It is reviewed against the contract, then the mechanical checks run: brick fields, optional-brick
defaults, adapter thinness, no cloud endpoints, library paths, prompt budget. A piece that fails those
**fails the build** — so a proposal that can't say how it satisfies the checklist isn't ready to submit.

## 5. Why this shape exists

Three times in this project, "these look alike, merge them" turned out to be wrong when measured
(a routing pair sharing 0 lines; three guide docs sharing 0–1; the one "dead" file being the recipe for
a 20 GB corpus). EMPIRE is coherent but was grown piece by piece. The contract's job is to make the next
piece attach cleanly rather than add a fourth way of doing something — which is exactly why §1 says
*reject* more often than it says *propose*.
