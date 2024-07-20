

# produto/urls.py

from django.urls import path
from . import views, htmx_views

app_name = 'produto'

urlpatterns = [
    path('', views.ProdutoListView.as_view(), name='produto_list'),
    path('categorias/', views.CategoriaListView.as_view(), name='categoria_list'),
    
]

# urls exclusiva para receber requisição do htmx
htmx_urlpatterns = [
    path('check_produto/', htmx_views.CheckProdutoView.as_view(), name='check_produto'),
    path('save_produto/', htmx_views.SaveProdutoView.as_view(), name='save_produto'),
    path('create_produto/', htmx_views.CreateProdutoView.as_view(), name='create_produto'),
    path('edit_produto/<int:id>/', htmx_views.EditProdutoView.as_view(), name='edit_produto'),
    path('update_produto/<int:id>/', htmx_views.UpdateProdutoView.as_view(), name='update_produto'),
    path('delete_produto/<int:id>/', htmx_views.DeleteProdutoView.as_view(), name='delete_produto'),
    path('add_categoria_modal/', htmx_views.AddCategoriaModalView.as_view(), name='add_categoria_modal'),
]

urlpatterns += htmx_urlpatterns


