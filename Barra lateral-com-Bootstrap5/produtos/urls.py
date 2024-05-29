from django.urls import path
from . import views

urlpatterns = [
    path("index/", views.index, name="index"),
    path("ver_produto/", views.ver_produto, name="ver_produto"),
    path("inserir_produto/", views.inserir_produto, name="inserir_produto"),
]
