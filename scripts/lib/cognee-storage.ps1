# Cognee file root on NTFS (Postgres holds graph; this is SYSTEM_ROOT_DIRECTORY).

$script:EmpireCogneeRootDefault = 'E:\EMPIRE_COGNEE'

function Get-EmpireCogneeRoot {
    if ($env:EMPIRE_COGNEE_ROOT) {
        return $env:EMPIRE_COGNEE_ROOT
    }
    if (Test-Path -LiteralPath $script:EmpireCogneeRootDefault) {
        return $script:EmpireCogneeRootDefault
    }
    if (Test-Path -LiteralPath 'V:\Cognee') {
        return 'V:\Cognee'
    }
    return $script:EmpireCogneeRootDefault
}

function Ensure-EmpireCogneeRoot {
    $root = Get-EmpireCogneeRoot
    if (-not (Test-Path -LiteralPath $root)) {
        New-Item -ItemType Directory -Force -Path $root | Out-Null
    }
    return $root
}
