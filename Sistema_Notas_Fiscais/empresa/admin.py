""" Vamos registrar os modelos no Django Admin para permitir o cadastro de notas fiscais e empresas. """

# empresa/admin.py
from django.contrib import admin
from .models import Empresa

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cnpj')
