---
name: rea-reconstruction-verification
description: Prove a reconstruction is correct, on any of three axes. Use when a claim must be provable: byte-exact compiler matching, whole-image hash contracts, behavioral artifact contracts against a frozen corpus, obligation ledgers, independent oracles, or deciding whether a reconstruction is actually done. Keywords: byte-exact, oracle, ledger, parity, matching, reccmp, objdiff, decomp-permuter, shiftable, frozen corpus, acceptance. Do not use to perform the recovery - use rea-native-function-recovery.
icon: IconChecklist
color: Bronze
---

# Reconstruction verification

Recovering source from a binary is only half the work. The other half is
proving the recovery is correct without fooling yourself. This skill captures
the verification methodology that the DX-Ball and TH04 reconstructions use to
make claims that survive scrutiny.

The core rule, stated by both projects: **no score or supporting oracle can
override a failed exact requirement.** A 99% similarity is not a match.

## Prerequisites

- The **original artifact** and its SHA-256, or a frozen literal corpus.
- For the byte-exact axis: the original toolchain (compiler version, flags).
- For the behavioral axis: a scenario corpus and independently written
  expectations.
- No analysis engine is required to run the audit script; it reads ledgers.

## When to use it

- Reconstructing a function and needing to prove it matches the original.
- Setting up a reconstruction project that will run for many sessions.
- Deciding whether a reconstruction claim is actually established.
- Reviewing someone else's reconstruction claim.

## When not to use it

- One-off analysis where you only need to understand behavior, not reproduce it
  byte-for-byte — use `rea-native-function-recovery`.
- Targets with no original binary to compare against.

## The claim vocabulary

Use these words precisely. Three independent projects enforce this, and the
distinction is the whole point.

**TH08's acceptance language** (the most compact form):

| Term | Means |
| --- | --- |
| `mapped` | An address/name association exists; behavior may be incomplete |
| `implemented` | Source is selected by the build; exactness is not implied |
| `compiles` | The relevant build target succeeds |
| `matching` | The accepted comparator proves exact target code/data for the stated scope |
| `blocked` | A concrete missing input, boundary, mapping, or tool is named |

**TH04's evidence classes** (finer-grained, for per-claim records):

| Word | Means | Does NOT mean |
| --- | --- | --- |
| `observed` | Read directly from a hash-attested target | Understood |
| `compiler-observed` | Reproduced by a pinned toolchain probe | Correct source |
| `runtime-observed` | Reproduced under a recorded emulator scenario | Full fidelity |
| `corroborated` | Supported by a separate game or external source | Independent proof |
| `inferred` | Falsifiable best explanation | Established |
| `source-present` | Maintained source exists | Exact |
| `structural` | Configured non-byte structural checks pass | Byte-exact |
| `exact` | Complete configured bytes and relocations are identical | Behaviorally complete |

A name, a successful build, a normalized instruction match, or a screen
similarity is **not** an exact-match claim.

## Evidence ranking

When sources disagree, rank them. TH08's order, which generalizes:

1. The exact hash-attested target executable.
2. Target disassembly, bytes, imports, relocations, xrefs, runtime behavior.
3. Exact compiler/comparator output produced in your own repository.
4. Inherited or upstream source and mapping files.
5. Adjacent-version references, decompiler output, other secondary material.

Lower-ranked evidence helps form hypotheses but **cannot override target
bytes**. Record the target observation and the inference separately.

## Four ownership axes

A field or function has four independent owners. None implies the others, and
conflating them is the most common source of wrong names.

| Axis | Meaning |
| --- | --- |
| Storage owner | The aggregate or allocation whose lifetime contains the bytes |
| Semantic owner | The object or subsystem whose behavior the field describes |
| Emission owner | The original translation unit or COMDAT that emitted the code |
| Build owner | The production, exact-probe, or portable source selected for a build |

A helper located beside ECL code may semantically operate on `Enemy`; a class
method may have been emitted from a consumer translation unit; an exact probe
may hold accepted behavior while the production file still has a stub.

## Two verification toolchains

Two independent toolchains have been proven on real projects. Pick by target.

**COFF replay (DX-Ball, VC4.0).** Compile with the pinned compiler, read the
COFF relocations, map them to the original executable's functions/imports/data,
and compare the complete section. `config/match-units.toml` records the source,
compiler inputs, original extent, and relocation bindings per unit. An exact
unit has zero differences across that complete comparison.

**reccmp / objdiff (TH08, VC7).** A per-unit comparator driven by
`config/match-units.toml` (name, object, decorated COFF symbol, target address,
size) plus `reccmp-project.yml` (target hash, data sources). The comparator
decodes `__real@...` float relocations from their COFF symbols automatically,
normalizes only the anonymous-namespace `?A0x........` discriminator (which
varies with checkout path), and requires a unique section-defined function with
the same remaining decorated name and signature.

