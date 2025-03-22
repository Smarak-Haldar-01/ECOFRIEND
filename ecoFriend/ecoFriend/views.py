from django.shortcuts import render

def home(request):
    return render(request, 'home/home.html', {'title': 'HOME | ECO-Friend'})

def login_signin_home(request):
    return render(request, 'home/login_signin.html', {'title': 'Login-Signin | ECO-Friend'})

def dashboard(request):  
    return render(request, 'home/dashboard.html', {'title': 'Dashboard | ECO-Friend'})  # Ensure the template exists
