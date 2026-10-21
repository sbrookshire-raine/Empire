---
name: rea-target-free-readers
description: Read a supplied file's metadata or interface without a disassembler. Use when reading Go build info, Rust crate dependencies, ELF layout, a WASM interface, EVM selectors, a SQLite schema, or a recorded crash core. Keywords: go buildinfo, rust crate, wasm, evm, sqlite, elf, core dump, objdump, gdb, pwntools. Do not use when you need decompiled logic - use rea-native-function-recovery.
icon: IconFileSearch
color: Teal
---

# Target-free static readers with REA

A family of REA readers that take a supplied file and return structured
metadata **without opening a disassembler**. No Ghidra, Hopper, IDA, or JADX.
Several need no external tool at all.

Use these first when they can answer the question — they are the cheapest path
and the least likely to fail on setup.

## Prerequisites

- The file to read. No disassembler or analysis engine is required.
- Optional per lane: `objdump` and `gdb` (verified working with no engine
  configured), `rizin`, Node 24.15+ for WASM, `wabt` for WASM text.
- Python 3 standard library for the reader helpers.

## When to use it

- You need build provenance (Go version, Rust crates) rather than code behavior.
- You need a file's layout, interface, or schema, not its logic.
- You have a crash core and need the recorded threads and signals.
- You need to compare two runs of a program's observable behavior.

## When not to use it

- You need to understand what code *does* — use
  `rea-native-function-recovery` (native), `rea-android-apk-trace` (APK),
  `rea-managed-dotnet-trace` (.NET), or `rea-static-js-electron-trace` (JS).
- You need to run or emulate the target — these readers never execute anything.

## The readers

| Reader | Command | External tool |
| --- | --- | --- |
| Go build info | `rea inspect-go-binary` | **None** |
| Rust dependency metadata | `rea inspect-rust-binary` | **None** |
| ELF layout, symbols, mitigations | `rea inspect-binary-layout` | pwntools (Linux x64) |
| **objdump static inspection** | `rea inspect-with-objdump` | GNU objdump (free) |
| WASM interface | `rea inspect-wasm-artifact` | WABT **1.0.42** |
| EVM selectors | `rea inspect-evm-interface` | **None** |
| SQLite schema and rows | `rea inspect-sqlite-database` | Node **24.15+** |
| PE resources | `rea inspect-pe-resources` | **None** |
| Recorded crash core | `rea inspect-recorded-crash` | pwntools (Linux x64) |
| Process capture | `rea capture-process` | native PTY (Linux/macOS) |
| **Process comparison** | `rea compare-process-captures` | **None** |

## The pwntools ELF layout lane

`inspect-binary-layout` reads a supplied ELF with **no disassembler** and
returns the full static picture:

```bash
export REA_PWNTOOLS_PYTHON=/absolute/path/to/python   # needs pwntools 4.15.0
rea inspect-binary-layout ./program --json
```

Returns: `format`, `architecture` (machine/bits/byte_order), `image_type`
(`ET_DYN`/`ET_EXEC`), `entry_point` with its `meaning` and
`execution_status: "unknown"`, `sections`, `segments`, `symbols`,
`relocations`, `packed_relative_relocations`,
`relocation_inventory_completeness`, `linkage`, and `mitigations`.

- `entry_point.meaning` distinguishes a linked virtual address from a file
  offset. `execution_status` is always `unknown` — this reader never runs the
  binary.
- `mitigations` reports static candidates (RELRO, NX, canary, CET). A
  mitigation candidate is a property of the file, not proof of runtime
  enforcement.
- Requires pwntools **4.15.0**, pyelftools **0.33**, unicorn **2.1.2**.

## The process comparison lane

`compare-process-captures` diffs two saved captures under a shared contract:

```bash
rea capture-process ./scenario.json --json > a.json
rea capture-process ./scenario.json --json > b.json
rea compare-process-captures a.json b.json --json
```

It returns a **verdict vector**, not one similarity score:

