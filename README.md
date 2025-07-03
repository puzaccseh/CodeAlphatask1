# CodeAlpha_SecureLoginApp

## 📌 Project Overview
This is a simple vulnerable Flask login app created for the CodeAlpha Cyber Security Internship **Secure Coding Review** task.

## ⚙️ Tech Stack
- Python 3.x
- Flask

## 🔍 Findings
| ID | File | Line | Issue | Impact | Recommendation |
|----|------|------|-------|--------|-----------------|
| 1 | app.py | 6 | Hardcoded credentials | Easily guessable and exposes admin login | Use secure password hashing + database |
| 2 | app.py | 19 | No input validation | Susceptible to injection attacks | Validate and sanitize input |
| 3 | Deployment | - | No HTTPS | Credentials sent in plaintext | Deploy with SSL/TLS |

## ✅ Recommended Fixes
- Store hashed passwords in a database (e.g., SQLite + bcrypt).
- Validate form input using Flask-WTF or regex.
- Deploy the app with HTTPS enforced.
- Add CSRF protection for forms.

## 🚀 How to Run
```bash
pip install -r requirements.txt
python app.py
