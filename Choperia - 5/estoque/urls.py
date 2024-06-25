# estoque/urls.py
from django.urls import path
from . import views

app_name = 'estoque'

urlpatterns = [
    path('entrada/', views.EstoqueEntradaListView.as_view(), name='estoque_entrada_list'),
    path('saida/', views.EstoqueSaidaListView.as_view(), name='estoque_saida_list'),
    path('protocolo/', views.ProtocoloEntregaListView.as_view(), name='protocolo_de_entrega_list'),
]