```json
{
  "status": "changed",
  "terminal": "unchanged",
  "interaction": "unchanged",
  "exit": "unchanged",
  "filesystem": "changed",
  "process": "unknown",
  "first_divergence": {"status": "found", "dimension": "filesystem", "index": 0}
}
```

- Each dimension is `unchanged`, `changed`, or `unknown`. **`unknown` is not
  `unchanged`** — residual unknowns or truncated observations prevent a
  complete-equivalence claim.
- `first_divergence` localizes the first difference by dimension and index.
- Comparison **rejects captures whose comparison contracts differ** and names
  the differing fields. Run both scenarios from the same absolute working
  directory and observation paths.
- Normalization defaults: paths not normalized, PIDs and ports normalized,
  10 ms time bucket. Matching scenario commitments do not reveal whether
  redacted sensitive inputs were equal.

## The objdump lane (free, no license)

When Ghidra, Hopper, and IDA are all unavailable, **objdump is the cheapest
native static lane**. It needs no engine and no license.

```bash
rea inspect-with-objdump ./program file_headers
rea inspect-with-objdump ./program section_headers
rea inspect-with-objdump ./program symbols
rea inspect-with-objdump ./program relocations
rea inspect-with-objdump ./program dwarf
rea inspect-with-objdump ./program disassemble        # -d
rea inspect-with-objdump ./program disassemble_all    # -D
rea list-objdump-architectures                        # -i, pathless
```

- Choose **one** operation per call. `disassemble` (`-d`) and
  `disassemble_all` (`-D`) have different symbol-boundary semantics.
- Output is captured **raw** — REA does not normalize it into a version-
  independent schema. The complete raw output is authoritative.
- For DWARF, local debug links are **not** followed by default. Pass
  `--follow-debug-links` to enable `-WK`; external debug-file identities are
  then not bound to Evidence.
- `list-objdump-architectures` describes BFD targets compiled into the
  installed binary — it is **not** a guarantee that a target is supported.
- Captured output is retained up to a 16 MiB combined limit;
  `output_truncated` marks the excess.

## The GDB lane (Linux only)

```bash
rea debug-with-gdb "file ./program" --inferior-tty /dev/pts/7
```

Runs **one** unrestricted GDB console command in an ephemeral MI session.
`--inferior-tty` is **required** — it selects the durable terminal that a live
inferior keeps writing to after GDB exits. The console is unrestricted: it can
run shell commands, change target state, and access files and the network in
your security context.

## The Rizin lane

```bash
rea execute-rizin-command ./program iI
rea debug-with-rizin ./program dr --inferior-tty /dev/pts/7
```

`execute-rizin-command` runs one selected Rizin command with `-N -q -c`
(user settings and scripts suppressed, plugins still available). Rizin is a
**tool, not a provider** — `--provider rizin` is rejected.

## Procedure

1. **Try the no-tool readers first.** Go, Rust, EVM, and PE resources need
   nothing installed:
   ```bash
   rea inspect-go-binary ./program --json
   rea inspect-rust-binary ./program --json
   rea inspect-evm-interface ./bytecode.hex hex --json
   rea inspect-pe-resources ./program.exe --json
   ```

2. **Read build provenance when you have it.**
   - **Go:** returns the embedded compiler version, module path, and build
     settings. Absent metadata does **not** prove a binary is not Go.
   - **Rust:** returns cargo-auditable crate names, versions, and dependency
     edges. A missing `.dep-v0` section is null metadata, not proof of no
     dependencies. A rustc commit hash is an *inference* from a read-only
     `/rustc/<40-hex>/` path.

3. **Read an interface, not behavior.**
   - **WASM:** validates the module and returns sections plus exact
     import/export WAT. WAT is not original source.
   - **EVM:** infers dispatch selectors, byte offsets, and argument candidates.
     These are **inferred candidates** — no chain lookup, no execution, and
     candidate coverage does not establish interface completeness.

