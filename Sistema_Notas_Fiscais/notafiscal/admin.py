# notafiscal/admin.py
from django.contrib import admin
from .models import NotaFiscal

@admin.register(NotaFiscal)
class NotaFiscalAdmin(admin.ModelAdmin):
    list_display = ('empresa', 'serie', 'numero', 'descricao', 'peso', 'cubagem', 'data_emissao')
    search_fields = ('numero', 'descricao')
