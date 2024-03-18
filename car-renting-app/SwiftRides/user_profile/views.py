from django.shortcuts import render, HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def Login(request):
    return render(request, 'Login.html')


def Signup(request):
    
    return render(request, 'Signup.html' ,{"form" : UserCreationForm})


def UserInfo(request):
    return render(request, 'UserInformation.html')
