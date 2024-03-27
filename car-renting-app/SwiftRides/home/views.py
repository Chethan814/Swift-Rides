from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return render(request, 'index.html')

def searching(request):
    return render(request,'search.html')
    # return HttpResponse('this is search page')

