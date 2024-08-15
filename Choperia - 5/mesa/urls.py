# mesa/urls.py
from django.urls import path
from . import views, htmx_views

app_name = 'mesa'

urlpatterns = [
    path('', views.MesaListView.as_view(), name='list_mesa'),
    path('<int:id_mesa>/', views.AbrirMesaView.as_view(), name='abrir_mesa'),
    path('update_user/<int:pk>/', views.UpdateUserView.as_view(), name='update_user'),
    path('gerar_comanda_pdf/<int:mesa_id>/', views.GerarComandaPDFView.as_view(), name='gerar_comanda_pdf'),
    path('excluir_item/<int:pk>/', views.ExcluirItemView.as_view(), name='excluir_item'),
]


# urls exclusiva para receber requisição do htmx
htmx_urlpatterns = [
    path('adicionar_item/<int:mesa_id>/', htmx_views.adicionar_item, name='adicionar_item'),
    path('adicionar_item/<int:mesa_id>/<int:produto_id>/', htmx_views.AdicionarItemView.as_view(), name='adicionar_item'),
    path('nova/', htmx_views.MesaCreateView.as_view(), name='nova_mesa'),
]

urlpatterns += htmx_urlpatterns

