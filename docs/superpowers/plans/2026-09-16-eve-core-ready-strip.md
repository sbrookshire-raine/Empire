# Eve Core Ready Strip Implementation Plan

> **For agentic workers:** Implement task-by-task. Steps use checkbox syntax.

**Goal:** Put Voice + Wiki as clickable green/amber/dim pills beside the mode picker; remove them from the Tools dock; keep Eve toolbelt access unchanged.

**Architecture:** UI relocate only. Pills call existing `setToolbeltCategory`. Health: `/api/voice/health` + `glasses_ok` on `/api/wiki/status`. Dock filters `readyStripIds`.

**Tech Stack:** Alpine Workbench (`eve.html` / `eve-workbench.js` / CSS), Python `wiki_api.py`, unittest.

## Global Constraints

- Keep existing neon/paper colors; no new palette
- Defaults stay `voice_presence` + `wiki_local` on
- No second permission system — same `active_tools` path Eve already uses
- Mechanic-green before Architect UX smoke

---

### Task 1: Wiki glasses_ok probe

**Files:**
- Modify: `frontend/wiki_api.py` (`wiki_status`)
- Test: `tests/frontend/test_wiki_glasses_status.py` (new)

- [ ] Add `glasses_ok` / `glasses_reason` to `wiki_status` (Title DNS sqlite exists + wiki_md year root exists)
- [ ] Unit test with temp paths mocked

### Task 2: Ready strip UI

**Files:**
- Modify: `frontend/eve.html`, `frontend/eve-workbench.js`, `frontend/eve-workbench.css`
- Modify: `docs/EMPIRE_CLARITY.md` (one note)

- [ ] Markup after mode picker
- [ ] JS: readyStrip items, refreshReadyHealth, dock filter, click toggle
- [ ] CSS for pills/dots
- [ ] Clarity note

### Task 3: Verify

- [ ] Unit tests + `.\scripts\mechanic-green.ps1` (or `-SkipStack` if stack flaky; prefer full green)
