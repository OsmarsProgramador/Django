from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("ap_choperia.urls")),
    path("ap_choperia/", include('ap_choperia.urls')),
    path("auth/", include('usuarios.urls')),
]