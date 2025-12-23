# Contributing to TencleOS-TLang

Thank you for considering contributing to TencleOS! 🎉

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Coding Guidelines](#coding-guidelines)
- [Commit Guidelines](#commit-guidelines)
- [Pull Request Process](#pull-request-process)

---

## 📜 Code of Conduct

- Be respectful and inclusive
- Welcome newcomers
- Focus on constructive feedback
- Keep discussions professional

---

## 🤝 How Can I Contribute?

### 1. Report Bugs

Found a bug? [Open an issue](https://github.com/yourusername/tencleos-tlang/issues/new) with:
- **Title**: Short description
- **Description**: Steps to reproduce
- **Expected vs Actual**: What should happen vs what happens
- **System**: Windows version, TLang version

### 2. Suggest Features

Have an idea? [Open an issue](https://github.com/yourusername/tencleos-tlang/issues/new) with:
- **Feature description**
- **Use case**: Why is it useful?
- **Proposed solution**

### 3. Write Code

#### Easy First Issues
- Add new examples
- Improve documentation
- Fix typos
- Add comments to code

#### Intermediate
- Convert more Python apps to TLang
- Add new games
- Improve error messages

#### Advanced
- Add file I/O support to TLang
- Create GUI framework
- Optimize interpreter

---

## 🛠️ Development Setup

### 1. Fork & Clone
```bash
git clone https://github.com/YOUR-USERNAME/tencleos-tlang.git
cd tencleos-tlang
```

### 2. Install Dependencies
```bash
cd tlang
pip install pygame pillow pyinstaller
```

### 3. Test Your Setup
```bash
python tlang.py main-os.tlang
```

---

## 📝 Coding Guidelines

### TLang Code Style

```tlang
# Good: Clear variable names
user_name = "John"
total_score = 100

# Bad: Unclear names
x = "John"
ts = 100

# Good: Comments explain why
# Calculate final score with 10% bonus
final_score = base_score * 1.1

# Good: Proper spacing
<< ! >func> if x > 5 {
    int << func >> ("Large")
}

# Bad: No spacing
<<!>func>if x>5{
int<<func>>("Large")
}
```

### Python Code Style

- Follow PEP 8
- Use meaningful variable names
- Add docstrings to functions
- Keep functions under 50 lines

---

## 💬 Commit Guidelines

### Format
```
type(scope): description

Body (optional)
Footer (optional)
```

### Types
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `style`: Formatting
- `refactor`: Code restructuring
- `test`: Tests
- `chore`: Maintenance

### Examples
```bash
feat(snake): add difficulty levels

Added easy, medium, and hard modes for snake game.
Speed increases with difficulty.

Closes #42
```

```bash
fix(calculator): division by zero error

Added check for zero denominator before division.
```

---

## 🔀 Pull Request Process

### 1. Create Branch
```bash
git checkout -b feature/my-amazing-feature
```

### 2. Make Changes
- Write clear, commented code
- Test your changes
- Update documentation if needed

### 3. Commit
```bash
git add .
git commit -m "feat: add amazing feature"
```

### 4. Push
```bash
git push origin feature/my-amazing-feature
```

### 5. Open PR
- Go to GitHub
- Click "New Pull Request"
- Fill in the template:
  - **What**: Description of changes
  - **Why**: Reason for changes
  - **How**: How you implemented it
  - **Testing**: How you tested it

### 6. Review Process
- Maintainers will review
- Address feedback
- Once approved, it will be merged!

---

## 🧪 Testing

Before submitting:

```bash
# Test main OS
python tlang.py main-os.tlang

# Test snake game
python tlang.py snake.tlang

# Test calculator
python tlang.py calculator.tlang

# Build IDE (if you changed it)
cd tlang
pyinstaller --name=TLangIDE --onefile --windowed tlang_ide.py
```

---

## 📚 Resources

- [TLang Documentation](README.md#documentation)
- [Python Style Guide](https://pep8.org/)
- [Git Tutorial](https://git-scm.com/docs/gittutorial)

---

## 🙏 Thank You!

Every contribution, no matter how small, helps make TencleOS better!

Questions? Open an issue or discussion.

Happy contributing! 🚀
