# produto/urls.py
from django.urls import path
from . import views, htmx_views

# urls exclusiva para receber requisição do usuario
urlpatterns = [
    path('list_produto/', views.ListProdutoView.as_view(), name='list_produto'),
]

# urls exclusiva para receber requisição do htmx
htmx_urlpatterns = [
    path('check_produto/', htmx_views.CheckProdutoView.as_view(), name='check_produto'),
    path('save_produto/', htmx_views.SaveProdutoView.as_view(), name='save_produto'),
    path('create_produto/', htmx_views.CreateProdutoView.as_view(), name='create_produto'),
    path('edit_produto/<int:id>/', htmx_views.EditProdutoView.as_view(), name='edit_produto'),
    path('update_produto/<int:id>/', htmx_views.UpdateProdutoView.as_view(), name='update_produto'),
    path('delete_produto/<int:id>/', htmx_views.DeleteProdutoView.as_view(), name='delete_produto'),
]

urlpatterns += htmx_urlpatterns