Both share the same acceptance rule: **only a reproducible comparison against
the exact target may support an exact-match claim.**

## Behavioral artifact contracts (the second axis)

Byte-exact matching is one axis. The other is **behavioral**: you cannot rebuild
the original bytes, but you can prove the reconstruction agrees with the original
on a frozen corpus of literal cases. This is the axis the
[REA-Reconstruction-Companion](https://github.com/ShadowSwaps/REA-Reconstruction-Companion)
uses, and it is the right one for managed/interpreted targets, format handlers,
CLI tools, and protocol implementations where a compiler match is impossible.

The two axes are not interchangeable. Say which one you are on.

| Axis | Proves | Requires |
| --- | --- | --- |
| Byte-exact | The same compiler emits the same bytes | Original toolchain, matching build |
| Behavioral | Agreement on a frozen literal corpus | Frozen reference bytes + independent literals |

### The six-step artifact trial

1. **Freeze before rebuilding.** Record license/authority, exact original bytes,
   SHA-256, format, runtime, build provenance, the selected behaviors, the literal
   acceptance/rejection expectations, and who authored the oracle. Keep reference,
   candidate, raw observations, and oracle in **separate** places. Preserve the
   original even when a rebuild changes timestamp/MVID.
2. **Declare exposure.** A same-agent synthetic fixture is **source-exposed** even
   when the folders are separate. Separately written literals avoid self-comparison
   but do not become "independent" or "hidden". A genuine blind trial needs a
   separate author/reviewer; do not manufacture one with agents.
3. **Route actual bytes.** Bind every finding to the artifact hash and to
   build-local coordinates (assembly MVID, method token). Metadata, strings, and
   CIL anchors are **not** decompiled source. An anchor summary can omit short
   constant opcodes and full control flow even when decoding is complete.
4. **Resolve consequential uncertainty.** Trace each requirement from static fact
   → explicit inference → a distinguishing runtime case. Test misleading strings
   and resources against active calls. Mark genuinely unavailable details as
   evidence-limited; do not leave behavior unknown once an observation resolves it.
5. **Build and challenge the comparison.** Run equivalent cases against the real
   reference and the candidate, comparing **each separately** to the frozen
   literals — stdout, stderr, exit code, and state. Keep raw output before any
   normalization. Reject capture failure, changed identity, missing/duplicate
   cases, and materially wrong candidates. **Agreement between two wrong programs
   is insufficient.**
6. **Keep evidence authority honest.** If a runtime adapter is unavailable, keep
   its concrete failure. An ordinary subprocess check is useful but is **not**
   canonical runtime Evidence — never relabel it to satisfy a typed verifier.

### The oracle must reject, not just accept

An oracle that only ever says "pass" is worthless. Prove it rejects before you
trust it. Three rejection tests, all runnable:

```bash
# 1. A deliberately faulty candidate must FAIL
#    (mutate a boundary, invert a guard, or use the misleading resource value)
node evals/artifact/check.mjs          # -> status: fail, with the failing case ids

# 2. A tampered frozen file must be REJECTED before any candidate runs
printf '\n' >> evals/artifact/corpus.json
node evals/artifact/check.mjs          # -> "Frozen bytes changed: corpus.json"

# 3. Restore and confirm PASS again
node evals/artifact/check.mjs          # -> status: pass-within-corpus
```

The reference implementation also ships **harness regression tests** that check
known-good candidates *and* deliberate defects, invalid case selection, malformed
worker results, output overflow, and accidental hangs. Run them:

```bash
node --test        # 482 tests, 479 pass, 3 skipped, 0 fail
```

Those are harness tests, **not** observed agent trials. Say so.

### The misleading-resource trap

A compiled artifact can carry a string or resource that states a rule the code
does not follow. In the Companion's Parcel fixture, `legacy-note.txt` says "all
fees are flat 99", and its hash matches the resource row — but the fee cases
contradict it, and no resource-loading call appears in the selected call edges.

**A string is not a behavior.** Test every human-readable claim against active
calls and actual runtime cases before believing it. Record the contradiction as a
finding; it is often the most valuable thing in the artifact.

### Bounded differential fuzzing and mutation testing

When a frozen corpus is too small to be convincing, extend it — under a declared
budget, in a disposable environment, never against a live service or a user's
real data:

- **Differential fuzzing.** Preserve a reference corpus and a comparator for
  outputs, errors, and state effects. Record target/version, reset procedure,
  generator/seed, size limits, and iteration/time budgets. Classify every
  difference as a behavioral discrepancy, allowed variation, reference defect, or
  harness failure. Minimize each discrepancy to the smallest reproducer and keep
  it as a regression case. **Coverage growth and a clean bounded run are not
  proof of equivalence.**
- **Mutation testing.** After ordinary tests pass, mutate a *disposable copy* of
  the reconstruction with a few plausible faults (off-by-one, inverted guard,
  removed validation, ignored auth failure). Record each as killed / survived /
  not covered / invalid-equivalent / inconclusive. A survivor is not automatically
  equivalent — it may expose a real gap in the oracle. Never ship a deliberate
  defect.

### What a finite pass does and does not establish

A pass establishes **agreement within that corpus and environment**. It is not
global equivalence, not decompiler correctness, not performance, and not security
validation. State the corpus size, the environment, and the limits in the report
itself — the Companion's checker emits them as a `limitations` field, which is the
right pattern.

### Dependency-selected revalidation (when the target changes)

Cold-replay-everything is correct but expensive. When a target changes version,
you can reuse prior verification **only where the bindings are unchanged** — and
you must prove which those are. The Companion's version-change trial does this
and it is the right pattern:

1. **Bind every claim to hashes, not to a version label.** Each verified
   requirement records the digests of the target, the candidate, the interface,
   the corpus, the harness, and the environment.
2. **On a version change, re-hash and diff the bindings.** A requirement whose
   bindings are all identical is **reused** with its original report digest
   retained. A requirement whose bindings changed is **re-executed** fresh.
3. **Report reused and executed separately**, with the binding hashes for each.
   Never let a reused result silently stand in for a re-run one.

The trial's own output is the model: `reused: [V-titles]` (bindings unchanged,
original report digest kept), `executed: [V-codec, V-interface, V-integration,
V-migration]` (bindings changed, re-run), and an explicit
`overallParity: "bounded selected workflows only; arbitrary inputs and external
applications unverified"`.

