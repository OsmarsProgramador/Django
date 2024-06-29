# usuarios/urls.py
from django.urls import path
from . import views

app_name = 'usuarios'
# Cada caminho é uma chamada para uma função em views.py

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("cadastro/", views.CadastroView.as_view(), name="cadastro"),   
    path("valida_cadastro/", views.ValidaCadastroView.as_view(), name="valida_cadastro"), 
    path("valida_login/", views.ValidaLoginView.as_view(), name="valida_login"),    
    path("sair/", views.SairView.as_view(), name="sair"), 
]

