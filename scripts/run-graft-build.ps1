# Rebuild the local Graft wiring graph for Cursor build-phase navigation.
# Scope: EMPIRE stack code only (excludes tools/archify and other vendored trees).
# Output: graft/ (gitignored). Wiring files live under .cursor/ (committed).

$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
Push-Location $root
try {
    npx --yes @nanonets/graft@latest build `
        --only-dir mcp `
        --only-dir pipeline `
        --only-dir frontend `
        --only-dir agents `
        --only-dir scripts `
        --only-dir backend `
        --only-dir tests
    npx --yes @nanonets/graft@latest check
}
finally {
    Pop-Location
}
