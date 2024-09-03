# mesa/urls.py
from django.urls import path
from . import views

app_name = 'mesa'

urlpatterns = [
    path('', views.mesa_list, name='mesa_list'),
    path('new/', views.mesa_create, name='mesa_create'),
    path('<int:pk>/edit/', views.mesa_update, name='mesa_update'),
    path('<int:pk>/delete/', views.mesa_delete, name='mesa_delete'),
    path('', views.index, name='index'),  # Lista de mesas
    path('<int:numero_mesa>/abrir/', views.abrir_mesa, name='abrir_mesa'),  # Abrir mesa
    path('<int:numero_mesa>/', views.detalhes_mesa, name='detalhes_mesa'),  # Detalhes da mesa
]

