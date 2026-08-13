@echo off
setlocal
title NeoLabs Windows Readiness Check
echo NeoLabs Windows readiness check
echo.
where py >nul 2>nul
if errorlevel 1 (
  where python >nul 2>nul
  if errorlevel 1 (
    echo [MISSING] Python 3.10 or newer
    echo Install Python, then run this file again.
    pause
    exit /b 1
  )
)
echo [OK] Python detected
where ssh >nul 2>nul
if errorlevel 1 (
  echo [MISSING] Windows OpenSSH Client
  echo Install OpenSSH Client from Windows Optional Features before a live tunnel session.
) else (
  echo [OK] OpenSSH Client detected
)
call "%~dp0neolabs.cmd" --help >nul
if errorlevel 1 (
  echo [ERROR] NeoLabs launcher self-check failed.
  pause
  exit /b 1
)
echo [OK] NeoLabs launcher ready
echo.
echo No pip installation or PATH editing is required.
echo From this toolkit folder, use: .\neolabs.cmd login
echo.
pause
