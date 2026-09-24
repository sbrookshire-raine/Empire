---
name: loom_process_shell
toolbelt: loom_intake
one_line: Process a 12-column Shell Packet CSV through the Keeper Knowledge Shell (validate, throttle max 7/cycle, gate…
---

## Description (verbatim from the tool schema, pre-R-03)

Process a 12-column Shell Packet CSV through the Keeper Knowledge Shell (validate, throttle max 7/cycle, gate, append to primitive_ledger.csv). CSV may be in Resource Queue or an absolute path. Requires Loom Intake Toolbelt.

## Parameters

- `csv_path` — Path or filename of Shell Packet CSV (12 columns). Tries Resource Queue then loom/intake.
- `domain_bucket` — Domain bucket label for gap matrix (e.g. education, software, general).
- `max_per_cycle` — Promotion cap per cycle (default 7, hard max 7).

## Usage

Registered by the Toolbelt category `loom_intake`. The model sees the name, the
one-line cue and the parameter names in its schema; this document is the deep syntax it
can fetch with `tool_docs` when a call needs more than the cue.
