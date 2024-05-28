from django.urls import path
from . import views
from .views import cadastrar_produto


urlpatterns = [
    path('cadastrar/', views.cadastrar, name = 'cadastrar'),
    path('home/', views.home, name = 'home'),
    path('tabela_produtos/', views.tabela_produtos, name='tabela_produtos'),
    path('cadastrar_produto/', views.cadastrar_produto, name='cadastrar_produto'),
]