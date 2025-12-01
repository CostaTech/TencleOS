# 🔧 TLang Technical Documentation

## Architecture Overview

TLang is a custom programming language built in Python with a three-stage execution pipeline:

```
Source Code (.tlang) → Lexer → Parser → Interpreter → Execution
```

### 1. Lexer (`lexer.py`)
- **Purpose**: Tokenization of source code
- **Key Features**:
  - Multi-character command recognition via `read_complex_command()`
  - Custom operator support (arithmetic, comparison, logical)
  - String literal parsing with escape sequences
  - Comment handling (`#` style)
  - Token types defined in `TokenType` enum

**Example Tokenization**:
```python
# Input: int << func >> ("Hello")
# Output: [Token(PRINT, "int << func >>"), Token(LPAREN, "("), 
#          Token(STRING, "Hello"), Token(RPAREN, ")")]
```

### 2. Parser (`tlang_parser.py`)
- **Purpose**: Abstract Syntax Tree (AST) construction
- **Architecture**: Recursive descent parser
- **Supported Constructs**:
  - Statements: print, if/elif/else, while, for, import, assignments
  - Expressions: binary operations, function calls, attribute access, list literals
  - Control flow: break, continue, return

**AST Node Types**:
```python
PrintNode, IfNode, WhileNode, ForNode, ImportNode,
AssignmentNode, FunctionCallNode, AttributeAccessNode,
BinaryOpNode, UnaryOpNode, VariableNode, ListNode
```

### 3. Interpreter (`interpreter.py`)
- **Purpose**: AST execution
- **Pattern**: Visitor pattern with `visit_*` methods
- **Key Features**:
  - Python library integration via `importlib`
  - Dynamic attribute/method resolution
  - Scope management with variable stack
  - Built-in function support

**Example Execution**:
```python
def visit_FunctionCallNode(self, node):
    func = self.visit(node.func)
    args = [self.visit(arg) for arg in node.args]
    kwargs = {k: self.visit(v) for k, v in node.kwargs.items()}
    return func(*args, **kwargs)
```

---

## Custom Syntax System

### Configuration File (`config.py`)

The entire syntax is defined in `config.py`, making it 100% customizable:

```python
# Customizable commands
COMANDO_PRINT = "int << func >>"
COMANDO_IF = "<< ! >func> if"
COMANDO_ELIF = "elif"
COMANDO_ELSE = ">> func << else"
COMANDO_WHILE = "<<While>>! <on>"
COMANDO_FOR = "for"
COMANDO_IMPORT = "use"
COMANDO_TRUE = "on"
COMANDO_FALSE = "off"
COMANDO_BREAK = "stop"
COMANDO_CONTINUE = "nextstep"
```

### Modifying Syntax

1. **Edit** `config.py` with your custom commands
2. **Rebuild** the executable:
   ```bash
   cd tlang
   pyinstaller --name=TLangIDE --onefile --windowed --icon=tlang_icon.ico \
               --hidden-import=pygame tlang_ide.py --clean
   ```
3. **Test** your changes in the IDE

**Example Custom Syntax**:
```python
# Change print to "say"
COMANDO_PRINT = "say"

# Now use: say("Hello World")
```

---

## IDE Features (`tlang_ide.py`)

### Architecture
- **Framework**: Tkinter (built-in Python GUI)
- **Components**:
  - Code editor with syntax highlighting
  - Three-tab output panel: Output / Debug / Variables
  - File menu with New/Open/Save
  - Run/Debug buttons

### Syntax Highlighting
```python
def highlight_syntax(self, event=None):
    # Keywords (orange)
    for keyword in ['int << func >>', '<< ! >func> if', ...]:
        # Color matching text
    
    # Strings (green)
    # Numbers (blue)
    # Comments (gray)
```

### Debug Mode
- **Variable Tracking**: Display all variables in scope
- **Execution Flow**: Show statement-by-statement execution
- **Error Messages**: Detailed error reporting with line numbers

### Keyboard Shortcuts
- `F5`: Run code
- `F6`: Debug mode
- `Ctrl+N`: New file
- `Ctrl+O`: Open file
- `Ctrl+S`: Save file

---

## Building TLangIDE.exe

### Requirements
```bash
pip install pyinstaller==6.17.0 pygame==2.6.1 pillow==11.3.0
```

### Build Command
```bash
cd tlang
pyinstaller --name=TLangIDE \
            --onefile \
            --windowed \
            --icon=tlang_icon.ico \
            --hidden-import=pygame \
            --hidden-import=pygame.base \
            --hidden-import=pygame.constants \
            --hidden-import=pygame.rect \
            --hidden-import=pygame.mixer \
            tlang_ide.py \
            --clean
```

### Result
- **Size**: 16.42 MB (includes Python 3.9 + Tkinter + Pygame)
- **Location**: `tlang/dist/TLangIDE.exe`
- **Icon**: 512x512 custom hexagon logo

### Troubleshooting Build Issues

