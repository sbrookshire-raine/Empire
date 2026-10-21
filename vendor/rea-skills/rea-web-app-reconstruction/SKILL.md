---
name: rea-web-app-reconstruction
description: Reconstruct or clone a web app, API, or file format from its observable behavior. Use when rebuilding a frontend, a backend service, a wire protocol, or a save format and the rebuild must be provably equivalent. Keywords: parity, clone, api, file format, clean-room, harness, reference, migration. Do not use for a native binary or APK - use rea-native-function-recovery or rea-android-apk-trace.
icon: IconCode
color: Bronze
---

# Web app, API, and format reconstruction

Rebuild a running system from what it *does*, not from its source. This covers
frontends, backends, wire protocols, and file formats — anything where you can
observe behavior and must prove your rebuild matches.

The method is the same at every layer: **freeze a reference, write expectations
independently, rebuild, compare each side to the literals, and prove the
comparison rejects.** What changes between layers is what you observe.

## Prerequisites

- A **reference** you are authorized to observe, and its frozen bytes/hashes.
- For the parity harness: any language runtime for the candidate; the interface
  is JSON over stdin/stdout plus an exit code.
- For browser work: a real browser and a disposable profile.
- No analysis engine is required.

## When to use it

- Cloning a web app's behavior for personal study or a local rebuild.
- Reimplementing an API or service you can call but cannot read.
- Rebuilding a file format's reader/writer from sample files.
- Recovering a wire protocol from captured traffic.
- Verifying that an "improved" version still honors the original's contracts.

## When not to use it

- You have the source and just want to read it — read it.
- You only need to understand behavior, not reproduce it — use
  `rea-browser-runtime-observation` or `rea-static-js-electron-trace`.
- The target is a native binary with no observable interface — use
  `rea-native-function-recovery`.

## The clean-room boundary — read this first

This skill exists to help you **learn how a system works and rebuild it for
yourself**. That is legitimate. The line is not "did you look at it" — it is
**what you ship**.

| You may | You may not |
| --- | --- |
| Observe a running system's behavior | Copy their source, assets, or data into your rebuild |
| Read shipped code to understand a mechanism | Redistribute their code or bundled assets |
| Reimplement the behavior yourself | Ship their trademarks, logos, or proprietary content |
| Study a format by inspecting sample files | Bypass DRM or license checks |
| Build a local tool for personal use | Publish a clone that competes on their assets |

**Record the boundary in the artifact.** State the license of the reference, that
the rebuild is an independent implementation, and that no original code or assets
were copied. The Companion's fixtures do this: every one carries an MIT license
line and an explicit "source-exposed same-agent" disclosure.

If a target's license forbids reverse engineering, or the goal is to circumvent a
protection measure, stop. That is outside this skill.

## The reference / parity / improved triple

Keep three things separate, always. Conflating them is the most common way a
reconstruction fools itself.

| Artifact | What it is | Rule |
| --- | --- | --- |
| **Reference** | The original, frozen | Never modify. Hash it. |
| **Parity** | Your rebuild, aiming to match | Byte-identical to reference is the goal |
| **Improved** | Deliberate changes on top | Separate acceptance profile, frozen first |

The Companion's browser trial demonstrates the distinction concretely: the
`reference/` and `parity/` files are kept **byte-identical** (tests pin all four
original hashes), while `improved/` is a separate candidate that changes save
feedback and conflict recovery. Its acceptance profile was **frozen before
implementation** — so the improvement is judged against a standard written in
advance, not one reverse-engineered from the result.

**An improvement is not parity.** Report them separately. A matching silent
data-loss bug is a *baseline observation*, not a reliability pass.

## The parity harness

`scripts/parity_harness.py` compares a reference program and a candidate against
frozen literal expectations, over a scenario corpus, and reports each separately.

```bash
python3 scripts/parity_harness.py \
    --reference "node target/app.mjs" \
    --candidate "python3 my_rebuild.py" \
    --scenarios scenarios.json \
    --out report.json
```

