# empresa/urls.py
from django.urls import path
from . import views

app_name = 'empresa'

urlpatterns = [
    
    path('', views.EmpresaListView.as_view(), name='empresa_list'),
    path('<int:pk>/', views.EmpresaDetailView.as_view(), name='empresa_detail'),
]


