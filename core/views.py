


from django.shortcuts import render

def home(request):
    return render(request, 'core/index.html')

def phishing(request):
    return render(request, 'core/phishing.html')

def password_safety(request):
    return render(request, 'core/password-safety.html')

def suspicious_links(request):
    return render(request, 'core/suspicious-links.html')

def quiz(request):
    return render(request, 'core/quiz.html')
