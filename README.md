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
  <a href="https://emeraldvoid.github.io/FileMorph/">Website</a>
</p>

<p align="center">
  <img src="https://img.shields.io/github/last-commit/emeraldvoid/FileMorph" alt="Last Commit">
  <img src="https://img.shields.io/github/repo-size/emeraldvoid/FileMorph" alt="Repo Size">
  <img src="https://img.shields.io/github/issues/emeraldvoid/FileMorph" alt="Issues">
  <img src="https://img.shields.io/github/license/emeraldvoid/FileMorph" alt="License">
  <img src="https://img.shields.io/badge/built%20with-python-blue" alt="Built With Python">
  <img src="https://img.shields.io/badge/maintained-yes-brightgreen" alt="Maintained">
</p>

---

## 📦 What is FileMorph?

**FileMorph** is a lightweight collection of Python-based scripts designed to convert one file format into another—quickly, cleanly, and with minimal setup. Whether you're converting `.webp` files to `.png`, or `.png` to `.ico`, FileMorph provides simple tools for your everyday file transformation needs.

> ⚠️ **Note:** These tools were built for personal use and convenience. They're offered as-is and may not support every file format or edge case.

---

## 🧰 Usage

To use any of the included file conversion tools:

1. **Download** the **[latest release](https://github.com/EmeraldVoid/FileMorph/releases)** of FileMorph.
2. **Extract** the contents to a folder of your choice.
3. **Double-click** the specific `.py` script you want to run.
4. When prompted:
   - Enter the **path** to the folder containing the files you want to convert.
   - Then, enter the **path** to the folder where the converted files should be saved.
5. Sit back and let the tool handle the conversion.

> 💡 All tools are terminal-based and require **Python 3.8+**.

---

## 🔁 Supported Conversions

FileMorph is **not** a universal file converter—it's a set of practical tools built for specific needs. Current supported conversions:

- `.webp` → `.png`
- `.png` → `.ico`

More tools will be added as needed based on real-world use cases.

---

## 📁 Suggested Folder Structure

Each script will prompt you to specify input/output directories, but you can optionally prepare folders like this:

```
FileMorph/
│
├── webp2png_tool.py
├── png2ico_tool.py
│
├── input_files/      ← Place original files here (e.g., .webp)
└── output_files/     ← Converted files will be saved here (e.g., .png)
```

---

## 🛠️ Dependencies

- The latest version of [python](https://www.python.org/)  
- [Pillow](https://python-pillow.org) – for image processing  
- [tqdm](https://github.com/tqdm/tqdm) – for progress bar display

```bash
pip install pillow tqdm
```

---

## 🧪 Future Plans

While FileMorph started as a personal utility toolkit, here are a few possibilities for the future:

- ✅ Additional format converters as needed.
- 🔄 Unified launcher script for all tools.
- 🖼️ Drag-and-drop interface (maybe!).
- 🧰 Packaging as an executable or simple GUI.

> ⏳ FileMorph was never meant to be a full application—these are tools made to solve recurring file conversion tasks in my workflow.

---

## ⚠️ AI Assistance Notice

> 🧠 This project was created with the help of artificial intelligence (AI). Some of the code, documentation, and ideas were generated or enhanced using AI tools. While every effort has been made to ensure the accuracy and quality of the work, the content might contain areas that could benefit from further human review and refinement.

Feel free to contribute or suggest improvements, and thank you for understanding!

---


