# choperia/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('empresa/', include('empresa.urls', namespace='empresa')),
    path('produto/', include('produto.urls', namespace='produto')),
    path('estoque/', include('estoque.urls', namespace='estoque')),
    path('mesa/', include('mesa.urls', namespace='mesa')),  # Certifique-se de que esta linha está correta
]

