# Internlytic Cyber Awareness Training Portal

**Learn. Identify. Protect.**

A Django-based educational project created for the **Phase 3 Internship Task – Cyber Security & Secure Coding** at **Internlytic Technologies**.

The portal is intended to help learners recognize common online risks and understand practical cybersecurity and secure-coding habits.

## Project status

This repository currently contains the initial Django project and a basic home page. The learning modules, interactive quiz, password-strength demonstration, progress tracking, and secure-coding checklist are planned development items and are not yet implemented.

## Planned learning areas

- **Phishing awareness** — learn to recognize suspicious messages and common social-engineering warning signs.
- **Password safety** — understand strong, unique passwords and safer authentication habits.
- **Suspicious links** — learn how to inspect links cautiously before opening them.
- **Secure coding** — review input validation, password hashing, and safe error handling.

## Planned interactive features

- Quiz questions using fictional safe/unsafe message examples, with scores and explanations.
- A progress indicator for learning activities.
- A password-strength meter that uses demonstration input only.
- A secure-coding checklist for learners.

## Technology

- Python
- Django
- HTML

## Run locally

### 1. Clone the repository

```bash
git clone https://github.com/aisha-the-creative-compiler/internlytic-cyber-awareness-portal.git
cd internlytic-cyber-awareness-portal
```

### 2. Create and activate a virtual environment

**Windows PowerShell**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, you can use Command Prompt instead:

```bat
venv\Scripts\activate.bat
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Apply database migrations

```bash
python manage.py migrate
```

### 5. Start the development server

```bash
python manage.py runserver
```

Open **http://127.0.0.1:8000/** in your browser.

## Security and safe-use notes

- This is an educational awareness project, not a penetration-testing or vulnerability-scanning tool.
- Use fictional examples and demonstration data only.
- Never enter real passwords into a demonstration password-strength meter.
- Do not collect, store, or share real passwords or credentials.
- Test only on systems and accounts you own or have explicit permission to use.
- For deployment, set a strong, unique `DJANGO_SECRET_KEY` environment variable and configure Django's production security settings. Do not publish secret keys, passwords, database files, or environment files.

## Project structure

```text
internlytic-cyber-awareness-portal/
├── config/                 # Django project settings and URL configuration
├── core/                   # Main application
│   └── templates/
│       └── core/
│           └── index.html  # Home page template
├── manage.py
├── requirements.txt
└── .gitignore
```

## Internship task

Developed as part of the **Internlytic Technologies – Phase 3 Internship Task: Cyber Security & Secure Coding**.

---

*This README describes the current starter version and planned features. It will be updated as the project is developed.*
