# Memory governance — how Eve adds to Cognee responsibly

Directions for what may be remembered, where it goes, and who decides. Written so it can be pasted
into a playbook limb almost verbatim (that is how it reaches her — **never** as an always-on prompt
line; see `OPERATING_CONTRACT.md` §4 on the context budget). Rules and tiers: §7 of the same document.

The governing principle: **recall is for what she should carry; the Library is for what she goes and
looks up; the Archive is for what nobody needs to read again.** Nothing is remembered just because it
was mentioned.

## 1. Three questions before anything is persisted

1. **Tier** — is this *knowledge* (Foundation / `eve_core`) or *reference* (a Library access point)?
   If reference: **do not embed it**, add a registry line in `config/library.json`.
2. **Durability** — will this still be true and useful in a month? If not, it belongs in the
   conversation, not in memory.
3. **Provenance** — can it name where it came from (source file, or conversation + date + who said it)?
   If not, it does not get persisted.

## 2. Eligible for `eve_core` (Foundation)

- Standing preferences and house rules ("answer like this", "never do X").
- Decisions **with their rationale**, which will be referenced later.
- Corrections to her behaviour, vocabulary, or assumptions.
- Definitions and vocabulary she is expected to use consistently.
- Universal primitives and frameworks the Architect is actively working on.

Foundation stays **small** (tens of files). Growing it is a deliberate act, not a side effect of use.

## 3. Never embedded — reference or archive instead

| Content | Where it goes |
|---|---|
| Manuals, vendor docs, product guides, tutorials | Library access point (`config/library.json`) |
| Transcripts, exports, large reference sets | Library, unless deliberately promoted |
| Harvested bulk, byte-identical duplicates, game notes | Archive — never recalled |
| Code, zips, WIP experiments | Archive |
| Anything without provenance | nowhere |
| **Secrets — keys, tokens, passwords** | **never in memory, in any tier** |
| Ephemeral session state | the conversation only |

## 4. The promotion path — already built, use it

The staging mechanism exists (`propose_remember` / `confirm_remember`); do not invent a parallel one.

1. **Propose.** `propose_remember(text)` — a candidate the Architect can accept or drop. This call
   writes nothing to recall.
2. **Confirm.** `confirm_remember(id)` — the promotion, and the only route by which a candidate
   becomes memory.
3. **His instruction *is* the consent.** When he says "remember X", `cognee_remember(...)` directly is
   correct. When he did not ask, it is `propose_remember` first — always.
4. **Repair and removal** are `cognee_improve()` (re-index/repair) and `cognee_forget(scope)` — the
   latter only on his explicit word, and confirmed by name.

The candour rule that goes with it: if a durable fact appears and no tool is at hand, **say it in the
reply** ("worth remembering: …") rather than writing silently. A candidate stated aloud can be acted
on; a silent write cannot be reviewed.

## 5. Communication standard — how she gets better at this

- When recalling, name the source: `source_file` plus its date.
- Distinguish **"you told me"** (recall) from **"I looked it up"** (a path, a URL, a wiki article).
- When a durable fact appears in conversation, *offer* to record it rather than silently doing so.
- Ask before persisting anything ambiguous — a wrong memory is worse than a missing one.

## 6. Tooling standard — how she gets better at that

- Reach for the **named access point** before guessing: a Library entry, `read_document`,
  `read_active_tool`, the wiki lead path.
- A new limb must satisfy the hand footprint (`OPERATING_CONTRACT.md` §5) and pass `check-legos`.
- If a capability is missing, **propose a brick** (the LEGO catalog) instead of improvising a workaround.

## 7. How these directions reach her (the wiring, in order)

| Step | Mechanism | Cost |
|---|---|---|
| 1 | Extend the existing playbook limb `memory-and-ideas.md` with §1–§4 above | read on demand, no prompt cost |
| 2 | `chat_reply_rule` on the `cognee_*` tool payloads: "this is a candidate — say so, do not persist silently" | zero prompt cost |
| 3 | A skill for capture-from-conversation | loaded only when retrieved |
| 4 | Create the `eve_candidates` staging dataset and add it to the promote flow (not to recall) | none |
| 5 | `check-legos` rule: `eve_core` may only contain registered Foundation sources; candidates may not appear in `chatRecallDatasets` | gate step |

Until steps 1–5 exist, this document is the policy — and the policy is what the wiring has to match,
not the other way round.
