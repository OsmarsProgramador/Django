# produto/urls.py
from django.urls import path
from . import views

app_name = 'produto'

urlpatterns = [
    path('', views.produto_list, name='produto_list'),  # Lista de produtos
    path('new/', views.produto_create, name='produto_create'),  # Adicionar produto
    path('<int:pk>/edit/', views.produto_update, name='produto_update'),  # Editar produto
    path('<int:pk>/delete/', views.produto_delete, name='produto_delete'),  # Excluir produto
    path('', views.index, name='index'),

    # URLs para categoria
    path('categorias/', views.categoria_list, name='categoria_list'),  # Listar categorias
    path('categorias/new/', views.categoria_create, name='categoria_create'),  # Adicionar categoria
]
