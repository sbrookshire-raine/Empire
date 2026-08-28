<#
.SYNOPSIS
    Export wiki status / titles report (wrapper).

.PARAMETER Year
    Snapshot year (default 2017).

.PARAMETER SkipTitles
    Status-only from checkpoint (safe during overnight).

.PARAMETER RebuildTitles
    Full titles rebuild — refused while overnight PID is alive.
#>
param(
    [string]$Year = "2017",
    [switch]$SkipTitles,
    [switch]$RebuildTitles
)

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
$py = Join-Path $Root "venv\Scripts\python.exe"
$env:PYTHONPATH = $Root

$argsList = @("-m", "pipeline.wiki_report_export", "--year", $Year)
if ($SkipTitles) {
    $argsList += "--skip-titles"
}
elseif ($RebuildTitles) {
    $argsList += "--rebuild-titles"
}
else {
    $argsList += "--skip-titles"
}

& $py @argsList
exit $LASTEXITCODE
