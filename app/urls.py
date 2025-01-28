
from django.contrib import admin
import os
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

def carview():
    return 'Meus carros'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/', carview),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


