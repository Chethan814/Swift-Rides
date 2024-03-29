from django.shortcuts import render, HttpResponse , get_object_or_404
from .models import Car , Location

# Create your views here.


def searching(request):

    query = request.GET.get('search')
    start_date = request.GET.get('start_date')
    start_datetime = request.GET.get('start_datetime')
    end_date = request.GET.get('end_date')
    end_datetime = request.GET.get('end_datetime')

    results = Car.objects.all()
    if query:
        results = results.filter(locations__city__icontains=query)

    return render(request, 'pages/search.html', {'results': results, 'query': query})

    # return HttpResponse('this is search page')


def index(request):
    return render(request, 'pages/index.html')


def car_detail(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    return render(request, 'pages/car.html', {'car': car})
