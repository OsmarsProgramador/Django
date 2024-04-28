from django.contrib import admin
from .models import Categoria, Produto

@admin.register(Categoria)
class CategoriaAdimin(admin.ModelAdmin):
    pass

@admin.register(Produto)
class ProdutoAdimin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'descricao', 'categoria')
    list_filter = ('categoria',)
    list_editable = ('preco', )
    list_display_links = ('nome', 'descricao')
    search_fields = ('nome', 'descricao')
    ordering  = ['nome', 'preco', 'descricao', 'categoria']