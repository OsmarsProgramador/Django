# choperia/urls.py
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

""" 
Esta forma inclui as URLs do aplicativo core na raiz do projeto e define um namespace core para elas. 
Isso é útil para evitar conflitos de nome de URL entre diferentes aplicativos e 
para referenciar URLs de maneira mais explícita nos templates.

Usar o namespace é uma boa prática em projetos Django, especialmente em projetos maiores com múltiplos 
aplicativos, pois ajuda a evitar conflitos e torna o código mais claro e fácil de manter.

Se um namespace é adicionado na url do projeto, ele também deve ser adicionado na url do aplicativo,
para que quando usar a tag { url %}, você deve incluir o namespace: como é o caso dessa teg: href="{ url 'core:index' %}"
"""
urlpatterns = [
    path('admin/', admin.site.urls), 
    path("auth/", include('usuarios.urls', namespace='usuarios')),
    path('', include('core.urls', namespace='core')),
    path('empresa/', include('empresa.urls', namespace='empresa')),
    path('produto/', include('produto.urls', namespace='produto')),
    path('estoque/', include('estoque.urls', namespace='estoque')),
    path('mesa/', include('mesa.urls', namespace='mesa')),  # Certifique-se de que esta linha está correta
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# Adicione esta configuração para servir arquivos de mídia durante o desenvolvimento



