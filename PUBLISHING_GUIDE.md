# 🚀 Publishing to GitHub - Step-by-Step Guide

This guide will help you publish **TencleOS-TLang** on GitHub.

---

## 📋 Pre-Publishing Checklist

Before uploading to GitHub, ensure:

- [x] All source files in `tlang/` folder
- [x] TLangIDE.exe built and included (16.42 MB)
- [x] Documentation complete (README, LICENSE, CONTRIBUTING, etc.)
- [x] .gitignore file configured
- [x] User credentials files created (`user/username.txt`, `user/password.txt`)
- [x] Example .tlang files working (main-os.tlang, snake.tlang, calculator.tlang)
- [x] No sensitive data in repository
- [x] All file paths use relative paths (not absolute)

---

## 🌐 Step 1: Create GitHub Repository

1. **Go to GitHub**: https://github.com/new

2. **Repository Settings**:
   ```
   Repository name: TencleOS-TLang
   Description: A complete custom programming language with 100% customizable syntax and a professional IDE
   Visibility: ✅ Public
   Initialize: ❌ Do NOT add README, .gitignore, or license (we already have them)
   ```

3. **Click**: "Create repository"

---

## 💻 Step 2: Initialize Git and Push

Open PowerShell in the project folder:

```powershell
# Navigate to project folder
cd "c:\Users\Utente\Desktop\tlang official\TencleOS-TLang-Edition"

# Initialize Git repository
git init

# Add all files
git add .

# Create first commit
git commit -m "feat: initial release of TencleOS-TLang v1.0.0"

# Connect to GitHub (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/TencleOS-TLang.git

# Push to GitHub
git branch -M main
git push -u origin main
```

**Note**: Replace `YOUR_USERNAME` with your actual GitHub username.

---

## 🏷️ Step 3: Create Release with TLangIDE.exe

GitHub doesn't allow files over 25 MB in normal commits, but releases support up to 2 GB.

### Option A: GitHub Web Interface

1. **Go to your repository**: `https://github.com/YOUR_USERNAME/TencleOS-TLang`

2. **Click**: "Releases" (right sidebar) → "Create a new release"

3. **Tag version**: `v1.0.0`

4. **Release title**: `TencleOS-TLang v1.0.0 - Initial Release`

5. **Description**:
   ```markdown
   # 🎉 TencleOS-TLang v1.0.0
   
   First official release of TLang - a custom programming language with 100% customizable syntax!
   
   ## 📦 What's Included
   - **TLangIDE.exe** (16.4 MB) - Standalone IDE with Python + Pygame embedded
   - Complete TencleOS operating system in TLang
   - Snake game and calculator applications
   - Full source code and documentation
   
   ## 🚀 Quick Start
   1. Download `TLangIDE.exe` below
   2. Clone this repository
   3. Open `main-os.tlang` in TLangIDE
   4. Press F5 to run!
   
   ## 📚 Documentation
   - [README](https://github.com/YOUR_USERNAME/TencleOS-TLang/blob/main/README.md)
   - [Quick Start Guide](https://github.com/YOUR_USERNAME/TencleOS-TLang/blob/main/QUICKSTART.md)
   - [Technical Docs](https://github.com/YOUR_USERNAME/TencleOS-TLang/blob/main/PROJECT_INFO.md)
   
   ## 🐛 Known Issues
   - File I/O not yet implemented
   - No OOP support (coming in v1.1)
   
   See [CHANGELOG](https://github.com/YOUR_USERNAME/TencleOS-TLang/blob/main/CHANGELOG.md) for details.
   ```

6. **Attach files**: Drag and drop `TLangIDE.exe`

7. **Click**: "Publish release"

### Option B: Git Command Line

```powershell
# Create release tag
git tag -a v1.0.0 -m "Release version 1.0.0"

# Push tag to GitHub
git push origin v1.0.0

# Then upload TLangIDE.exe manually in web interface
```

---

## 📸 Step 4: Add Screenshots (Optional but Recommended)

1. **Take screenshots**:
   - TLangIDE with code editor
   - Snake game running
   - TencleOS main menu
   - Debug mode in action

2. **Create folder**: `screenshots/` (already exists)

3. **Add images**:
   ```powershell
   # Copy screenshots to folder
   Copy-Item "C:\path\to\screenshot1.png" "screenshots\ide-editor.png"
   Copy-Item "C:\path\to\screenshot2.png" "screenshots\snake-game.png"
   Copy-Item "C:\path\to\screenshot3.png" "screenshots\tencleos-menu.png"
   
   # Commit and push
   git add screenshots/
   git commit -m "docs: add screenshots"
   git push
   ```

