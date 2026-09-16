# Eve Core Ready Strip — Design Spec

**Date:** 2026-09-16  
**Status:** Approved — Phase 1 implemented  
**Scope:** Phase 1 only — Voice + Wiki header status (Approach 2). Later phases cover other limbs / resource sharing (out of scope here).

## One-breath goal

Chat feels ready: Voice and Wiki show as clickable status pills beside the mode picker. They leave the Tools dock checklist. Eve still receives them as real toolbelt limbs whenever enabled — same `active_tools` persistence — so post-ship tests can prove she always has access when those limbs are on.

## Decisions locked

| Decision | Choice |
|----------|--------|
| Placement | Header strip to the **right of the mode picker**, before history / dock icons |
| Which limbs | **Voice Presence** (`voice_presence`) + **Wiki Local** (`wiki_local`) |
| Interaction | **Clickable** toggles (Approach 2) |
| Status meaning | **C** — green = enabled + healthy; amber = enabled + unhealthy; dim = off |
| Dock | Remove both from the toolbelt checkbox list |
| Colors | Keep existing Eve neon/paper aesthetics; no new palette |
| Eve access | UI relocate only — no second permission system |

## Layout

In `frontend/eve.html` `chat__toolbar-actions`:

1. EMPIRE menu  
2. Mode picker (unchanged)  
3. **NEW:** `ready-strip` with two pills: **Voice**, **Wiki**  
4. History, DAZE (if product on), Toolbelt, New chat  

Each pill:

- Short label (`Voice` / `Wiki`)
- Status dot (green / amber / dim)
- `title` / `aria-label` with full name + state (e.g. `Wiki Local · enabled · healthy`)
- `aria-pressed` reflects enabled state
- Click → `setToolbeltCategory(id, !enabled)` (existing API)

CSS: compact horizontal flex; reuse `--color-neon-green`, amber/warn token if present, muted for dim. No card chrome; no purple/glow redesign.

## Health mapping

Reuse Workbench connectivity already known to the chat page; do **not** invent always-green dots.

| Pill | Enabled flag | Healthy when |
|------|--------------|--------------|
| Voice | `activeTools.voice_presence` | `GET /api/voice/health` reports ok (existing Speaches probe) |
| Wiki | `activeTools.wiki_local` | Glasses readiness, not overnight ingest status. Prefer extending `/api/wiki/status` with a boolean such as `glasses_ok` (Title DNS index present + `wiki_md` year root reachable), or a tiny dedicated GET. Do **not** treat ingest `phase` alone as healthy |

If a probe is missing today, add the **smallest** existing-style check in `eve-workbench.js` / `serve.py` — still not a fake green.

Dot logic:

```
if (!enabled) → dim
else if (healthy) → green
else → amber
```

Refresh: piggyback on existing health / connection refresh; no spinner on the strip.


## Tools dock

- `toolbeltBuckets` / template: **exclude** categories in a `readyStripIds` set (`voice_presence`, `wiki_local`) from the checkbox list.
- Always bucket may render empty → hide empty buckets (`x-show="bucket.categories.length"` already exists).
- Session + Products unchanged.
- More tab product shelf unchanged.
- Defaults remain `DEFAULT_ACTIVE_TOOLS = ("voice_presence", "wiki_local")` in `eve_toolbelt.py`.

## Eve tool access (non-negotiable)

- Chat send still posts `toolbelt` / `active_tools` through `eve_toolbelt.apply_active_tools` (existing path).
- Enabling a pill **must** leave the limb in persisted `config/eve-toolbelt.json` (or workbench copy) so Eve’s capability filter admits voice / wiki tools.
- Disabling a pill **must** remove that limb from effective tools.
- No silent “UI on but Eve off” or the reverse.

### Acceptance tests (Architect bar)

1. Cold open Workbench with defaults → Voice + Wiki pills not dim; Eve chat can use wiki extract/glasses path and voice mic path when services are up (green).  
2. Toggle Wiki off via pill → disappears from dock (already gone) **and** next chat turn Eve must not get wiki limb tools; toggle back on → she gets them again.  
3. Stop Speaches → Voice pill amber while still enabled; re-enable Speaches → green without flipping the toggle.  
4. `.\scripts\mechanic-green.ps1` exits 0 after UI changes (unit + stack); optional `-Full` if live Eve chat assertions are extended.

## Out of scope (Phase 2+)

- Other session/product limbs in the header  
- Combining limbs that share GPU / network resources  
- Redesigning the full Tools dock or Research Partner bar  
- New health backend services beyond mapping existing probes  

Phase 2 will revisit “other tools and how they appear / combine if same resources” after Phase 1 ships and tests green.

## Files expected to change

| File | Role |
|------|------|
| `frontend/eve.html` | Ready-strip markup in toolbar |
| `frontend/eve-workbench.js` | Strip model helpers, health→dot, filter dock buckets, click toggles |
| `frontend/eve-workbench.css` | Compact strip / pill / dot styles |
| `tests/frontend/test_eve_toolbelt.py` | Only if defaults/meta helpers change; prefer JS-side behavior covered by existing toolbelt persistence tests |
| `docs/EMPIRE_CLARITY.md` | One short note: Core ready strip vs dock |

## Success criteria

- Header shows Voice + Wiki without opening the Toolbelt.  
- Tools dock no longer lists those two.  
- Click toggles persist and Eve’s tool access tracks enable state.  
- Dot colors match enabled+healthy / enabled+down / off.  
- Mechanic green before Architect UX feel pass.
