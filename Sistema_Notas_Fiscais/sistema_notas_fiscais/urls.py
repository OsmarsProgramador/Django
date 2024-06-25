# sistema_notas_fiscais/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('empresas/', include('empresa.urls')),
    path('notas-fiscais/', include('notafiscal.urls')),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    #path('', include('empresa.urls')),
]
