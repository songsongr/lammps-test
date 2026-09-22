@echo off
REM Internal helper: polls 127.0.0.1:8000 and opens the default browser
REM when the port starts answering. Launched by start.bat via start /B.
REM
REM Lifecycle: it is spawned detached by start.bat. When the user closes
REM the main start.bat console, this child cmd is killed by its parent
REM (because /B shares the console) so it won't keep the browser tab alive.
REM
REM ASCII-only.

setlocal
set "LOG=%~dp0start.log"
set "TRIES=0"

:loop
set /a TRIES+=1
powershell -NoProfile -Command "$c = New-Object System.Net.Sockets.TcpClient; try { $c.ConnectAsync('127.0.0.1', 8000).Wait(200) | Out-Null; if ($c.Connected) { $c.Close(); exit 0 } else { $c.Close(); exit 1 } } catch { exit 1 }" >nul 2>nul
if not errorlevel 1 goto :ready
if %TRIES% GEQ 30 (
    >>"%LOG%" echo [WARN] browser watcher gave up after 30s
    exit /b 0
)
ping -n 2 127.0.0.1 >nul
goto :loop

:ready
>>"%LOG%" echo [OK] port 8000 answered, opening browser (after %TRIES% tries)
start "" "http://127.0.0.1:8000"
exit /b 0
