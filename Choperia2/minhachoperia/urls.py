
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("choperia/", include('choperia.urls')),
    path("auth/", include('usuarios.urls')),
]
