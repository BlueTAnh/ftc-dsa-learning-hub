# Python Setup

Get your computer ready before **Week 2**. This takes about 15 minutes.

You have two options:

- **Option A — Local setup (recommended):** Python + VSCode on your computer. This is what we use in class.
- **Option B — Google Colab:** runs in your browser, nothing to install. Good as a backup.

---

## Option A: Local setup

### 1. Install Python 3

**Windows**
1. Go to [python.org/downloads](https://www.python.org/downloads/) and download the latest Python 3 installer.
2. Run the installer. On the first screen, **tick "Add python.exe to PATH"** before clicking *Install Now*.

   > ⚠️ If you skip this box, the `python` command won't work in the terminal. If that happens, re-run the installer, choose *Modify*, and enable it.

**macOS**
1. Go to [python.org/downloads](https://www.python.org/downloads/) and download the latest Python 3 installer.
2. Open the `.pkg` file and follow the steps.
3. On macOS, use `python3` instead of `python` in all commands below.

### 2. Check it works

Open a terminal (**Command Prompt** or **PowerShell** on Windows, **Terminal** on macOS) and run:

```bash
python --version
```

You should see something like `Python 3.x.x`. (macOS: `python3 --version`.)

### 3. Install VSCode

1. Download from [code.visualstudio.com](https://code.visualstudio.com/) and install.
2. Open VSCode → **Extensions** (left sidebar, or `Ctrl+Shift+X` / `Cmd+Shift+X`).
3. Search **Python** and install the extension published by **Microsoft**.

### 4. Run your first file

1. In VSCode: **File → Open Folder** and pick (or create) a folder for this course.
2. Create a file named `hello.py`:
   ```python
   print("Hello, DSA!")
   ```
3. Click the **▶ Run** button at the top right of the editor.
4. You should see `Hello, DSA!` in the terminal at the bottom.

> If VSCode asks you to **select an interpreter**, press `Ctrl+Shift+P` / `Cmd+Shift+P`, type **Python: Select Interpreter**, and choose the Python 3 you installed.

---

## Option B: Google Colab

1. Go to [colab.research.google.com](https://colab.research.google.com/) and sign in with a Google account.
2. Click **New notebook**, type `print("Hello, DSA!")` in a cell, and press `Shift+Enter`.

**To open a notebook from this repo:**
1. In Colab: **File → Open notebook → GitHub** tab.
2. Paste `https://github.com/BlueTAnh/ftc-dsa-learning-hub` and press Enter.
3. Pick the `.ipynb` file you want.

> Changes you make in Colab are not saved to this repo. Use **File → Save a copy in Drive** to keep your work.

---

## Get the course materials

**With Git** (if you have it installed):
```bash
git clone https://github.com/BlueTAnh/ftc-dsa-learning-hub.git
```
Then in VSCode: **File → Open Folder → `ftc-dsa-learning-hub`**.

To get new materials each week, run this inside the folder:
```bash
git pull
```

**Without Git:** on the repo page, click **Code → Download ZIP**, then unzip it. Download again each week for new materials.

---

## Other accounts and tools

| Tool | What it's for | Link |
|---|---|---|
| **LeetCode** | Most homework problems. Create a free account. | [leetcode.com](https://leetcode.com/) |
| **Python Tutor** | Visualize code step by step (great for recursion and pointers). | [pythontutor.com](https://pythontutor.com/) |
| **VisuAlgo** | Animations of data structures and algorithms. | [visualgo.net](https://visualgo.net/) |

---

## Troubleshooting

| Problem | Fix |
|---|---|
| `'python' is not recognized...` (Windows) | Python isn't on PATH. Re-run the installer → *Modify* → enable "Add Python to environment variables". Restart the terminal. |
| `python` opens the Microsoft Store (Windows) | Settings → search **App execution aliases** → turn off the `python.exe` and `python3.exe` aliases. |
| `command not found: python` (macOS) | Use `python3` instead. |
| VSCode runs the wrong Python | `Ctrl+Shift+P` / `Cmd+Shift+P` → **Python: Select Interpreter** → pick Python 3. |
| Still stuck | Ask in the group chat with a screenshot of the error. |

---

✅ **Ready for Week 2 when:** `python --version` shows Python 3, and `hello.py` runs in VSCode (or a cell runs in Colab).