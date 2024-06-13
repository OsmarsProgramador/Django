from usuarios.models import Usuario
from django.contrib import admin

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'ativo')
    list_editable = ('email',)
    readonly_fields = ('senha',) # naõ permite que no campoa admin altere, tornando o compo somente para leitura
    search_fields = ('nome', 'email')
    list_filter = ('ativo',)