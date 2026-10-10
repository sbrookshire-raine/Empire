# Portfolio maintenance — keeping PORTFOLIO.md in sync with ODYSSEY

**Roles**

| Document | Job | Audience |
|----------|-----|----------|
| [`ODYSSEY.md`](ODYSSEY.md) | Growing **audit log** — measure, add chapters, keep corrections visible | You, future sessions, students (§5) |
| [`PORTFOLIO.md`](PORTFOLIO.md) | **Demonstration hub** — curated extract for web portfolio (Empire/Eve *story*, not runtime) | Employers, collaborators, Framer site |
| [`PORTFOLIO_FRAMER.md`](PORTFOLIO_FRAMER.md) | **Framer / slide layout** — progression arc, 15 slides, image checklist | Paste into Framer; sync when PORTFOLIO case studies change |
| [`MOTIVATION.md`](MOTIVATION.md) | Compact **why** (+ Eve `<history>` source) | Prompt-sized; link from portfolio, do not duplicate long prose |

**Rule:** ODYSSEY **adds and witnesses**; PORTFOLIO **selects and refines**. Never paste whole ODYSSEY sections into PORTFOLIO — summarize and link (`ODYSSEY §8`, row name).

---

## When to update

| Event | Update ODYSSEY? | Update PORTFOLIO? |
|-------|-----------------|-------------------|
| New project finished or registered | Yes — §8 row + §2–§4 timeline if dated | Yes — case study or timeline bullet if portfolio-worthy |
| New measured estate / backup chapter | Yes — §14 style | Optional — only if it shows **systems/ops** skill for portfolio |
| Read a major unread source (§7 list) | Yes — §12 / digest | Yes — if it changes thesis or adds a case study |
| Typo / correction in audit | Yes — **record correction** (ODYSSEY style) | Fix portfolio **only if** the fact was copied there |
| External portfolio site (Framer) | No | Update copy from `PORTFOLIO.md`; re-import or edit CSVs in `data/framer-portfolio/` |

After any PORTFOLIO edit, set **`synced_from_odyssey`** at the top of [`PORTFOLIO.md`](PORTFOLIO.md) to the ODYSSEY file date or git commit you used.

---

## Section mapping (ODYSSEY → PORTFOLIO)

Use this when ODYSSEY grows so you know what to refresh in the portfolio.

| ODYSSEY | Pull into PORTFOLIO section |
|---------|----------------------------|
| §1 Problem, one sentence | **Executive summary** — thesis (keep identical wording) |
| §2–§4 Timeline tables | **Timeline** — one row per major beat; drop file paths |
| §5 Difficulties → lessons | **What I learned** — 5–7 bullets max |
| §6 What survived | **Outcomes / assets** — corpus, design pattern, relationship to Eve |
| §8 Project register | **Case studies** — one block per featured project (see list below) |
| §9 Friction case study | Case study **“Failures → contracts”** or skills **governance** |
| §9.1 PREVaiL / engagement | **About how I work** — unlocks not grind |
| §10 Blueprint → EMPIRE | Case study **EMPIRE** — spec to ship table (shortened) |
| §11 Earliest artifact | Timeline **2024-11** + skills **document pipelines** |
| §12 Heptabase / Indie Art Hub | Optional case study **Local Indie Art Hub** when you add demo link |
| §8 Hatch + Playful blockquote | Case study **Hatch exports** — platform risk, IP preservation |
| §8 Stem Factory row | Case study **Stem Factory** — shipped limb, audio DSP |
| §14 Hub / cloud | Omit from portfolio unless applying for **infra/SRE** roles; then one bullet under EMPIRE ops |
| §7 / §13 Unread lists | **Do not** copy into portfolio — internal backlog only |

---

## Featured case studies (default set)

Refresh these from §8 and linked sections when ODYSSEY changes. Add/remove rows in PORTFOLIO § Case studies; update this list if the set changes.

