# Game-decompilation patterns

Read this when reconstructing a game, a console binary, or any project that runs
for months, or when you need the matching-decompilation vocabulary (whole-image
hash contract, shiftable, permuter, objdiff metrics).

## The matching-decompilation pattern

The game-decompilation community has run this problem for two decades at scale —
SM64, Ocarina of Time, Majora's Mask, Perfect Dark, Pokémon Emerald, GoldenEye,
LEGO Island, Snowboard Kids 2. Their vocabulary and their tooling are worth
adopting wholesale.

**The contract, stated precisely** (Perfect Dark's README): *"When a matching
decompilation is compiled with the same compiler that the original developers
used, the output will be exactly the same as the retail game, byte for byte."*

### The whole-image hash contract

The strongest check is **not** per-function. Build the whole ROM and compare its
hash to the retail hash:

| Project | Contract |
| --- | --- |
| SM64 | 5 retail SHA-1s (`jp`/`us`/`eu`/`sh`/`cn`) |
| Pokémon Emerald | 1 SHA-1 (`f3ae0881…`) |
| OoT | MD5 per build version |

A whole-image hash catches **linking, ordering, initialization, and lifetime**
defects that function-level matching misses. Report it separately from the
per-function exact count — they are different claims.

### Progress is more than one number

Modern tooling reports **separate** metrics, and you should too:

| Metric | Means |
| --- | --- |
| `matched_data_percent` | data matched |
| `fuzzy_match_percent` | code matched, allowing minor differences |
| exact function count | strict byte matches |
| **shiftable** | you can insert or remove code without breaking the build |

**Shiftable is a distinct axis.** OoT and MM state parts of the ROM are *not yet
shiftable*, so modifying them is difficult. Code can match byte-for-byte and
still not be shiftable. Never fold it into the match percentage.

### When a function will not match: search, don't hand-edit

`decomp-permuter` permutes C to find a formulation the original compiler turns
into the target bytes. Two modes:

- **Random** — introduce temporaries, change types, put statements on one line.
- **Manual** — `PERM_GENERAL(a, b)` tries alternatives; `PERM_VAR`,
  `PERM_LINESWAP`, `PERM_INT`, `PERM_ONCE` compose them.

Randomization weights are **per-compiler** and overridable. Input is a directory
with a `.c`, the target `.o`, a `.sh` that compiles it, and a `.toml`. Supports
MIPS (IDO/GCC), PowerPC, ARM32. A distributed mode (`permuter@home`) pools CPU.

**The lesson generalizes:** when a reconstruction will not converge, stop
editing by hand and search the space of equivalent formulations.

### Tooling

| Tool | Does |
| --- | --- |
| `objdiff` | Compares whole `.o` files — functions **and** data. Demangles GCC/MSVC/CodeWarrior/Itanium. ARM/ARM64/MIPS/PowerPC/SuperH/x86. Powers decomp.dev |
| `asm-differ` | The older assembly diff viewer; default on decomp.me |
| `decomp-permuter` | The search above |

### The second axis: static recompilation

Not every project aims for byte-identical output. **Static recompilation**
translates each instruction literally into C and compiles that for the host:

```
addiu $r4, $r4, 0x20   ->   ctx->r4 = ADD32(ctx->r4, 0x20);
```

It does not claim a byte match; it claims the original behaviour runs natively.
Handle branch delay slots by duplicating instructions, and turn `jr` into a
`switch` when a jump table is detected. OpenGOAL does the same for a custom LISP
(GOAL): decompile to readable GOAL, write a compiler for it, recompile for
x86-64.

**Say which axis you are on.** A recompilation port is not a matching
decompilation, and a matching decompilation is not a port.

## Working at scale: the findings log

A reconstruction that runs for months needs its knowledge indexed, or an agent
will drown in it. The GoldenEye PC port's `AGENTS.md` is the best example found:

- **A numbered findings log** (`Dxx` entries) plus a **generated index CSV**
  (label, one-liner, status), rebuilt by a tool.
- **"Never linear-read."** Look the label up in the index, then read *only* that
  section. Multi-pass labels have large sections — grep within the section or
  read with an offset.
- **One tracker.** New items go in the existing `ROADMAP.md`; never start a
  second backlog file.
- **A presentation layer that may go stale.** Site pages that summarise the
  ROADMAP are explicitly *not* a source of truth, and a mismatch between a site
  page and the ROADMAP is **not a bug**. Name the single source of truth per
  question, or an agent will chase phantom inconsistencies.
- **Subagent dispatch** with task budgets, file partitioning, and a standard
  brief template.

### Route documentation by task

Do not make an agent read everything. `wakaru`'s `AGENTS.md` says *"Read
`docs/architecture.md` first. Then read by task, instead of reading
everything"* — with a table mapping task → doc. `plx-native` does the same with
per-subsystem `CLAUDE.md` files: *"read the relevant section before changing a
subsystem; do not load the whole file when a narrower section is enough."*

### Check the contribution policy first

Some reconstruction communities **ban generative-AI contributions outright**
(Zelda64Recomp's `CONTRIBUTING.md` bans any GenAI tooling in any capacity).
A technique can be sound and still unwelcome in a given repo. Check before
proposing an agent-assisted workflow against someone else's project.

## Sources

| Source | Contributed |
| --- | --- |
| `n64decomp/sm64` | Five retail SHA-1s; the whole-image hash contract |
| `n64decomp/perfect_dark` | The precise statement of the matching contract |
| `pret/pokeemerald` | Single whole-ROM SHA-1 |
| `zeldaret/oot`, `zeldaret/mm` | The **shiftable** concept; per-version MD5s |
| `encounter/objdiff` | `matched_data_percent` / `fuzzy_match_percent`; whole-`.o` diffing |
| `simonlindholm/decomp-permuter` | The permuter search and its `PERM_*` macros |
| `simonlindholm/asm-differ` | The older diff viewer |
| `N64Recomp/N64Recomp` | The static-recompilation axis |
| `open-goal/jak-project` | Decompile-a-custom-LISP-then-recompile |
| `jkdansereau/goldeneye-pc-port` | The findings log, generated index, presentation-layer rule |
| `pionxzh/wakaru`, `GLinnik21/plx-native` | Task-routed documentation |
| `Zelda64Recomp/Zelda64Recomp` | The GenAI contribution ban |

Observed 2026-10-18 via the awesomerea.org Games case collection. All entries are
**first-party documented** — read from each project's own README/AGENTS.md, not
reproduced here.
