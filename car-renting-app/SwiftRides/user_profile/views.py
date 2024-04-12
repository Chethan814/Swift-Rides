from django.shortcuts import render, HttpResponse ,redirect
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from django.contrib.auth import login , logout , authenticate
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

from django.http import HttpResponseNotFound
from django.shortcuts import render, HttpResponse, get_object_or_404
from home.models import Car, Location

# Create your views here.

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('UserLog')  # Redirect to some logged-in page
        else:
            messages.error(request, 'Invalid username or password.')  # Use error message
            return redirect('login')  # Redirect back to login page
    else:
        return render(request, 'pages/Login.html')  # Render the login page template

   
@login_required(login_url='login')
def UserInfo(request):
    return render(request, 'user/UserInformation.html')


@login_required(login_url='login')
def UserLog(request):
    return render(request, 'user/user.html')



def Signup(request):
    if request.method == 'GET':
        return render(request, 'pages/Signup.html', {"form": UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password= request.POST['password1']  )
                user.save()
                login(request, user)
                return redirect('UserLog')
            except IntegrityError:
                return render(request,'pages/signup.html',{'form': UserCreationForm, 'error': 'User is already exits '})
            
        else:
            return render(request,'pages/signup.html',{'form': UserCreationForm, 'error': 'Password do not match'})
        
        
def Logout(request):
    logout(request)
    return redirect('login')

def user_searching(request):
    query = request.GET.get('search')
    destination = request.GET.get('destination')
    start_date = request.GET.get('start_date')
    start_datetime = request.GET.get('start_datetime')
    end_date = request.GET.get('end_date')
    end_datetime = request.GET.get('end_datetime')

    results = Car.objects.all()
    if query:
        results = results.filter(locations__city__icontains=query)

    return render(request, 'user\search.html', {'results': results, 'query': query, 'destination': destination})

    # return HttpResponse('this is search page')
            