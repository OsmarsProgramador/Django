# notafiscal/urls.py
from django.urls import path
from . import views

app_name = 'notafiscal'

urlpatterns = [
    path('', views.NotaFiscalListView.as_view(), name='notafiscal_list'),
]

