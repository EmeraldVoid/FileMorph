 <p align="center">
  <img width="200" height="200" src="https://i.imgur.com/MHrWKKt.png">
</p>

<h3 align="center">FileMorph</h3>

<p align="center">
  a lightweight collection of <a href="https://www.python.org/">Python-based</a> scripts
  <br>
 <br>
  <a href="https://github.com/EmeraldVoid/FileMorph/releases"><strong>Latest Releases »</strong></a>
  <br>
  <br>
  <a href="https://github.com/EmeraldVoid/FileMorph/issues/new">Report bug</a>
  ·
  <a href="https://github.com/EmeraldVoid/FileMorph/issues/new">Request feature</a>
  ·
  <a href="https://emeraldvoid.github.io/EmeraldVoid/">Website</a>
</p>

# 🌀 FileMorph

![GitHub last commit](https://img.shields.io/github/last-commit/emeraldvoid/FileMorph)
![GitHub repo size](https://img.shields.io/github/repo-size/emeraldvoid/FileMorph)
![GitHub issues](https://img.shields.io/github/issues/emeraldvoid/FileMorph)
![GitHub](https://img.shields.io/github/license/emeraldvoid/FileMorph)
![Maintained](https://img.shields.io/badge/maintained-yes-brightgreen)
![Built with Python](https://img.shields.io/badge/built%20with-python-blue)



**FileMorph** is a lightweight collection of Python-based scripts designed to convert one file format into another—quickly, cleanly, and with minimal setup. Whether you're converting `.webp` files to `.png`, or `.png` to `.ico`, FileMorph provides simple tools for your everyday file transformation needs.

> ⚠️ **Note:** These tools were built for personal use and convenience. They're offered as-is, and may not support every file format or edge case.

---

## 📦 Usage

To use any of the included file conversion tools:

1. **Download** the latest release of FileMorph.
2. **Extract** the contents to a folder of your choice.
3. **Double-click** the specific `.py` script you want to run.
4. When prompted:
   - Enter the **path** to the folder containing the files you want to convert.
   - Then, enter the **path** to the folder where the converted files should be saved.
5. Sit back and let the tool handle the conversion.

All tools are terminal-based and require **Python 3.8+** to be installed on your system.

---

## 🔁 Supported Conversions

FileMorph is **not** a universal file converter—it's a set of practical tools built for specific needs. Current supported conversions:

- `.webp` → `.png`
- `.png` → `.ico`

More tools will be added as needed based on real-world use cases.

---

## 🧪 Future Plans

While FileMorph started as a personal utility toolkit, here are a few possibilities for the future:

- ✅ Additional format converters as needed.
- 🔄 Unified launcher script for all tools.
- 🖼️ Drag-and-drop interface (maybe!).
- 🧰 Packaging as an executable or simple GUI.

No timeline is guaranteed. FileMorph is an evolving toolset made to scratch specific itches.

---

## 🛠️ Dependencies

All scripts use built-in or widely used Python libraries:
- `os`
- `sys`
- `Pillow` (for image processing)
- `tqdm` (for progress bars)

You can install missing dependencies with:

```bash
pip install pillow tqdm