The candidate may be **any language**: the interface is JSON over stdin/stdout
plus an exit code. This is the Companion's language-independent process interface
(`evals/reference/check.mjs`), generalized.

**Process contract.** Each step runs as a fresh process in a per-scenario
directory. State does not survive in memory between steps — a program that must
carry state persists it on disk in its cwd. This is deliberate: it makes restart
behavior testable, which is where real defects live.

**Why compare each to literals, not to each other.** Two programs that share a
defect agree with each other. The harness checks the reference *and* the
candidate against independently written expectations, so a shared defect is
caught. Verified:

```
correct candidate          -> comparisons-passed   (6/6 both sides)
broken candidate           -> failed, step named   (cand 1 pass, 2 fail)
candidate matching a WRONG reference -> failed     (both sides flagged)
in-memory-only candidate   -> failed at step 2     (contract working)
```

## Procedure

1. **Freeze the reference.** Record license, exact bytes, SHA-256, version,
   runtime, and the observation method. Keep reference, candidate, raw
   observations, and oracle in separate places. Preserve the original even when
   a rebuild would change it.

2. **Declare exposure.** A same-agent synthetic fixture is **source-exposed**
   even with separate folders. Separately written literals avoid self-comparison
   but do not become "independent". A genuine blind trial needs a separate
   author/reviewer — do not manufacture one with agents.

3. **Write expectations before the rebuild.** Literal inputs and expected
   outputs, authored independently of either implementation. Include boundary
   and rejection cases, not just the happy path.

4. **Rebuild against the contract.** Implement from the recorded behavior. Do
   not read the reference's source while writing the candidate if you want a
   clean-room claim — and if you do read it, say so.

5. **Compare each side to the literals.** Run the harness. A pass means
   agreement within that corpus and environment — not global equivalence.

6. **Prove the comparison rejects.** Mutate the candidate and confirm it fails.
   An oracle that only accepts is worthless. See
   `rea-reconstruction-verification` for the full rejection-test discipline.

## Layer-specific guidance

### Frontend / browser

Observe through the real browser, not a fetch. Record the origin, browser
profile, storage keys, and reset method — **different paths and tabs can share
persistent storage**, which silently corrupts comparisons.

- Isolate reference and candidate on **separate ports/origins**; deliberately
  share an origin only when testing concurrency.
- Reset disposable state before each independent run and assert the expected
  starting UI.
- Distinguish **page reload**, **fresh tab**, and **browser-process restart** —
  they exercise different persistence paths. Report unavailable stages as
  unrun rather than assuming they pass.
- Compare semantic fields, not incidental object-key order. Preserve meaningful
  row order, selection, and error state.
- Screenshot agreement alone does not validate data or interaction correctness.

The Companion's fixture injects faults deliberately (`Storage.prototype.setItem`
throwing `QuotaExceededError`, `navigator.locks.request` refusing) and **labels
them as fixture instrumentation, not real browser denial**. Do the same: a
controlled rejection is not evidence about real quota or permission behavior.

### Backend / API

- Capture real request/response pairs as the corpus. Record method, path,
  headers that matter, body, status, and error shape.
- Test **missing vs null** fields, unknown fields, and type errors separately —
  they often diverge.
- Check error precedence: when several defects are present, which one wins may
  be unspecified. Say so rather than inventing an order.
- Verify authentication, retry/idempotency, and ordering behavior if in scope.
- A mock returning success does not establish integration. Label each
  interaction verified-against-real, mock-only, proposed, or blocked.

### File formats

- Recover the **raw byte contract**: encoding, BOM, newlines, size bounds,
  schema/type checks, duplicate keys, order, numeric/string limits, versions.
- Check **expansion during migration**, not just input length — a small valid
  import can produce an unreadable oversized save. The Companion's trial caught
  exactly this: a v1 file at 8018 bytes would expand to 8243 as canonical v2.
- Test **both directions** (reference→candidate and candidate→reference) in each
  supported version. A round trip is supplemental: a reader and writer sharing a
  defect can agree.
- State when a downgrade is lossy, rejected, or transformed. Preserve
  representability limits instead of quietly dropping fields.
