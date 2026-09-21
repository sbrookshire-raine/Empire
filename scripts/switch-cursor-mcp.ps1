# Swap Cursor MCP profile. Restart Cursor after switching.
param(
    [ValidateSet("Lean", "Full", "Remote")]
    [string]$Profile = "Lean"
)

$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
$cursorDir = Join-Path $root ".cursor"
$source = Join-Path $cursorDir ("mcp.{0}.json" -f $Profile.ToLower())
$target = Join-Path $cursorDir "mcp.json"

if (-not (Test-Path -LiteralPath $source)) {
    throw "Profile file not found: $source"
}

Copy-Item -LiteralPath $source -Destination $target -Force
Write-Host "Cursor MCP profile: $Profile"
Write-Host "  wrote $target"
Write-Host "  Lean = 7 servers. Remote = 6 (no graft npx). Full = all 19."
Write-Host "Restart Cursor to apply."
