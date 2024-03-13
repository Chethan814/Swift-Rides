from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return render(request, 'index.html')


def Login(request):
    return render(request, 'Login.html')


def Signup(request):
    return render(request, 'Signup.html')

def UserInfo(request):
    return render(request, 'UserProfileInfo.html')
