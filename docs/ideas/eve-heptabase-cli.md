---
id: E-44
slug: eve-heptabase-cli
title: Eve gets Heptabase CLI access — a host-side limb for the live card library
status: in_progress
area: memory
priority: later
depends_on: []
touches: [mcp, toolbelt, docs, tests]
created: 2026-09-27
source: Architect, 2026-09-27 — "i just wanted you to have cli access to heptabase if it helped our tasks and eventually the same for eve"
---

# Eve gets Heptabase CLI access — a host-side limb for the live card library

## Intent

Give Eve the same reach Cursor now has into Heptabase: ask about her own recorded thinking and get it
back as live cards, journals, transcripts and whiteboard structure — instead of the April 2026 export
that is already five months stale. The Architect's ask is deliberately open-ended (*"if it helped our
tasks"*), so this is parked until a task actually needs it; the measured case for it is recorded below so
the decision does not have to be re-derived.

## Why it matters

Measured 2026-09-27: the live library holds **1,574 cards**; the export Cursor read (`All-Data.json`,
2026-04-08) holds **775**, and the newest 100 cards by `createdTime` (2026-08-12 → 2026-09-05) *all*
postdate it. So roughly **800 cards — five months of thinking — exist nowhere in EMPIRE's reach today**.
Heptabase is also the source of EMPIRE's own lineage (`ODYSSEY.md` §12.3–§12.6): Truthdrift's five-phase
design card, the Feb 2026 local-stack blueprint, and the 30 concept cards. A limb that can read it makes
*"did we already build a version of this?"* (`MOTIVATION.md` §4) answerable against the newest material
rather than a snapshot.

## What "done" looks like (acceptance)

- Ask *"what did I write about <topic> in Heptabase?"* → Eve returns **card titles with dates**, never a
  fabricated card, and says plainly when the search found nothing.
- Ask for a specific card by name/topic → its text comes back, attributed as Heptabase content, with the
  card id so the Architect can open it.
- Say *"search my recent journals for <x>"* → date-scoped results from `journal read`, not a whole-library scan.
- Fail closed: if the desktop app is not running (or the CLI/token is missing), Eve says so **in one line**
  and does not narrate a retry loop.
- Read-only by default. Any write (note, journal, tag, property) requires the Architect's explicit confirm
  in the same turn, and is marked so Heptabase can tell AI-authored content apart.
- Gates stay green: the limb is Toolbelt-gated (off by default, admitted via `admit_for_goal`), so
  `tests/test_prompt_budget.py` ceilings and the PLAYBOOK coverage contract are unaffected.

## Stack plan (how it applies in EMPIRE)

| Layer | What it gets |
|-------|--------------|
| Mechanism | The CLI is a **host binary** (`C:\Users\m69nr\.heptabase\bin\heptabase.cmd`, `0.6.0`, on the user PATH) that talks to a local server **inside the running desktop app**, authenticated by `~/.heptabase/local-server-token`. Everything is JSON on stdout. |
| `mcp/` + agent tool | A `heptabase` limb following the existing host-service pattern — `daze-mcp.ts` already reads `POCKETBASE_URL ?? http://127.0.0.1:8090`, and `wiki-scout-mcp.ts` pins `127.0.0.1` for Weaviate/Ollama. Start with **one MCP server so Cursor and Eve share the same surface** (the `media_scout` precedent), then two tools: `heptabase_search` (cards/journals by keyword or date, titles+ids) and `heptabase_read_card` (one card's text, or a PDF page range / transcript time range). Writes only later, behind confirm. |
| Sandbox boundary | **The CLI must run in the host agent process, not in a sandbox container.** Eve's local Docker sandbox backend supports only coarse `allow-all` / `deny-all` network policies, so a sandboxed task cannot reach the app's local server, and the sandbox has neither the binary nor the token. Anything sandboxed gets the honest one-line refusal instead. |
| Governance | New Toolbelt category `heptabase`, **off by default**; tool docs under `config/eve-capabilities/tool-docs/`; a `playbook` area so it has worked examples; `capability-manifest.json` + `check-legos.py` updated; MEMORY_GOVERNANCE respected (nothing from Heptabase enters Cognee without the Architect's confirm). |
| Docs + tests | `docs/PLAYBOOK.md` row; `tests/pipeline/test_heptabase_limb.py` hermetic (fake CLI JSON, no live app); prompt-budget ceiling test must stay green. |

## Constraints and identity

- **Local-first, no vendor API, no keys** — the CLI is local process-to-process, which fits the stack. Its
  one hard dependency is the **desktop app running**, so the limb fails closed rather than pretending.
- **The CLI is the only data-access path.** The `heptabase-cli` skill states this outright: never read or
  write Heptabase app storage, caches or internal endpoints. That rule is inherited by this limb.
- **The token is a secret.** `~/.heptabase/local-server-token` must never be printed, logged, traced, or
  placed in a prompt — it belongs in the environment only.
- **Heptabase content is personal and unvetted.** Journals and chats are private; the 71 placeholder and
  63 journal-date cards are noise (`ODYSSEY.md` §12.3). Reads are fine; *promotion* into memory is not
  automatic.
- **Writes are the risky half.** Heptabase offers `--no-created-by-ai` for human-owned content, so the
  default must be to mark AI-authored work rather than pass it off as the Architect's.
- Prompt budget: gated, never always-on — two tools is small, but the ceiling test decides.

## Open questions

1. **Does Eve need it, or does Cursor suffice?** The estate extraction is a Cursor-side archaeology task
   today. The case for Eve is *conversational recall of recent thinking*; if that is not a felt gap, this
   stays parked.
2. **Scope:** whole library, selected whiteboards (e.g. `KNOWTHYSELF`, `PROJECT: RESEARCH TITAN`), or
   journals only? Whole-library search will surface personal material in ordinary chat.
3. **Read-only forever, or propose-then-confirm writes?** Writes could be genuinely useful (a thought
   experiment captured straight into the right board) but need the confirm path first.
4. **Token lifecycle:** how does the limb behave when Heptabase rotates the token, and how is that
   surfaced as a one-line fix rather than a mystery failure?
5. **`jq` is not installed** on this machine; the skill's recipes assume it. Either install it or keep the
   limb on `python -m json.tool`/native parsing.
6. **Version pinning:** the skill requires `heptabase` `0.6.x`. What does the limb do when a desktop-app
   update moves the CLI outside that range — refuse, or warn?

## Promotion checklist (idea → Work Order)

- [x] Open question 1 answered — Eve + Cursor via `empire-heptabase` MCP; scoped to Disassembly catalog publish (2026-10-10).
- [ ] Scope chosen (question 2) and the read-only boundary agreed (question 3).
- [ ] Missing-CLI / app-closed / token-rotated behaviour specified as one-line refusals.
- [ ] Tool names, tool docs, playbook area and test file names chosen.
- [ ] Prompt-budget check run with the limb admitted.
