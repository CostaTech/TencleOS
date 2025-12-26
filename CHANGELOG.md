# TencleOS v2.0 - Changelog

**Release Date:** December 22, 2025

## 🎉 Major Updates

### 1. DOS-Style Terminal Shell
- **Replaced** numbered menu system with professional command-line interface
- **Added** `T:\TencleOS>` prompt inspired by MS-DOS
- **Implemented** 30+ commands for system navigation and control
- **Loop system** using .bat file instead of TLang while loop (compatibility fix)
- **Clean ASCII art** logo without Unicode characters (encoding-safe)

### 2. TLangIDE Matrix Theme
- **New theme:** "Matrix" with black background (#000000) and green text (#00ff00)
- **Total themes:** 4 (Dark, Light, Monokai, Matrix)
- **Updated** TLangIDE.exe compiled with new theme
- **File association:** Created associate_tl_files.bat for .tl files

### 3. Organized File Structure
```
TencleOS/
├── os.bat                 (Main launcher)
├── Apps/                  (Applications folder)
│   ├── TLangIDE.exe       (IDE with Matrix theme)
│   ├── calculator.bat
│   ├── browser.pyw
│   ├── notepad.pyw
│   ├── explorer.pyw
│   └── time.bat
├── Games/                 (Games folder)
│   ├── snake.bat
│   ├── minecraft.bat
│   ├── slamdunk.bat
│   └── flappybird.tl
└── System/                (System files)
    ├── tlang/             (Interpreter)
    ├── os.tl              (Shell commands)
    ├── startup_music.py
    └── icon.ico
```

### 4. Shell Commands (30+)

**System Commands:**
- `help` - Show all available commands
- `ver` - Display TencleOS version
- `time` - Show current date/time
- `sysinfo` - System information
- `about` - About TencleOS
- `cls` / `clear` - Clear screen
- `exit` / `quit` - Exit shell

**File Commands:**
- `dir` / `ls` - List files and folders
- `pwd` - Show current directory
- `tree` - Display directory tree structure

**Application Commands:**
- `apps` - List all installed applications
- `run <app>` - Launch an application
- `studio` - Open TLang IDE
- `calc` - Launch calculator
- `snake` - Play Snake game
- `browser` - Open web browser
- `notepad` - Open text editor

**Utilities:**
- `echo <text>` - Print text to console
- `color` - Show color information
- `credits` - Display credits

### 5. Parser Improvements
- **Fixed** `<< ! >func>` marker handling in if/while statements
- **Added** EOF safety checks to prevent infinite loops
- **Fixed** token skipping logic to avoid hanging on invalid syntax
- **Support** for nested control structures

### 6. Python 3.14 Compatibility
- **Updated** all .bat files with Python 3.14.2 paths
- **Fixed** PyInstaller 6.17.0 compilation
- **Resolved** module dependencies (pygame, numpy)
- **Removed** datetime/time imports that caused blocking in TLang

### 7. Bug Fixes
- **Fixed** `input()` returning numbers instead of strings (changed PIN from "1234" to 1234)
- **Fixed** `use os` and `use sys` causing file hanging
- **Fixed** `while` loop blocking in .bat execution context
- **Fixed** Unicode characters in logo causing encoding issues
- **Removed** obsolete IDE executables (kept only Apps/TLangIDE.exe)

## 📊 Technical Changes

### Files Modified
- `os.tl` - Complete rewrite for shell system (from 179 to 250+ lines)
- `os.bat` - Updated to use System/tlang/tlang.py path
- `README.md` - Updated with v2.0 features and command list
- `tlang_parser.py` - Parser improvements for marker handling
- All `.bat` files - Updated Python paths to Python314

### Files Added
- `associate_tl_files.bat` - File association tool
- `shell_loop.tl` - Shell command handler (renamed to os.tl)
- Apps/, Games/, System/ folders - Organized structure

### Files Removed
- `dist/` and `build/` folders - Cleaned up compilation artifacts
- Old test files - Removed debug and test scripts
- Duplicate TLangIDE.exe files - Kept only one in Apps/

## 🎯 Conversion Progress

### TLang Applications (4/12)
✅ **os.tl** - Shell system with commands  
✅ **snake.tl** - Snake game  
✅ **calculator.tl** - Calculator  
✅ **time.tl** - Clock/Timer  

### Python Applications (8/12)
- browser.pyw
- notepad.pyw
- explorer.pyw
- flappybird.tl
- minecraft.py
- slamdunk.py
- TLangIDE (with Matrix theme)

## 🚀 Installation

1. Download TencleOS-GitHub folder
2. Run `associate_tl_files.bat` as Administrator (for .tl file association)
3. Double-click `os.bat` to launch TencleOS Shell
4. Enter PIN: 1234
5. Type `help` to see all commands

## 📝 Known Limitations

- TLang `while` loops don't work in .bat context (workaround: .bat handles the loop)
- `use os` and `use sys` cause file hanging (removed from os.tl)
- No file I/O support in TLang yet (apps launch via messages)
- `cls` command shows message instead of clearing (terminal limitation)

## 🎓 Credits

- **Developer:** CostaTech
- **Language:** TLang v1.1
- **Python Version:** 3.14.2
- **Year:** 2025

## 📅 Version History

- **v2.0** (Dec 22, 2025) - DOS shell, Matrix theme, organized structure
- **v1.0** (Nov 2025) - Initial release with numbered menu

---

**For updates and documentation, visit:** [GitHub Repository]
