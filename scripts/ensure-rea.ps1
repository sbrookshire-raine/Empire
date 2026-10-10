# Pin-install rea-agents for Cursor + Eve REA limb.
# Usage: .\scripts\ensure-rea.ps1

$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
$reaDir = Join-Path $root "tools\rea"

if (-not (Test-Path $reaDir)) {
    New-Item -ItemType Directory -Path $reaDir -Force | Out-Null
}

Push-Location $reaDir
try {
    if (-not (Test-Path "package.json")) {
        npm init -y | Out-Null
    }
    npm install rea-agents@6.3.0 --save-exact
    $script = Join-Path $reaDir "node_modules\rea-agents\scripts\rea.mjs"
    if (-not (Test-Path $script)) {
        throw "rea.mjs missing after install: $script"
    }
    Write-Host "REA OK: $script"
    & node $script mcp doctor
    if ($LASTEXITCODE -ne 0) {
        throw "rea mcp doctor failed with exit $LASTEXITCODE"
    }
}
finally {
    Pop-Location
}
