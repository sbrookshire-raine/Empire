# EMPIRE Agent Updates Log

**Purpose:** Append-only continuity record for Architect + coding agents. Read this
after [`EMPIRE_GUIDE.md`](../EMPIRE_GUIDE.md) when resuming work after a compacted
chat, credit limit, crash, or handoff to a new agent.

This is an operational journal, not the product backlog:

| Need | Canonical location |
|---|---|
| Product ideas, Architect smoke items, future forge work | [`EMPIRE_IDEA_QUEUE.md`](EMPIRE_IDEA_QUEUE.md) |
| Human/AI project bootstrap and architecture | [`EMPIRE_GUIDE.md`](../EMPIRE_GUIDE.md) |
| Cursor implementation request | `C:\Empire_Workbench\05_Work_Orders\` |
| What changed, what was validated, and exact next handoff | **This file** |

## Operating rules

1. **Append; do not rewrite history.** Correct an earlier entry with a new dated
   entry that names the correction.
2. Record exact commands, tests, paths, branch, and outcomes. Do not claim a test
   passed unless it actually exited successfully.
3. Clearly distinguish **source changes** from generated/runtime artifacts. Do not
   stage or clean incidental workspace changes without Architect review.
4. Preserve `C:\Empire_Workbench` as Architect-owned and non-destructive. In
   particular, `05_Work_Orders` is a harness handoff, not a general scratch area.
5. Before UX handoff, run `.\scripts\mechanic-green.ps1`; use `-Full` when live
   Eve/Workbench behavior is involved. Architect smoke is product validation, not CI.
6. For heavy/GPU products, do not start a job, copy/move personal input, or change
   Toolbelt state merely to test unless the Architect explicitly requests it. Prefer
   read-only status/list checks first.

## Resume checklist

1. Confirm branch and preserve unrelated changes:

   ```powershell
   Set-Location C:\EMPIRE
   git branch --show-current
   git status --short
   ```

2. Check live services only if the task needs them:

   ```powershell
   .\scripts\verify-stack.ps1
   ```

3. Read the newest entry below, then open only its listed source/test files.
4. After a source/test change, run targeted tests first, then the authoritative gate:

   ```powershell
   .\scripts\advance-arms.ps1 -Continue
   .\scripts\mechanic-green.ps1 -Full
   .\venv\Scripts\python.exe .\scripts\smoke-eve-hands.py --eve-chat
   ```

---

## 2026-09-18 — Governed-arms validation and Stem Factory diagnosis

### Intent

Validate the live `cursor/eve-governed-arms` stack, identify the prior
`mechanic-green -Full` failure, and investigate why Eve said she could not navigate
the filesystem after an MP3 was placed outside the Stem Factory inbox.

### Branch and preserved workspace state

- Branch: `cursor/eve-governed-arms`
- Do **not** clean or stage unrelated/generated state. Existing incidental changes
  included dashboard/verify-stack snapshots, local MCP variants, `audio_conversion/`,
  `tmp/`, eval logs, and helper scripts.
- Intentional source/test changes made in this pass:
  - `tests\pipeline\test_admission_controller.py`
  - `tests\pipeline\test_stem_factory.py` (new)
  - `docs\AGENT_UPDATES_LOG.md` (this file)

### Validation results

| Check | Result | Notes |
|---|---:|---|
| `scripts\advance-arms.ps1 -Continue` | PASS | Governed-arm phases P0–P4 passed. |
| Canonical unit suite | PASS | 361 tests, 0 failures, 0 errors. Use the discovery invocation inside `scripts\mechanic-green.ps1`, not a bare `unittest discover -s tests`, which can resolve `tests\pipeline` incorrectly. |
| `scripts\mechanic-green.ps1 -Full` | PASS | Unit suite, fail-closed capability governance, wiki battery, stack verification, and all 14 live Workbench stages passed. |
| `scripts\smoke-eve-hands.py --eve-chat` | PASS | Resource pulse, light autonomous admission, GitHub Scout, offline workspace search, Switchboard safety, and live Eve tool-call behavior passed. |
| Stem Factory backend `python -m pipeline.stem_factory status` | PASS | Shard venv resolves, Demucs import succeeds, CUDA available. |
| Live Eve Stem Factory chat | PASS, read-only | With Stem Factory active, Eve called `stem_status` and `stem_list_inbox`; no separation job was launched. |

### Mechanic failure fixed

**Original failure:**

```text
tests.pipeline.test_admission_controller.AdmissionControllerTests.
test_non_auto_category_denied
```

**Cause:** The test depended on the real per-user Toolbelt file at
`%LOCALAPPDATA%\EMPIRE\eve-toolbelt.json`. Stem Factory was manually enabled there,
so `request_capability("stem_factory", ...)` correctly returned already-active instead
of exercising auto-admission denial.

**Fix:** Mock `frontend.eve_toolbelt.category_enabled` to `False` inside that test and
assert the explicit `cannot be auto-enabled` response. This preserves policy:

- `stem_factory` remains `auto_enable: false`;
- it remains GPU tenant `stem`;
- Eve may not autonomously enable it through `admit_for_goal`;
- the Architect enables the product limb deliberately.

### Stem Factory: verified current behavior

**Healthy local runtime:**

| Item | Value |
|---|---|
| Product Toolbelt category | `stem_factory` |
| Live per-user Toolbelt | `%LOCALAPPDATA%\EMPIRE\eve-toolbelt.json` includes `stem_factory` |
| Shard project | `C:\Users\m69nr\OneDrive\Desktop\HIDDEN\Shard_of_the_Division` |
| Working Python | `...\Shard_of_the_Division\.venv-cuda\Scripts\python.exe` |
| CUDA | Available |
| Bounded inbox | `C:\Empire_Workbench\stem_factory\input` |
| Bounded output | `C:\Empire_Workbench\stem_factory\output` |
| Eve tools when product limb is active | `stem_status`, `stem_list_inbox`, `stem_run` |

**Important constraint:** Stem Factory is deliberately **not** general filesystem
access. Its wrapper allows only approved roots and its Eve tool has no arbitrary
source-path input. The configured inbox had no audio at validation time (only
`README.md`).

**Observed user source file not processable by current intake:**

```text
C:\EMPIRE\audio_conversion\Frown - 04 - Enslaved Hope.mp3
```

It is outside the Stem Factory approved input roots. The current user workflow is:

1. User copies/drops an audio file into `C:\Empire_Workbench\stem_factory\input`.
2. Eve calls `stem_list_inbox`.
3. Eve calls `stem_run` (default `limit=1`; GPU-heavy; may take minutes).
4. Outputs appear under `C:\Empire_Workbench\stem_factory\output`.

The historical chat summary contains Eve's earlier incorrect “I cannot access the
filesystem” wording. The live validation confirmed that the current turn used the
real bounded Stem Factory tools. Do not mistake quoted historical context in an
NDJSON stream for the current turn's tool behavior.

### Tests added for Stem Factory safety

`tests\pipeline\test_stem_factory.py` covers:

1. `list_inbox()` lists supported audio files in the approved inbox and ignores
   non-audio files.
2. `run_stems()` rejects an input path outside approved roots.

### Highest-value next feature: bounded audio intake

Implement a narrowly scoped import capability rather than unrestricted filesystem
browsing. Candidate contract:

```text
stem_import_audio(source_path, copy=true)
```

Required policy:

- Explicit user-supplied source path only; no recursive drive scan.
- Accept known audio extensions only.
- Validate existence, regular-file status, reasonable size, and canonical path.
- Copy by default; never move/delete source without separate explicit confirmation.
- Destination must always be `C:\Empire_Workbench\stem_factory\input`.
- Avoid overwriting: deterministic collision-safe destination name or explicit
  overwrite flag that defaults false.
- Return source, destination, byte count, and any collision/validation result.
- Keep `stem_run` limited to the approved inbox/output roots.
- Add focused unit tests for accepted audio, extension/path rejection, collision
  handling, and no-source-deletion behavior.
- Add an Eve dynamic tool and routing/skill instruction: when a user names an audio
  file outside the inbox, ask for confirmation before copying it into the inbox;
  then list and optionally run it. Heavy GPU separation still requires the existing
  explicit Stem Factory product limb.

Likely implementation locations:

| Concern | Path |
|---|---|
| Python bounded wrapper | `pipeline\stem_factory.py` |
| FastMCP endpoint | `mcp\stem_factory_mcp.py` |
| Eve MCP client | `agents\empire-task-agent\agent\lib\stem-factory-mcp.ts` |
| Eve dynamic tool definitions | `agents\empire-task-agent\agent\tools\stem_*.ts` |
| Agent routing | `agents\empire-task-agent\agent\empire-routing.md` |
| Product skill | `agents\empire-task-agent\agent\skills\skill-stem-factory.md` |
| Focused tests | `tests\pipeline\test_stem_factory.py` |

### Separate next major governed-arms task

Add shared fail-closed `verify_capability()` enforcement at real Python governed-arm
pipeline entrypoints. Current capability schema verification is green in seed/CI
gates and TypeScript/MCP wrappers, but it is not yet uniformly enforced at each
Python execution boundary. Add focused tests for approved, absent, and drifted
snapshots. Do not combine this large governance task with the bounded audio-import
feature unless the Architect explicitly requests that scope.

---

## Append template

Copy this section to the end for every meaningful work session:

```markdown
## YYYY-MM-DD — Short outcome title

### Intent
- What was being validated or changed.

### Changed
- `absolute-or-repo-relative/path`: concise reason.

### Validated
| Command / check | Result | Relevant output |
|---|---:|---|
| `...` | PASS/FAIL | ... |

### Known limitations / blockers
- Concrete behavior, not speculation.

### Resume next
1. Exact first action.
2. Exact target tests/commands.
3. Explicit safety or ownership constraints.

### Workspace caution
- Branch:
- Intentional modified files:
- Incidental/generated files to preserve:
```