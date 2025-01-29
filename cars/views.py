from django.shortcuts import render
from cars.models import Car
#from django.http import HttpResponse



def carview(request):
    cars = Car.objects.all()
    search = request.GET.get('search')
    print(search)

    if search:
        cars = Car.objects.filter(model__icontains=search)

    return render(
        request,
        'cars.html',
        {'cars': cars})
    #request
    #template name - local
