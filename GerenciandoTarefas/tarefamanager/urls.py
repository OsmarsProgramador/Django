# tarefamanager/urls.py
from django.contrib import admin
from django.urls import path
from tarefas import views as tarefa_views
from usuarios import views as usuario_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tarefas/', tarefa_views.listar_tarefas, name='listar_tarefas'),
    path('tarefas/criar/', tarefa_views.criar_tarefa, name='criar_tarefa'),
    path('tarefas/editar/<int:tarefa_id>/', tarefa_views.editar_tarefa, name='editar_tarefa'),
    path('login/', usuario_views.CustomLoginView.as_view(), name='login'),
    path('logout/', usuario_views.logout_view, name='logout'),
    path('registrar/', usuario_views.registrar_usuario, name='registrar_usuario'),
]


