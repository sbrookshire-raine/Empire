# Evidence, provenance, and confidence

Read this when you need the worked counts behind the method, or to check what
was reproduced versus sourced.

## Worked example (from sources)

**DX-Ball v1.07** (target SHA-256 `756da1ba...72ba`, 158,208 bytes, VC4.0).
The published ledgers were audited directly:

```
Provisional independent entries      553
Source-present entries               475
Accepted complete exact functions    394
Compiler fragments (parent-owned)     24
Origins: 270 authored / 261 runtime / 21 generated / 1 unknown
```

Every one of the 394 exact rows carries `difference_count = 0` and three
SHA-256 digests binding it to its target, object, and manifest. The audit
confirms no exact claim lacks source and no address is orphaned.

**TH08** (Japanese 1.00d, 840,704 bytes, SHA-256 `330fbdbf...d924`, VC7).
The most complete reconstruction found — authored source 1,107/1,107,
strict exact 1,106/1,107 (99.92% by bytes), plus a separate library ledger
(260/1,119 exact). Its methodology is the richest:

- **Two-oracle acceptance** — every change validated by a VC7 exact oracle and
  a portable behavior oracle.
- **Runtime replay oracle** — 108 recordings, 12,311,460 calculations, all 25
  fields including exact float bits, across three products.
- **Whole-image link contracts** — `/OPT:NOREF` and `/OPT:ICF` each proven
  independently from the target, with a rejected trial recorded (a `/OPT:REF`
  trial shrank `.text` from `0xAA26F` to `0x72B6F` and dropped accepted anchors
  from 931 to 719).
- **Library archive pinning** — separate ledger; archive and member SHA-256; a
  same-name adjacent-version archive is explicitly not a substitute.
- **Six native agent skills** — `th08-re`, `th08-matching`, `th08-semantic`,
  `th08-library`, `th08-typed-re`, plus a shared `th08` skill.

**TH04** (PC-98, Turbo C++ 4.0J): 275 units pass a strict two-cold-build
aggregate replay with identical output SHA-256. The oracle policy lists 11
required exact oracles and 7 supporting ones, with the rule that a supporting
oracle cannot override a failed exact requirement.

All three projects keep `exact` separate from `source-present` and from
`semantic-acceptance`, and all state that an exact-function count is not the
project's completion measure.

## Provenance

**Byte-exact axis** — DX-Ball v1.07, TH04 (PC-98), TH07, TH08, TH105
reconstruction repositories; ledgers and oracle configs read directly.

