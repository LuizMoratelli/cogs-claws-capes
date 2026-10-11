@echo off
rem Adds a friend to the server whitelist with the right ID (HUD button "Add friend to whitelist").
cd /d "%~dp0.."
set /p NAME=Friend's exact Minecraft name: 
set /p PAID=Does this friend own Minecraft (paid account)? [s/n]: 
if /i "%PAID%"=="s" (python tools\whitelist.py add "%NAME%" --paid) else (python tools\whitelist.py add "%NAME%" --offline)
echo.
echo If the server is running, type in its window:  whitelist reload
pause
