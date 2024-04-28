from django.urls import path  # importando a função path do Django
from . import views

# definindo a URL desejada utilizando a função path
# criando uma URL que aponte para uma view chamada members
urlpatterns = [
    path('', views.main, name='main'),
    path('appmembers/', views.members, name='members'),
    path('appmembers/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
]

"""
'appmembers/' representa o caminho da URL que será acessado no navegador.
views.members é a view que será chamada quando essa URL for acessada.
'members' é o nome atribuído a essa URL, que pode ser usado para referenciar a URL em templates ou em outras partes do código.
"""