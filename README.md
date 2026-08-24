# 🎨 AI Image Studio

**MirAI School of Technology | Virtual Summer Internship 2026 | AI Builder Track – Assignment 4**

An upgraded AI Image Studio built with **Python**, **Streamlit**, and **Pollinations AI**. This assignment focuses on debugging an existing prototype and enhancing it with new AI-powered UX features.

---

## 📌 Overview

This project allows users to generate AI images from text prompts while customizing the art style and image dimensions. It also includes creative features like **Magic Enhance** and **Surprise Me** for a smoother user experience.

---

## ✨ Features

* Generate AI images from text prompts
* Multiple art styles
* Adjustable width and height
* ✨ Magic Enhance prompt booster
* 🎲 Surprise Me random prompt generator
* Download images as PNG
* Clean Streamlit interface

---

## 🚀 Assignment Improvements

### ✅ Task 1 – Fixed Width & Height Sliders

The selected image dimensions are now passed directly to the Pollinations AI API.

### ✅ Task 2 – Dynamic PNG Download

Downloaded images now:

* Save with the `.png` extension
* Use a filename based on the selected art style

Example:

* `anime_image.png`
* `watercolor_image.png`

### ✅ Task 3 – Magic Enhance

When enabled, the app automatically enriches prompts with quality-enhancing keywords.

### ✅ Task 4 – Surprise Me

A random creative prompt is selected instantly using Python's `random.choice()`.

---

## 🖥️ Tech Stack

| Technology      | Purpose              |
| --------------- | -------------------- |
| Python          | Programming Language |
| Streamlit       | Web App Framework    |
| Requests        | API Calls            |
| Pollinations AI | Image Generation     |
| Random          | Surprise Prompt      |
| urllib.parse    | URL Encoding         |

---

## 📂 Project Structure

```text
AI-image-studio/
│
├── app.py
├── README.md
├── requirements.txt
└── OUTPUT.png
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone <YOUR_GITHUB_REPO_LINK>
cd AI-image-studio
```

### Create a virtual environment

```bash
python -m venv .venv
```

### Activate the environment

**PowerShell**

```powershell
.\.venv\Scripts\Activate.ps1
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
streamlit run app.py
```

---

## 📦 Requirements

```text
streamlit
requests
```

---

## 📸 Screenshots

### Home Screen

> *(Replace with your screenshot)*

![Home Screen](OUTPUT.png)

### Generated Image

> *(Replace with your generated image screenshot)*

---

## 🎥 Demo Video

**Screen Recording:** *Add your video link here.*

---

## 🌐 Live Demo

**Streamlit App:** *Add deployment link here.*

---

## 📚 Learning Outcomes

* Debugged an existing Streamlit application.
* Connected UI controls with API parameters.
* Improved user experience with interactive features.
* Implemented random content generation using Python.
* Built a more polished AI-powered application.

---

## 👩‍💻 Author

**Akshada Kapadi**

* B.Tech Computer Engineering
* MirAI School of Technology – AI Builder Virtual Summer Internship 2026

---

## 🙏 Acknowledgements

* MirAI School of Technology
* Pollinations AI
* Streamlit
