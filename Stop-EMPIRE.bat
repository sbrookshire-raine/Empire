@echo off
setlocal EnableExtensions
set "REPO_ROOT=%~dp0"
if "%REPO_ROOT:~-1%"=="\" set "REPO_ROOT=%REPO_ROOT:~0,-1%"
cd /d "%REPO_ROOT%"

title EMPIRE Shutdown

set "KEEP_OLLAMA=0"
set "KEEP_DOCKER=0"
set "STOP_WEAVIATE=0"
:parse_args
if "%~1"=="" goto args_done
if /I "%~1"=="/keep-ollama" set "KEEP_OLLAMA=1"
if /I "%~1"=="-keep-ollama" set "KEEP_OLLAMA=1"
if /I "%~1"=="/keep-docker" set "KEEP_DOCKER=1"
if /I "%~1"=="-keep-docker" set "KEEP_DOCKER=1"
if /I "%~1"=="/Weaviate" set "STOP_WEAVIATE=1"
if /I "%~1"=="-Weaviate" set "STOP_WEAVIATE=1"
if /I "%~1"=="/weaviate" set "STOP_WEAVIATE=1"
if /I "%~1"=="-weaviate" set "STOP_WEAVIATE=1"
shift
goto parse_args
:args_done

echo.
echo EMPIRE shutdown
echo ===============
echo.
echo No PowerShell stop scripts - AV-safe batch shutdown by port.
if "%STOP_WEAVIATE%"=="1" echo Also stopping Wiki Local Weaviate ^(-Weaviate^).
echo.

echo [1/4] Eve, Workbench, PocketBase...
call :StopPort 2000 eve
call :StopPort 8080 workbench
call :StopPort 8090 pocketbase
echo.

if "%STOP_WEAVIATE%"=="1" (
    echo [2/4] Wiki Local Weaviate...
    docker info >nul 2>&1
    if errorlevel 1 (
        echo   Docker not running - skipped
    ) else (
        docker stop empire-weaviate-heist-2017 >nul 2>&1
        docker rm empire-weaviate-heist-2017 >nul 2>&1
        echo   Weaviate container stopped/removed ^(port 8091^)
    )
) else (
    echo [2/4] Wiki Local Weaviate - left running ^(pass -Weaviate to stop^)
)
echo.

if "%KEEP_DOCKER%"=="1" (
    echo [3/4] Cognee Postgres - skipped ^(/keep-docker^)
) else (
    echo [3/4] Cognee Postgres ^(Docker^)...
    docker info >nul 2>&1
    if errorlevel 1 (
        echo   Docker not running - skipped
    ) else (
        docker compose stop
        if errorlevel 1 (
            echo   WARN: docker compose stop failed
        ) else (
            echo   Postgres stopped
        )
        docker stop empire-speaches >nul 2>&1
        echo   Speaches voice stopped ^(port 8000^)
    )
)
echo.

if "%KEEP_OLLAMA%"=="1" (
    echo [4/4] Ollama - skipped ^(/keep-ollama^)
) else (
    echo [4/4] Ollama...
    tasklist /FI "IMAGENAME eq ollama.exe" 2>nul | find /I "ollama.exe" >nul
    if errorlevel 1 (
        echo   Ollama not running - skipped
    ) else (
        taskkill /IM ollama.exe /F >nul 2>&1
        if errorlevel 1 (
            echo   Could not stop Ollama - quit it from the system tray
        ) else (
            echo   Ollama stopped
        )
    )
)
echo.

echo Shutdown complete.
echo V:\Cognee stays mounted; memory data is preserved.
echo To start again: Start-EMPIRE.bat
echo With wiki:      Start-EMPIRE.bat -Weaviate
echo.
if not "%STOP_EMPIRE_NO_PAUSE%"=="" exit /b 0
pause
exit /b 0

:StopPort
set "_PORT=%~1"
set "_LABEL=%~2"
set "_FOUND=0"
for /f "tokens=5" %%p in ('netstat -ano ^| findstr /C:":%_PORT% " ^| findstr LISTENING') do (
    if not "%%p"=="0" (
        set "_FOUND=1"
        echo   [%_LABEL%] stopping pid %%p on port %_PORT%...
        taskkill /PID %%p /T /F >nul 2>&1
    )
)
if "%_FOUND%"=="0" echo   [%_LABEL%] not running on port %_PORT%
exit /b 0
