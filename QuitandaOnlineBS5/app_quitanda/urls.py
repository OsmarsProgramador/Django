from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # URL para a página inicial
    path('contato/', views.contato, name='contato'),  # URL para a página de contato
    path('login/', views.login, name='login'),  # URL para a página de login
    path("index/", views.index, name='index'),
    path("confirmarcadastro/", views.confirmarcadastro, name='confirmarcadastro'),
    path("cadastrarnovasenha/", views.cadastrarnovasenha, name='cadastrarnovasenha'),
    path("cadastro/", views.cadastro, name='cadastro'),
    path("carrinho/", views.carrinho, name='carrinho'),
    path("cliente/", views.cliente, name='cliente'),
    path('valida_cadastro/', views.valida_cadastro, name='valida_cadastro'),
    path("privacidade/", views.privacidade, name='privacidade'),
    path("quemsomos/", views.quemsomos, name='quemsomos'),
    path("termos/", views.termos, name='termos'),
    path("trocas/", views.trocas, name='trocas'),
]