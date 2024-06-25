# produto/urls.py
from django.urls import path
from . import views

app_name = 'produto'

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.ProdutoListView.as_view(), name='produto_list'),
]


