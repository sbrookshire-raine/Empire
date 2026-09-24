---
id: E-19
slug: media-limb-yt-dlp
title: Media limb — local video search, links, transcripts, and (later) a player
status: idea
area: media
priority: later
depends_on: []
touches: [pipeline, mcp, toolbelt, frontend, pocketbase, cognee, docs, tests]
created: 2026-09-24
source: Architect question in chat, 2026-09-24 (E-19)
---

# Media limb — local video search, links, transcripts, and (later) a player

## Intent

Let Eve find videos and the resources around them without a corporate dependency: the Architect asks
*"find me a video that explains magnetism"*, Eve returns candidates **with links**, keeps the ones the
Architect wants, and later can answer *"what was that magnetism video?"* and open it in a window.

## Why it matters

Today Eve answers that request with a one-line honest refusal (fixed 2026-09-24) because no video tool
exists. Video is how the Architect actually learns, and the link/resource pile inside descriptions
(docs, repos, papers) is exactly the kind of material `web_scout` can then fetch and summarise.

## What "done" looks like (acceptance)

- Ask for a video by topic → Eve returns **2–5 candidates with titles, channel, duration, and URLs**
  from a local search, never a fabricated link.
- "Keep that one" → the link is stored (PocketBase) and confirmed; nothing enters Cognee without the
  Architect's confirm.
- Later: "what was the magnetism video I kept?" → Eve recalls the title/link from memory, in words.
- Ask for a transcript of a kept video → local captions or Whisper output, attributed, cached under
  `04_Thought_Experiments/media_cache` (never auto-promoted).
- Regression guard: `states the limit in one line instead of narrating a browser` stays green
  (the rule added to `empire-routing.md` on 2026-09-24), and the new limb is Toolbelt-gated so the
  prompt-budget ceilings in `tests/test_prompt_budget.py` stay satisfied.

## Stack plan (how it applies in EMPIRE)

| Layer | What it gets |
|-------|--------------|
| `pipeline/` | `media_scout.py` — three functions over the local `yt-dlp` binary: `search(query, limit)` (uses `ytsearchN:`), `metadata(url)` (`--dump-json` → title, channel, duration, description, chapters), `transcript(url)` (subtitles, then Whisper fallback). Cache JSON/markdown under `04_Thought_Experiments/media_cache` |
| `mcp/` + agent tool | `mcp/media_scout_mcp.py` (one server, so Cursor and Eve share it) + `agent/tools/media_scout_search.ts` / `media_scout_keep.ts`, gated by a new Toolbelt category **`media_scout`** (off by default, admitted with `admit_for_goal`) and documented in `config/eve-capabilities/tool-docs/` |
| Storage | **PocketBase** collection `media_links` (state: title, url, channel, duration, topic, kept_at, notes, hand-editable, backed up). **Cognee** gets a `propose_remember` only on the Architect's confirm. Cache files stay on disk |
| Frontend | Later: a **LEGO page** `media.html` (zero-build Alpine, like `wiki.html`/`daze.html`) listing kept links with an `<iframe src="https://www.youtube.com/embed/<id>">` player, plus a "Kept media" dock panel in `eve.html` |
| Docs + gates | tool docs for both tools; `tests/pipeline/test_media_scout.py` (hermetic: fake `yt-dlp` output, no network); ceiling test unaffected because the limb is gated |

## Constraints and identity

- **No API keys, no quota, no cloud in the loop** (Architect's decision 2026-09-24): `yt-dlp` is the
  mechanism. Nothing in this limb may call a vendor API.
- Local-only: the limb runs the local binary; network access is *outbound fetch for the video page*,
  the same class as `web_scout` — so it stays deny-by-default and only runs when the limb is admitted.
- Attribution and ToS: transcripts and descriptions are third-party content; store the source URL with
  everything and never present a transcript as our own text.
- Prompt budget: gated, never always-on (2 tools ≈ small, but the ceiling test is the arbiter).
- Disk: transcripts and media caches are bounded (size + count), with a documented prune step.
- One heavy tenant: transcription on GPU must respect the GPU lease, like `stem_factory`.

## Open questions

1. Transcription: captions when available, else Whisper via Speaches — or never Whisper for media
   (cost) and captions only?
2. Is the player a new LEGO page (`media.html`) or a dock panel in `eve.html` first?
3. Do kept videos get an "why kept" note field the Architect fills, or only what Eve inferred?
4. yt-dlp version pinning: vendored binary vs `winget`/`pip` install, and what the health check says
   when it is missing.

## Promotion checklist (idea → Work Order)

- [ ] Open questions 1–2 answered (they change the scope).
- [ ] Acceptance statements confirmed as the definition of done.
- [ ] `yt-dlp` availability check designed (fail closed with a one-line message).
- [ ] Tool doc names + test file names chosen.
- [ ] Cache bounds and prune step written down.