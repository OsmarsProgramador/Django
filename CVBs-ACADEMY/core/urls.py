# core/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('erp.urls', namespace='erp')),

    path('admin/', admin.site.urls),
]
