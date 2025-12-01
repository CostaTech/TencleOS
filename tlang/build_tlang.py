# Build Script per TLang IDE
# Crea eseguibile standalone dell'IDE

"""
REQUISITI:
pip install pyinstaller pillow

UTILIZZO:
python build_tlang.py
"""

import os
import sys

def build_ide():
    print("=" * 60)
    print("TLang - Build System")
    print("=" * 60)
    print()
    
    # Check if pyinstaller is installed
    try:
        import PyInstaller
    except ImportError:
        print("❌ PyInstaller non trovato!")
        print("Installa con: pip install pyinstaller")
        return False
    
    print("✅ PyInstaller trovato")
    
    # Build command
    cmd = [
        "pyinstaller",
        "--name=TLangIDE",
        "--onefile",
        "--windowed",  # No console window
        "--icon=tlang_icon.ico" if os.path.exists("tlang_icon.ico") else "",
        "--add-data=config.py;.",
        "--add-data=lexer.py;.",
        "--add-data=tlang_parser.py;.",
        "--add-data=interpreter.py;.",
        "tlang_ide.py"
    ]
    
    # Remove empty strings
    cmd = [c for c in cmd if c]
    
    print("\n📦 Creazione eseguibile...")
    print(f"Comando: {' '.join(cmd)}\n")
    
    import subprocess
    result = subprocess.run(cmd)
    
    if result.returncode == 0:
        print("\n✅ Build completato!")
        print(f"Eseguibile: dist/TLangIDE.exe")
        return True
    else:
        print("\n❌ Build fallito")
        return False

def create_icon():
    """Crea icona per TLang"""
    print("\n🎨 Creazione icona TLang...")
    
    try:
        from PIL import Image, ImageDraw, ImageFont
        
        # Crea immagine 256x256
        size = 256
        img = Image.new('RGB', (size, size), color='#1e1e1e')
        draw = ImageDraw.Draw(img)
        
        # Disegna "T"
        draw.rectangle([50, 50, 206, 206], fill='#007acc', outline='#569cd6', width=5)
        
        try:
            font = ImageFont.truetype("arial.ttf", 150)
        except:
            font = ImageFont.load_default()
        
        draw.text((128, 128), "T", fill='white', anchor="mm", font=font)
        
        # Salva come ICO
        img.save("tlang_icon.ico", format='ICO')
        print("✅ Icona creata: tlang_icon.ico")
        return True
        
    except ImportError:
        print("⚠️ PIL/Pillow non trovato, icona non creata")
        print("Installa con: pip install pillow")
        return False
    except Exception as e:
        print(f"⚠️ Errore creazione icona: {e}")
        return False

def create_registry_script():
    """Crea script per associare .tlang a TLangIDE"""
    
    script = """@echo off
REM Associa estensione .tlang a TLang IDE
REM Esegui come Amministratore

echo ================================================
echo TLang - Associazione File .tlang
echo ================================================
echo.

REM Get IDE path
set IDE_PATH=%~dp0TLangIDE.exe

echo IDE Path: %IDE_PATH%
echo.

REM Create file association
echo Creazione associazione .tlang...
reg add "HKEY_CLASSES_ROOT\\.tlang" /ve /d "TLangFile" /f
reg add "HKEY_CLASSES_ROOT\\TLangFile" /ve /d "TLang Source File" /f
reg add "HKEY_CLASSES_ROOT\\TLangFile\\DefaultIcon" /ve /d "%IDE_PATH%,0" /f
reg add "HKEY_CLASSES_ROOT\\TLangFile\\shell\\open\\command" /ve /d "\"%IDE_PATH%\" \"%%1\"" /f
reg add "HKEY_CLASSES_ROOT\\TLangFile\\shell\\edit\\command" /ve /d "\"%IDE_PATH%\" \"%%1\"" /f

echo.
echo ================================================
echo Associazione completata!
echo ================================================
echo.
echo Ora puoi aprire file .tlang con doppio click!
echo.
pause
"""
    
    with open("associate_tlang.bat", "w") as f:
        f.write(script)
    
    print("\n✅ Script associazione creato: associate_tlang.bat")
    print("   (Esegui come Amministratore per associare .tlang)")

def create_installer_script():
    """Crea script Inno Setup per installer"""
    
    script = r"""
; TLang Installer Script (Inno Setup)
; Compila con Inno Setup Compiler

[Setup]
AppName=TLang IDE
AppVersion=1.0
DefaultDirName={autopf}\TLang
DefaultGroupName=TLang
OutputDir=.
OutputBaseFilename=TLangSetup
Compression=lzma2
SolidCompression=yes
ChangesAssociations=yes

[Files]
Source: "dist\TLangIDE.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "*.tlang"; DestDir: "{app}\examples"; Flags: ignoreversion recursesubdirs

[Icons]
Name: "{group}\TLang IDE"; Filename: "{app}\TLangIDE.exe"
Name: "{commondesktop}\TLang IDE"; Filename: "{app}\TLangIDE.exe"

[Registry]
Root: HKCR; Subkey: ".tlang"; ValueType: string; ValueName: ""; ValueData: "TLangFile"; Flags: uninsdeletevalue
Root: HKCR; Subkey: "TLangFile"; ValueType: string; ValueName: ""; ValueData: "TLang Source File"; Flags: uninsdeletekey
Root: HKCR; Subkey: "TLangFile\DefaultIcon"; ValueType: string; ValueName: ""; ValueData: "{app}\TLangIDE.exe,0"
Root: HKCR; Subkey: "TLangFile\shell\open\command"; ValueType: string; ValueName: ""; ValueData: """{app}\TLangIDE.exe"" ""%1"""

[Run]
Filename: "{app}\TLangIDE.exe"; Description: "Avvia TLang IDE"; Flags: postinstall nowait skipifsilent
"""
    
    with open("tlang_installer.iss", "w") as f:
        f.write(script)
    
    print("\n✅ Script installer creato: tlang_installer.iss")
    print("   (Compila con Inno Setup per creare installer)")

def main():
    print("\n🚀 TLang Build System\n")
    
    # Step 1: Crea icona
    create_icon()
    
    # Step 2: Build IDE
    if not build_ide():
        print("\n⚠️ Build fallito, altri file non creati")
        return
    
    # Step 3: Crea script associazione
    create_registry_script()
    
    # Step 4: Crea script installer
    create_installer_script()
    
    print("\n" + "=" * 60)
    print("✅ BUILD COMPLETATO!")
    print("=" * 60)
    print("\n📁 File creati:")
    print("   • dist/TLangIDE.exe - Eseguibile IDE")
    print("   • associate_tlang.bat - Associa .tlang (esegui come Admin)")
    print("   • tlang_installer.iss - Installer Inno Setup")
    print("\n🎯 PROSSIMI PASSI:")
    print("   1. Testa TLangIDE.exe in dist/")
    print("   2. Esegui associate_tlang.bat come Amministratore")
    print("   3. Doppio click su file .tlang per aprirli nell'IDE!")
    print("\n   (Opzionale) Crea installer con Inno Setup")
    print("=" * 60)

if __name__ == "__main__":
    main()
