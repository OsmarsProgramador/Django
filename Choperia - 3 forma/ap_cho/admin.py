from django.contrib import admin
from .models import Produto, Mesa

"""@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'data_criacao']  # Campos a serem exibidos na lista de objetos
    list_filter = ['data_criacao']  # Filtros laterais para a data de criação
    search_fields = ['nome']  # Campos pelos quais a busca será realizada"""

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome_produto', 'categoria', 'custo', 'venda', 'estoque']  # Campos a serem exibidos na lista de objetos
    list_filter = ['categoria']  # Filtro lateral para a categoria
    search_fields = ['nome_produto', 'descricao']  # Campos pelos quais a busca será realizada

@admin.register(Mesa)
class MesaAdmin(admin.ModelAdmin):
    list_display = ['nome']  
    list_filter = ['nome']  
    search_fields = ['nome']  