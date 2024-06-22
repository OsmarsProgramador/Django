from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("ap_cho.urls")),
    path("ap_cho/", include("ap_cho.urls")),
    path("auth/", include('usuarios.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Configura urls.py para servir arquivos de mídia durante o desenvolvimento
"""from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
"""