# Verification log

Read this to check what was reproduced versus sourced, or to see the
generalization and fallback test results.

## Discovery verification (reproduced)

The discovery mode was run against live GitHub and its output checked:

```
python3 scripts/discover.py --topics reverse-engineering ghidra decompiler \
    --min-stars 500 --top 12 --probe
-> 91 unique candidates from 3 topic queries (40 each, deduped)
-> 3 methodology-rich (>=3 artifacts) among the top 12
-> morluto/rea (308k stars, 78k forks) confirmed as the top RE repo by forks
```

The probe correctly separated tools from methodology sources: `radare2` returned
`AGENTS.md,CONTRIBUTING.md,Makefile` (3), while `iBotPeaches/Apktool` and
`Perfare/Zygisk-Il2CppDumper` returned 0 — they are tools with a README only.
The search API reported `rate_remaining` on every call, and the probe used
`raw.githubusercontent.com`, which did not consume search budget.

**What discovery found that case-mining did not:** a 818-skill cybersecurity
library (`mukul975/Anthropic-Cybersecurity-Skills`, 34.6k stars / 4.2k forks,
Apache-2.0, agentskills.io format, each skill a `SKILL.md` + `references/` +
`scripts/` triple) and a scanner shipping its own agent skill
(`shadow1ng/fscan`). Neither was cited by any curated case, so no case-mining
pass could have surfaced them. This is the argument for discovery mode: it
reaches repos that no curator has screened.

**Use-case-seeded discovery (reproduced).** The loop was closed end to end:
`search_seeds.py` turned the use-case layer into queries, `discover.py --seeds`
ran them, and the run surfaced three repos no prior sweep had found —
`gojue/ecapture` (5 methodology artifacts), `zeek/zeek` (3), and
`AFLplusplus/AFLplusplus` (3). Each candidate carries the use case that surfaced
it. Two vocabulary bugs were found and fixed in the process: `agent-skills`
appeared on five use cases and could not discriminate them (fixed with inverse
document frequency), and `topic:dotnet` returned every .NET repo because it is a
language tag, not a capability (fixed by pairing platform terms with capability
terms).

## Generalization (verified)

The token filter and search logic were tested against unrelated projects to
confirm they are not tuned to one name:

| Project | Curated lists found | Notes |
| --- | --- | --- |
| `morluto/rea` | 5 | `awesome-REA-cases`, `awesome-rea`, `Awesome-REA` |
| `junegunn/fzf` | 12 | Correctly finds `awesome-fzf` (122 stars) |
| `BurntSushi/ripgrep` | 3 | No false positives from the `rg` substring |

The `rea` case is the important one: an earlier version matched `react/react`
because `rea` is a substring of `react`. The standalone-token filter fixed it.

## Fallback verification (reproduced)

With the GitHub API at **0 remaining**, a full sweep of `morluto/rea`
completed using only the fallbacks:

```
meta:    ungh.cc
forks:   github-html (owners only, no star counts)
compare: git (no rate limit)
refs:    git ls-remote (no rate limit)  -> 139 branches
```

The git-only divergence check was verified against two known forks:

| Fork | Result | Meaning |
| --- | --- | --- |
| `heaven-hm/re-agent` | `diverged`, ahead=127, behind=928, 968 files | Real derivative work |
| `shijianzhong/rea` | `behind`, ahead=0, behind=104 | Untouched mirror |

The git path returned **more** than the API's compare endpoint: full commit
history and a diffstat (`968 files changed, 1059003 insertions`).

## Case-mining verification (reproduced)

The curated-list workflow was run against `awesome-REA-cases` (401 cases,
machine-readable `data/cases.json`):

- **61 cases cite a GitHub repo**; 31 of those are REA-labeled.
- The list's own `build.py` validates that every entry has a public HTTPS
  source and no duplicate source sets — a curation standard worth respecting.
- Its README states entries are "based on author and project reports; not
  independently reproduced here," which is exactly the honesty the evidence
  ladder preserves.

Drilling into the cited repos surfaced the highest-value artifacts of the whole
investigation: the **DX-Ball** and **TH04** reconstruction repositories, which
contain complete verification methodologies (obligation ledgers, oracle
taxonomies, toolchain attestation). Those became the
`rea-reconstruction-verification` skill.

**Technique frequency across the 401 cases** (from descriptions):

```
firmware 46 · apk 38 · ghidra 33 · rust 19 · electron 15 · ida 11
emulator 9 · hopper 6 · z3 5 · differential 5 · jadx 5
```

Status distribution: `unverified` 222, `in-progress` 76, `case` 43,
`analysis-test` 34, `related-project` 26. The large `unverified` share is a
reminder to grade each case rather than trusting the collection wholesale.

## Provenance

- GitHub REST API: `/repos/{owner}/{repo}`, `/forks`, `/compare/{base}...{head}`,
  `/search/repositories`.
- ungh.cc — unlimited cached GitHub proxy: https://ungh.cc ,
  https://github.com/unjs/ungh (MIT). Endpoints used: `/repos/{owner}/{repo}`,
  `/repos/{owner}/{repo}/branches`, `/repos/{owner}/{repo}/contributors`,
  `/repos/{owner}/{repo}/files/{branch}`.
- GitHub HTML scraping: repo page `"stargazerCount"` JSON, `/forks` owner list.
- git protocol: `git ls-remote`, blobless clone (`--filter=blob:none`), and
  `git rev-list --count` for divergence.
- Worked example: `morluto/rea` (https://github.com/morluto/rea), observed
  2026-10-17.
- Curated-list methodology: https://github.com/songshikang0111/awesome-REA-cases
  (`MAINTENANCE.md`, `CONTRIBUTING.md`, `data/cases.json`, `scripts/build.py`).
- Derived lists: https://github.com/yibie/awesome-rea ,
  https://github.com/mytechnotalent/rea , https://github.com/lkimuk/ReArk ,
  https://github.com/reacher-z/Awesome-REA .
- High-value repos found by drilling: https://github.com/N0zoM1z0/dx-ball ,
  https://github.com/N0zoM1z0/th04 , https://github.com/NullLabTests/OpenBSD_netcat_REA .
- Script verified locally 2026-10-17 against `morluto/rea`, including a full
  sweep with the GitHub API at 0 remaining.

## Confidence

- **Verified by reproduction:** the sweep, fork enumeration, divergence
  comparison, derivative search, and curated-case mining all ran and returned
  the results shown. The token filter was tested against `morluto/rea`,
  `junegunn/fzf`, and `BurntSushi/ripgrep`. The layered fallback was verified
  with the API at 0, and the git divergence path was checked against a diverged
  fork and a mirror. The case-mining workflow was run against the 401-case
  `awesome-REA-cases` collection and its cited repos were drilled.
- **From sources:** the curated-list grading vocabulary (`case`, `unverified`,
  `in-progress`, `analysis-test`, `related-project`) is that list's own
  convention, adopted here because it is well-defined.
- **Limitation:** ungh.cc is cached and its counts lag live values (observed
  290,855 vs 307,107 stars). The HTML fallback returns fork owners without
  star counts, so `--compare-top` cannot rank by divergence when the API is
  spent. The git fallback is slow (tens of seconds per fork) and downloads
  objects; use it selectively.
- **Bugs found and fixed during reproduction:** the compare endpoint needs
  `owner:repo:branch` with colons (a slash form 404s silently); the
  curated-list search matched `react/react` for `rea`; the upstream repo
  appeared in its own fork list; and `--source` was parsed but ignored. All are
  fixed and documented above.
