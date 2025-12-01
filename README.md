# TencleOS - TLang Edition

<div align="center">

![TencleOS Logo](assets/logo.png)

**A Full Operating System Interface Written in TLang**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![TLang](https://img.shields.io/badge/Language-TLang-orange.svg)](https://github.com/yourusername/tlang)
[![Version](https://img.shields.io/badge/Version-1.0-blue.svg)](https://github.com/yourusername/tencleos-tlang)

[Features](#features) • [Installation](#installation) • [Usage](#usage) • [Documentation](#documentation) • [Contributing](#contributing)

</div>

---

## 📖 About

**TencleOS** is a custom operating system interface built entirely in **TLang**, a programming language with 100% customizable syntax. This project demonstrates the power and flexibility of TLang by implementing a complete OS menu system with integrated applications.

### What is TLang?

TLang is a revolutionary programming language where **every command can be customized**. Don't like `print()`? Change it to anything you want in `config.py`!

**Example:**
```tlang
int << func >> ("Hello, World!")

<< ! >func> if x > 10 {
    int << func >> ("X is large")
}

<<While>>! <on> running {
    int << func >> ("Loop running...")
}
```

---

## ✨ Features

### 🎯 TencleOS Applications

- **🌐 Tencle-Browser** - Web browser interface
- **📝 Tencle-Pad** - Text editor
- **📁 Tencle-Explorer** - File manager
- **⏰ Tencle-Time** - Clock and timer
- **🎮 Games:**
  - Snake Game (fully functional in TLang!)
  - Flappy Bird
  - Slam Dunk
  - Minecraft Clone
- **🧮 Tencle-Calculator** - Full calculator in TLang
- **💻 Tencle-Studio** - Code editor
- **🛒 Tencle-Store** - App store interface
- **💬 Tencle-Social** - Social network (Terext)

### 🚀 TLang Features

- ✅ **Custom Syntax** - Change any command in `config.py`
- ✅ **Python Integration** - Import any Python library with `use`
- ✅ **Pygame Support** - Full game development capability
- ✅ **Professional IDE** - Syntax highlighting & debug mode
- ✅ **Standalone EXE** - 16MB executable with no dependencies

---

## 📦 Installation

### Prerequisites

- **Windows 10/11** (64-bit)
- No Python installation required! (Everything is included)

### Method 1: Standalone Executable (Recommended)

1. **Download TLangIDE.exe**
   ```bash
   # Download from releases page
   https://github.com/yourusername/tencleos-tlang/releases
   ```

2. **Download TencleOS Files**
   ```bash
   git clone https://github.com/yourusername/tencleos-tlang.git
   cd tencleos-tlang
   ```

3. **Run TencleOS**
   - Double-click `TLangIDE.exe`
   - File → Open → Select `main-os.tlang`
   - Press **F5** to run

### Method 2: Python Source

1. **Clone Repository**
   ```bash
   git clone https://github.com/yourusername/tencleos-tlang.git
   cd tencleos-tlang
   ```

2. **Install TLang** (if using source)
   ```bash
   cd tlang
   pip install pygame pillow
   ```

3. **Run TencleOS**
   ```bash
   python tlang.py main-os.tlang
   ```

---

## 🎮 Usage

### Starting TencleOS

1. **Open TLangIDE.exe**
2. **Load main-os.tlang**
3. **Press F5** to execute
4. **Choose an option** from the menu (1-13)

### Menu Options

```
████████╗███████╗███╗   ██╗ ██████╗██╗     ███████╗ ██████╗ ███████╗
╚══██╔══╝██╔════╝████╗  ██║██╔════╝██║     ██╔════╝██╔═══██╗██╔════╝
   ██║   █████╗  ██╔██╗ ██║██║     ██║     █████╗  ██║   ██║███████╗
   ██║   ██╔══╝  ██║╚██╗██║██║     ██║     ██╔══╝  ██║   ██║╚════██║
   ██║   ███████╗██║ ╚████║╚██████╗███████╗███████╗╚██████╔╝███████║
   ╚═╝   ╚══════╝╚═╝  ╚═══╝ ╚═════╝╚══════╝╚══════╝ ╚═════╝ ╚══════╝

Welcome Costantino!
Today is: 120125

[1] Open Google In Tencle-Browser
[2] Open Tencle-Pad
[3] Open Tencle-Explorer
[4] Open Tencle-Time
[5] Open Tencle-game(flappybird)
[6] Open Tencle-game(slamdunk)
[7] Open Tencle-game(Minecraft)
[8] Open Tencle-game(Snake)
[9] Open Tencle-Social(Terext)
[10] Open Tencle-calculator
[11] Open Tencle-Studio code editor
[12] Open Tencle-Store
[13] Quit Tencle-Os Safely
```

### Running Individual Apps

**Snake Game:**
```bash
# In TLangIDE
File → Open → snake.tlang
Press F5
```

**Calculator:**
```bash
# In TLangIDE  
File → Open → calculator.tlang
Press F5
```

### IDE Shortcuts

- **F5** - Run program
- **F6** - Debug mode (show Lexer/Parser/Interpreter)
- **Ctrl+O** - Open file
- **Ctrl+S** - Save file
- **Ctrl+N** - New file

---

## 📚 Documentation

### TLang Syntax Reference

#### Variables
```tlang
name = "TencleOS"
version = 1.0
active = on  # on/off instead of True/False
```

#### Print Statement
```tlang
int << func >> ("Hello World!")
int << func >> (variable)
```

#### Conditionals
```tlang
<< ! >func> if x == 5 {
    int << func >> ("Five")
} elif x > 5 {
    int << func >> ("Greater than five")
} >> func << else {
    int << func >> ("Less than five")
}
```

#### Loops
```tlang
# While loop
<<While>>! <on> running {
    int << func >> ("Running...")
}

# For loop
for i in [1, 2, 3, 4, 5] {
    int << func >> (i)
}

# Break
for i in [1, 2, 3] {
    << ! >func> if i == 2 {
        stop  # Break
    }
    int << func >> (i)
}
```

#### Importing Libraries
```tlang
use pygame
use math
use random

pygame.init()
result = math.sqrt(16)
num = random.randint(1, 100)
```

#### Lists
```tlang
numbers = [10, 20, 30, 40]
int << func >> (numbers[0])  # Prints 10

for num in numbers {
    int << func >> (num)
}
```

### Customizing TLang Syntax

Edit `config.py` to change commands:

```python
# config.py
COMANDO_PRINT = "stampa"  # Change print command
COMANDO_IF = "se"         # Change if command
COMANDO_WHILE = "mentre"  # Change while command
```

Now you can write:
```tlang
stampa ("Ciao!")

se if x > 5 {
    stampa ("Grande!")
}
```

---

## 🏗️ Project Structure

```
TencleOS-TLang-Edition/
├── main-os.tlang          # Main OS menu (START HERE)
├── snake.tlang            # Snake game
├── calculator.tlang       # Calculator app
├── user/                  # User data
│   ├── username.txt
│   └── password.txt
├── assets/                # Images and resources
├── TLangIDE.exe          # Standalone IDE (16MB)
├── README.md             # This file
└── tlang/                # TLang source code
    ├── config.py         # Syntax customization
    ├── lexer.py          # Tokenizer
    ├── tlang_parser.py   # Parser
    ├── interpreter.py    # Interpreter
    ├── tlang.py          # CLI
    └── tlang_ide.py      # GUI IDE
```

---

## 🔧 Building from Source

### Build TLangIDE.exe

```bash
cd tlang
pip install pyinstaller pygame pillow

pyinstaller --name=TLangIDE \
            --onefile \
            --windowed \
            --icon=tlang_icon.ico \
            --hidden-import=pygame \
            --hidden-import=pygame.base \
            --hidden-import=pygame.constants \
            --hidden-import=pygame.rect \
            --hidden-import=pygame.mixer \
            tlang_ide.py
```

Output: `dist/TLangIDE.exe` (16MB standalone)

### Associate .tlang Files (Windows)

Run as Administrator:
```bash
associate_tlang.bat
```

Now double-clicking any `.tlang` file opens it in TLangIDE!

---

## 🎯 Examples

### Example 1: Hello World
```tlang
int << func >> ("Welcome to TencleOS!")
int << func >> ("Made with TLang")
```

### Example 2: Simple Calculator
```tlang
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

n1 = float(num1)
n2 = float(num2)

result = n1 + n2
int << func >> ("Result: " + str(result))
```

### Example 3: Snake Game Loop
```tlang
use pygame

pygame.init()
screen = pygame.display.set_mode([600, 400])
running = on

<<While>>! <on> running {
    events = pygame.event.get()
    
    for e in events {
        << ! >func> if e.type == pygame.QUIT {
            running = off
        }
    }
    
    screen.fill([0, 0, 0])
    pygame.display.flip()
}

pygame.quit()
```

---

## 🐛 Known Limitations

TLang currently does NOT support:
- ❌ File I/O (`open()`, `read()`, `write()`)
- ❌ Complex Tkinter GUI components
- ❌ `.pyw` files (Python windowless)
- ❌ Some advanced Python libraries

**Workaround:** Use hardcoded values or Python imports where needed.

---

## 🤝 Contributing

Contributions are welcome! Here's how:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Commit your changes**
   ```bash
   git commit -m 'Add amazing feature'
   ```
4. **Push to branch**
   ```bash
   git push origin feature/amazing-feature
   ```
5. **Open a Pull Request**

### Areas for Contribution

- [ ] Add file I/O support to TLang
- [ ] Convert more Python apps to TLang
- [ ] Create GUI library for TLang
- [ ] Add more games
- [ ] Improve documentation
- [ ] Create video tutorials

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Costantino**

- GitHub: [@yourusername](https://github.com/yourusername)
- Project: [TencleOS-TLang](https://github.com/yourusername/tencleos-tlang)

---

## 🙏 Acknowledgments

- **TLang** - The revolutionary customizable programming language
- **Pygame** - Game development library
- **Python** - Base implementation language
- **Terry A. Davis** - Inspiration from TempleOS and HolyC

---

## 📸 Screenshots

### TencleOS Main Menu
![Main Menu](screenshots/main-menu.png)

### Calculator
![Calculator](screenshots/calculator.png)

### TLangIDE
![TLangIDE](screenshots/ide.png)

---

## 🚀 Roadmap

- [x] Core OS menu system
- [x] Snake game in TLang
- [x] Calculator in TLang
- [x] Standalone EXE distribution
- [ ] File I/O support
- [ ] GUI framework for TLang
- [ ] More games (Flappy Bird, Minecraft)
- [ ] Text editor in TLang
- [ ] Browser integration
- [ ] Plugin system

---

## ❓ FAQ

**Q: Do I need Python installed?**  
A: No! TLangIDE.exe is completely standalone (16MB).

**Q: Can I modify the TLang syntax?**  
A: Yes! Edit `config.py` to change any command.

**Q: How do I run TencleOS?**  
A: Open `main-os.tlang` in TLangIDE and press F5.

**Q: Can I create my own TLang programs?**  
A: Absolutely! Check the documentation and examples.

**Q: Is TencleOS a real OS?**  
A: It's an OS interface/menu system, not a kernel-level OS.

**Q: Can I contribute?**  
A: Yes! See the [Contributing](#contributing) section.

---

<div align="center">

**⭐ Star this repo if you find it useful! ⭐**

Made with ❤️ and TLang

</div>
