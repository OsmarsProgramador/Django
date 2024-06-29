# produto/urls.py
from django.urls import path
from . import views

app_name = 'produto'

urlpatterns = [
    path('list/', views.ProdutoListView.as_view(), name='produto_list'),
    path('import_xlsx/', views.import_xlsx, name='import_xlsx'),
]


