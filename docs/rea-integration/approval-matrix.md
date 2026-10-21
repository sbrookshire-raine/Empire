# REA integration — approval matrix

**Date:** 2026-10-21 · **Scope:** the 22-skill Gumloop REA bundle
**Decision rule:** a skill is **Bin-1** only if it can run on this host with
nothing beyond a local Python, *and* it adds a capability EMPIRE does not
already have. Everything else is **Bin-3** and stays out of the tree.

Evidence for every row is in [`probe-log.md`](probe-log.md).

---

## Bin-1 — approved and integrated (6)

| Skill | Why it earns Bin-1 | How it is exposed | Verified |
|---|---|---|---|
| `claim-ledger` | Stores claims **with the command that would falsify them**. Cognee stores text for *recall*; this stores claims for *execution*. A check cannot go stale silently. | `claim_ledger` tool → `mcp/claim_ledger_mcp.py` (vendored) | add / verify / health / list all pass; a failing check is reported as a failure |
| `rea-evidence-verification` | Audits an Evidence record and the claims resting on it, so a conclusion is never stated more strongly than its evidence supports. EMPIRE has no such audit. | `rea_skills(action="verify_evidence")` | `verify_evidence.py` passes on the upstream good record |
| `rea-reconstruction-verification` | Checks a reconstruction's ledgers, digests and duplicate addresses. "Is this reconstruction actually correct?" had no answer in EMPIRE. | `rea_skills(action="audit_reconstruction")` | `audit_reconstruction.py` passes, 10 checks green |
| `rea-web-app-reconstruction` | Proves a rebuild matches a reference over a **frozen corpus**, scoring reference and candidate separately against literals — not against each other. | `rea_skills(action="parity_check")` | 3/3 pass for a matching rebuild; the broken candidate **fails** (exit 1) |
| `rea-target-free-readers` | Reads Go/Rust/WASM/EVM/SQLite metadata **without a disassembler** — the cheapest path, and the one least likely to fail on setup. | `rea_skills(action="build_fixtures")` | fixtures built locally: SQLite (2 rows), WASM (2 exports), EVM (2 selectors) |
| `repo-forkdiving` | Mines a repo's fork network and derivatives for **proven** use cases. EMPIRE has `github_scout` (search), not prior art. | `rea_skills(action="forkdive" / "discover")` | script present and loadable; **network run not executed** |

**Why `claim-ledger` counts even though the upstream index marks it `standalone: false`:**
it is the only skill with `needs_rea: false` that ships a runnable script. The
`standalone` flag means "no REA CLI *and* no script"; `claim-ledger` ships
`scripts/claim_ledger.py` and needs only the stdlib. The upstream review that
preceded this integration also kept it as the single surviving candidate.

---

## Bin-3 — deferred, deliberately absent (16)

Nothing in this table is vendored, registered, routed, or mentioned to Eve.
`tests/pipeline/test_rea_skills.py` asserts their absence, so a later import
cannot slip in unnoticed.

### 3a — REA-CLI skills (11): need an analysis engine this host does not have

| Skill | Needs | Why deferred |
|---|---|---|
| `rea-investigation-setup` | REA CLI + node | Entry point for the REA engine; EMPIRE already has `rea_doctor` / `rea_invoke` for the same job. |
| `rea-native-function-recovery` | REA + Ghidra/Hopper/IDA | Native decompilation. Ghidra is present, but the skill's readers are not in the installed engine's 139-tool list. |
| `rea-android-apk-trace` | REA + jadx/apktool | No JADX jar, no apktool on this host. |
| `rea-android-device-adb` | REA + adb | `adb` absent; no device attached. |
| `rea-firmware-extraction` | REA + binwalk/unblob | `binwalk` absent. |
| `rea-browser-runtime-observation` | REA + chromium | No chromium driver configured. |
| `rea-managed-dotnet-trace` | REA | CIL tracing; duplicates the installed engine's own `inspect_managed_*` tools. |
| `rea-mobile-package-formats` | REA | Format identification; no EMPIRE problem it solves. |
| `rea-packet-and-signal-capture` | REA + tshark/sigrok | `tshark` absent. |
| `rea-runtime-instrumentation` | REA + frida | `frida` absent; instrumenting a running process is also the highest-risk lane. |
| `rea-static-js-electron-trace` | REA + node | EMPIRE already has `rea_analyze_javascript` for this exact job. |

### 3b — protocol/utility skills (5): no script, and they duplicate EMPIRE

| Skill | Why deferred |
|---|---|
| `agent-memory-architecture` | Memory tiers and promotion — Cognee plus `eve_staging` already own this. |
| `ai-experience-dialogue` | A conversation protocol, not a capability. Adds prompt weight, no executable. |
| `intake-triage` | Intake and triage — EMPIRE's own `intake_to_lego` / `research_desk` already own this. |
| `source-capture` | Capture and compress sources — `read_document` / `docs_guide_scraper` already own this. |
| `tool-model-extraction` | Build a tool model from docs — `tool_docs` + `capability_route` already own this. |

---

## Safety invariants the integration holds

| Invariant | How it is enforced | Pinned by |
|---|---|---|
| Only the six approved skills are reachable | `BIN1_SKILLS` allowlist in `pipeline/rea_skills.py`; the deferred set is not vendored | `AllowlistTests` |
| No path escapes the scratch root | `pipeline.paths.resolve_within` for every file/dir argument; an escape is **refused**, not rewritten | `PathJailTests` |
| The vendored upstream tree is never modified | Scripts are copied into a scratch workdir before running; upstream stays byte-identical | `test_the_vendored_tree_is_never_modified_by_a_run` |
| The vendored tree is byte-identical to upstream | The bundle's own SHA-256 `manifest.json` is vendored and every file is checked against it | `VendoredTreeIntegrityTests` |
| A failure is never dressed as a success | Non-zero exit → `ok: false` with the output; a missing interpreter/script fails closed | `ReportShapeTests` |
| The report cannot claim a check ran under a broken interpreter | The interpreter is resolved explicitly and reported in every result | `InterpreterTests` |
| Claim checks stay inside a declared root | Roots are parsed without shredding the drive letter; the working directory must exist | `test_claim_ledger.py` |
| The always-on prompt does not grow | The new tools are gated limbs; prose lives in tool docs and the playbook | `test_prompt_budget.py` |

---

## Rollback

One command, no state left behind:

```powershell
.\scripts\rollback-rea-integration.ps1
```

It removes the two tools, two skill files, the vendored tree, the MCP server and
its registration, the two capabilities from the registry/manifest, and the
playbook/routing entries — then re-seeds the registry and regenerates the
operating context. `git checkout` on the tracked files is the fallback.
