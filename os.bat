@echo off
title TencleOS Shell v2.1

cd /d "%~dp0"

REM Clean up old marker files on startup
if exist ".current_Apps" del ".current_Apps"
if exist ".current_Games" del ".current_Games"
if exist ".current_System" del ".current_System"

cls
echo.
echo ===============================================================================
echo                            TENCLEOS SHELL v2.1
echo ===============================================================================
echo.
echo TencleOS Shell v2.1 [Version 1.2.0]
echo (c) 2025 CostaTech. All rights reserved.
echo.
echo Navigate with 'cd' and run apps with 'run' command
echo Type 'help' for more info or 'exit' to quit
echo.

:loop
"System\tlang\tlang.exe" "System\os_new.tl" 

REM Check for directory change commands
if exist ".launch_cd_root" (
    del ".launch_cd_root"
    if exist ".current_Apps" del ".current_Apps"
    if exist ".current_Games" del ".current_Games"
    if exist ".current_System" del ".current_System"
)
if exist ".launch_cd_Apps" (
    del ".launch_cd_Apps"
    if exist ".current_Games" del ".current_Games"
    if exist ".current_System" del ".current_System"
    echo. > ".current_Apps"
)
if exist ".launch_cd_Games" (
    del ".launch_cd_Games"
    if exist ".current_Apps" del ".current_Apps"
    if exist ".current_System" del ".current_System"
    echo. > ".current_Games"
)
if exist ".launch_cd_System" (
    del ".launch_cd_System"
    if exist ".current_Apps" del ".current_Apps"
    if exist ".current_Games" del ".current_Games"
    echo. > ".current_System"
)

REM Check for exit command
if exist ".launch_exit" (
    del ".launch_exit"
    if exist ".current_Apps" del ".current_Apps"
    if exist ".current_Games" del ".current_Games"
    if exist ".current_System" del ".current_System"
    exit /b
)

REM Check for launch commands - Apps folder
if exist ".launch_studio" (
    del ".launch_studio"
    start "" "Apps\TLangIDE.exe"
)
if exist ".launch_calc" (
    del ".launch_calc"
    start "" /wait "System\tlang\tlang.exe" "Apps\calculator.tl"
)
if exist ".launch_browser" (
    del ".launch_browser"
    start "" pythonw "Apps\browser.pyw"
)
if exist ".launch_notepad" (
    del ".launch_notepad"
    start "" pythonw "Apps\notepad.pyw"
)
if exist ".launch_explorer" (
    del ".launch_explorer"
    start "" pythonw "Apps\explorer.pyw"
)
if exist ".launch_time" (
    del ".launch_time"
    start "" /wait "System\tlang\tlang.exe" "Apps\time.tl"
)

REM Check for launch commands - Games folder
if exist ".launch_snake" (
    del ".launch_snake"
    start "" "System\tlang\tlang.exe" "Games\snake.tl"
)
if exist ".launch_flappybird" (
    del ".launch_flappybird"
    start "" "System\tlang\tlang.exe" "Games\flappybird.tl"
)
if exist ".launch_minecraft" (
    del ".launch_minecraft"
    start "" python "Games\minecraft.py"
)
if exist ".launch_slamdunk" (
    del ".launch_slamdunk"
    start "" python "Games\slam dunk.py"
)

goto loop

