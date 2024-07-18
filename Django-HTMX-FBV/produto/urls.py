# produto/urls.py
from django.urls import path
from . import views, htmx_views

# urls exclusiva para receber requisição do usuario
urlpatterns = [
    path('list_produto/', views.list_produto, name='list_produto'),
]

# urls exclusiva para receber requisição do htmx
htmx_urlpatterns = [
    path('check_produto/', htmx_views.check_produto, name='check_produto'),
    path('save_produto/', htmx_views.save_produto, name='save_produto'),
    path('delete_produto/<int:id>', htmx_views.delete_produto, name='delete_produto'),
]

urlpatterns += htmx_urlpatterns

