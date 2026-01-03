# python-projects

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)  
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)  
[![Type Checking: Pylance](https://img.shields.io/badge/type%20checking-pylance-lightgrey.svg)](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)  
[![freeCodeCamp](https://img.shields.io/badge/freeCodeCamp-certification-green.svg)](https://www.freecodecamp.org/)  
[![Progress](https://img.shields.io/badge/Projects%20Completed-2%2F5-success.svg)](https://github.com/<your-username>/python-projects)  

A collection of Python projects completed as part of the **freeCodeCamp certification** curriculum, along with additional projects inspired and guided by **Microsoft Copilot**.  
This repository showcases practical applications of Python, ranging from beginner exercises to more advanced, real‑world projects.

---

## 📂 Project Index

| Project Name            | Source        | Description                                                                 |
|-------------------------|---------------|-----------------------------------------------------------------------------|
| User Configuration App  | freeCodeCamp  | Manipulates a dictionary of user configurations.                            |
| Budget App              | freeCodeCamp  | Tracks spending in categories and generates a spend chart.                  |
| Polygon Area Calculator | freeCodeCamp  | Defines Rectangle and Square classes,  with methods for geometric calculations and ASCII rendering.                  |
| Queue Project           | Microsoft Copilot  | Implement a queue using a list.                            |
| Queue with linked list  | Microsoft Copilot  | Implement a queue using a linked list.                            |
| Queue With doubly linked list | Microsoft Copilot | Implement a queue using a doubly linked list |

---

## 🚀 Getting Started

Clone the repository:
```bash
git clone https://github.com/<your-username>/python-projects.git
cd python-projects
```

Install dependencies (if any):
```bash
pip install -r requirements.txt
```

Run a project:
```bash
python project_name.py
```

## 📝 Translation Setup

This project uses **GNU gettext** for internationalisation (i18n).  
Python’s `gettext` module is part of the standard library, so no extra Python package is needed.  
However, you must install the **gettext command‑line tools** (`xgettext`, `msgfmt`, `msgmerge`) to extract and compile translations.

### 🔧 Installation

#### Windows 10/11
1. Download the latest Windows build of gettext tools (e.g. from [mlocati/gettext-windows](https://github.com/mlocati/gettext-windows/releases)).
2. Extract the archive to a folder such as `C:\DevTools\gettext`.
3. Add the `bin` folder to your **PATH**:
   - Press **Win + R**, type `sysdm.cpl`, go to **Advanced → Environment Variables**.
   - Edit `Path` → Add:  
     ```
     C:\DevTools\gettext\bin
     ```
   - Restart PowerShell or Command Prompt.
4. Test with:
   ```powershell
   xgettext --version
   ```

#### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install gettext
```

#### macOS (Homebrew)
```bash
brew install gettext
brew link --force gettext
```

---

### 📂 Workflow

1. **Extract strings** into a template:
   ```bash
   xgettext --language=Python --keyword=_ --output=locales/messages.pot queue-with-fixed-size-array.py language_constants.py
   ```

2. **Create `.po` files** for each language:
   ```bash
   mkdir -p locales/af_ZA/LC_MESSAGES
   cp locales/messages.pot locales/af_ZA/LC_MESSAGES/messages.po
   ```

3. **Translate** the `msgstr` entries in `.po`.

4. **Compile** into `.mo`:
   ```bash
   msgfmt locales/af_ZA/LC_MESSAGES/messages.po -o locales/af_ZA/LC_MESSAGES/messages.mo
   ```

5. **Run your app** — gettext will load the `.mo` file automatically.

---

### Version Control

- Commit `messages.pot` and all `.po` files.  
- Ignore `.mo` files (compiled binaries) in `.gitignore`:
  ```
  locales/*/LC_MESSAGES/*.mo
  ```

---

## 🛠️ Technologies
- Python 3.x  
- Standard libraries (`math`, `typing`, etc.)  
- Tools like **Black** (formatter) and **Pylance** (type checker) for clean, reliable code.  

---

## 📈 Learning Goals
- Strengthen Python fundamentals.  
- Practice **object‑oriented programming** and **data structures**.  
- Explore **type hints**, **docstrings**, and **best practices**.  
- Build a portfolio of projects that demonstrate growth and versatility.  

---

## 📅 Status
- Ongoing development: new projects will be added as certifications progress and Copilot proposes new ideas.  

---

## 👩‍💻 Author
**Juliana Albertyn**  
- 📧 julie_albertyn@yahoo.com  
- 🌍 Barrydale, Western Cape, South Africa  

---