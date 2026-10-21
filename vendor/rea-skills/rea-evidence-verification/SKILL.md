---
name: rea-evidence-verification
description: Audit whether a conclusion is actually supported by its Evidence record. Use when checking a finding before you report it, writing up a reconstruction, or publishing a case study. Keywords: evidence, overclaim, provenance, audit, verify, claim, confidence, unsupported. Do not use to perform the analysis itself - use rea-native-function-recovery, rea-android-apk-trace, or rea-web-app-reconstruction, whichever produced the claim.
icon: IconShieldCheck
color: Red
---

# REA evidence verification

REA returns Evidence records that separate observed facts, inferences, and
unknowns. This skill audits a record and the claims resting on it, so a
conclusion is never stated more strongly than its evidence supports.

Use it before reporting any REA-derived finding, and whenever an agent's
summary sounds more certain than the analysis behind it.

## When to use it

- Before publishing or reporting a conclusion drawn from REA analysis.
- When a finding will inform a decision (a security assessment, a
  reconstruction, an interoperability claim).
- When reviewing another agent's REA-based output.
- When a claim sounds absolute ("this always runs", "there is no backdoor").

## When not to use it

- To re-run analysis — this audits records, it does not produce them.
- On non-REA evidence. The checks assume REA's record shape.

## Prerequisites

- One or more REA Evidence JSON files, as produced by `rea ... --json` or
  captured from an MCP tool result.
- `scripts/verify_evidence.py` from this skill (Python 3 standard library only).

## The two failure classes

**Structural.** The record is missing something that makes it trustworthy —
no limitations, no authority, an unrecognized confidence value, no provider
identity. A record missing these cannot support a strong claim.

**Epistemic.** The record is fine but the *claim* exceeds it — calling a
`derived` static finding `observed`, or asserting runtime behavior from static
analysis. This is the more dangerous class because the evidence looks solid.

## Procedure

1. **Collect the Evidence records.** Save each one to a file. From the CLI:
   ```bash
   npx -y rea-agents@latest analyze-javascript-application /path/to/app --json > app-evidence.json
   ```
   From MCP, save the `structuredContent` of each result.

2. **Write down the claims you intend to make.** One entry per claim, with the
   Evidence ID it rests on and whether you are asserting it as observed or
   inferred:
   ```json
   [
     {"text": "The app exposes one IPC channel.", "evidence_id": "ev_...", "kind": "observed"},
     {"text": "The export handler writes notes.csv.", "evidence_id": "ev_...", "kind": "inferred"}
   ]
   ```

3. **Run the audit.**
   ```bash
   python3 scripts/verify_evidence.py app-evidence.json --claims claims.json
   ```
   Exit code 0 means every check passed; 1 means at least one failed; 2 means
   the input could not be read.

4. **Resolve every failure before reporting.** For a structural failure, the
   record is incomplete — re-run the analysis or note the gap. For an epistemic
   failure, weaken the claim to match the evidence, or gather the evidence the
   claim needs.

5. **State the residual unknowns.** The record's `limitations` field is not
   boilerplate. Carry the relevant ones into your report verbatim.

**Done when:** the audit passes, or every remaining failure is either fixed or
explicitly disclosed as a limitation in the report.

## What the checks mean

| Check | Fails when | Why it matters |
| --- | --- | --- |
| `required_fields` | A core field is absent | The record is incomplete |
| `has_evidence_id` | ID is missing or malformed | The claim cannot be traced |
| `confidence_recognized` | Value is not a known REA confidence | The strength is unknown |
| `limitations_declared` | Empty limitations | REA always has limits; none stated means none considered |
| `authority_stated` | Authority is empty | The basis of the finding is unstated |
| `normalized_result_present` | Result is empty | Nothing was actually observed |
| `provider_recorded` | No provider id | The analysis engine is unknown |
| `no_runtime_overclaim_from_static` | Static op + runtime language | Static analysis cannot prove execution |
| `runtime_environment_recorded` | Runtime op without environment | A runtime result needs its environment |

## Worked example (reproduced)

Two real records from REA 6.5.0, audited on 2026-10-17:

```
[PASS] analyze_javascript_application (derived) ev_7f4f0fcb...468a70
[PASS] capture_browser_scenario (observed) ev_5cb60283...e474fb
Overall: PASS
```

The same verifier against a deliberately bad record and three overclaiming
claims:

```
[FAIL] analyze_javascript_application (certain) not-an-evidence-id
        x has_evidence_id: evidence_id='not-an-evidence-id'
        x confidence_recognized: confidence='certain'
        x limitations_declared: 0 limitation(s)
        x authority_stated: authority=''
        x normalized_result_present: type=dict
        x provider_recorded: provider=None

Claims:
  [FAIL] The export handler always executes at runtime and proves that notes are written.
        x claim says 'observed' but evidence confidence is 'derived'
        x claim text contains overclaim phrase 'proves that'
        x claim text contains overclaim phrase 'always executes'
  [FAIL] The page requested notes.json.
        x cited evidence_id 'ev_DOES_NOT_EXIST' not among supplied records
Overall: FAIL
```

Both failure classes were caught: the structural gaps in the record, and the
claim that overstated a `derived` static finding as an `observed` runtime fact.

## Common failure modes

| Symptom | Cause | Fix |
| --- | --- | --- |
| `confidence='derived'` on a static analysis | Normal — static analysis infers | State the claim as inferred, not observed |
| Claim cites an ID not in the file set | You saved the wrong record | Save the record the claim actually rests on |
| `no_runtime_overclaim_from_static` flags clean text | A phrase like "secure" appears incidentally | Read the flagged phrase in context; the check is conservative |
| Exit 2 | File is not valid JSON | Re-export; a truncated MCP preview is not a record |

## Safety and authorization

- This skill reads local files and reports. It performs no network access and
  no analysis.
- Evidence records may contain target paths and strings. Do not publish a
  record containing credentials, private paths, or third-party data.
- Verification does not authorize anything. A passing audit means the claim
  matches its evidence, not that the underlying analysis was permitted.

## Provenance

- REA Evidence contract: https://github.com/morluto/rea —
  `docs/mcp-contracts.md`, `docs/cli.md`, and the native skill's
  `references/evidence-workflows.md`.
- Confidence and authority vocabulary: REA Evidence records as observed in
  `analyze_javascript_application` and `capture_browser_scenario` output,
  REA 6.5.0, 2026-10-17.
- Overclaim patterns: informed by https://www.apriorit.com/dev-blog/reverse-engineering-with-ai
  (AI outputs in reverse engineering should be treated as hypotheses requiring
  verification).
- Script verified locally 2026-10-17 against real and deliberately bad records.

## Confidence

- **Verified by reproduction:** the passing audit on two real records and the
  failing audit on a bad record plus overclaiming claims.
- **From sources:** the required-field list and confidence vocabulary come from
  REA's documented contract and observed output.
- **Limitation:** the overclaim phrase list is heuristic and conservative. It
  flags suspicious language; it does not judge meaning. A human or model must
  read flagged text in context.
