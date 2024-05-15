from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("choperia/", include("choperia.urls")),
    path("admin/", admin.site.urls),
    path("auth/", include("usuarios.urls")),
]
