# usuarios/admin.py
from django.contrib import admin
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'ativo')
    list_filter = ('ativo',)
    readonly_fields = ('senha',)

    # Método para tornar a senha somente leitura
    def senha(self, obj):
        return obj.senha

    
    