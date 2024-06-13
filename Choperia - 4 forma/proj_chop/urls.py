
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("app_chop.urls")),
    path("app_chop/", include('app_chop.urls')),
    path("auth/", include('usuarios.urls')),
]
