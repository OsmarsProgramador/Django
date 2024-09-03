# usuario/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .forms import UserForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'usuario/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'usuario/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def index(request):
    if not request.user.is_superuser:
        return render(request, 'index.html')
    return redirect('admin:index')

def usuario_list(request):
    usuarios = User.objects.all()
    return render(request, 'usuario/usuario_list.html', {'usuarios': usuarios})

def usuario_create(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuario:usuario_list')
    else:
        form = UserCreationForm()
    return render(request, 'usuario/usuario_form.html', {'form': form})

def usuario_update(request, pk):
    usuario = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('usuario:usuario_list')
    else:
        form = UserForm(instance=usuario)
    return render(request, 'usuario/usuario_form.html', {'form': form})

def usuario_delete(request, pk):
    usuario = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        usuario.delete()
        return redirect('usuario:usuario_list')
    return render(request, 'usuario/usuario_confirm_delete.html', {'usuario': usuario})

