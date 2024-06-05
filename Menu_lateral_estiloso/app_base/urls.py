from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home", views.home, name="home"),
    path('profile/', views.profile, name='profile'),
    path('products/', views.products, name='products'),
    path('tables/', views.tables, name='tables'),
    path('reports/', views.reports, name='reports'),
    path('logout/', views.logout, name='logout'),
]

