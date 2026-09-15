# Import MediaWiki redirect + disambiguation metadata into Title DNS.
# Requires an existing title-index.sqlite (build-wiki-title-index.ps1).
#
# Optional dumps (place under I:\EMPIRE_DATA\wiki-reports\{year}\ or pass paths):
#   redirects.tsv
#   page_props_disambig.tsv
#   enwiki-*-redirect.sql.gz + enwiki-*-page.sql.gz

param(
    [string]$Year = "2026",
    [string]$Index = "",
    [string]$RedirectsTsv = "",
    [string]$DisambigTsv = "",
    [string]$RedirectSql = "",
    [string]$PageSql = "",
    [int]$MaxSqlRows = 0
)

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
$Python = Join-Path $Root "venv\Scripts\python.exe"
if (-not (Test-Path $Python)) {
    throw "Missing venv python at $Python"
}

$env:PYTHONPATH = $Root
$argsList = @(
    "-m", "pipeline.wiki_mediawiki_meta",
    "--year", $Year
)
if ($Index) { $argsList += @("--index", $Index) }
if ($RedirectsTsv) { $argsList += @("--redirects-tsv", $RedirectsTsv) }
if ($DisambigTsv) { $argsList += @("--disambig-tsv", $DisambigTsv) }
if ($RedirectSql) { $argsList += @("--redirect-sql", $RedirectSql) }
if ($PageSql) { $argsList += @("--page-sql", $PageSql) }
if ($MaxSqlRows -gt 0) { $argsList += @("--max-sql-rows", "$MaxSqlRows") }

& $Python @argsList
exit $LASTEXITCODE
