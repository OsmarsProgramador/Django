# mesa/urls.py
from django.urls import path
from .views import MesaListView, MesaDetailView

app_name = 'mesa'

urlpatterns = [
    path('', MesaListView.as_view(), name='mesa_list'),
    path('<int:pk>/', MesaDetailView.as_view(), name='mesa_detail'),
]

