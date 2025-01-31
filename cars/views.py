from django.shortcuts import render, redirect
from django.views import View
from cars.models import Car
from cars.forms import CarModelForm



def carview(request):
    cars = Car.objects.all().order_by('model')
    search = request.GET.get('search')

    if search:
        cars = Car.objects.filter(model__icontains=search).order_by('model')

    return render(
        request,
        'cars.html',
        {'cars': cars})
    #request
    #template name - local

class carsview (View):
    def get(self, request):
        cars = Car.objects.all().order_by('model')
        search = request.GET.get('search')
        if search:
            cars = Car.objects.filter(model__icontains=search).order_by('model')
        return render(
            request,
            'cars.html',
            {'cars': cars})
    


def new_car_view(request):
    if request.method == 'POST':
        new_car_form = CarModelForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list')
        print (new_car_form.data)
    else:
        new_car_form = CarModelForm()
    return render(request, 'new_car.html', {'new_car_form': new_car_form})