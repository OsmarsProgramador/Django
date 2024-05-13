from django.urls import path
from .views import cadastrar_produto

from . import views

urlpatterns = [
    # ex: /choperia/
    path("", views.index, name="index"),
    # ex: /choperia/5/
    path("<int:categoria_id>/", views.detail, name="detail"),
    # ex: /choperia/5/results/
    path("<int:categoria_id>/results/", views.results, name="results"),
    # ex: /choperia/5/vote/
    path("<int:categoria_id>/vote/", views.vote, name="vote"),
    path('home/', views.home, name = 'home'),
    path('cadastrar_produto/', cadastrar_produto, name='cadastrar_produto'),
]