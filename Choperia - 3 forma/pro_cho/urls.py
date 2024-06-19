from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("ap_cho.urls")),
    path("ap_cho/", include("ap_cho.urls")),
    path("auth/", include('usuarios.urls')),
]
