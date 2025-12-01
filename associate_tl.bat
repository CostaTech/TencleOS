@echo off
REM Associa estensione .tl a TLang IDE
REM Esegui come Amministratore

echo ================================================
echo TLang - Associazione File .tl
echo ================================================
echo.

REM Get IDE path (directory corrente)
set IDE_PATH=%~dp0TLangIDE.exe
set ICON_PATH=%~dp0icon.ico

echo IDE Path: %IDE_PATH%
echo Icon Path: %ICON_PATH%
echo.

REM Create file association
echo Creazione associazione .tl...
reg add "HKEY_CLASSES_ROOT\.tl" /ve /d "TLangFile" /f
reg add "HKEY_CLASSES_ROOT\TLangFile" /ve /d "TLang Source File" /f
reg add "HKEY_CLASSES_ROOT\TLangFile\DefaultIcon" /ve /d "%ICON_PATH%" /f
reg add "HKEY_CLASSES_ROOT\TLangFile\shell\open\command" /ve /d "\"%IDE_PATH%\" \"%%1\"" /f
reg add "HKEY_CLASSES_ROOT\TLangFile\shell\edit\command" /ve /d "\"%IDE_PATH%\" \"%%1\"" /f

echo.
echo ================================================
echo Associazione completata!
echo ================================================
echo.
echo Ora puoi aprire file .tl con doppio click!
echo I file .tl avranno l'icona personalizzata!
echo.
pause
