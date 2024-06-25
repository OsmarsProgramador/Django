# mesa/urls.py
from django.urls import path
from . import views

app_name = 'mesa'

urlpatterns = [
    path('', views.MesaListView.as_view(), name='mesa_list'),
    # Adicione outras rotas aqui se necessário
]
