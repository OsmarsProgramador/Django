# mesa/urls.py
from django.urls import path
from . import views

app_name = 'mesa'

urlpatterns = [
    path('', views.MesaListView.as_view(), name='mesa_list'),
    path('abrir/<int:pk>/', views.MesaDetailView.as_view(), name='abrir_mesa'),  # Exemplo de rota
    # Adicione outras rotas aqui se necessário
]

