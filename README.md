# 🔷 TencleLang

<div align="center">

![TencleLang Logo](tencleos_logo.svg)

**A powerful, innovative programming language with unique syntax**

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-2.1-green.svg)](https://github.com/CostaTech/TencleLang)
[![Platform](https://img.shields.io/badge/platform-Windows-lightgrey.svg)](https://github.com/CostaTech/TencleLang)

</div>

---

##  About

**TencleLang** (`.tl`) is a modern programming language featuring a distinctive syntax design with special keywords and operators. Built for both beginners and experienced developers, TencleLang offers intuitive programming constructs with powerful capabilities.

##  Features

- ** Unique Syntax**: Special keyword syntax with `<< >>` and `< >` operators
- ** Variables**: Support for integers, floats, strings, and lists
- ** Conditionals**: `if`, `elif`, `else` statements with flexible comparison
- ** Loops**: `while` loops with condition-based iteration
- ** Functions**: Function definitions with parameters and return values
- ** Pygame Integration**: Built-in support for game development
- ** Cross-platform**: Windows executable ready to use

## Installation

### Quick Start

1. Download the repository
2. Navigate to `System/tlang/`
3. Run `tlang.exe` to execute `.tl` files

```bash
cd System/tlang
tlang.exe your_program.tl
```

##  Syntax Overview

### Special Keywords

TencleLang uses unique syntax markers:
- `<< ! >func>`: Function definition
- `<< func >>`: Function call
- `<<While>>!`: While loop
- `<on>`: Loop condition

### Variables

```
int x = 10
float y = 3.14
string name = "TencleLang"
list numbers = [1, 2, 3, 4, 5]
```

### Functions

```
<< ! >func> greet(name)
    int << func >> ("Hello, " + name + "!")
</func>

<< func >> greet("World")
```

### Conditionals

```
if x == 10
    int << func >> ("X is 10")
elif x > 10
    int << func >> ("X is greater than 10")
else
    int << func >> ("X is less than 10")
```

### Loops

```
int i = 0
<<While>>! <on> i < 5
    int << func >> (i)
    i = i + 1
```

##  Examples

### Calculator

```tl
<< ! >func> somma(a, b)
    return a + b
</func>

<< ! >func> sottrai(a, b)
    return a - b
</func>

<< ! >func> moltiplica(a, b)
    return a * b
</func>

<< ! >func> dividi(a, b)
    if b == 0
        int << func >> ("Error: Division by zero!")
        return 0
    return a / b
</func>

int << func >> ("Result: " + << func >> somma(10, 5))
```

### Fibonacci Sequence

```tl
<< ! >func> fibonacci(n)
    if n <= 1
        return n
    return << func >> fibonacci(n - 1) + << func >> fibonacci(n - 2)
</func>

int i = 0
<<While>>! <on> i < 10
    int << func >> (<< func >> fibonacci(i))
    i = i + 1
```

### FizzBuzz

```tl
int i = 1
<<While>>! <on> i <= 100
    if i % 15 == 0
        int << func >> ("FizzBuzz")
    elif i % 3 == 0
        int << func >> ("Fizz")
    elif i % 5 == 0
        int << func >> ("Buzz")
    else
        int << func >> (i)
    i = i + 1
```

### Pygame Example

```tl
import pygame

int << func >> pygame.init()
screen = << func >> pygame.display.set_mode([800, 600])
running = true

<<While>>! <on> running
    for event in << func >> pygame.event.get()
        if event.type == pygame.QUIT
            running = false
    
    << func >> screen.fill([0, 0, 0])
    << func >> pygame.display.flip()

<< func >> pygame.quit()
```

## 📖 Documentation

### Keywords

- `int`, `float`, `string`, `list`: Variable types
- `if`, `elif`, `else`: Conditionals
- `<<While>>!`, `<on>`: Loop constructs
- `<< ! >func>`, `</func>`: Function definition
- `<< func >>`: Function call
- `return`: Return value from function
- `import`: Import modules
- `true`, `false`: Boolean values

### Operators

**Arithmetic:** `+`, `-`, `*`, `/`, `%`  
**Comparison:** `==`, `!=`, `<`, `>`, `<=`, `>=`  
**Logical:** `and`, `or`, `not`  
**Assignment:** `=`

### Built-in Functions

- `int << func >> (value)`: Print/output
- `<< func >> input(prompt)`: Get user input
- `<< func >> len(list)`: Get list length
- `<< func >> range(start, end)`: Generate number range

## 🛠️ Building from Source

TencleLang is built with Python using PyInstaller:

```bash
cd src/
pyinstaller --onefile --name tlang interpreter.py
```

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Links

- **Repository**: [github.com/CostaTech/TencleLang](https://github.com/CostaTech/TencleLang)
- **Issues**: [github.com/CostaTech/TencleLang/issues](https://github.com/CostaTech/TencleLang/issues)
- **Releases**: [github.com/CostaTech/TencleLang/releases](https://github.com/CostaTech/TencleLang/releases)

## 🌟 Acknowledgments

Developed with ❤️ by the TencleLang team.

---

<div align="center">

**[⬆ Back to Top](#-tenclelang)**

</div>
