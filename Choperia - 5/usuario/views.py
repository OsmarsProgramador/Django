# usuario/views.py
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

#usuario: osmarnegao
# senha: 2324*-9+
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
        form = UserCreationForm()
        return render(request, 'usuario/cadastro.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuario:login')
        return render(request, 'usuario/cadastro.html', {'form': form})


