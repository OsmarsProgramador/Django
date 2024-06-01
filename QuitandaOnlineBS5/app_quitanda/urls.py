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
    path("cliente_contatos/", views.cliente_contatos, name='cliente_contatos'),
    path("cliente_dados/", views.cliente_dados, name='cliente_dados'),
    path("cliente_endereco/", views.cliente_endereco, name='cliente_endereco'),
    path("cliente_favoritos/", views.cliente_favoritos, name='cliente_favoritos'),
    path("cliente_pedidos/", views.cliente_pedidos, name='cliente_pedidos'),
    path("cliente_senha/", views.cliente_senha, name='cliente_senha'),
    path('confirmcadastrosenha/', views.confirmcadastrosenha, name='confirmcadastrosenha'),
    path("confirmcontato/", views.confirmcontato, name='confirmcontato'),
    path("confirmrecupsenha/", views.confirmrecupsenha, name='confirmrecupsenha'),
    path("fechamento_endereco/", views.fechamento_endereco, name='fechamento_endereco'),
    path("fechamento_itens/", views.fechamento_itens, name='fechamento_itens'),
    path("fechamento_pagamento/", views.fechamento_pagamento, name='fechamento_pagamento'),
    path("fechamento_pedido/", views.fechamento_pedido, name='fechamento_pedido'),
    path("produto/", views.produto, name='produto'),
    path("recuperarsenha/", views.recuperarsenha, name='recuperarsenha'),
]