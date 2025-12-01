@echo off
REM Associa estensione .tlang a TLang IDE
REM Esegui come Amministratore

echo ================================================
echo TLang - Associazione File .tlang
echo ================================================
echo.

REM Get IDE path
set IDE_PATH=%~dp0dist\TLangIDE.exe

echo IDE Path: %IDE_PATH%
echo.

REM Create file association
echo Creazione associazione .tlang...
reg add "HKEY_CLASSES_ROOT\.tlang" /ve /d "TLangFile" /f
reg add "HKEY_CLASSES_ROOT\TLangFile" /ve /d "TLang Source File" /f
reg add "HKEY_CLASSES_ROOT\TLangFile\DefaultIcon" /ve /d "%IDE_PATH%,0" /f
reg add "HKEY_CLASSES_ROOT\TLangFile\shell\open\command" /ve /d "\"%IDE_PATH%\" \"%%1\"" /f
reg add "HKEY_CLASSES_ROOT\TLangFile\shell\edit\command" /ve /d "\"%IDE_PATH%\" \"%%1\"" /f

echo.
echo ================================================
echo Associazione completata!
echo ================================================
echo.
echo Ora puoi aprire file .tlang con doppio click!
echo.
pause
