# 📘 Hello Flask  
*A simple Flask web application I built by following the Visual Studio Code Python + Flask tutorial.*

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.x-lightgrey.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

This project was created using the official VS Code Flask tutorial:  
https://code.visualstudio.com/docs/python/tutorial-flask

It demonstrates how to set up a Python virtual environment, install Flask, structure a basic web app, and run it locally.

---

## 🚀 Features
- Minimal Flask application inside the `hello_app` package  
- HTML templates using Jinja2  
- Static assets (CSS, images, etc.)  
- Clean project layout recommended by the tutorial  
- `requirements.txt` for easy environment setup  

---

## 🧱 Project Structure
```
hello_flask/
│
├── hello_app/
│   ├── __init__.py
│   ├── views.py
│   ├── static/
│   └── templates/
│
├── requirements.txt
└── .vscode/
```

---

## 👨‍🏫 Setup Instructions

### 1. Create a virtual environment
```
python -m venv .venv
```

### 2. Activate it  
**Windows**
```
.venv\Scripts\activate
```

**Mac/Linux**
```
source .venv/bin/activate
```

### 3. Install dependencies
```
pip install -r requirements.txt
```

---

## ▶️ Run the App
From the project root:

```
python -m flask --app hello_app run
```

Then open your browser and go to:

```
http://127.0.0.1:5000
```

---

## 📦 Dependencies
All required packages are listed in:

```
requirements.txt
```

This file was generated using:

```
pip freeze > requirements.txt
```

---

## 📝 Credits
This project is based on the official Visual Studio Code Flask tutorial:  
https://code.visualstudio.com/docs/python/tutorial-flask
