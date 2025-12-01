# Quick Start Guide

## 🚀 Running TencleOS in 3 Steps

### Step 1: Download
```bash
git clone https://github.com/yourusername/tencleos-tlang.git
cd tencleos-tlang
```

### Step 2: Get TLangIDE
Download `TLangIDE.exe` from the [releases page](https://github.com/yourusername/tencleos-tlang/releases)

### Step 3: Run
1. Double-click `TLangIDE.exe`
2. File → Open → `main-os.tlang`
3. Press **F5**

That's it! 🎉

---

## 📝 Creating Your First TLang Program

1. **Open TLangIDE**
2. **Create New File** (Ctrl+N)
3. **Write code:**
```tlang
int << func >> ("Hello from TLang!")

name = input("What's your name? ")
int << func >> ("Welcome " + name + "!")
```
4. **Save as** `hello.tlang` (Ctrl+S)
5. **Run** (F5)

---

## 🎮 Running Snake Game

1. Open `snake.tlang` in TLangIDE
2. Press **F5**
3. Use **Arrow Keys** to play
4. Try to eat the red food!

---

## 🧮 Using Calculator

1. Open `calculator.tlang` in TLangIDE
2. Press **F5**
3. Choose operation (1-6)
4. Enter numbers
5. See result!

---

## 🔧 Customizing TLang

Edit `tlang/config.py`:

```python
# Change print command
COMANDO_PRINT = "show"  # Now use: show ("text")

# Change if command
COMANDO_IF = "when"     # Now use: when if condition {}

# Change while command
COMANDO_WHILE = "repeat" # Now use: repeat! <on> {}
```

Save and restart TLangIDE to see changes!

---

## ❓ Troubleshooting

**Problem:** TLangIDE doesn't open  
**Solution:** Make sure you're on Windows 10/11 64-bit

**Problem:** "Module not found" error  
**Solution:** Use `use modulename` to import Python libraries

**Problem:** Syntax error  
**Solution:** Check that you're using parentheses: `int << func >> ("text")`

---

## 📚 Learn More

- [Full Documentation](README.md)
- [TLang Syntax Guide](README.md#tlang-syntax-reference)
- [Examples](README.md#examples)

Happy coding! 🚀