Two traps it demonstrates:

- **An old candidate must fail the new schema.** The trial records
  `oldCandidateMismatch: "schema2 rejected"` — the v1 candidate is *rejected*
  against the v2 contract rather than quietly accepted. Prove the version
  boundary rejects, the same way you prove the oracle rejects.
- **A preserved failure is evidence.** The recoveries list keeps each caught
  fault with its kind — `actual validation rejection` for unsupported/late/
  duplicate, `injected exception; retry observed` for the pre-rename case, and
  `controlled real OS I/O failure, not spontaneous` for the rename-to-nonempty
  case. Label how each failure was produced; a spontaneous failure and an
  injected one are not the same evidence.

## Procedure

1. **Attest the target before anything else.** Pin size, SHA-256, MD5, format,
   and container structure. Every later claim binds to this identity.
   ```bash
   python3 scripts/verify-target.py   # or the project's equivalent
   ```
   A target that fails attestation invalidates every claim resting on it.
   TH08's target: Japanese 1.00d, 840,704 bytes, SHA-256 `330fbdbf...d924`,
   image base `0x00400000`, entry `0x004A619E`.

2. **Attest the toolchain.** Pin the compiler, assembler, linker, JDK, and
   analysis engine by version and file digest. Record the exact flags.
   ```bash
   python3 scripts/attest_toolchain.py
   ```
   A "locally attested candidate" is honest language for a toolchain whose
   download source has no independent provenance. Say so; do not call it
   canonical.

3. **Build the obligation ledger.** Enumerate every function as a claim with
   its extent, origin, and current state. Keep these ledgers separate — never
   collapse them into one percentage:
   - `functions.csv` — provisional entries, reconciled extents
   - `function-origins.csv` — authored / runtime / compiler-generated / unknown
   - `implemented.csv` — source-present claims
   - `matches.csv` — byte-exact claims, with digests
   - `compiler-fragments.csv` — parent-owned compiler output, tracked separately
   - `semantic-acceptance.csv` — scoped semantic claims

   ```bash
   python3 scripts/audit_reconstruction.py --config-dir ./config
   ```

4. **Close an obligation only with a complete comparison.** A required
   obligation closes when one manifest binding supplies a unique owner, every
   required fixture, and a passing verifier whose authority is comparable to
   the original observation. Contradictions, duplicate owners, residual
   unknowns, and unavailable authority keep it open.

5. **Compare the complete extent, not a prefix.** The extent authority is the
   whole dedicated COMDAT section or the whole function span. A requested
   prefix is not a match. Apply every relocation; mask none.
   ```bash
   scripts/repo-python scripts/replay-exact-units.py --unit append-projectile
   ```

