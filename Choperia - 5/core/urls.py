# core/urls.py
from django.urls import path
from .views import IndexView
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    # path('', IndexView.as_view(), name='index'),
]

