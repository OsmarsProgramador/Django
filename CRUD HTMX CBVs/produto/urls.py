# produto/urls.py
from django.urls import path
from . import views, htmx_views

app_name = 'produto'  # namespace está definido aqui

# urls exclusiva para receber requisição do usuario
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('list_produto/', views.ListProdutoView.as_view(), name='list_produto'),
    path('categorias/', views.CategoriaListView.as_view(), name='list_categoria'),
]

# urls exclusiva para receber requisição do htmx
htmx_urlpatterns = [
    path('check_produto/', htmx_views.CheckProdutoView.as_view(), name='check_produto'),
    path('check_categoria/', htmx_views.CheckCategoriaView.as_view(), name='check_categoria'),
    path('save_produto/', htmx_views.SaveProdutoView.as_view(), name='save_produto'),
    path('create_produto/', htmx_views.CreateProdutoView.as_view(), name='create_produto'),    
    path('criar_categoria_modal/', htmx_views.AddCategoriaModalView.as_view(), name='criar_categoria_modal'),    
    path('delete_produto/<int:id>/', htmx_views.DeleteProdutoView.as_view(), name='delete_produto'),
    path('edit_produto/<int:id>/', htmx_views.EditProdutoView.as_view(), name='edit_produto'),
    path('update_produto/', htmx_views.UpdateProdutoView.as_view(), name='update_produto'),

]

urlpatterns += htmx_urlpatterns


