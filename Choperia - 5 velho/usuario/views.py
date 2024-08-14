# usuario/views.py
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

# usuario: osmarnegao
# senha: 2324*-9+
"""
O uso do LoginRequiredMixin tem como objetivo garantir que apenas usuários autenticados possam acessar essa view.
Caso o usuário não esteja autenticado, o Django irá redirecionar o usuário para a página de login especificada.

Quando um usuário não está autenticada, a classe de redirecionamento, é aquela para 
o redirecionamento é configurado no arquivo settings.py, na variável LOGIN_URL. 
Essa variável define a URL para a qual o usuário será redirecionado quando uma view que 
requer autenticação for acessada por um usuário não autenticado.
configuração no settings.py: LOGIN_URL = 'usuario:login'

A classe de redirecionamento seria a UserLoginView

"""


class UserLoginView(View):
    def get(self, request):
        return render(request, 'usuario/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('core:index')
        else:
            return render(request, 'usuario/login.html', {'error': 'Invalid credentials'})

class UserLogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect('usuario:login')

class UserSignupView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'usuario/cadastro.html', {'form': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuario:login')
        return render(request, 'usuario/cadastro.html', {'form': form})

