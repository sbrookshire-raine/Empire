# REA integration — probe log

**Date:** 2026-10-21 · **Host:** Windows 11, `C:\EMPIRE` · **Branch:** `revision-refactor`
**Purpose:** the evidence trail behind the Bin-1 integration. Every claim below was
measured, not assumed. Each probe records what was run, what was observed, and
what it changed about the plan.

---

## P0 — Is the source real, and what is in it?

| Probe | Command | Result |
|---|---|---|
| Locate the bundle | `Get-ChildItem C:\EMPIRE -Recurse -Directory -Filter '*rea*'` | an unpacked bundle directory (index only) + the bundle tarball, both in a local upstream drop (`fromgumloop/`, not committed) |
| Extract the tree | `tar -xzf …tar.gz -C %TEMP%\rea_bundle_probe` | 22 skill directories, 74 files, all present |
| Read the index | `index.json` | `count: 22`, `bundle: rea-agent-skills`, upstream `morluto/rea`, MIT, packaged against REA **6.5.0** (`4f7b5fb`) |
| Verify the archive | `tar -tzf` | `manifest.json`, `verify.sh`, `install.sh` present — the bundle ships its own hash manifest |

**Finding:** the extracted directory held only `AGENTS.md`, `index.json`, `README.md`,
`VERSION`. The `skills/` tree is *inside the tarball*. Any plan that assumed a
checked-out skill tree would have read nothing.

**What is committed:** the six approved skills, under `vendor/rea-skills/`, with
the bundle's own `manifest.json` beside them. **What is not committed:** the
upstream drop itself (the unpacked bundle and the tarball) — it also contains
the 16 deferred Bin-3 skills, and shipping those would undo the triage this
integration is built on. The vendored tree is self-verifying: it carries the
upstream hashes, so a fresh clone can prove it got the right bytes without the
original drop (see P5c).

---

## P1 — Which six are Bin-1?

The upstream index carries the metadata the triage needs: `standalone`,
`needs_rea`, `tools`, `has_script`.

| Skill | standalone | needs_rea | external tools | Verdict |
|---|---|---|---|---|
| `rea-evidence-verification` | **true** | false | python3 | **Bin-1** |
| `rea-reconstruction-verification` | **true** | false | python3 | **Bin-1** |
| `rea-web-app-reconstruction` | **true** | false | python3 | **Bin-1** |
| `repo-forkdiving` | **true** | false | python3 | **Bin-1** (network) |
| `rea-target-free-readers` | **true** | false | objdump, gdb | **Bin-1** |
| `claim-ledger` | false | **false** | — (stdlib) | **Bin-1** |
| 11 `rea-*` CLI skills | false | **true** | rea CLI, ghidra, jadx, adb, frida, tshark, chromium… | Bin-3 |
| 5 protocol/utility skills | false | false | — (no script) | Bin-3 |

**Arithmetic check:** 5 `standalone:true` + `claim-ledger` = **6**. The remaining
**16** = 11 REA-CLI + 5 protocol/utility. This matches the approved 6/16 split
exactly, and is confirmed by the count of skills absent from the vendored tree
(pinned in `tests/pipeline/test_rea_skills.py`).

**Why `claim-ledger` is Bin-1 despite `standalone: false`:** it is the only skill
with `needs_rea: false` that ships a runnable script. The upstream flag
`standalone` means "no REA CLI *and* no script"; `claim-ledger` ships
`scripts/claim_ledger.py` and needs only the stdlib. It is also the only skill
the upstream review that preceded this integration kept as a candidate.

**Why the other 5 protocol/utility skills are Bin-3:** `agent-memory-architecture`,
`ai-experience-dialogue`, `intake-triage`, `source-capture` and
`tool-model-extraction` ship no script and no tool — they are prose procedures
that duplicate EMPIRE surfaces (Cognee memory tiers, the intake pipeline,
`read_document`, `tool_docs`). Adding them would add prompt weight with no
capability.

---

## P2 — What does EVE actually load, and will it accept these skills?

EVE 0.25.3 was read directly (`node_modules/eve/dist/src/`).