4. **Read a schema from a quiescent snapshot.**
   ```bash
   rea inspect-sqlite-database ./app.db --json
   rea inspect-sqlite-database ./app.db --table users --row-limit 20 --json
   ```
   Read the schema first (compact inventory by default). Request
   `--schema-scope database` for the complete stored schema. Row samples report
   truncation and have unspecified order. Use a quiescent snapshot rather than
   assuming a live database/WAL pair was copied atomically.

5. **Read a crash core.**
   ```bash
   rea inspect-recorded-crash ./core.12345 --json
   ```
   Returns every recorded thread, its registers and signals, plus raw notes.
   `target_execution` is `not-performed` — the core is read, never replayed.
   Historical PIDs do not select live processes.

6. **Capture and compare process behavior.**
   ```bash
   rea capture-process ./scenario.json --json > capture.json
   rea compare-process-captures authority.json reconstruction.json
   ```
   The scenario uses `executable` + `arguments`, not `command`:
   ```json
   {
     "executable": "/bin/echo",
     "arguments": ["hello"],
     "working_directory": "/tmp/work",
     "filesystem_observation_paths": ["/tmp/work"],
     "timeout_ms": 10000
   }
   ```
   This is **not a sandbox** — the command runs with your permissions and
   inherits the host environment. Filesystem paths select what is *observed*,
   not what is *restricted*. Comparison rejects captures whose comparison
   contracts differ and names the differing fields.

**Done when:** the metadata is read, each claim cites the reader's Evidence, and
inferred values (EVM selectors, rustc commit) are labeled as inferred.

## Validation

- The artifact SHA-256 is recorded in the result.
- Inferred values are not reported as observed.
- A missing metadata section is reported as unknown, not as absence.
- Process captures are compared only under matching contracts.

## Worked example (reproduced)

All readers exercised on 2026-10-17 with REA 6.5.0 on Debian 13.

**pwntools ELF layout** (the CTF binary, SHA-256 `dcd3bec4...51ae`):
```
format: elf  architecture: EM_X86_64 64-bit little
image_type: ET_DYN
entry_point: {reported_value: "0x1090", meaning: "linked-virtual-address",
              execution_status: "unknown"}
provider: pwntools-elf (pwntools@4.15.0;pyelftools@0.33;unicorn@2.1.2)
```
Returns sections, segments, symbols, relocations, linkage, and static
mitigation candidates — with no disassembler configured.

**Process comparison** (two runs of the same shell scenario):
```
status: changed
  terminal: unchanged   interaction: unchanged   exit: unchanged
  filesystem: changed   process: unknown
first_divergence: {status: found, dimension: filesystem, index: 0}
```
The verdict vector localizes the difference to the filesystem dimension rather
than reporting a single similarity number. `process: unknown` is reported as
unknown, not as unchanged.

**Go** (built with go1.24.4):
```
format: elf  architecture: amd64  bits: 64
build_info.go_version: "go1.24.4"
module_text: "path\tgotest\nmod\tgotest\t(devel)\nbuild\t-buildmode=exe\n..."
```

**Rust** (cargo release build):
```
format: elf  architecture: amd64
auditable_metadata: null          <- no cargo-auditable section; not proof of no deps
rustc_commit: {evidence_kind: "inferred", hashes: ["b940084d..."]}
```

**WASM** (WABT 1.0.42):
```
validation: "valid"
sections: Type, Function, Memory, Export, Code
interface.entries: export "add" func(i32,i32)->i32; export "mem" memory
```

**EVM** (82-byte runtime, hex carrier):
```
functions: [{selector: "0x2e64cec1", bytecode_offset: 45, ...},
            {selector: "0x6057361d", ...}]
evidence_kind: "inferred"
runtime_execution: (not performed)
```

**SQLite** (Node 24.15.0):
```
engine: SQLite 3.51.3
schema.tables: users (3 columns)
schema.indexes: idx_name
```