- Trace validation → staging → persistence → memory replacement → success.
  Reject *before* modifying committed state.

### Wire protocols

- Capture the whole bus/stream and filter at analysis time — a physical or
  network event may not be reproducible byte-for-byte.
- Record the matching pair: the same operation from both sides while conditions
  are identical.
- Distinguish controlled injections, controlled real I/O failures, and actual
  spontaneous failures. They are not the same evidence.

## Done when

- The reference is frozen and hashed, and the candidate is separate from it.
- The parity harness reports `comparisons-passed` for **both** sides against the
  literals, and a deliberately broken candidate **fails** with the step named.
- Every claim carries its evidence class, and the report states its limitations.
- The clean-room boundary is recorded in the artifact.

## Common failure modes

| Symptom | Cause | Fix |
| --- | --- | --- |
| Candidate passes but is wrong | Compared to the reference, not to literals | Compare each side to independent expectations |
| Oracle only ever accepts | No rejection test run | Mutate the candidate; it must fail |
| "Independent" literals from the same agent | Self-comparison in disguise | Declare source exposure |
| Improvement reported as parity | The two were conflated | Separate acceptance profiles, frozen first |
| Silent data loss scored as a pass | Baseline behavior mistaken for correctness | Report baseline observations as failures of the goal |
| Relative command fails in the harness | Per-scenario cwd isolation | Paths are absolutized; pass absolute paths if unsure |
| State lost between steps | In-memory-only program | Persist to disk in cwd — this is the contract |
| Finite corpus pass called equivalence | Corpus is not the world | State corpus size, environment, and limits |
| Controlled fault called real denial | Fixture instrumentation unlabeled | Label how each failure was produced |

## Validation

- `parity_harness.py` accepts a correct candidate and rejects a broken one,
  naming the failing step.
- A candidate that matches a deliberately wrong reference is still flagged.
- Every claim carries its evidence class; the report states its limitations.
- The clean-room boundary is recorded in the artifact.

## Provenance

**Method source** — [ShadowSwaps/REA-Reconstruction-Companion](https://github.com/ShadowSwaps/REA-Reconstruction-Companion),
manifest version `1.3.23`, observed 2026-10-18. Blobless clone; 189 files. The
reference/parity/improved triple, the language-independent process interface,
the file-format contract, and the browser fault-injection fixture are from its
`evals/reference/`, `evals/browser-improvement/`, `evals/import-export/`, and
`references/file-compatibility.md`.

**Verified by reproduction:**

```
node evals/reference/check.mjs --reference
    -> reference-self-check, comparisons-passed, 16/16 sessions
node evals/reference/prepare.mjs /tmp/ref
    -> packet identity pinned: TASK.md + target/pocket-tasks.mjs SHA-256
node evals/import-export/check.mjs
    -> passed, 33 cases per target (reference and candidate)
parity_harness.py (this skill's script), three tests:
    correct candidate        -> comparisons-passed (6/6 both sides)
    broken candidate         -> failed, step named
    candidate matching wrong reference -> failed (both sides flagged)
```

**From sources:** the browser improvement profile, the import/export contract
(R1/R2/R3), and the format-recovery procedure are quoted from the Companion's
own documents. Its fixtures are **source-exposed same-agent** synthetic
examples; their own `limitations` fields say so, and this skill repeats it.

**Not tested here:** a real third-party web app or API; a real browser-process
restart; a live service. The harness was verified against local fixtures only.

## Confidence

- **Verified by reproduction:** the parity harness was run on three fixtures and
  behaved correctly in all three (accept, reject-with-step, shared-defect
  caught). The Companion's reference and import-export oracles were executed and
  passed. A bug was found and fixed during this work: per-scenario cwd isolation
  broke relative command paths, producing false failures on a correct candidate.
- **From sources:** the reference/parity/improved discipline, the format
  contract structure, and the browser fault-injection approach.
- **Limitation:** all fixtures are local and synthetic. No real third-party
  target was reconstructed, so the method is proven on its own harness, not yet
  on an external system.