1. **Trustworthy ranking (IRENE → Wiki Scout)** — §1, §2, §6, MOTIVATION §1  
2. **PREVaiL → Eve persona** — §8 PREVaiL, §9.1, §3  
3. **Hatch + Playful (platform beta, export on shutdown)** — §8 Hatch block  
4. **Friction → EMPIRE governance** — §9  
5. **EMPIRE (local-first agent stack)** — §4, §10, [manifest](../manifest/README.md)  
6. **Stem Factory / Shard (audio pipeline → MCP limb)** — §8 Stem row  
7. **Living Book Worlds** (optional) — §8 — extraction + vector + cards  

---

## Sync checklist (after editing ODYSSEY)

1. Read new/changed §§ (usually §2–§4, §8, §12, §14).  
2. Decide: **timeline bullet**, **new case study**, or **footnote only**.  
3. Edit [`PORTFOLIO.md`](PORTFOLIO.md):  
   - Update **Timeline** table.  
   - Update affected **Case study** (problem / approach / outcome / evidence).  
   - Bump **`synced_from_odyssey`** (date + optional `git rev-parse --short HEAD`).  
4. If thesis (§1) changed, rewrite **Executive summary** first sentence to match.  
5. Update [`DOC_MAP.md`](DOC_MAP.md) only if portfolio role changed (rare).  
6. Do **not** duplicate ESTATE_INVENTORY tables — link ODYSSEY §14 or BACKUP_CONSOLIDATION instead.
7. Update **`data/framer-portfolio/*.csv`** (timeline, case-studies, slides) when timeline or case study text changes.

---

## Recommendations (evaluation summary, 2026-10-08)

These are **why** PORTFOLIO exists separately from ODYSSEY.

### What ODYSSEY already does well for portfolio source material

- Dated, evidence-backed narrative (2024–2026).  
- **§8 register** — many apps and carry-forward columns (portfolio case-study seeds).  
- **§5 / §9** — transferable lessons and failure→design (strong “what I learned”).  
- **§1 + MOTIVATION** — stable thesis across architectures.  
- Honest gaps (§7) — credibility if you cite “audit, not marketing” on the portfolio.

### What holds ODYSSEY back as a public portfolio

- Length (~545 lines) and **internal paths** (`K:\`, §13 handoff).  
- **Uneven depth** — EMPIRE/estate very deep; Hatch/Indie Hub registered but not storyboarded.  
- **Add-first workflow** (§13) — correct for audit; portfolio needs **ruthless selection**.  
- Few **demo links**, screenshots, or “outcome in one line” for non-technical readers.

### Design choices for PORTFOLIO.md

- **One page to ~3 screens** of case studies — link to ODYSSEY for depth.  
- **Same thesis sentence** as §1 (do not paraphrase).  
- **Case study template:** Problem → Approach → Outcome → Evidence (file/repo/metric).  
- **Skills matrix** derived from register, not from every tool ever mentioned.  
- **Explicit “still building”** — student-facing blueprint rows (§10) as roadmap, not hidden gaps.

### Future automation (optional)

A small script could warn when `ODYSSEY.md` mtime is newer than `PORTFOLIO.md` frontmatter — not required for v1.

```powershell
# Manual check
$o = (Get-Item docs\ODYSSEY.md).LastWriteTime
$p = (Get-Item docs\PORTFOLIO.md).LastWriteTime
if ($o -gt $p) { Write-Warning 'ODYSSEY newer than PORTFOLIO — run sync checklist in PORTFOLIO_MAINTENANCE.md' }
```

---

## Related

- [`PORTFOLIO.md`](PORTFOLIO.md) — public-facing extract  
- [`ODYSSEY.md`](ODYSSEY.md) — full audit  
- [`MOTIVATION.md`](MOTIVATION.md) — why (short)  
- [`audits/2026-09-28-vault-and-dialogue-digest.md`](audits/2026-09-28-vault-and-dialogue-digest.md) — optional depth for “collaboration with AI” story  