| Probe | File | Result |
|---|---|---|
| Skill discovery | `discover/skills.js` | `agent/skills/*.md` (flat) **or** a directory containing `SKILL.md` (package) |
| Frontmatter rules | `internal/helpers/markdown.js` | allowed keys: `description`, `files`, `license`, `markdown`, `metadata`; `name` is stripped and ignored |
| Strictness | `internal/authored-module.js` | `expectOnlyKnownKeys` throws on **any** unknown key |
| Package layout | `discover/filesystem.js` | a skill dir may contain `scripts/`, `references/`, `assets/` |

**Empirical frontmatter test** (run against EVE's own `lowerSkillMarkdown`):

```
FAIL  :: REA original (name+description+icon+color) :: Unknown key "icon".
PASS  :: REA minus icon/color :: description= "Does a thing." keys= description,markdown
PASS  :: with metadata :: keys= description,markdown,metadata
PASS  :: no frontmatter (flat, slug given)
```

**Finding — this changed the plan.** The upstream skills carry `icon:` and
`color:` frontmatter keys. EVE **rejects** them outright. Copying `SKILL.md`
verbatim would have produced six skills that silently fail to load. The
integration therefore ships **EMPIRE-authored skill files** in
`agent/skills/` (EVE-compatible frontmatter) that *route to* the vendored
upstream procedures, rather than dropping upstream `SKILL.md` files into the
agent's skill directory. The upstream files stay vendored, unmodified, as
reference material.

---

## P3 — Does the host have what the skills need?

| Probe | Command | Result |
|---|---|---|
| `python3` | `python3 --version` | **"Python was not found"** — Microsoft Store alias stub |
| `python` | `python --version` | 3.11.9 at `C:\EMPIRE\venv\Scripts\python.exe` |
| `objdump`, `gdb` | `Get-Command` | **MISSING** (so `rea-target-free-readers`' objdump lane cannot run) |
| `tshark`, `binwalk`, `adb`, `frida` | `Get-Command` | **MISSING** (Bin-3 skills — further reason to defer) |
| `node` | `Get-Command node` | `C:\Program Files\nodejs\node.exe` |
| `java` | `Get-Command java` | JDK 21 |
| REA package | `tools/rea/node_modules/rea-agents` | present, version **6.3.0** |
| REA MCP tools | live `listTools()` over stdio | **139 tools** |
| FastMCP | `python -c "from mcp.server.fastmcp import FastMCP"` | OK (SDK-bundled) |

**Finding — `python3` is unusable.** Every upstream skill documents
`python3 script.py`. On this host that is a Store stub that prints an error and
exits non-zero, so every skill would have "failed" for a reason that had
nothing to do with the skill. The runner resolves the interpreter itself
(`EMPIRE_REA_PYTHON` → repo venv → a real `python3`), and **reports which
interpreter ran** in every result, so a report can never claim a check ran
under an interpreter that does not exist.

**Finding — the installed REA is older than the bundle targets.** The bundle was
packaged against REA 6.5.0; `tools/rea` has 6.3.0. `rea-target-free-readers`
documents readers such as `inspect-go-binary` and `inspect-with-objdump` that
are **not** in the 139-tool list of the installed engine. The skill's *own*
script (`build_fixtures.py`) does run, and is what the integration exposes. The
skill body is kept as reference, with the limitation stated rather than papered over.

---

## P4 — Does the claim-ledger MCP work here?

The server was copied from the Gumloop handoff and exercised directly.

| Probe | Result |
|---|---|
| Import under SDK FastMCP | OK — tools `claim_add`, `claim_verify`, `claim_health`, `claim_list` |
| `claim_add` | OK — returns slug and `document`/`capability` |
| `claim_verify` (upstream code) | **FAILED** — `NotADirectoryError: [WinError 267] The directory name is invalid` |

**Root cause:** the upstream root parser split on `[;:]`. On Windows,
`C:\Users\...\tmp;D:\other` became `C`, `\Users\...\tmp`, `D`, `\other` — the
drive letter was shredded and the resulting working directory did not exist.

**A second bug, found while fixing the first:** the working directory was chosen
with `next((str(x) for x in ROOTS if _within(x, ROOTS)), str(ROOTS[0]))`.
`_within(x, ROOTS)` is true for every root, so the expression always returned
the *first* root and never actually checked that it existed.

**A third:** `shell=True` runs `cmd.exe` on Windows, where the POSIX operators
the upstream checks use (pipe, `grep`) do not exist — a POSIX check would report
a false failure.

**Fixes applied** (each pinned by a test in `tests/pipeline/test_claim_ledger.py`):
roots split on `;`/newline only; the working directory is the first root that
is a real directory; the shell is configurable and resolved to an absolute path
(`subprocess(executable=…)` does no PATH lookup, so a bare `cmd.exe` failed
with WinError 2 even though it is on PATH).

**Re-probe after the fix:**

```
ROOTS: ['C:\\Users\\m69nr\\AppData\\Local\\Temp\\claimledger-fix-f1bv8yyn']
ADD   -> {"ok": true, "slug": "probe-claim-true", "kind": "capability"}
VERIFY-> passed 1, failed 0
ADD2  -> slug probe-claim-false
VERIFY-> passed 1, failed 1   (exit 3)
HEALTH-> total 2, checked 2, passing 1, passing_pct 50,
          verdict "partly executable - checks exist but are failing"
```

---

## P5 — Do the upstream scripts actually run on this host?

All four offline skills were run against their **own upstream fixtures**.

| Skill | Script | Result |
|---|---|---|
| `rea-evidence-verification` | `verify_evidence.py` | `ok: true`, `passed: true` (all checks green) |
| `rea-reconstruction-verification` | `audit_reconstruction.py` | `ok: true`, `passed: true` (10 checks green) |
| `rea-target-free-readers` | `build_fixtures.py` | `ok: true` — built SQLite (2 rows), WASM (2 exports), EVM (2 selectors), Go + Rust sources |
| `rea-web-app-reconstruction` | `parity_harness.py` | `ok: true`, `status: comparisons-passed` (3/3 reference, 3/3 candidate) |
| `rea-web-app-reconstruction` | `parity_harness.py` (broken candidate) | **`ok: false`, exit 1**, `status: failed` — the harness can go red |

**Finding — the parity harness needed a Windows fix.** The upstream harness
splits the reference/candidate commands with POSIX `shlex`, where a backslash is
an escape character: `C:\EMPIRE\venv\Scripts\python.exe` arrived as
`C:EMPIREvenvScriptspython.exe` and the program could not be found
(`[WinError 2]`). The runner now emits forward-slash paths, which survive the
split and which Windows accepts.

**Finding — the parity harness takes *commands*, not paths.** `--reference` is
documented as `node target/app.mjs`; the candidate may be in any language. The
integration therefore jails the *path-like arguments inside* a command rather
than the command string itself, and refuses an absolute path that escapes the
scratch root.

---

## P5b — Is the vendored tree byte-identical to upstream?

The bundle ships its own SHA-256 manifest (`manifest.json`, one entry per file
per skill). A first copy of the six skills was checked against it and **five
files were missing**: the `rea-target-free-readers` example fixtures
(`gotest/main.go`, `module.wat`, `rusttest/Cargo.toml`, `rusttest/src/main.rs`)
and `repo-forkdiving/SKILL.md.nulbak`. A second copy attempt then *nested* the
directories (`vendor/rea-skills/rea-target-free-readers/rea-target-free-readers/…`)
instead of merging them — PowerShell's `Copy-Item` semantics, not a skill
problem.

**Finding:** "the files are there" is not the same as "the files are right".
The vendored tree is now re-copied correctly and **`manifest.json` is vendored
with it**, and `tests/pipeline/test_rea_skills.py` checks every vendored file
against the upstream SHA-256. A half-copied or tampered file now fails the
build rather than quietly changing what EMPIRE runs.

`SKILL.md.nulbak` is the upstream's NUL-padded backup of the `repo-forkdiving`
skill body (1,075 NUL bytes — the padding bug the Gumloop review documents). It
is vendored as-is because the manifest lists it, and it is never loaded: EVE
reads only `SKILL.md`.

### P5c — Would the integrity check survive a fresh clone? (it did not)

The hash check above only proves the tree is intact **in this working copy**.
The repo has `core.autocrlf=true`, and the vendored files are LF on disk. So
the obvious next question: what does a *fresh Windows clone* look like?

**Finding: the integrity test would have failed for anyone who cloned the repo.**
The tree was committed without a `.gitattributes`, so Git applied the CRLF
conversion on checkout and rewrote 30 of the 31 hash-pinned files:

| Clone state | Files checked | SHA-256 mismatches |
|---|---|---|
| Fresh clone, `core.autocrlf=true`, no `.gitattributes` | 31 | **30** |
| Fresh clone, with `vendor/rea-skills/** -text` | 31 | **0** |

The NUL-padded `SKILL.md.nulbak` was unaffected (Git treats it as binary
because of the NUL bytes) — it was the 30 *text* files that drifted.

**Fix:** a `.gitattributes` marks the vendored tree as `-text`, so Git stores
and checks it out byte-for-byte. Verified end to end: commit the tree to a
scratch repo, clone it with `core.autocrlf=true`, re-run the manifest check
against the clone — 0 mismatches, and the staged blob hash equals the raw file
hash (`git hash-object --no-filters` == `git rev-parse :path`).

This is the kind of failure that hides: the tree is intact locally, every test
passes here, and the repo still breaks for the next person.

---

## P6 — What did the integration change in EMPIRE's own gates?

`mechanic-green` and the unit suite were run at `HEAD` (a clean worktree) and
again with the integration applied, so pre-existing failures could be separated
from regressions.

| Gate | Baseline (HEAD) | With integration | Verdict |
|---|---|---|---|
| Unit suite | 643 tests, **9 fail** | 643 tests, **8 fail** | no regression; one baseline failure now passes |
| `playbook --coverage` | pass | pass (102 tools, 38 skills) | pass |
| Capability governance | 7 capabilities verified | **9** capabilities, 15 tools, 0 fail | pass |
| `capability_verification` (offline) | — | **34 pass, 0 fail** | pass |
| `tsc` typecheck | 1 error (`sandbox.ts`, pre-existing) | 1 error (same file, untouched) | no regression |
| Prompt budget — instructions | 5033 tokens (ceiling 5050) | **4940** | improved |

**Two regressions were found and fixed during the integration:**

1. `test_capability_seed` asserted `tool_count == 13`; the seed now has 15
   tools. The assertion was updated to 15 and extended to assert the two new
   capability ids.
2. `test_instruction_weight_under_ceiling` failed at 5071 tokens (ceiling 5050).
   The cause was **not** the new tools — it was a pre-existing duplication in
   `pipeline/eve_operating_context.py`: the verified-tool list was written
   twice (once inside the pulse snippet, once again as a "Proven names
   (sample)" line). The duplicate line was removed; the information is still in
   the snippet. This *lowered* the always-on prompt below its pre-integration
   size.

**The 8 remaining failures are pre-existing and unrelated** to this work:
two `eve_workbench_static` CSS/markup assertions, two `wiki_drift_api` band-name
lookups, one `intake-and-legos` playbook area with thin sections, and the two
prompt-budget ceilings (`default_schema_weight`, `floor_leaves_conversation_headroom`)
which fail at baseline too (1447 and 6481 tokens; this work lowered the floor to
6387, still above the 6250 ceiling).

**Baseline measured, not assumed.** A clean `git worktree` at HEAD (`7081ea5`)
was run with the same command to separate pre-existing failures from new ones:

| | Tests | Failures |
|---|---|---|
| Clean HEAD worktree | 643 | 8 |
| This worktree | 678 | 8 |

The failure *names* and *reasons* match one-for-one across the two runs, so this
work added 35 tests and **zero** new failures.

---

## P7 — Live tiers

The full stack was brought up for this verification: PocketBase (8090), the
frontend (8080), Eve (2000), Ollama (11434), Speaches (8000) and the Cognee
Postgres container (5432, `V:\Cognee` mounted).

### The tools work on the wire, not just in a test

A real Eve turn was sent through the frontend proxy, asking Eve to call
`rea_skills(action="list")` and `claim_ledger(action="health")`. The NDJSON
transcript shows both tool calls and both results:

```
actions.requested :: {"actions": [{"input": {"action": "list"}, "kind": "tool-call",
                     "toolName": "rea_skills"}]}
action.result     :: {"output": {"ok": true, "root": "C:\\EMPIRE\\vendor\\rea-skills",
                     "count": 6, "skills": [...]}, "toolName": "rea_skills"}

actions.requested :: {"actions": [{"input": {"action": "health"}, "kind": "tool-call",
                     "toolName": "claim_ledger"}]}
action.result     :: {"output": {"ok": true, "total": 0, "verdict": "empty"},
                     "toolName": "claim_ledger"}
```

Eve's live agent info reports **38 static skills** (including
`skill-rea-skills` and `skill-claim-ledger`) and **0 discovery errors**.

A second live turn exercised the claim ledger end to end — add, verify, health:

```
RESULT: {"ok": true, "slug": "empire-rea-bin-1-integration-is-live", "kind": "capability"}
RESULT: {"ok": true, "passed": [{"slug": "empire-rea-bin-1-integration-is-live",
         "exit": 0, "output": ""}], "failed": [], "unchecked": [],
         "summary": "passed 1, failed 0, unchecked 0"}
RESULT: {"ok": true, "total": 1, "checked": 1, "passing": 1, "unchecked": 0,
         "checked_pct": 100, "passing_pct": 100,
         "verdict": "forge - most claims are executable and true"}
```

A real check ran and passed, and the health number moved — which is the whole
point of the limb.

### Gate results with the stack up

| Gate | Result |
|---|---|
| `baseline-audit.ps1` | PASS (after reaping two orphan `llama-server` processes left by the Ollama restart) |
| Unit tests | 678 tests, 8 fail — all pre-existing; the clean-HEAD baseline is 643 tests with the same 8 failures |
| `verify-capabilities.ps1` (offline) | PASS |
| `verify-capabilities.ps1 -Live` | **PASS — 36 checks, 0 failed, `live_ran: true`** |
| Capability governance (fail-closed) | PASS — 9 capabilities, 15 tools, 0 fail |
| LEGO contract | PASS |
| Foundation registry | PASS (advisory) |
| Infra checks | PASS (advisory) |
| Workbench UI harness | PASS — 15 passed |
| `verify-stack.py` | **PASS — 19 passed, 0 failed, 0 skipped** |
| `audit-empire.py` (operating contract) | **PASS — "contract satisfied"** |

### `mechanic-green`, captured in full

The gate was run to completion on the committed tree with unfiltered output
(the capture lives in the local `tmp/` scratch dir, which is git-ignored). It
exits **1**, and the reason is exactly one step — the pre-existing unit
failures above:

```
PASS baseline audit (L1-L4)
FAIL unit tests (exit 1)          <- 678 tests fail=8 err=0, all pre-existing
PASS verify-capabilities (offline)
PASS capability governance (fail-closed)
PASS LEGO contract (check-legos)
PASS foundation registry (check-foundation, advisory)
PASS infra checks (deptry/ruff/gitleaks, advisory)
SKIP wiki extract battery (no I:\EMPIRE_DATA\wiki-reports\... title-index.sqlite)
PASS workbench UI harness (node)
PASS verify-stack
PASS operating contract (audit-empire)   <- "contract satisfied"
```

Ten steps pass, one fails, and that one is the same eight failures the clean
HEAD worktree produces. `mechanic-green` therefore still reports "1 step(s)
failed - do not hand to Architect yet" — correctly, because it cannot tell
pre-existing failures from new ones. That is why the HEAD worktree comparison
above exists.

The two non-code failures along the way were environmental, and both are
documented in AGENTS.md:

- `audit-empire` reported `llama3.1:latest loaded at ctx 4096, contract says
  24576`. The documented remedy was applied
  (`ensure-ollama-parallel.ps1 -NumParallel 1 -ContextLength 24576
  -KvCacheType q8_0 -FlashAttention`), after which the audit reported
  *"contract satisfied"*.
- The baseline audit then flagged two orphan `llama-server` processes left by
  that restart; they were reaped and the audit passed.

### Still not run

| Tier | Status | Reason |
|---|---|---|
| `verify-capabilities.ps1 -Live -SyncCognee` | **not run** | it would write the verification report into the Cognee `eve_core` dataset; the offline + live reports were already written to disk, and the Architect has not asked for the memory write |
| `forkdive` / `discover` (network skills) | **not run** | they reach the public network for repo data; the scripts load and their arguments are validated, but no live GitHub call was made |
| REA engine lanes (Ghidra, JADX, Frida) | **not run** | not required by Bin-1; `objdump`/`gdb` are absent on this host |

These are reported as **not run**, not as passed.
