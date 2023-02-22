from audioop import reverse
from imaplib import _Authenticator
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.http import HttpResponse

from django.contrib.auth import authenticate, login

# Create your views here.
def login_user(request):
    if (request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user = authenticate(request, username=username, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid username, email or password'
            return render(request, 'auth/login.html', {'error_message': error_message})
    return render(request, 'auth/login.html')

def register(request):
    if (request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user = User.objects.create_user(username,email,password)
    return render(request, 'auth/register.html')

def template_home(request):
    return render(request, "home.html")