# Shared Cognee VHDX path resolution (dot-source from mount/create/restore/start-stack).

$script:EmpireCogneeDriveLetter = 'V'
$script:EmpireCogneeRoot        = 'V:\Cognee'

function Get-EmpireCogneeVhdxPath {
    if ($env:EMPIRE_COGNEE_VHDX -and (Test-Path -LiteralPath $env:EMPIRE_COGNEE_VHDX)) {
        return $env:EMPIRE_COGNEE_VHDX
    }

    $candidates = @(
        'E:\EMPIRE_VHDX\empire_cognee.vhdx',
        'I:\EMPIRE_VHDX\empire_cognee.vhdx',
        'D:\EMPIRE_VHDX\empire_cognee.vhdx',
        'K:\EMPIRE_BACKUP_2026-09-27\09_i_drive_leftovers\EMPIRE_VHDX\empire_cognee.vhdx',
        'E:\EMPIRE_HUB\00_CORE\state\cognee_vhdx\empire_cognee.vhdx'
    )

    foreach ($path in $candidates) {
        if (Test-Path -LiteralPath $path) {
            return $path
        }
    }

    # Preferred live location when creating/restoring (NTFS on T7 Shield, not Google Drive I:)
    return 'E:\EMPIRE_VHDX\empire_cognee.vhdx'
}

function Get-EmpireCogneeVhdxHubSnapshot {
    return 'E:\EMPIRE_HUB\00_CORE\state\cognee_vhdx\empire_cognee.vhdx'
}
