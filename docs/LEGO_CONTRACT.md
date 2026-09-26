# LEGO contract — what fits EMPIRE, and what does not

The standard for adding capability to this project. Written against the catalogs that already exist, so
it describes the system as built rather than an ideal one:

| Catalog | File | Governs |
|---|---|---|
| Brick palette | `config/lego-bricks.json` | which limbs exist, and whether they are switchable |
| Admission policy | `config/capability-manifest.json` | what a session may auto-admit (TTL, GPU tenant, network, services, disk) |
| Content access points | `config/library.json` | reference material Eve reaches by name |
| Human mirror | `03_Active_Tools/LEGO_INDEX.md`, board at `/lego.html` | the Architect's view of the palette |

**Brick fields (existing schema, `schema_version: 1`)** — `id`, `label`, `toolbelt`, `default_on`,
`gpu_tenant`, `ports {in,out}`, `tools[]`, `note`. Optional limbs are `default_on: false` and reachable
only through the Toolbelt / LEGO Apply.

## 1. The four-part footprint of a hand

A limb is complete when all four parts exist and agree:

| Part | Path | Content |
|---|---|---|
| Server | `mcp/<name>_mcp.py` | FastMCP tools, stdio transport |
| Transport adapter | `agent/lib/<name>-mcp.ts` | `createEmpireMcpClient({ label, clientName, script, env })` + thin adapters |
| Shared client | `agent/lib/mcp-client.ts` | one place for SDK import, lifetime, env pinning, error shape — **never duplicated** |
| Contract | `config/eve-capabilities/playbook/<limb>.md` + a `config/lego-bricks.json` brick + (if admissible) a `capability-manifest.json` category | what it is for, when to reach for it |

## 2. Adding a brick — the authoring sequence

1. **Server.** Add the Python tools under `mcp/`. Stdio only. Never read or write outside the roots it
   declares in its env.
2. **Adapter.** Add `agent/lib/<name>-mcp.ts` using the shared client — a config plus one thin function
   per tool. No SDK imports, no process handling, no JSON parsing of your own.
3. **Limb page.** Add `config/eve-capabilities/playbook/<limb>.md` with the `area` / `one_line` /
   `tools` / `skills` frontmatter and worked pathways ("ask → do → get"). This is how Eve learns to use
   it — **read on demand, so it costs no prompt budget.**
4. **Palette.** Add the brick to `config/lego-bricks.json`: `default_on: false` unless it is core,
   `gpu_tenant` declared honestly (`none` / `chat` / `extract` / `vision` / `ops`), `ports.in` and
   `ports.out` named, `tools` listed.
5. **Admission (only if it needs the network, a service, a GPU tenant, or disk).** Add a category to
   `config/capability-manifest.json` with `auto_enable`, `session_ttl_min`, `gpu_tenant`, `network`,
   `requires_services`, `min_disk_free_gb`.
6. **Reference content?** Then it is *not* memory: add a line to `config/library.json` instead of
   embedding anything.
7. **Verify.** `mechanic-green` must be green, playbook coverage `ok: true`, and the brick entry must
   match the tools that actually exist.

## 3. Invariants — true of every limb, no exceptions

1. **Local-only at runtime.** No cloud API calls, no API keys, no telemetry. The only network limbs are
   those that declare `network: true` in the admission manifest.
2. **One transport, one client.** stdio via `PYTHON_BIN`; adapters use `agent/lib/mcp-client.ts` and
   stay thin (the seven consolidated wrappers average ~43 lines).
3. **One error contract.** Tools return `{ ok: false, error }` naming the failing server. No silent
   failures, no invented envelopes.
4. **Env overrides win last.** Wrapper overrides are applied after inheriting `process.env` — the host
   carries `OLLAMA_HOST=0.0.0.0` (a bind address), and a limb that inherits it breaks.
5. **Optional limbs default OFF** and are admitted explicitly or by TTL policy.
6. **GPU tenancy is declared and honoured.** A limb that uses the GPU says which tenant it needs; the
   lease allows exactly one interactive chat model at a time.
7. **Reference is never embedded.** Manuals, guides, transcripts and exports are access points.
8. **No secrets in memory, in any tier.**
9. **Always-on prompt content requires an explicit trade** — the budget is `eve_instructions.md` +
   `empire-routing.md` (≈13.5 KB) plus tool schemas. Detail goes in a skill or a playbook limb.
10. **Registered paths stay put.** `03_Active_Tools` must never be relocated (strict protocol;
    `read_active_tool` resolves only inside it). New top-level directories and ports require catalog
    entries first.

## 4. Does not fit — reject on sight

- A cloud API, an API key, or a hosted service in the runtime path.
- A new service or port with no `capability-manifest.json` entry and no `start-stack.ps1` wiring.
- A tool that reads or writes outside the roots it declares.
- Embedding reference material (manuals, vendor docs, transcripts) into a recall dataset.
- A new always-on prompt rule where a skill or playbook limb would do.
- Reviving Weaviate (see `docs/WIKI_LAYER_AUDIT.md`: it is a source being drained, not a dependency).
- Vendor documentation dumped into `docs/` — that is `docs/reference/`, and it is never ingested.
- A second copy of something that already exists (the registry points at the original).
- Anything that requires a rewrite of `mcp-client.ts` or the playbook frontmatter to bolt on.

## 5. Acceptance checklist for a proposed piece

| Question | Pass condition |
|---|---|
| Does it have all four parts (§1)? | server + adapter + limb page + catalog entry |
| Does it declare what it needs? | `gpu_tenant`, `ports`, `network`, `requires_services`, disk |
| Does it stay local? | no cloud endpoints, no keys |
| Is it thin? | no SDK/lifetime/parsing logic in the adapter |
| Does it stay out of the prompt? | usage taught via a playbook limb, not always-on text |
| Does it pass the gate? | `mechanic-green` green, coverage `ok: true` |
| Is its data honest? | reference → `library.json`; knowledge → governance rules; nothing else persisted |

## 6. Known drift to resolve (found while writing this)

`config/capability-manifest.json` lists `requires_services: ["weaviate:8091"]` for `wiki_local`, but
`docs/WIKI_LAYER_AUDIT.md` records Weaviate as retired-by-design (the v2 archive is a one-time drain).
One of the two is stale; the wiki limb now reads `D:\wiki_md` leads directly. Resolve before the next
`wiki_local` admission relies on it — this is the kind of mismatch `check-legos` exists to catch.

## 7. How this becomes enforced

This document is the standard; `scripts/check-legos.py` (next increment) is the enforcement:
brick ↔ limb ↔ tools ↔ playbook ↔ catalog alignment, adapter thinness, no cloud endpoints, library
paths existing, and the prompt-layer budget. Wired into `mechanic-green` like `audit-empire.py`, so a
non-conforming brick **fails the gate** rather than being discovered months later. Until then, this
contract is the checklist a human or an external model follows by hand.

