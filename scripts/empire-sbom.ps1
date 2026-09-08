# EMPIRE Mechanic SBOM / vulnerability scan (NOT an Eve tool)
# Generates reports under data/eval/sbom/. Graceful if scanners missing.
$ErrorActionPreference = "Continue"
$Root = Resolve-Path (Join-Path $PSScriptRoot "..")
$Out = Join-Path $Root "data\eval\sbom"
New-Item -ItemType Directory -Force -Path $Out | Out-Null
$Stamp = Get-Date -Format "yyyyMMddTHHmmss"
$Report = Join-Path $Out "sbom_$Stamp.txt"

function Write-Section($title) {
  Add-Content $Report "`n==== $title ====`n"
}

Set-Content $Report "EMPIRE SBOM / audit report $Stamp`nRoot: $Root`n"

# pip-audit
Write-Section "pip-audit"
$pipAudit = Get-Command pip-audit -ErrorAction SilentlyContinue
if ($pipAudit) {
  & pip-audit -r (Join-Path $Root "requirements.txt") 2>&1 | Out-File -Append $Report
} else {
  Add-Content $Report "pip-audit not installed. Optional: pip install pip-audit"
}

# osv-scanner
Write-Section "osv-scanner"
$osv = Get-Command osv-scanner -ErrorAction SilentlyContinue
if ($osv) {
  & osv-scanner -r $Root 2>&1 | Select-Object -First 200 | Out-File -Append $Report
} else {
  Add-Content $Report "osv-scanner not installed. Optional: https://github.com/google/osv-scanner"
}

# syft
Write-Section "syft"
$syft = Get-Command syft -ErrorAction SilentlyContinue
if ($syft) {
  & syft dir:$Root -o spdx-json=(Join-Path $Out "syft_$Stamp.spdx.json") 2>&1 | Out-File -Append $Report
} else {
  Add-Content $Report "syft not installed. Optional: https://github.com/anchore/syft"
}

# grype (if sbom exists)
Write-Section "grype"
$grype = Get-Command grype -ErrorAction SilentlyContinue
$sbom = Get-ChildItem $Out -Filter "syft_*.spdx.json" | Sort-Object LastWriteTime -Descending | Select-Object -First 1
if ($grype -and $sbom) {
  & grype "sbom:$($sbom.FullName)" 2>&1 | Select-Object -First 200 | Out-File -Append $Report
} else {
  Add-Content $Report "grype skipped (missing binary or syft sbom)."
}

Write-Host "Wrote $Report"
Write-Host "Eve must NOT expose these scanners as tools."
