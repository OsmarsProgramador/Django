# tarefas/views.py
from django.shortcuts import render, redirect
from .models import Tarefa
from .forms import TarefaForm

def listar_tarefas(request):
    tarefas = Tarefa.objects.filter(usuario=request.user)
    return render(request, 'tarefas/listar_tarefas.html', {'tarefas': tarefas})

def criar_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            tarefa = form.save(commit=False)
            tarefa.usuario = request.user
            tarefa.save()
            return redirect('listar_tarefas')
    else:
        form = TarefaForm()
    return render(request, 'tarefas/criar_tarefa.html', {'form': form})

def editar_tarefa(request, tarefa_id):
    tarefa = Tarefa.objects.get(id=tarefa_id, usuario=request.user)
    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect('listar_tarefas')
    else:
        form = TarefaForm(instance=tarefa)
    return render(request, 'tarefas/editar_tarefa.html', {'form': form})