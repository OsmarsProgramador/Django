# usuario/urls.py
from django.urls import path
from . import views

app_name = 'usuario'

urlpatterns = [
    path('', views.usuario_list, name='usuario_list'),
    path('new/', views.usuario_create, name='usuario_create'),
    path('<int:pk>/edit/', views.usuario_update, name='usuario_update'),
    path('<int:pk>/delete/', views.usuario_delete, name='usuario_delete'),
    path('signup/', views.signup, name='signup'),  # Cadastro de usuário
    path('login/', views.login_view, name='login'),  # Login de usuário
    path('logout/', views.logout_view, name='logout'),  # Logout de usuário
    path('', views.index, name='index'),  # Tela inicial para usuários logados
]

