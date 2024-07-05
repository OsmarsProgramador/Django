# mesa/urls.py
from django.urls import path
from .views import MesaListView, AbrirMesaView, UpdateUserView, GerarComandaPDFView, ExcluirItemView, AdicionarProdutoView

app_name = 'mesa'

urlpatterns = [
    path('', MesaListView.as_view(), name='mesa_list'),
    path('<int:pk>/', AbrirMesaView.as_view(), name='abrir_mesa'),
    path('update_user/<int:pk>/', UpdateUserView.as_view(), name='update_user'),
    path('gerar_comanda_pdf/<int:pk>/', GerarComandaPDFView.as_view(), name='gerar_comanda_pdf'),
    path('excluir_item/<int:pk>/', ExcluirItemView.as_view(), name='excluir_item'),
    path('adicionar_item_mesa/<int:mesa_id>/<int:produto_id>/', AdicionarProdutoView.as_view(), name='adicionar_item_mesa'),
]