**Crash core** (gcore of a sleeping process):
```
format: elf-core  architecture: x86_64-little-endian
target_execution: "not-performed"
segments: PT_NOTE, PT_LOAD, ...
```

**Process capture** (a shell writing a file):
```
exit: {code: 0, signal: 0, reason: "exited"}
files_after: out.json size=16 sha256=6489d6d7...
```

## Common failure modes

| Symptom | Cause | Fix |
| --- | --- | --- |
| `capability_unavailable` on WASM | WABT version is not 1.0.42 | Download `wabt-1.0.42-linux-x64.tar.gz`; set `REA_WABT_BIN_DIRECTORY` |
| `capability_unavailable` on SQLite | Node older than 24.15 | Use Node 24.15+ or 26+ (24.11 is too old) |
| `provider_unavailable` on layout/crash | `REA_PWNTOOLS_PYTHON` unset | Install pwntools; set the var to an absolute python path |
| `VALIDATION_ERROR` on EVM | `encoding` passed as a flag | It is positional: `rea inspect-evm-interface PATH hex` |
| `invalid_request` on process capture | Scenario used `command` | Use `executable` + `arguments` |
| JSON parse error on capture output | Progress lines went to stderr and were merged | Redirect stderr to `/dev/null`, not into the JSON |
| Comparison rejects two captures | Their comparison contracts differ | Run both from the same absolute working directory and observation paths |
| `process: unknown` in a comparison | Residual unknowns or truncation | Report unknown; do not read it as unchanged |
| `Expected a PE signature` | Not a PE, or a malformed fixture | Verify with `file`; the reader validates the signature before parsing |
| Rust deps look empty | No cargo-auditable section | Report unknown, not "no dependencies" |
| Go metadata absent | Not a Go binary, or stripped | Absence is not proof; check other readers |

## Safety and authorization

- Analyze only files you own or are authorized to examine.
- These readers never execute the target. Process capture **does** run a
  command with your permissions and is not a sandbox — only capture commands
  you are authorized to run.
- Crash cores and SQLite databases may contain credentials, personal data, or
  memory from other processes. Do not publish or reproduce their contents.
- Do not use these readers to extract credentials or personal data from
  software or devices you do not own.

## Provenance

- REA documentation: https://github.com/morluto/rea — `docs/go-binaries.md`,
  `docs/rust-binaries.md`, `docs/binary-diagnostics.md`,
  `docs/wasm-artifacts.md`, `docs/evm-bytecode.md`, `docs/sqlite-databases.md`,
  `docs/recorded-crashes.md`, `docs/process-capture.md`.
- Tool inventory: `docs/mcp-contracts.md#generated-catalog`.
- Reproduced locally 2026-10-17: all eight readers exercised against
  source-derived fixtures (Go 1.24.4 build, cargo release build, WABT 1.0.42
  WASM, hex EVM carrier, SQLite 3.51.3 database, gcore core dump, shell
  process capture).

## Confidence

- **Verified by reproduction:** Go build info, Rust metadata shape, WASM
  validation and interface, EVM selector inference, SQLite schema, crash-core
  segment/thread reading, process capture with filesystem observation,
  **pwntools ELF layout** (sections/segments/symbols/relocations/linkage/
  mitigations), and **process comparison** (the multi-dimensional verdict
  vector with `first_divergence`).
- **From sources:** the resource limits, the PE-resource reader, and the
  `compare-process-captures` contract semantics.
- **Not tested here:** `inspect-pe-resources` on a valid PE (the synthetic
  fixture was malformed and correctly rejected), and real-world third-party
  artifacts (only source-derived fixtures).
- **Corrections found during reproduction:** WABT must be exactly 1.0.42 (apt
  ships 1.0.36); SQLite needs Node 24.15+ (24.11 fails); EVM `encoding` is
  positional; process-capture scenarios use `executable`, not `command`;
  capture progress goes to stderr, so merging it corrupts the JSON; and
  `compare-process-captures` reports `unknown` per dimension rather than
  collapsing to one score.
