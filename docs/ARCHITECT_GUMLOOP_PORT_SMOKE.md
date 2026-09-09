# Architect smoke — Gumloop port (Tool Forge + Loom Intake)

Use after `Start-EMPIRE.bat` and a hard refresh of http://127.0.0.1:8080/eve.html (Ctrl+F5).

## 1. Loom Intake (~3 min)

1. Open Eve Workbench → **Toolbelt** → enable **Loom Intake**
2. Click composer chip **Loom** or type: *Show Loom ledger status and where the Seeker prompt lives*
3. Expect: `ok: true`, ledger row count **> 0**, paths under `04_Thought_Experiments/loom/`
4. Optional CLI:
   ```powershell
   cd C:\EMPIRE
   .\scripts\run-loom-intake.ps1 -CsvPath sample_shell_packets.csv -DomainBucket education
   ```
5. Expect: report with `added` rows, no `fatal_error`

**Seeker workflow (real data):**

1. Open `C:\Empire_Workbench\04_Thought_Experiments\loom\intake\seeker_extraction_prompt_v5.md`
2. Run the fenced prompt against your notes → save CSV with 12 columns
3. Drop CSV in `C:\Empire_Workbench\00_Resource_Queue\`
4. Eve: *Process my shell packet CSV for domain education* (filename only is fine)

## 2. Tool Forge (~3 min)

1. Enable **Tool Forge** in Toolbelt
2. *List harvest_cache outputs and Active Tools I can read with Tool Forge*
3. Optional:
   ```powershell
   .\scripts\run-skill-inventory.ps1
   ```
   Expect: manifest under `harvest_cache/SKILL_TRIAGE_MANIFEST.md`
4. Optional docs scrape (needs network):
   ```powershell
   .\scripts\run-docs-guide-scrape.ps1 -Url "https://docs.ollama.com" -MaxPages 5 -DiscoverOnly
   ```

## 3. Regression spot-checks (if time)

| Area | Quick check |
|------|-------------|
| DAZE dock | Toolbelt → Time Reclaim → DAZE carousel fits viewport |
| Chat dock | Composer flush with dock, mic/send row |
| Stem Factory | Only if you drop a song in `stem_factory/input` |

## Pass criteria

- Loom status returns without MCP error
- Sample CSV intake appends ledger (or corroborates existing rows)
- Tool Forge triage writes manifest JSON + MD
- No Eve crash when toggling limbs on/off

## Reference

- Port index: `docs/reference/GUMLOOP_AGENT_PORT_INDEX.md`
- Work orders: `05_Work_Orders/WO-20260909T210000Z-keeper-loom-intake.md` (delete after pass)