6. **Run independent oracles.** Choose oracles that fail for different reasons
   and publish a verdict vector, not one similarity number.

   **Two-oracle acceptance (TH08).** Every change is validated by two
   independent oracles: a **VC7 exact oracle** (build the smallest object,
   replay every accepted unit in it) and a **portable behavior oracle**
   (compile/link the modern target). A private rename needs both; a shared
   header change expands the replay scope to every affected object.

   | Oracle class | Establishes | Does NOT establish |
   | --- | --- | --- |
   | target-identity | Same executable, sampled bytes | Semantic correctness |
   | format-integrity | Container/header/relocation validity | Code meaning |
   | toolchain-identity | Same compiler/linker | Source correctness |
   | toolchain-replay | Reproducible build | Original emission |
   | layout-relocations | Address/relocation agreement | Behavior |
   | raw-bytes | Byte identity | Runtime behavior |
   | ledger-consistency | Claims agree with each other | Any of the above |
   | instruction-cfg | Control-flow shape | Exact bytes |
   | runtime-trace | Observed behavior under a scenario | Full fidelity |
   | cross-emulator | Agreement across emulators | Hardware fidelity |
   | metamorphic-invariants | Invariance under transformation | Correctness |

   A supporting oracle can raise confidence or localize a mismatch. It cannot
   override a failed exact requirement.

   **Runtime replay as an oracle (TH08).** For a playable target, recorded
   inputs are a strong independent oracle: TH08 replays 108 recordings and
   12,311,460 calculations across three products, agreeing on all 25 recorded
   fields including exact floating-point bits. This catches source-ownership,
   linking, initialization, and lifetime defects that function-level matching
   misses. It is separate from exactness — a replay pass is not a byte match.

7. **Reject circular validation.** Decompiler output and source copied from it
   are one hypothesis, not two oracles. Upstream source, comments, and progress
   labels enter as untrusted candidate material and cannot satisfy an exact
   requirement by themselves.

8. **Cold-replay after shared changes.** When a shared header or input changes,
   rebuild and re-verify every affected accepted unit. A warm build is not
   evidence. TH08's aggregate attestation rebuilds every configured input
   before replay; the durable lesson is that a stale object or PCH can pass a
   warm check.

9. **Recover fields dependency-first.** When a large function repeatedly touches
   anonymous structure offsets, first look for tiny target helpers that own the
   same fields. Reconstruct and strictly match those helpers in isolation, then
   promote the proven offsets to named fields and rerun every accepted unit for
   that class. This keeps semantic naming evidence separate from guesses made
   inside a large function.

10. **Keep a semantic evidence packet.** Before choosing a name or type, record
    a compact packet: identity, representation (offset/width/signedness/
    packing), producers (every observed write), consumers (every observed use),
    transitions (initial value, valid domain, lifetime, reset), corroboration,
    and boundary (remaining unknowns). Choose a concept that explains the
    producers, consumers, and transitions consistently.

**Done when:** every claim carries its evidence class, exact claims have zero
raw differences across the complete extent with all relocations applied, and
the residual unknowns are named.

## Validation

- `audit_reconstruction.py` passes: no exact claim without source, no orphan
  addresses, no duplicate entries, zero difference counts on exact rows.
- Every exact claim cites input and output digests.
- Compiler fragments name their parent; they are never counted as standalone
  recovered functions.
- Semantic claims carry an explicit scope.

## Common failure modes

| Symptom | Cause | Fix |
| --- | --- | --- |
| Exact claim without source | Ledger inconsistency | `audit_reconstruction.py` flags it |
| Match only on a prefix | Requested prefix, not full extent | Compare the complete COMDAT/span |
| Relocation-normalized equality claimed as exact | Normalization hides differences | Only raw zero-difference is exact |
| Decompiler output used as a second oracle | Circular validation | Use an independent oracle class |
| Upstream source treated as proof | Untrusted candidate material | Re-attest locally against the pinned target |
| Warm build claimed as evidence | No cold replay | Cold-build and re-verify |
| Fragment counted as a recovered function | Compiler output mistaken for source | Track fragments separately with parents |
| One similarity percentage | Hides which dimension failed | Publish a verdict vector |
| Oracle only ever accepts | No rejection test was run | Mutate a candidate and tamper a frozen file; both must fail |
| A resource string treated as behavior | Human-readable claim, no call edge | Test it against active calls and runtime cases |
| Subprocess check relabeled as runtime Evidence | Convenience over authority | Keep the adapter's real failure; label the check honestly |
| "Independent" literals from the same agent | Self-comparison in disguise | Declare source exposure; a blind trial needs a separate author |
| Finite corpus pass called equivalence | Corpus is not the world | State corpus size, environment, and limits in the report |

## Safety and authorization

- Reconstruct only software you own or are authorized to examine.
- Preserve the original artifact; never modify it. Work on copies.
- Do not use reconstruction to defeat licensing, DRM, or access controls.
- Keep original binaries, toolchains, and raw evidence private; publish only
  recovered source and research notes you have the right to publish.

## Worked evidence and provenance

The published DX-Ball / TH04 / TH08 counts, the Companion trial results,
and the verified-versus-sourced split are in
`references/evidence-and-provenance.md`. Read it before citing a count or
claiming a method was reproduced.
