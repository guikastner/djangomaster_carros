from django.contrib import admin
from .models import Car

class CarAdmin(admin.ModelAdmin): 
    list_display = ('brand', 'model', 'factory_year', 'model_year', 'value')
    list_filter = ('brand', 'model', 'factory_year', 'model_year', 'value')
    search_fields = ['model', 'brand']


admin.site.register(Car, CarAdmin)