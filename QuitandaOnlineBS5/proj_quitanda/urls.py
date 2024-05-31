from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("proj_quitanda", include('app_quitanda.urls')),  # Incluir as URLs do aplicativo
]


"""urlpatterns = [
    path("admin/", admin.site.urls),
    path("app_quitanda/", include('app_quitanda.urls')),
]"""
