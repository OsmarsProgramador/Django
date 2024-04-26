from django.urls import path  # importando a função path do Django
from . import views

# definindo a URL desejada utilizando a função path
# criando uma URL que aponte para uma view chamada members
urlpatterns = [
    path('appmembers/', views.members, name='members'),
]
