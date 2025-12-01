# TencleOS

<div align="center">

![TencleOS Logo](assets/logo.png)

**A Complete Operating System Interface Built with TLang & Python**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![TLang](https://img.shields.io/badge/Language-TLang-orange.svg)](https://github.com/CostaTech/TencleOS)
[![Python](https://img.shields.io/badge/Language-Python-blue.svg)](https://www.python.org/)
[![Version](https://img.shields.io/badge/Version-1.0-green.svg)](https://github.com/CostaTech/TencleOS)

[Features](#features) • [Installation](#installation) • [Usage](#usage) • [Documentation](#documentation) • [Contributing](#contributing)

</div>

---

## 📖 About

### 🖥️ What is TencleOS?

**TencleOS** is a complete operating system interface that reimagines how you interact with your computer. Think of it as a custom desktop environment with its own launcher, applications, and ecosystem - all accessible through an elegant text-based menu.

**The Vision:**
TencleOS isn't trying to replace Windows or Linux. It's a **proof of concept** that demonstrates how you can build a cohesive, functional operating system interface using a custom programming language (TLang). It shows that with the right tools, anyone can create their own OS experience.

**What Makes TencleOS Special:**

1. **🎨 Unified Design Language**
   - Every app follows the "Tencle" naming convention (Tencle-Browser, Tencle-Pad, etc.)
   - Consistent ASCII art branding across all components
   - Professional look despite being text-based

2. **🔐 Security First**
   - PIN-based authentication (not just decorative - it actually works!)
   - User session management
   - Protected access to all applications

3. **🎮 Entertainment & Productivity**
   - 4 fully functional games (Snake, Flappy Bird, Minecraft clone, Slam Dunk)
   - 3 productivity tools (Text editor, File explorer, Calculator)
   - Web browser integration
   - Social network platform (Terext)

4. **🚀 Zero Installation**
   - Single 8.99 MB executable (TLangIDE.exe)
   - No Python installation required
   - Portable - run from USB stick
   - Works on any Windows 10/11 machine

5. **🧪 Educational Value**
   - See how OS interfaces work under the hood
   - Learn TLang by reading real application code
   - Understand the boot → login → menu → app workflow
   - Perfect for computer science students

**The Hybrid Technology Stack: TLang + Python**

TencleOS uses a **dual-language architecture** combining the strengths of both languages:

| Component | Language | Why? |
|-----------|----------|------|
| **Login System** | TLang | Demonstrates custom syntax for authentication |
| **Main Menu** | TLang | Shows TLang handling user input & flow control |
| **Snake Game** | TLang | Proves TLang can build full games with Pygame |
| **Calculator** | TLang | Math operations in custom syntax |
| **Clock/Timer** | TLang | Real-time display with TLang |
| **Web Browser** | Python | Complex GUI - Python's strength |
| **File Explorer** | Python | File I/O not yet in TLang |
| **Text Editor** | Python | Advanced text handling |
| **Flappy Bird** | Python | Physics engine complexity |
| **Minecraft Clone** | Python | 3D graphics with Ursina |
| **Other Games** | Python | Mature libraries available |

**Why Not 100% TLang?**
TLang is still evolving. File I/O and complex GUI aren't implemented yet. Rather than limit functionality, we use Python for advanced features while showcasing TLang for core OS components. This proves TLang can **coexist and integrate** with established languages.

**Architecture Benefits:**
- ✅ TLang handles the OS "shell" (login, menu, launcher)
- ✅ Python handles the "applications" (browser, games, tools)
- ✅ Best of both worlds: innovation + stability
- ✅ Total Size: Only 15 MB including all assets

**Why "TencleOS"?**
The name comes from "Tentacle" - representing how the system reaches out to connect different applications, languages (TLang + Python), and user needs into one cohesive experience.

### 🌟 What is TLang?

TLang is a revolutionary programming language where **every command can be customized**. Unlike traditional languages that lock you into their syntax, TLang lets you define your own keywords, operators, and commands in `config.py`.

**Why TLang is Different:**
- **100% Customizable Syntax** - Change `print` to `stampa`, `if` to `se`, anything you want
- **Python Library Integration** - Use pygame, ursina, and any Python module
- **Game Development Ready** - Full support for 2D/3D game engines
- **Educational** - Learn how lexers, parsers, and interpreters work
- **Portable** - One 8.99 MB executable, no installation needed

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

### 📜 Project Origin & Evolution

**Phase 1: The Python Era (Original TencleOS)**
TencleOS began as a Python project - a collection of apps and games unified under one menu system. It was functional but limited to Python's ecosystem.

**Phase 2: The TLang Revolution (Current)**
When TLang was created with its revolutionary customizable syntax, we asked: *"Can TLang build real applications?"*

The answer: **Convert TencleOS to TLang.**

**The Conversion Journey:**
- ✅ **os.py → os.tl** - Login system converted (from username/password to PIN due to TLang limitations)
- ✅ **main-os.py → main-os.tl** - Main menu fully converted
- ✅ **snake.py → snake.tl** - Full game with Pygame graphics
- ✅ **calculator.py → calculator.tl** - Complete calculator logic
- ✅ **time.py → time.tl** - Real-time clock display
- 🔄 **Other apps** - Remaining 8 apps kept in Python (Flappy Bird, Minecraft, etc.)

**Challenges Overcome:**
1. **String Comparison Issue** - TLang's `input()` couldn't reliably compare strings, so we switched from username/password to numeric PIN
2. **File I/O Limitation** - TLang doesn't support file operations yet, so user data stays in Python files
3. **`!` Character Bug** - The `!` in `<< ! >func> if` wasn't recognized - we added NOT token to lexer
4. **Extension Migration** - Changed from `.tlang` to `.tl` for simplicity (15 files renamed)

**What This Proves:**
TencleOS demonstrates that TLang isn't just a toy or educational language. It's a **production-capable** language that can:
- Handle user input and conditional logic
- Integrate with powerful libraries (Pygame, os module)
- Build games with collision detection and scoring
- Create professional interfaces with ASCII art
- Run as standalone executables

**The Future:**
With file I/O support (planned for TLang v2.0), we could convert ALL Python apps to TLang, making TencleOS a 100% custom-language operating system.

---

## ✨ Features

### 🎯 TencleOS Applications

TencleOS includes **13 integrated applications**:

| App | Description | Language | Features |
|-----|-------------|----------|----------|
| 🌐 **Tencle-Browser** | Web browser | Python | Google search integration |
| 📝 **Tencle-Pad** | Text editor | Python | File editing, syntax highlighting |
| 📁 **Tencle-Explorer** | File manager | Python | Browse directories, open files |
| ⏰ **Tencle-Time** | Clock/Timer | **TLang** | Real-time clock display |
| 🐍 **Snake Game** | Classic snake | **TLang** | Collision detection, scoring, game over |
| 🧮 **Tencle-Calculator** | Calculator | **TLang** | All math operations |
| 🐦 **Flappy Bird** | Flappy Bird clone | Python | Full game with physics |
| ⛏️ **Minecraft** | Minecraft clone | Python | 3D world with Ursina engine |
| 🏀 **Slam Dunk** | Basketball game | Python | Sports game simulation |
| 💻 **Tencle-Studio** | Code editor | Python | Development environment |
| 🛒 **Tencle-Store** | App store | Python | Browse and install apps |
| 💬 **Tencle-Social** | Social network | Python | Terext social platform |
| 🔐 **Login System** | Authentication | **TLang** | PIN-based login (1234) |

**4 apps converted to TLang** (os.tl, main-os.tl, snake.tl, calculator.tl, time.tl) - proving TLang can handle real applications!

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

3. **Associate .tl Files (Optional)**
   - Right-click `associate_tl.bat`
   - Select "Run as Administrator"
   - Now .tl files have custom icon and open with TLangIDE

4. **Run TencleOS**
   - Double-click `os.bat` OR
   - Open `TLangIDE.exe` → File → Open → `main-os.tl`
   - Press **F5** to run
   - Enter PIN: **1234**

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

## 🎮 How to Use TencleOS

### 📖 Tutorial: Opening Software (3 Methods)

TencleOS offre **3 modi** per aprire le applicazioni:

#### **Metodo 1: Dal Menu Principale** (Raccomandato per nuovi utenti)

**Passo 1 - Avvia TencleOS:**
```bash
# Doppio click su uno di questi file:
os.bat           # Con login (PIN: 1234)
main-os.bat      # Direttamente al menu
```

**Passo 2 - Vedi il Menu:**
```
████████╗███████╗███╗   ██╗ ██████╗██╗     ███████╗ ██████╗ ███████╗
╚══██╔══╝██╔════╝████╗  ██║██╔════╝██║     ██╔════╝██╔═══██╗██╔════╝
   ██║   █████╗  ██╔██╗ ██║██║     ██║     █████╗  ██║   ██║███████╗
   ██║   ██╔══╝  ██║╚██╗██║██║     ██║     ██╔══╝  ██║   ██║╚════██║
   ██║   ███████╗██║ ╚████║╚██████╗███████╗███████╗╚██████╔╝███████║
   ╚═╝   ╚══════╝╚═╝  ╚═══╝ ╚═════╝╚══════╝╚══════╝ ╚═════╝ ╚══════╝

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

[?]:
```

**Passo 3 - Scegli App:**
```
# Vuoi giocare a Snake? Digita 8 e premi ENTER
[?]: 8

# Vuoi usare la calcolatrice? Digita 10 e premi ENTER
[?]: 10

# Vuoi cercare su Google? Digita 1 e premi ENTER
[?]: 1
```

**Esempio Completo - Giocare a Snake:**
```
1. Doppio click su os.bat
2. Inserisci PIN: 1234
3. Premi ENTER → appare menu
4. Digita: 8
5. Premi ENTER → Snake si avvia!
6. Gioca (frecce per muoverti)
7. Chiudi la finestra → torni al prompt
8. Per menu: doppio click main-os.bat
```

---

#### **Metodo 2: Launcher Diretti** (Veloce per app specifiche)

Ogni app ha un file `.bat` dedicato. Basta fare **doppio click**!

**Lista Launcher:**
```
📁 TencleOS/
├── snake.bat           ← Doppio click = Snake Game
├── calculator.bat      ← Doppio click = Calculator
├── time.bat            ← Doppio click = Clock
├── flappybird.bat      ← Doppio click = Flappy Bird
├── minecraft.bat       ← Doppio click = Minecraft
├── slamdunk.bat        ← Doppio click = Slam Dunk
└── explorer.bat        ← Doppio click = File Explorer
```

**Esempio - Aprire Calculator:**
```
1. Vai nella cartella TencleOS
2. Trova calculator.bat
3. Doppio click
4. La calcolatrice si apre immediatamente!
```

**Screenshot Tutorial:**
```
Windows Explorer:
┌──────────────────────────────────────┐
│ TencleOS                              │
├──────────────────────────────────────┤
│ 📄 calculator.bat    ← DOPPIO CLICK   │
│ 📄 snake.bat                          │
│ 📄 time.bat                           │
│ 📄 main-os.bat                        │
└──────────────────────────────────────┘
```

---

#### **Metodo 3: TLangIDE** (Per sviluppatori e modifiche)

Usa l'IDE per aprire file `.tl` e modificare/eseguire codice TLang.

**Passo 1 - Apri IDE:**
```
Doppio click su: TLangIDE.exe
```

**Passo 2 - Apri File TLang:**
```
1. Click su "File" in alto
2. Click su "Open" (o premi Ctrl+O)
3. Naviga alla cartella TencleOS
4. Seleziona un file .tl:
   - snake.tl
   - calculator.tl
   - time.tl
   - main-os.tl
5. Click "Open"
```

**Passo 3 - Esegui:**
```
Premi F5 (o click sul pulsante "Run")
```

**Passo 4 - Debug (Opzionale):**
```
Premi F6 per vedere:
- Lexer tokens
- Parser tree
- Interpreter execution
```

**Screenshot Tutorial:**
```
TLangIDE Window:
┌────────────────────────────────────────┐
│ File  Edit  Run  Debug                 │
├────────────────────────────────────────┤
│ 1  use pygame                          │
│ 2  use random                          │
│ 3                                      │
│ 4  int << func >> ("Snake Game!")     │
│ 5  ...                                 │
│                                        │
│ [F5 = Run]  [F6 = Debug]              │
└────────────────────────────────────────┘
```

**Esempio - Modificare Snake:**
```
1. Apri TLangIDE.exe
2. File → Open → snake.tl
3. Trova riga: speed = 10
4. Cambia in: speed = 20  (serpente più veloce!)
5. Premi F5
6. Gioca alla versione modificata!
```

---

### 🔧 System Architecture

TencleOS è un sistema a 3 livelli:

```
┌─────────────────────────────────────────────────────┐
│  LIVELLO 1: Login System (os.tl)                    │
│  • Chiede PIN (1234)                                 │
│  • Se corretto → lancia main-os.bat                  │
└─────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────┐
│  LIVELLO 2: Main Menu (main-os.tl)                  │
│  • Mostra banner ASCII                               │
│  • Lista 13 opzioni                                  │
│  • Riceve input utente (1-13)                        │
│  • Lancia app corrispondente                         │
└─────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────┐
│  LIVELLO 3: Applications                             │
│  • Browser → browser.pyw (Python)                    │
│  • Snake → snake.bat → snake.tl (TLang)              │
│  • Calculator → calculator.bat → calculator.tl       │
│  • Ogni app ha il suo launcher .bat                  │
└─────────────────────────────────────────────────────┘
```

### 🚀 Starting TencleOS

**Metodo 1: Esperienza Completa (con Login)**
```bash
# Doppio click su:
os.bat

# Output:
Enter PIN: 1234
Access Granted!
[Il sistema lancia automaticamente main-os.bat]
```

**Metodo 2: Direttamente al Menu Principale**
```bash
# Doppio click su:
main-os.bat

# Oppure in TLangIDE:
File → Open → main-os.tl
Press F5
```

**Metodo 3: App Singola**
```bash
# Doppio click su qualsiasi .bat:
snake.bat          # Lancia Snake game
calculator.bat     # Lancia Calculator
time.bat           # Lancia Clock
```

### 📝 Detailed Workflow

**Passo 1 - Login (os.tl):**
```tlang
# Codice semplificato da os.tl
use os

int << func >> ("=== TencleOS Login ===")
pin = input("Enter PIN: ")

<< ! >func> if pin == 1234 {
    int << func >> ("Access Granted!")
    os.startfile("main-os.bat")  # Lancia menu principale
} >> func << else {
    int << func >> ("Access Denied!")
}
```

**Passo 2 - Main Menu (main-os.tl):**
```tlang
# Mostra banner
int << func >> ("████████╗███████╗...")
int << func >> ("[1] Open Google In Tencle-Browser")
int << func >> ("[2] Open Tencle-Pad")
...

# Riceve scelta
select_input = input("[?]: ")

# Lancia app corrispondente
<< ! >func> if select_input == 1 {
    os.startfile("browser.pyw")
} elif select_input == 8 {
    os.startfile("snake.bat")
}
```

**Passo 3 - Esecuzione App:**
- **.bat files** → lanciano TLang o Python
- **.tl files** → eseguiti da TLangIDE/tlang.py
- **.pyw files** → eseguiti da Python (senza console)

### 🎯 Come Funzionano i Launcher .bat

Ogni app ha un suo file `.bat` che la esegue:

**snake.bat:**
```batch
@echo off
cd /d "%~dp0"
python tlang\tlang.py snake.tl
pause
```

**calculator.bat:**
```batch
@echo off
cd /d "%~dp0"
python tlang\tlang.py calculator.tl
pause
```

**Flusso completo:**
```
User → Doppio click snake.bat
       ↓
snake.bat → chiama python tlang\tlang.py snake.tl
       ↓
tlang.py → carica snake.tl
       ↓
Lexer → tokenizza il codice
       ↓
Parser → crea Abstract Syntax Tree
       ↓
Interpreter → esegue il gioco
       ↓
Output → finestra Pygame con Snake funzionante
```

### 🎮 Usage Examples

**Scenario 1: Avvio Completo Sistema**
1. Doppio click `os.bat`
2. Inserisci PIN: `1234`
3. Premi Enter → appare menu principale
4. Digita `8` → lancia Snake game
5. Gioca a Snake
6. Chiudi Snake → torni al prompt
7. Riapri `main-os.bat` per menu

**Scenario 2: Test Singola App**
1. Doppio click `snake.bat`
2. Snake si avvia direttamente
3. Gioca e chiudi

**Scenario 3: Sviluppo in IDE**
1. Apri `TLangIDE.exe`
2. File → Open → `snake.tl`
3. Premi `F5` → esegue in IDE
4. Vedi output nella console IDE
5. Modifica codice e ripremi F5

### 📋 Menu Options Explained

```
████████╗███████╗███╗   ██╗ ██████╗██╗     ███████╗ ██████╗ ███████╗
╚══██╔══╝██╔════╝████╗  ██║██╔════╝██║     ██╔════╝██╔═══██╗██╔════╝
   ██║   █████╗  ██╔██╗ ██║██║     ██║     █████╗  ██║   ██║███████╗
   ██║   ██╔══╝  ██║╚██╗██║██║     ██║     ██╔══╝  ██║   ██║╚════██║
   ██║   ███████╗██║ ╚████║╚██████╗███████╗███████╗╚██████╔╝███████║
   ╚═╝   ╚══════╝╚═╝  ╚═══╝ ╚═════╝╚══════╝╚══════╝ ╚═════╝ ╚══════╝

Welcome Costantino!
Today is: 120125

[1] Open Google In Tencle-Browser     → browser.pyw (Python)
[2] Open Tencle-Pad                   → notepad.pyw (Python)
[3] Open Tencle-Explorer               → explorer.pyw (Python)
[4] Open Tencle-Time                   → time.bat → time.tl (TLang)
[5] Open Tencle-game(flappybird)       → flappybird.bat → flappybird.py
[6] Open Tencle-game(slamdunk)         → slamdunk.bat → slam dunk.py
[7] Open Tencle-game(Minecraft)        → minecraft.bat → minecraft.py
[8] Open Tencle-game(Snake)            → snake.bat → snake.tl (TLang)
[9] Open Tencle-Social(Terext)         → terextsocial(incomplete).py
[10] Open Tencle-calculator            → calculator.bat → calculator.tl (TLang)
[11] Open Tencle-Studio code editor    → (Not implemented)
[12] Open Tencle-Store                 → (Not implemented)
[13] Quit Tencle-Os Safely             → Exits system
```

### 🎲 Complete Guide: How to Open & Use Each App

#### 🌐 **1. Tencle-Browser (Google Search)**
```
Dal Menu: Digita 1 e premi Enter
Diretto: Doppio click su browser.pyw

Cosa fa: Apre una finestra con ricerca Google
Come usare:
  1. Inserisci termine di ricerca
  2. Premi "Search" → apre browser predefinito
  3. Chiudi finestra quando finisci
```

#### 📝 **2. Tencle-Pad (Text Editor)**
```
Dal Menu: Digita 2 e premi Enter
Diretto: Doppio click su notepad.pyw

Cosa fa: Editor di testo semplice
Come usare:
  1. Scrivi o incolla testo
  2. File → Save per salvare
  3. File → Open per aprire file esistente
```

#### 📁 **3. Tencle-Explorer (File Manager)**
```
Dal Menu: Digita 3 e premi Enter
Diretto: Doppio click su explorer.pyw

Cosa fa: Esplora file e cartelle
Come usare:
  1. Naviga tra le cartelle
  2. Doppio click per aprire file
  3. Tasto destro per opzioni
```

#### ⏰ **4. Tencle-Time (Clock)** [TLang]
```
Dal Menu: Digita 4 e premi Enter
Diretto: Doppio click su time.bat
TLangIDE: Apri time.tl → F5

Cosa fa: Mostra orologio in tempo reale
Output:
  ╔══════════════════════════════╗
  ║   TENCLE TIME & DATE SYSTEM  ║
  ╚══════════════════════════════╝
  Current Time: 14:30:45
  Current Date: 2025-12-01
```

#### 🐦 **5. Flappy Bird Game**
```
Dal Menu: Digita 5 e premi Enter
Diretto: Doppio click su flappybird.bat

Cosa fa: Clone di Flappy Bird
Controlli:
  - SPAZIO: Fai saltare l'uccello
  - ESC: Esci dal gioco
Obiettivo: Passa tra i tubi senza colpirli
```

#### 🏀 **6. Slam Dunk (Basketball)**
```
Dal Menu: Digita 6 e premi Enter
Diretto: Doppio click su slamdunk.bat

Cosa fa: Gioco di basket
Controlli:
  - Mouse: Mira
  - Click: Tira
Obiettivo: Fai canestro!
```

#### ⛏️ **7. Minecraft Clone (3D)**
```
Dal Menu: Digita 7 e premi Enter
Diretto: Doppio click su minecraft.bat

Cosa fa: Mondo 3D stile Minecraft (Ursina engine)
Controlli:
  - WASD: Muovi
  - SPAZIO: Salta
  - Mouse: Guarda intorno
  - Click Sinistro: Rompi blocco
  - Click Destro: Piazza blocco
Nota: Richiede scheda grafica 3D
```

#### 🐍 **8. Snake Game** [TLang] ⭐
```
Dal Menu: Digita 8 e premi Enter
Diretto: Doppio click su snake.bat
TLangIDE: Apri snake.tl → F5

Cosa fa: Gioco classico Snake con Pygame
Controlli:
  - Frecce: Muovi serpente
  - ESC: Esci
Regole:
  - Mangia cibo rosso = +10 punti
  - Non colpire pareti o te stesso
  - Il serpente cresce ad ogni cibo
  
Output esempio:
  ╔════════════════════════╗
  ║   TENCLE SNAKE GAME    ║
  ╚════════════════════════╝
  Score: 50
  [Grafica Pygame con serpente verde]
```

#### 💬 **9. Tencle-Social (Terext)**
```
Dal Menu: Digita 9 e premi Enter
Diretto: Doppio click su terextsocial(incomplete).py

Cosa fa: Social network (incompleto)
Stato: In sviluppo
```

#### 🧮 **10. Tencle-Calculator** [TLang] ⭐
```
Dal Menu: Digita 10 e premi Enter
Diretto: Doppio click su calculator.bat
TLangIDE: Apri calculator.tl → F5

Cosa fa: Calcolatrice completa
Come usare:
  Enter first number: 15
  Enter second number: 7
  Choose operation (+, -, *, /): +
  Result: 22.0

Operazioni supportate:
  + (addizione)
  - (sottrazione)
  * (moltiplicazione)
  / (divisione)
```

#### 💻 **11. Tencle-Studio**
```
Stato: Non implementato
Futuro: Editor di codice integrato
```

#### 🛒 **12. Tencle-Store**
```
Stato: Non implementato
Futuro: App store per scaricare nuove app
```

#### 🚪 **13. Quit TencleOS**
```
Dal Menu: Digita 13 e premi Enter

Cosa fa: Chiude il sistema in modo sicuro
Output: "Goodbye! Exiting TencleOS..."
```

---

### 🎯 Quick Reference Table

| # | App | Launcher | Language | Difficulty | Time to Play |
|---|-----|----------|----------|------------|--------------|
| 1 | Browser | `browser.pyw` | Python | ⭐ Easy | 1 min |
| 2 | Notepad | `notepad.pyw` | Python | ⭐ Easy | 2 min |
| 3 | Explorer | `explorer.pyw` | Python | ⭐ Easy | 1 min |
| 4 | Time | `time.bat` | **TLang** | ⭐ Easy | Instant |
| 5 | Flappy Bird | `flappybird.bat` | Python | ⭐⭐⭐ Hard | 5-10 min |
| 6 | Slam Dunk | `slamdunk.bat` | Python | ⭐⭐ Medium | 3-5 min |
| 7 | Minecraft | `minecraft.bat` | Python | ⭐⭐ Medium | 10+ min |
| 8 | Snake | `snake.bat` | **TLang** | ⭐⭐ Medium | 5-10 min |
| 9 | Social | - | Python | - | N/A |
| 10 | Calculator | `calculator.bat` | **TLang** | ⭐ Easy | 30 sec |
| 11 | Studio | - | - | - | N/A |
| 12 | Store | - | - | - | N/A |
| 13 | Quit | - | **TLang** | ⭐ Easy | Instant |

### 💡 Pro Tips

**Per Sviluppatori:**
- Usa `F6` in TLangIDE per vedere Lexer/Parser/Interpreter in debug mode
- Modifica `config.py` per cambiare sintassi TLang
- Leggi il codice di `snake.tl` per capire come integrare Pygame

**Per Gamer:**
- Snake è il gioco più bilanciato (né troppo facile né impossibile)
- Minecraft richiede GPU dedicata per performance ottimali
- Flappy Bird è difficile - non demordere!

**Per Utenti:**
- Usa TencleOS come launcher alternativo per app veloci
- Crea le tue app TLang e aggiungile al menu
- Cambia PIN di default in `os.tl` per sicurezza

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
TencleOS/
├── 🔐 os.tl               # Login system (PIN: 1234) [TLang]
├── 🖥️ main-os.tl          # Main OS menu (START HERE) [TLang]
├── 🐍 snake.tl            # Snake game [TLang]
├── 🧮 calculator.tl       # Calculator app [TLang]
├── ⏰ time.tl             # Clock/Timer [TLang]
│
├── 📦 Batch Launchers
│   ├── os.bat            # Launch login system
│   ├── main-os.bat       # Launch main menu
│   ├── snake.bat         # Launch snake game
│   ├── calculator.bat    # Launch calculator
│   └── time.bat          # Launch timer
│
├── 🎮 Python Apps
│   ├── browser.pyw       # Web browser
│   ├── notepad.pyw       # Text editor
│   ├── explorer.pyw      # File manager
│   ├── flappybird.py     # Flappy Bird game
│   ├── minecraft.py      # Minecraft clone (Ursina)
│   └── slam dunk.py      # Basketball game
│
├── 📂 Resources
│   ├── Immagini/         # Game assets (Flappy Bird)
│   ├── user/             # User credentials
│   ├── icon.ico          # TLang icon
│   └── Gemini_Generated_Image_*.png  # Logo
│
├── 🛠️ Tools
│   ├── TLangIDE.exe      # Standalone IDE (8.99 MB)
│   ├── associate_tl.bat  # Associate .tl files
│   └── TLangIDE.spec     # PyInstaller config
│
└── 💻 TLang Source
    └── tlang/
        ├── config.py         # Syntax customization
        ├── lexer.py          # Tokenizer (with NOT token fix)
        ├── tlang_parser.py   # Parser
        ├── interpreter.py    # Interpreter
        ├── tlang.py          # CLI
        └── tlang_ide.py      # GUI IDE (with icon support)
```

### 📊 Project Statistics
- **Total Files:** 30+
- **TLang Applications:** 5 (os.tl, main-os.tl, snake.tl, calculator.tl, time.tl)
- **Python Applications:** 8
- **Total Lines of Code:** ~2,000
- **TLangIDE Size:** 8.99 MB
- **Supported Extensions:** .tl (TLang source files)

---

## 🔧 Building from Source

### Build TLangIDE.exe

```bash
cd TencleOS
pip install pyinstaller pygame pillow

# Build with icon
pyinstaller --onefile --windowed --icon=icon.ico --name=TLangIDE tlang/tlang_ide.py
```

Output: `dist/TLangIDE.exe` (8.99 MB standalone)

### Associate .tl Files (Windows)

Run as Administrator:
```bash
associate_tl.bat
```

This will:
- ✅ Set `icon.ico` as the icon for all `.tl` files
- ✅ Associate `.tl` files with TLangIDE.exe
- ✅ Enable double-click to open .tl files

### How TencleOS Works

**Architecture:**
```
os.bat → os.tl (Login)
            ↓
        PIN Check (1234)
            ↓
main-os.bat → main-os.tl (Main Menu)
            ↓
        User Selection (1-13)
            ↓
    Launch App (.bat launcher)
            ↓
    App Execution (TLang or Python)
```

**TLang Execution Flow:**
```
.tl file → TLangIDE.exe → Lexer → Parser → Interpreter → Output
                              ↓
                        Config.py (custom syntax)
```

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

## 🐛 Known Limitations & Solutions

### Current TLang Limitations

| Issue | Status | Solution |
|-------|--------|----------|
| ❌ File I/O | Not supported | Use Python for file operations |
| ❌ String comparison | Unreliable with `input()` | Use numeric input (PIN system) |
| ⚠️ While loops | Syntax issues | Simplified to single conditions |
| ❌ Complex GUI | Limited Tkinter | Use Pygame for graphics |
| ✅ `!` character | **FIXED** | Added NOT token to lexer |

### Why We Changed to PIN System

Originally, `os.py` used username/password strings:
```python
username = input("Username: ")
if username == "admin":
    # This didn't work in TLang!
```

**Problem:** TLang's `input()` string comparison was unreliable.

**Solution:** Changed to numeric PIN:
```tlang
pin = input("Enter PIN: ")
<< ! >func> if pin == 1234 {
    int << func >> ("Access Granted!")
}
```

### Development Challenges Solved

1. **`!` Character Not Recognized**
   - Added `TokenType.NOT` to lexer.py (line 42)
   - Added `'!': TokenType.NOT` to single_char_tokens (line 299)

2. **File Extension Migration**
   - Changed from `.tlang` to `.tl` (15 files)
   - Updated TLangIDE file filter
   - Updated all .bat launchers

3. **Icon Integration**
   - Converted PNG to ICO
   - Added to TLangIDE.exe with PyInstaller
   - Added to IDE window with `iconbitmap()`
   - Created associate_tl.bat for file associations

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

**CostaTech (Costantino)**

- GitHub: [@CostaTech](https://github.com/CostaTech)
- Project: [TencleOS](https://github.com/CostaTech/TencleOS)
- Language Creator: TLang v1.0

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

### Snake Game
![Snake Game](screenshots/snake-game.png)

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
A: No! TLangIDE.exe is completely standalone (8.99 MB).

**Q: What's the login PIN?**  
A: Default PIN is **1234**. You can change it in `os.tl`.

**Q: Can I modify the TLang syntax?**  
A: Yes! Edit `tlang/config.py` to change any command. Want Italian commands? Spanish? Make your own!

**Q: How do I run TencleOS?**  
A: Run `os.bat` for full experience with login, or open `main-os.tl` in TLangIDE and press F5.

**Q: Why .tl instead of .tlang?**  
A: Shorter extension for convenience. Old `.tlang` files still work.

**Q: Can I create my own TLang programs?**  
A: Absolutely! Check the documentation, examples, and use TLangIDE.exe.

**Q: Is TencleOS a real operating system?**  
A: It's an OS interface/menu system with applications, not a kernel-level OS like Windows or Linux.

**Q: Which apps are in TLang vs Python?**  
A: **TLang:** os.tl, main-os.tl, snake.tl, calculator.tl, time.tl (5 apps)  
**Python:** Browser, Notepad, Explorer, Flappy Bird, Minecraft, Slam Dunk, Studio, Store, Social (8 apps)

**Q: Can I contribute?**  
A: Yes! See the [Contributing](#contributing) section. We especially need help with file I/O support.

**Q: Does TLang support file operations?**  
A: Not yet. This is a planned feature for v2.0.

---

<div align="center">

**⭐ Star this repo if you find it useful! ⭐**

Made with ❤️ and TLang

</div>
