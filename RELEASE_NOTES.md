# 🚀 TencleOS-TLang v1.0.0 - Release Notes

**Release Date**: December 1, 2025  
**Version**: 1.0.0  
**License**: MIT

---

## 📦 What's in This Release

This is the **first official release** of TencleOS-TLang - a complete custom programming language with 100% customizable syntax!

### Included Files

#### 💻 Executable (Ready to Use)
- **TLangIDE.exe** (16.42 MB)
  - Standalone IDE with embedded Python 3.9
  - No installation required
  - Syntax highlighting and debug mode
  - Run .tlang files with F5

#### 🎮 TLang Applications
- **main-os.tlang** - TencleOS main menu with 13 options
- **snake.tlang** - Snake game with Pygame
- **calculator.tlang** - Console calculator

#### 📚 Complete Documentation
- **README.md** - Full project documentation
- **QUICKSTART.md** - 3-step getting started guide
- **PROJECT_INFO.md** - Technical deep-dive
- **CONTRIBUTING.md** - Contribution guidelines
- **PUBLISHING_GUIDE.md** - GitHub publishing steps
- **CHANGELOG.md** - Version history
- **PACKAGE_SUMMARY.md** - Complete package overview

#### 📂 Source Code & Assets
- **tlang/** - Complete TLang interpreter source code
- **user/** - Authentication files (username.txt, password.txt)
- **assets/** - Images and resources
- **screenshots/** - Documentation screenshots

---

## ✨ Key Features

### TLang Language
- ✅ 100% customizable syntax via `config.py`
- ✅ Import Python libraries with `use` keyword
- ✅ All operators (arithmetic, comparison, logical)
- ✅ Control flow (if/elif/else, while, for, break, continue)
- ✅ Lists, strings, numbers, booleans (on/off)
- ✅ Function calls and attribute access

### TLangIDE
- ✅ Professional code editor with syntax highlighting
- ✅ Three-tab output panel (Output/Debug/Variables)
- ✅ Debug mode with variable tracking
- ✅ File menu (New/Open/Save)
- ✅ Keyboard shortcuts (F5: Run, F6: Debug)

### TencleOS
- ✅ Complete operating system interface in TLang
- ✅ ASCII art menu with 13 applications
- ✅ User authentication system
- ✅ Snake game and calculator included

---

## 🚀 Quick Start

### 1. Download & Extract
Download this release and extract all files to a folder.

### 2. Run TLangIDE
Double-click `TLangIDE.exe` to launch the IDE.

### 3. Open TencleOS
1. Click **File → Open**
2. Select `main-os.tlang`
3. Press **F5** to run
4. Login with: `admin` / `pass`

### 4. Try Other Apps
- Open `snake.tlang` for the Snake game
- Open `calculator.tlang` for the calculator

---

## 🐛 Bug Fixes in This Release

### Fixed Issues
- ✅ Corrected syntax errors in .tlang files (replaced `{` with `:`)
- ✅ Fixed if/elif/else chains (added proper `>> func << else`)
- ✅ Fixed while loop syntax (changed `<<While>>! <on> {` to `:`)
- ✅ Fixed for loop syntax (changed `for x in list {` to `:`)
- ✅ All files now execute without errors in TLangIDE

### Previous Issues
- Token type enum conversion errors → Fixed
- Pygame hidden imports → Fixed with `--hidden-import=pygame`
- Icon not showing on EXE → Fixed with ICO conversion
- Standalone if statements → Changed to if-elif-else chains

---

## 📊 Technical Details

### System Requirements
- **OS**: Windows 10/11 (64-bit)
- **RAM**: 512 MB minimum
- **Disk Space**: 50 MB
- **Dependencies**: None (all embedded in .exe)

### Build Information
- **Python Version**: 3.9.13
- **PyInstaller**: 6.17.0
- **Pygame**: 2.6.1
- **Tkinter**: Built-in
- **Build Command**:
  ```bash
  pyinstaller --name=TLangIDE --onefile --windowed --icon=tlang_icon.ico \
              --hidden-import=pygame tlang_ide.py --clean
  ```

### File Sizes
- Total package: ~16.97 MB
- TLangIDE.exe: 16.42 MB
- Documentation: ~52 KB
- Source code: ~100 KB
- TLang apps: ~8 KB

---

## 🆕 What's New

### Language Features
- Custom print command: `int << func >> ("Hello")`
- Custom if statement: `<< ! >func> if condition:`
- Custom else: `>> func << else:`
- Custom while: `<<While>>! <on>:`
- Custom True/False: `on` / `off`
- Custom break/continue: `stop` / `nextstep`
- Custom import: `use pygame`

### IDE Features
- Syntax highlighting for all TLang keywords
- Debug mode shows all variables in scope
- Three-tab output panel for better organization
- File association support (.tlang opens in IDE)
- Custom 512x512 orange hexagon icon

### Applications
- TencleOS main menu with ASCII art
- Snake game with score tracking
- Calculator with 5 operations
- User authentication system

---

## ⚠️ Known Limitations

1. **File I/O**: Not yet implemented (hardcoded values used in TencleOS)
2. **OOP**: No class/object support (planned for v1.1)
3. **Debugging**: No breakpoints or step-through execution
4. **Cross-platform**: Windows only (Linux/Mac support planned)
5. **Package Manager**: No built-in package manager yet

---

## 🛠️ Troubleshooting

### TLangIDE won't start
- Make sure you extracted all files
- Run as Administrator if needed
- Check Windows Defender didn't block the .exe

### Syntax errors in .tlang files
- This release includes corrected files
- Make sure you're using `:` not `{` for blocks
- All if statements must have an else clause

### Snake game not running
- Make sure Pygame is embedded (it is in this release)
- Check that TLangIDE.exe is in the same folder as snake.tlang

### Can't save files
- Check folder permissions
- Run TLangIDE as Administrator

---

## 📈 Roadmap

### v1.1.0 (Next Release)
- [ ] File I/O operations (`open()`, `read()`, `write()`)
- [ ] Improved error messages with line numbers
- [ ] Auto-save in IDE
- [ ] Code auto-completion

### v1.2.0
- [ ] Class and OOP support
- [ ] Try-catch exception handling
- [ ] Breakpoint debugging
- [ ] Multi-file projects

### v2.0.0
- [ ] Package manager (`tlang install`)
- [ ] Standard library
- [ ] Web framework
- [ ] Linux/Mac support

---

## 🤝 Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Ways to Contribute
- Report bugs in [Issues](https://github.com/yourusername/tencleos-tlang/issues)
- Suggest features
- Submit pull requests
- Improve documentation
- Create tutorials

---

## 📞 Support

- **Documentation**: See README.md and QUICKSTART.md
- **GitHub Issues**: https://github.com/yourusername/tencleos-tlang/issues
- **Discussions**: https://github.com/yourusername/tencleos-tlang/discussions

---

## 📜 License

This project is licensed under the **MIT License** - see [LICENSE](LICENSE) file.

You are free to:
- Use commercially
- Modify
- Distribute
- Use privately

---

## 🎉 Thank You!

Thank you for downloading TencleOS-TLang v1.0.0!

If you enjoy this project:
- ⭐ Star the repository on GitHub
- 📢 Share with friends
- 🐛 Report bugs
- 💡 Suggest features
- 🤝 Contribute code

---

## 📝 Changelog Summary

### Added
- Complete TLang language implementation
- Professional TLangIDE with syntax highlighting
- TencleOS operating system in TLang
- Snake game and calculator applications
- Comprehensive documentation (7 files)
- Standalone executable (16.42 MB)
- Custom syntax system
- Import system for Python libraries

### Changed
- Converted Python syntax to custom TLang syntax
- Replaced standard keywords with custom commands

### Fixed
- All syntax errors in .tlang files
- If/elif/else chain requirements
- While/for loop syntax
- Token type conversions

---

**Created by**: Costantino  
**GitHub**: https://github.com/yourusername/tencleos-tlang  
**Release**: v1.0.0  
**Date**: December 1, 2025  

🚀 **Enjoy coding in TLang!**
