from django.urls import path
from . import views
# from .views import cadastrar_produto


urlpatterns = [
    path('cadastrar/', views.cadastrar, name = 'cadastrar'),
    path('home/', views.home, name = 'home'),
    # path('cadastrar_produto/', cadastrar_produto, name='cadastrar_produto'),
]