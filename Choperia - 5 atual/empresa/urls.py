# empresa/urls.py
from django.urls import path
from .views import EmpresaListView, EmpresaDetailView, NotaFiscalListView

app_name = 'empresa'

urlpatterns = [
    path('', EmpresaListView.as_view(), name='empresa_list'),
    path('<int:pk>/', EmpresaDetailView.as_view(), name='empresa_detail'),
    path('notas/', NotaFiscalListView.as_view(), name='nota_list'),
]

