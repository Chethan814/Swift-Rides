from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return render(request, 'index.html')

def searching(request):
    return HttpResponse('this is search page')

