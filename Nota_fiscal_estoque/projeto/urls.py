
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import include, path

urlpatterns = [
    path('', include('core.urls')),
    path('produto/', include('produto.urls')),
    path('estoque/', include('estoque.urls')),
    path('admin/', admin.site.urls),
    path('logout/', LogoutView.as_view(), name='logout'),
]
