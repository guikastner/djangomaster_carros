from django.contrib import admin
from cars.models import Car, Brand	# Import the Car and Brand models

class CarAdmin(admin.ModelAdmin): 
    list_display = ('brand', 'model', 'factory_year', 'model_year', 'value')
    list_filter = ('brand', 'model', 'factory_year', 'model_year', 'value')
    search_fields = ['model', 'brand']

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)

admin.site.register(Brand, BrandAdmin)
admin.site.register(Car, CarAdmin)	# Register the Car and Brand models with the admin site