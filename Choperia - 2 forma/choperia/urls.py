from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('tabela_produtos/', views.tabela_produtos, name='tabela_produtos'),
    path('cadastrar_produto/', views.cadastrar_produto, name='cadastrar_produto'),
    path("valida_cadastro_produto/", views.valida_cadastro_produto, name="valida_cadastro_produto"),
    # url configurada para receber um parâmetro para o produto.id, pois foi enviado através da pagina via teg url
    path('editar_produto/<int:produto_id>/', views.editar_produto, name='editar_produto'),
    path('deletar_produto/<int:produto_id>/', views.deletar_produto, name='deletar_produto'),
    path('deletar_produto_confirmacao/<int:produto_id>/', views.deletar_produto_confirmacao, name='deletar_produto_confirmacao'),
    path('valida_edicao_produto/<int:produto_id>/', views.valida_edicao_produto, name='valida_edicao_produto'),
]
