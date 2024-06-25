from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('home/', views.home, name = 'home'),
    path('tabela_produtos/', views.tabela_produtos, name='tabela_produtos'),
    path('cadastrar_produto/', views.cadastrar_produto, name='cadastrar_produto'),
    path("valida_cadastro_produto/", views.valida_cadastro_produto, name="valida_cadastro_produto"),
    # url configurada para receber um parâmetro para o produto.id, pois foi enviado através da pagina via teg url
    path('editar_produto/<int:produto_id>/', views.editar_produto, name='editar_produto'),
    path('deletar_produto/<int:produto_id>/', views.deletar_produto, name='deletar_produto'),
    path('deletar_produto_confirmacao/<int:produto_id>/', views.deletar_produto_confirmacao, name='deletar_produto_confirmacao'),
    path('valida_edicao_produto/<int:produto_id>/', views.valida_edicao_produto, name='valida_edicao_produto'),
    path('lista_mesas/', views.lista_mesas, name='lista_mesas'),
    path('cadastrar_mesa/', views.cadastrar_mesa, name='cadastrar_mesa'),
    path('valida_cadastro_mesa/', views.valida_cadastro_mesa, name='valida_cadastro_mesa'),
    path('abrir_mesa/<int:mesa_id>/', views.abrir_mesa, name='abrir_mesa'),  # Nova rota para abrir mesa
    path('update_user/<int:mesa_id>/', views.update_user, name='update_user'),
    path('adicionar_item_mesa/<int:mesa_id>/<int:produto_id>/', views.adicionar_item_mesa, name='adicionar_item_mesa'),
    path('excluir_item_mesa/<int:mesa_id>/<int:item_codigo>/', views.excluir_item_mesa, name='excluir_item_mesa'),
    path('gerar_comanda_pdf/<int:mesa_id>/', views.gerar_comanda_pdf, name='gerar_comanda_pdf'),
    path('finalizar_pagamento/<int:mesa_id>/', views.finalizar_pagamento, name='finalizar_pagamento'),
    # path('adicionar_produto/<int:mesa_id>/', views.adicionar_produto, name='adicionar_produto'),
    path('criar_categoria/', views.criar_categoria, name='criar_categoria'),
    path('get_user_info/', views.get_user_info, name='get_user_info'),
]