**Issue**: Module not found errors
```bash
# Solution: Add hidden imports
--hidden-import=module_name
```

**Issue**: Icon not appearing
```bash
# Solution: Convert PNG to ICO with multiple resolutions
from PIL import Image
img = Image.open('logo.png')
img.save('icon.ico', format='ICO', sizes=[(512,512), (256,256), (128,128), (64,64), (48,48), (32,32), (16,16)])
```

**Issue**: Large executable size
```bash
# Solution: Use UPX compression (reduces size by ~30%)
pyinstaller ... --upx-dir=c:\path\to\upx
```

---

## TLang Language Specification

### Data Types
- **Numbers**: `42`, `3.14`
- **Strings**: `"hello"`, `'world'`
- **Booleans**: `on` (True), `off` (False)
- **Lists**: `[1, 2, 3]`
- **None**: `none`

### Operators
```tlang
# Arithmetic
+ - * / % **

# Comparison
== != > < >= <=

# Logical
and or not

# Assignment
= += -= *= /= %=
```

### Control Flow
```tlang
# If-Elif-Else
<< ! >func> if condition:
    # code
elif condition:
    # code
>> func << else:
    # code

# While Loop
<<While>>! <on>:
    # code
    stop  # break
    nextstep  # continue

# For Loop
for i in range(10):
    # code
```

### Functions & Imports
```tlang
# Import modules
use pygame
use math

# Function calls
pygame.init()
math.sqrt(16)

# Attribute access
screen.fill([0, 0, 0])
```

### Comments
```tlang
# Single-line comment
int << func >> ("Hello")  # Inline comment
```

---

## TencleOS Integration

### File Structure
```
main-os.tlang        # Main menu with 13 options
├── snake.tlang      # Option 1: Snake game
├── calculator.tlang # Option 2: Calculator
└── user/
    ├── username.txt # Default: admin
    └── password.txt # Default: pass
```

### Authentication System
```tlang
# Hardcoded credentials (TLang doesn't support file I/O yet)
username = "admin"
password = "pass"

<< ! >func> if user_input == username and pass_input == password:
    int << func >> ("Login successful!")
>> func << else:
    int << func >> ("Access denied!")
```

### Launching Apps
```tlang
<< ! >func> if choice == "1":
    # Import and run snake game
    use pygame
    exec(open("snake.tlang").read())
```

---

## Limitations & Future Roadmap

### Current Limitations
1. **No File I/O**: Cannot read/write files (working on `open()` support)
2. **No Classes**: Object-oriented programming not yet supported
3. **Limited Debugging**: No breakpoints or step-through debugging
4. **No Package Manager**: External modules require Python installation

### Planned Features (v2.0)
- [ ] File I/O operations (`open`, `read`, `write`)
- [ ] Class definitions and inheritance
- [ ] Try-catch exception handling
- [ ] Package manager (`tlang install <package>`)
- [ ] REPL improvements (auto-complete, history)
- [ ] Breakpoint debugging in IDE
- [ ] Multi-file project support
- [ ] Standard library (file, network, regex)

---

## Testing

### Unit Tests
```bash
cd tlang
python -m pytest tests/
```

### Manual Testing Checklist
- [ ] Print statements work
- [ ] All operators function correctly
- [ ] If/elif/else branching
- [ ] While/for loops execute
- [ ] Break/continue work
- [ ] Import statements load modules
- [ ] Function calls execute
- [ ] Lists can be created and accessed
- [ ] IDE syntax highlighting works
- [ ] Debug mode shows variables
- [ ] File save/load works

### Example Test File (`tests/test_basic.py`)
```python
import unittest
from lexer import Lexer
from tlang_parser import Parser
from interpreter import Interpreter

class TestTLang(unittest.TestCase):
    def run_code(self, code):
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        interpreter = Interpreter()
        return interpreter.interpret(ast)
    
    def test_print(self):
        code = 'int << func >> ("Hello")'
        result = self.run_code(code)
        # Assert output contains "Hello"
```

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

### Quick Start for Developers

1. **Fork** the repository
2. **Clone** your fork:
   ```bash
   git clone https://github.com/yourname/tencleos-tlang.git
   cd tencleos-tlang
   ```
3. **Create branch**:
   ```bash
   git checkout -b feature/my-feature
   ```
4. **Make changes** to `tlang/` source files
5. **Test** with `python tlang/tlang.py` or IDE
6. **Commit**:
   ```bash
   git commit -m "feat: add feature description"
   ```
7. **Push** and create Pull Request

---

## License

MIT License - see [LICENSE](LICENSE) file

---

## Credits

- **Creator**: Costantino (TencleOS & TLang)
- **Year**: 2025
- **Language**: Python 3.9.13
- **Frameworks**: Tkinter, Pygame, PyInstaller

---

## Support

- **Issues**: [GitHub Issues](https://github.com/yourusername/tencleos-tlang/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/tencleos-tlang/discussions)
- **Email**: your.email@example.com
