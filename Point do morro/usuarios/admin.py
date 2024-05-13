from django.contrib import admin
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'ativo')
    list_editable = ('email',)
    readonly_fields = ('senha',)  # define o campo apenas para leitura, não permitindo alteração, quando for acesado por admin
    search_fields = ('nome', 'email')
    list_filter = ('ativo',)
