# AI Career Advisor – Flask Web App
![Python](https://img.shields.io/badge/Python-3.12-blue)
![Flask](https://img.shields.io/badge/Framework-Flask-black)
![AI](https://img.shields.io/badge/AI-Gemini-orange)
![Status](https://img.shields.io/badge/Status-Working-success)

This is a Flask-based web application that generates **personalised career advice** using AI.  
Users enter details about their background, interests, and goals, and the app returns:

- A motivational summary
- 3 suggested career paths
- An explanation of why those careers match their profile

---

## Features

- Web interface built with HTML & CSS
- Backend built with Python and Flask
- AI-powered career advice based on user input
- Clean, structured prompt engineering for consistent responses
- Environment-based configuration (API keys stored securely in `.env`)

---

## What It Does
- Collects user information through an HTML form (name, email, education, career goals)
- Sends data to Flask backend running on Python
- Calls Google's Gemini API to generate personalized career advice
- Displays results

##  Project Demo

▶️ Watch the full demo here:  
https://youtu.be/kQrIvrk3lWs

This video demonstrates:
- User form submission
- Backend API communication
- Gemini AI response generation
- Displaying structured career advice

---
##  Tech Stack

- **Backend:** Python, Flask  
- **Frontend:** HTML, CSS  
- **Config & Secrets:** `.env`, `config.py`  
- **Others:** `requirements.txt` for dependencies

---

## Project Structure

```text
project-root/
│
├── app_simple.py               # Main Flask application
├── config.py                   # Configuration & settings
├── requirements.txt            # Python dependencies
├── .env                        # Environment variables 
└── index.html                  # Main HTML file
```

---
##  Clone the Repository

```bash
git clone https://github.com/naz-can-code/GenAI-career-advisor.git
cd GenAI-career-advisor
```
---




## Setup  — (Requires Python 3.12.4)

**Note:** This project is tested with **Python 3.12.4**. If your machine has a newer Python (e.g., 3.14.x) you do not need to replace system Python — install Python 3.12.4 and create a venv that uses that interpreter (instructions below).

1. **Get API Key**
   - Visit https://aistudio.google.com/app/apikey
   - Click "Create API Key"
   - Copy the key

2. **Configure .env**
   - Create/edit `.env`
   - Add: GOOGLE_API_KEY="your_key_here" 

3. **Install Python 3.12.4 & create a venv (Mac & Windows)**

   macOS (official installer)
   - Official installer: download Python 3.12.4 from https://www.python.org/downloads/macos/

   - Create venv and activate:
     ```bash
     python3.12 -m venv .venv
     source .venv/bin/activate
     python -m pip install --upgrade pip setuptools wheel
     python -m pip install -r requirements.txt
     ```

   Windows (installer or py launcher)
   - Download Python 3.12.4 from https://www.python.org/downloads/windows/
   - Or use py launcher if installed:
     ```powershell
     py -3.12 -m venv .venv
     .\.venv\Scripts\Activate.ps1    # PowerShell
     # or .\.venv\Scripts\activate  # cmd.exe
     python -m pip install --upgrade pip setuptools wheel
     python -m pip install -r requirements.txt
     ```

   Downgrade note: If you already have a higher Python installed, **install 3.12.4 separately** (installer/conda/pyenv) and make a fresh venv with that interpreter. Do not modify or remove your system Python.

4. **Run the Flask backend**
   - Default: `python app_simple.py` (binds to 127.0.0.1:5000 by default)
   - If port 5000 is occupied (e.g., macOS AirPlay uses 5000), run on another port: edit app_simple.py to change app.run(port=5001)
    

5. **Run the static HTML server**
   ```bash
   python -m http.server 3000
   ```
   - Open http://localhost:3000 in your browser and use the form.

---

## Project Files

### Core Files
- **`app_simple.py`** - Main Flask backend (clean, minimal comments)
- **`config.py`** - Loads Google API credentials
- **`index.html`** - Frontend form and UI
- **`.env`** - API key 
- **`requirements.txt`** - Python dependencies

### Key Features
- ✅ Google Generative AI (Gemini) integration
- ✅ Token usage tracking
- ✅ Error handling with helpful messages
- ✅ Clean, documented code

---
