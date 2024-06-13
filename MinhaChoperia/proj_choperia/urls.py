from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("app_choperia.urls")),
    path("app_choperia/", include('app_choperia.urls')),
    path("auth/", include('usuarios.urls')),
]