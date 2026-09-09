# Knowledge Shell intake — Shell Packet CSV → primitive_ledger.csv
param(
    [Parameter(Mandatory = $true)][string]$CsvPath,
    [string]$DomainBucket = "general",
    [int]$MaxPerCycle = 7
)

$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
$py = Join-Path $root "venv\Scripts\python.exe"
& $py -m pipeline.loom_intake process $CsvPath --domain-bucket $DomainBucket --max-per-cycle $MaxPerCycle
