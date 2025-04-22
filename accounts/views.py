from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomAuthenticationForm

def home_view(request):
    return render(request, 'accounts/home.html')

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')



def about_view(request):
    developer_info = {
        'name': "Shishir Ronjon Dey",
        'bio': "Full Stack Developer and AI Enthusiast",
        'photo': "https://media.licdn.com/dms/image/D5603AQE-micMpybQbg/profile-displayphoto-shrink_200_200/0/1709400140556?e=2147483647&v=beta&t=A-BUUWsSg8g4A7fl2Pt8FuaRc6_O1amHf1JAEhWXSKE",
        'skills': ["Python", "Django", "JavaScript", "React", "Problem Solver"],
        'education': "High School Student",
        'experience': "2+ years of web development experience",
        'email': "deyshuvo2022@gmail.com",
        'github': "https://github.com/Shishir-Dey-coder",
        'linkedin': "https://www.linkedin.com/in/shishir-ronjon-dey-39b23b238/",
        'projects': [
            {"name": "ChatBot", "description": "AI-powered conversational agent"},
            {"name": "E-commerce Platform", "description": "Full-featured online store"},
            {"name": "Data Analysis Tool", "description": "Python-based analytics dashboard"},
        ]
    }
    
    return render(request, 'accounts/about.html', {
        'developer': developer_info,
        'MEDIA_URL': settings.MEDIA_URL
    })
