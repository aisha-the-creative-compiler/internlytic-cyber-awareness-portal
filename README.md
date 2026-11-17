# CyberGuard – Cybersecurity Awareness Portal

**Learn. Identify. Protect.**

CyberGuard is an educational cybersecurity awareness portal developed as part of the Cyber Security & Secure Coding Internship Program at **Internlytic Technologies**.

The project helps users understand common online threats, recognize suspicious activities, and develop safer digital habits through interactive learning materials and practical demonstrations.

## Features

- **Phishing Awareness:** Learn to recognize fraudulent messages and common phishing warning signs.
- **Password Safety:** Understand strong password practices and use an interactive password-strength checker.
- **Suspicious Links:** Learn to identify potentially unsafe links and avoid online risks.
- **Interactive Cybersecurity Quiz:** Answer five questions, receive explanations, track question progress, and view your final score.
- **Secure-Coding Checklist:** Learn about input validation, password hashing, and safe error handling.

## Technologies Used

- Python
- Django
- HTML5
- CSS3
- JavaScript
- Visual Studio Code

## Security Concepts Demonstrated

- Recognizing phishing attempts and social engineering.
- Creating strong and unique passwords.
- Identifying suspicious links.
- Understanding secure input validation.
- Using secure password hashing methods.
- Handling application errors without exposing sensitive information.

## Safe Testing Boundaries

- All examples are fictional and intended for educational purposes.
- The password-strength checker uses demo input only.
- Never enter real passwords or confidential information into the demonstration.
- The project does not intentionally collect or store passwords.
- No real websites, accounts, or individuals are targeted or tested.

## Run Locally

### 1. Create a virtual environment

```bash
python -m venv venv
```

### 2. Activate the virtual environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
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

Open http://127.0.0.1:8000/ in your browser.

## Project Structure

```text
cyber-awareness-portal/
├── config/
│   ├── settings.py
│   └── urls.py
├── core/
│   ├── templates/
│   │   └── core/
│   │       ├── index.html
│   │       ├── phishing.html
│   │       ├── password-safety.html
│   │       ├── suspicious-links.html
│   │       └── quiz.html
│   └── views.py
├── manage.py
└── README.md
```

## Developed For

**Internlytic Technologies**  
Cyber Security & Secure Coding Internship Program

## Project Purpose

This project was developed for educational purposes to promote cybersecurity awareness and encourage safer online practices.