@echo off
setlocal
cd /d "%~dp0"

title EMPIRE Wiki Test Launcher

echo.
echo EMPIRE Wiki Test — full stack + Weaviate + preflight
echo ====================================================
echo.

set "WARCHIVE=D:\weaviate_v2_archive\weaviate"
if not "%EMPIRE_WEAVIATE_ARCHIVE%"=="" set "WARCHIVE=%EMPIRE_WEAVIATE_ARCHIVE%"

powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0scripts\launch-empire.ps1" -Weaviate
if errorlevel 1 (
    echo.
    echo Stack launch failed.
    pause
    exit /b 1
)

echo.
echo Wiki Local preflight...
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0scripts\verify-wiki-local.ps1" -ArchivePath "%WARCHIVE%"
set "PF=%ERRORLEVEL%"
if %PF% GEQ 2 (
    echo.
    echo Preflight WARN — Weaviate is up but search looked weak. You can still try Eve.
)
if %PF% EQU 1 (
    echo.
    echo Preflight FAIL — fix Weaviate before wiki Q and A.
    echo   Archive: %WARCHIVE%
    echo   Or set EMPIRE_WEAVIATE_ARCHIVE=I:\your\path\weaviate
    pause
    exit /b 1
)

echo.
echo Ready. Open http://127.0.0.1:8080/eve.html
echo Toolbelt: Wiki Local should be ON.
echo Calibration: set PYTHONPATH=C:\EMPIRE ^&^& venv\Scripts\python.exe scripts\test-wiki-chat-smoke.py
echo.
pause
exit /b 0
