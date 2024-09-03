# chopperia/urls.py
from django.contrib import admin
from django.urls import path, include
from usuario import views as usuario_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('produtos/', include('produto.urls')),
    path('mesas/', include('mesa.urls')),
    path('login/', usuario_views.login_view, name='login'),
    path('logout/', usuario_views.logout_view, name='logout'),
    path('signup/', usuario_views.signup, name='signup'),
    path('', usuario_views.index, name='index'),  # Tela inicial
]