**Behavioral axis** — [ShadowSwaps/REA-Reconstruction-Companion](https://github.com/ShadowSwaps/REA-Reconstruction-Companion),
manifest version `1.3.23`, observed 2026-10-18. Blobless clone; 189 files.
The `evals/artifact/` trial (Parcel fixture) was **run**, not just read:

```
node --test                     482 tests, 479 pass, 3 skipped, 0 fail
node evals/artifact/check.mjs   status: pass-within-corpus, 30/30 cases
frozen hashes                   5/5 verified independently (sha256)
rejection test 1 (mutated candidate)   status: fail, 27/30 cases flagged
rejection test 2 (tampered corpus)     "Frozen bytes changed: corpus.json"
rejection test 3 (restored)            status: pass-within-corpus
node evals/import-export/check.mjs     status: passed, 33 cases per target
node evals/version-change/run.mjs prepare /tmp/vc   -> status: prepared
node evals/version-change/run.mjs continue /tmp/vc  -> status: version-change-passed
    reused:   [V-titles]   (bindings unchanged, original report digest retained)
    executed: [V-codec, V-interface, V-integration, V-migration]
    oldCandidateMismatch: "schema2 rejected"
```

Frozen identities confirmed: `reference/Parcel.exe` sha256
`6f4e7e1d49e03f60adf9deb4929aafbe3fdd6babb628881807c63efb3ee089b4`,
`corpus.json` sha256 `cec3c120b8e39a8025af07d6f52ee705b075d7887c6b4d4f507b5d0a28542c26`.
The fixture is a **source-exposed same-agent** synthetic example; its own
`limitations` field says so, and this skill repeats it rather than hiding it.

## Provenance

- DX-Ball reconstruction: https://github.com/N0zoM1z0/dx-ball — `AGENTS.md`,
  `docs/agent/WORKFLOW.md`, `docs/MATCHING.md`, `docs/REA.md`,
  `docs/research/ORACLES.md`, `config/{functions,implemented,matches,function-origins,compiler-fragments}.csv`,
  `config/match-units.toml`, `scripts/{coff,verify-target,replay-exact-units,validate-tracking,report-reconstruction-status}.py`.
  Observed 2026-10-17.
- TH08 reconstruction: https://github.com/N0zoM1z0/th08 — `AGENTS.md`,
  `README.md`, `reccmp-project.yml`, `objdiff.json`,
  `docs/{RE_WORKFLOW,RE_HANDOFF,PROGRESS,BUILD_MATCHING,WHOLE_IMAGE_RECONSTRUCTION,SEMANTIC_PLAYBOOK,SEMANTIC_RECONSTRUCTION,REPLAY_RESULTS,REPLAY_TESTING,LIBRARY_PROGRESS,TOOLS,KNOWLEDGE_BASE}.md`,
  `config/{matches,implemented,mapping,reccmp-functions,match-units}.csv|toml`,
  `.agents/skills/th08-{re,matching,semantic,library,typed-re}/SKILL.md`.
  Observed 2026-10-17.
- TH04 reconstruction: https://github.com/N0zoM1z0/th04 — `AGENTS.md`,
  `docs/ORACLES.md`, `docs/BUILD_MATCHING.md`, `config/oracles.toml`,
  `config/evidence.csv`, `.agents/skills/th04-{matching,oracle}/SKILL.md`.
  Observed 2026-10-17.
- REA methodology: https://github.com/morluto/rea — `docs/reconstruction-coverage.md`,
  `docs/reconstruction-obligation-ledgers.md`, `docs/reconstruction-readiness.md`.
- Independent static-analysis write-up: https://github.com/NullLabTests/OpenBSD_netcat_REA
  (evidence-per-claim structure, `files/` artifacts).

## Confidence

- **Verified by reproduction:** the ledger audit script was run against the
  **real DX-Ball ledgers** (downloaded from the repository) and its invariants
  hold on the published data: 553 provisional entries, 475 source-present, 394
  byte-exact, 24 compiler fragments, all 394 exact rows carry
  `difference_count = 0`, and every exact address appears in the functions and
  implemented ledgers. The negative test (an exact claim with no source and a
  nonzero difference count) was correctly flagged.
- **From sources:** the oracle taxonomy, claim vocabulary, four ownership axes,
  two-oracle acceptance rule, and the "no score overrides a failed exact
  requirement" rule are quoted from the three projects' own policy files. The
  DX-Ball, TH04, and TH08 counts are their published values, not independently
  recomputed here.
- **Not tested here:** running any project's full oracle suite (needs their
  private original binaries and pinned toolchains).
- **Verified by reproduction (behavioral axis):** the Companion's `evals/artifact`
  oracle was executed. `node --test` → 482 tests, 479 pass, 3 skipped, 0 fail.
  `node evals/artifact/check.mjs` → `pass-within-corpus`, 30/30 cases. All 5
  frozen SHA-256 hashes were recomputed independently and matched. Three
  rejection tests were run: a mutated candidate produced `status: fail` with 27
  of 30 cases flagged; a tampered `corpus.json` was rejected with "Frozen bytes
  changed" before any candidate ran; restoring the candidate returned to
  `pass-within-corpus`. The oracle demonstrably rejects, not just accepts.
  Two further suites were also run: `evals/import-export/check.mjs` →
  `passed`, 33 cases per target; and the version-change trial
  (`run.mjs prepare` then `continue`) → `version-change-passed`, with `V-titles`
  reused on unchanged bindings and `V-codec/V-interface/V-integration/V-migration`
  re-executed, and the v1 candidate rejected as `schema2 rejected`.
- **From sources (behavioral axis):** the six-step artifact trial, the
  exposure-declaration rule, the misleading-resource trap, bounded differential
  fuzzing, and targeted mutation testing are quoted from the Companion's
  `references/artifact-trials.md` and `references/validation-methods.md`
  (manifest v1.3.23). Its Parcel fixture is a source-exposed same-agent
  synthetic example, per its own `limitations` field.
- **Adaptation:** the audit script generalizes the ledger invariants the
  projects enforce; the column names follow their convention and can be
  overridden.
