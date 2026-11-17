


from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('phishing/', views.phishing, name='phishing'),
    path('password-safety/', views.password_safety, name='password_safety'),
    path('suspicious-links/', views.suspicious_links, name='suspicious_links'),
    path('quiz/', views.quiz, name='quiz'),
]
