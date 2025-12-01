# Changelog

All notable changes to TencleOS-TLang will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned Features
- File I/O operations (`open()`, `read()`, `write()`)
- Class definitions and object-oriented programming
- Try-catch exception handling
- Package manager for TLang modules
- REPL auto-completion and history
- Breakpoint debugging in IDE
- Multi-file project support
- Standard library (file, network, regex)

---

## [1.0.0] - 2025-01-XX

### Added
- **TLang Language**: Complete custom programming language with 100% customizable syntax
- **Lexer**: Multi-character command tokenization with operator support
- **Parser**: Recursive descent parser supporting all statement types
- **Interpreter**: AST execution with Python library integration
- **TLangIDE**: Professional IDE with syntax highlighting and debug mode
- **Standalone Executable**: TLangIDE.exe (16.42 MB) with embedded Python + Pygame
- **Custom Syntax System**: Fully configurable commands via `config.py`
- **Import System**: Import Python modules with `use` keyword
- **Operators**: All arithmetic, comparison, logical, and assignment operators
- **Control Flow**: if/elif/else, while, for, break, continue
- **Data Types**: Numbers, strings, booleans (on/off), lists, None
- **Function Calls**: Call Python functions with arguments and keyword arguments
- **Attribute Access**: Access object attributes and methods
- **List Operations**: Create and index lists
- **Comments**: Python-style `#` comments
- **TencleOS**: Complete operating system interface converted to TLang
  - Main menu with ASCII art and 13 options
  - Snake game with pygame
  - Calculator application
  - User authentication system
- **Documentation**:
  - Comprehensive README with examples and FAQ
  - Quick start guide (QUICKSTART.md)
  - Contribution guidelines (CONTRIBUTING.md)
  - Technical documentation (PROJECT_INFO.md)
  - MIT License
- **IDE Features**:
  - Syntax highlighting (keywords, strings, numbers, comments)
  - Three-tab output panel (Output/Debug/Variables)
  - File menu (New/Open/Save)
  - Keyboard shortcuts (F5: Run, F6: Debug, Ctrl+N/O/S)
  - Debug mode with variable tracking
  - File association support (.tlang files open in IDE)
- **Custom Icon**: 512x512 orange hexagon logo embedded in executable
- **Website**: Full documentation site with HTML/CSS/JS

### Changed
- Moved from Python syntax to custom TLang syntax
- Replaced `print()` with `int << func >> ()`
- Replaced `if/else` with `<< ! >func> if` / `>> func << else`
- Replaced `while` with `<<While>>! <on>`
- Replaced `True/False` with `on/off`
- Replaced `break/continue` with `stop/nextstep`
- Replaced `//` comments with `#` comments
- Replaced `import` with `use` keyword

### Fixed
- Token type string to enum conversion in lexer
- Parser support for complex multi-character commands
- Standalone if statements (enforced if-elif-else chains)
- Icon not showing on EXE (cleared Windows icon cache)
- Print statements without parentheses
- Pygame module hidden imports for PyInstaller
- Comment recognition (changed from // to #)

### Technical Details
- **Python Version**: 3.9.13
- **Dependencies**: 
  - PyInstaller 6.17.0 (EXE compilation)
  - Pygame 2.6.1 (game library)
  - Pillow 11.3.0 (image/icon processing)
  - Tkinter (built-in, for IDE GUI)
- **Build Command**: 
  ```bash
  pyinstaller --name=TLangIDE --onefile --windowed --icon=tlang_icon.ico \
              --hidden-import=pygame tlang_ide.py --clean
  ```
- **File Structure**:
  ```
  TencleOS-TLang-Edition/
  ├── TLangIDE.exe (16.42 MB)
  ├── main-os.tlang
  ├── snake.tlang
  ├── calculator.tlang
  ├── tlang/ (source code)
  ├── user/ (authentication)
  ├── assets/ (images)
  └── documentation files
  ```

### Known Issues
- File I/O not implemented (hardcoded values used)
- No class/OOP support yet
- Limited debugging features (no breakpoints)
- No package manager for external modules
- Large executable size due to embedded Python + Pygame

### Security
- User credentials stored in plain text (development only)
- No encryption for sensitive data
- Recommend changing default credentials in production

---

## [0.9.0] - 2025-01-XX (Beta)

### Added
- Initial TLang prototype
- Basic lexer and parser
- Simple interpreter
- CLI interface
- Python syntax compatibility

### Changed
- N/A (first release)

### Fixed
- N/A (first release)

---

## Version History Summary

- **v1.0.0**: Full release with IDE, TencleOS, documentation
- **v0.9.0**: Beta prototype with basic functionality

---

## Release Notes

### How to Read This Changelog
- **Added**: New features
- **Changed**: Changes to existing functionality
- **Deprecated**: Features that will be removed in future versions
- **Removed**: Features that have been removed
- **Fixed**: Bug fixes
- **Security**: Security vulnerability fixes

### Version Numbering
- **MAJOR**: Incompatible API changes
- **MINOR**: Add functionality in a backward-compatible manner
- **PATCH**: Backward-compatible bug fixes

Example: v1.2.3 = Major.Minor.Patch

---

## Future Releases

### v1.1.0 (Planned)
- File I/O operations
- Improved error messages with line numbers
- Auto-save in IDE
- Dark/light theme toggle
- Code auto-completion

### v1.2.0 (Planned)
- Class and OOP support
- Try-catch exception handling
- Built-in debugger with breakpoints
- Step-through execution

### v2.0.0 (Long-term)
- Package manager (`tlang install`)
- Standard library
- Multi-file projects
- Module system
- Web framework

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to contribute.

Report bugs and request features in [GitHub Issues](https://github.com/yourusername/tencleos-tlang/issues).

---

**Last Updated**: 2025-01-XX
