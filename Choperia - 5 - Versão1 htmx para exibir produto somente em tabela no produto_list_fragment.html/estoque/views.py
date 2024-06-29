# estoque/views.py
from django.views.generic import ListView
from .models import Estoque

class EstoqueEntradaListView(ListView):
    model = Estoque
    template_name = 'estoque/estoque_entrada_list.html'
    context_object_name = 'entradas'

    def get_queryset(self):
        return Estoque.objects.filter(tipo='entrada')

class EstoqueSaidaListView(ListView):
    model = Estoque
    template_name = 'estoque/estoque_saida_list.html'
    context_object_name = 'saidas'

    def get_queryset(self):
        return Estoque.objects.filter(tipo='saida')

class ProtocoloEntregaListView(ListView):
    model = Estoque
    template_name = 'estoque/protocolo_entrega_list.html'
    context_object_name = 'protocolos'

    def get_queryset(self):
        # Adicione aqui a lógica para listar os protocolos de entrega
        pass
