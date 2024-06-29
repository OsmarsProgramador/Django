# choperia/urls.py
from django.contrib import admin
from django.urls import path, include

""" 
Esta forma inclui as URLs do aplicativo core na raiz do projeto e define um namespace core para elas. 
Isso é útil para evitar conflitos de nome de URL entre diferentes aplicativos e 
para referenciar URLs de maneira mais explícita nos templates."""
urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', include('core.urls', namespace='core')),
    path('empresa/', include('empresa.urls', namespace='empresa')),
    path('produto/', include('produto.urls', namespace='produto')),
    path('estoque/', include('estoque.urls', namespace='estoque')),
    path('mesa/', include('mesa.urls', namespace='mesa')),  # Certifique-se de que esta linha está correta
]

