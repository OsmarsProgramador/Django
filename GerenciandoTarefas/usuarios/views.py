# usuarios/views.py
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from .forms import RegistrarUsuarioForm

def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistrarUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('listar_tarefas')
    else:
        form = RegistrarUsuarioForm()
    return render(request, 'usuarios/registrar_usuario.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'usuarios/login.html'

def logout_view(request):
    logout(request)
    return redirect('login')