4. **Update README.md** to include images:
   ```markdown
   ## 📸 Screenshots
   
   ![IDE Editor](screenshots/ide-editor.png)
   *TLangIDE with syntax highlighting*
   
   ![Snake Game](screenshots/snake-game.png)
   *Snake game running in TLang*
   ```

---

## 🎨 Step 5: Customize Repository

### Add Topics (Tags)

Go to repository → Settings → About → Topics:
```
programming-language, interpreter, ide, custom-syntax, python, 
pygame, gui, windows, standalone, educational
```

### Add Description

Repository → About → Description:
```
🚀 A complete custom programming language with 100% customizable syntax + professional IDE | Built with Python
```

### Add Website (if you have one)

Repository → About → Website:
```
https://your-website.com (or leave blank)
```

---

## 🔧 Step 6: Set Up GitHub Pages (Optional)

Host your documentation website on GitHub Pages:

1. **Create `docs/` folder**:
   ```powershell
   mkdir docs
   Copy-Item "website\*" "docs\" -Recurse
   git add docs/
   git commit -m "docs: add website"
   git push
   ```

2. **Enable GitHub Pages**:
   - Repository → Settings → Pages
   - Source: Deploy from a branch
   - Branch: `main`, Folder: `/docs`
   - Click "Save"

3. **Access website**: `https://YOUR_USERNAME.github.io/TencleOS-TLang`

---

## 📢 Step 7: Promote Your Project

### Add to GitHub Topics

- [awesome-programming-languages](https://github.com/topics/programming-language)
- [custom-syntax](https://github.com/topics/custom-syntax)
- [python-interpreter](https://github.com/topics/interpreter)

### Share on Social Media

**Twitter/X**:
```
🚀 Just released TencleOS-TLang v1.0.0!

A programming language with 100% customizable syntax 🎨
+ Professional IDE with debug mode 🐛
+ Embedded Python + Pygame in 16MB EXE 📦

Check it out: https://github.com/YOUR_USERNAME/TencleOS-TLang

#Python #ProgrammingLanguage #OpenSource
```

**Reddit**:
- r/programming
- r/Python
- r/learnprogramming
- r/programming_languages

---

## 🛠️ Step 8: Maintenance

### Update Version

When releasing new versions:

```powershell
# Make changes
git add .
git commit -m "feat: add new feature"
git push

# Update version
git tag -a v1.1.0 -m "Release version 1.1.0"
git push origin v1.1.0

# Create GitHub release with new TLangIDE.exe
```

### Respond to Issues

- Check [Issues](https://github.com/YOUR_USERNAME/TencleOS-TLang/issues) regularly
- Label issues: `bug`, `enhancement`, `question`, `help wanted`
- Close issues when resolved

### Accept Pull Requests

1. Review code changes
2. Test locally
3. Merge if approved
4. Thank contributor!

---

## 📊 Step 9: Add Badges to README

Add these to the top of `README.md`:

```markdown
# TencleOS-TLang

![GitHub release](https://img.shields.io/github/v/release/YOUR_USERNAME/TencleOS-TLang)
![GitHub stars](https://img.shields.io/github/stars/YOUR_USERNAME/TencleOS-TLang)
![GitHub issues](https://img.shields.io/github/issues/YOUR_USERNAME/TencleOS-TLang)
![License](https://img.shields.io/github/license/YOUR_USERNAME/TencleOS-TLang)
![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![Platform](https://img.shields.io/badge/platform-Windows-blue.svg)
```

Commit and push:
```powershell
git add README.md
git commit -m "docs: add badges to README"
git push
```

---

## ✅ Final Checklist

Before announcing your project:

- [ ] Repository is public
- [ ] README is complete with examples
- [ ] LICENSE file is present (MIT)
- [ ] .gitignore excludes build artifacts
- [ ] Release v1.0.0 created with TLangIDE.exe
- [ ] Topics/tags added to repository
- [ ] Description set in About section
- [ ] Screenshots uploaded and displayed
- [ ] All links work (no broken links)
- [ ] Code is tested and working
- [ ] No sensitive data (API keys, passwords)
- [ ] Contributing guidelines clear
- [ ] Issue templates set up (optional)
- [ ] Star your own repo! ⭐

---

## 🎉 Congratulations!

Your project is now live on GitHub! 🚀

**Share your repository URL**:
```
https://github.com/YOUR_USERNAME/TencleOS-TLang
```

---

## 📞 Need Help?

- GitHub Docs: https://docs.github.com
- Git Tutorial: https://git-scm.com/docs/gittutorial
- GitHub Desktop: https://desktop.github.com (GUI alternative)

---

**Last Updated**: 2025-01-XX
