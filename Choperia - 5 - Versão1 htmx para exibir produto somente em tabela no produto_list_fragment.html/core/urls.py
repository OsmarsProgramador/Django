# core/urls.py
from django.urls import path
from . import views

app_name = 'core'  # Define o namespace para este conjunto de URLs

urlpatterns = [
    path('', views.index, name='index'),  # Define o nome da URL como 'index' no namespace 'core'
]

