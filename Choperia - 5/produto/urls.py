# produto/urls.py
from django.urls import path
from .views import ProdutoListView, ProdutoCreateView, ProdutoUpdateView, ProdutoDeleteView, CategoriaListView

app_name = 'produto'

urlpatterns = [
    path('', ProdutoListView.as_view(), name='produto_list'),
    path('new/', ProdutoCreateView.as_view(), name='produto_create'),
    path('<int:pk>/edit/', ProdutoUpdateView.as_view(), name='produto_update'),
    path('<int:pk>/delete/', ProdutoDeleteView.as_view(), name='produto_delete'),
    path('categorias/', CategoriaListView.as_view(), name='categoria_list'),
]

