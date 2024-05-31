from django.urls import path
from . import views

urlpatterns = [
    path("index/", views.index, name='index'),
    #path("login/", views.login, name='login'),
    #path("contato/", views.contato, name='contato'),
    # path("cadastrarnovasenha/", views.cadastrarnovasenha, name='cadastrarnovasenha'),
    #path("cadastro/", views.cadastro, name='cadastro'),
    #path("carrinho/", views.carrinho, name='carrinho'),
    #path("cliente/", views.cliente, name='cliente'),
]