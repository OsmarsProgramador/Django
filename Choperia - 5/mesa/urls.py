# mesa/urls.py
from django.urls import path
from . import views, htmx_views

app_name = 'mesa'

urlpatterns = [
    path('', views.MesaListView.as_view(), name='list_mesa'),
    path('<int:pk>/', views.AbrirMesaView.as_view(), name='abrir_mesa'),
    path('update_user/<int:pk>/', views.UpdateUserView.as_view(), name='update_user'),
    path('gerar_comanda_pdf/<int:mesa_id>/', views.GerarComandaPDFView.as_view(), name='gerar_comanda_pdf'),
    path('excluir_item/<int:pk>/', views.ExcluirItemView.as_view(), name='excluir_item'),
    
    path('nova/', views.MesaCreateView.as_view(), name='nova_mesa'),
]


# urls exclusiva para receber requisição do htmx
htmx_urlpatterns = [
    path('adicionar_item_mesa/<int:mesa_id>/<int:produto_id>/', htmx_views.AdicionarProdutoView.as_view(), name='adicionar_item_mesa'),
]

urlpatterns += htmx_urlpatterns
