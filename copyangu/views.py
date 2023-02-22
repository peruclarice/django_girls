from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def base(request):
    return render(request, 'base.html')

def login(request):
    return HttpResponse("<h1>Login Successfull</h1>")

def sign_up(request):
    return JsonResponse({
        "id": 101,
        "email": "clarice@copyangu.com",
        "auth-token": "",
        "phone-number": "265789300456"
    })

def forgot_password(request):
    return ''

def reset_password(request):
    return ''

def me(request):
    return ''



