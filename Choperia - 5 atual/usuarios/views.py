# usuarios/views.py

from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Usuario
from hashlib import sha256

from django.views import View
from django.views.generic import TemplateView
from django.http import QueryDict


class LoginView(TemplateView):
    # model = Usuario
    template_name = "usuarios/login.html"

    # para o caso de o usuario estive logado
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('core:index')
        return super().dispatch(request, *args, **kwargs)
    
    print("Entrei na classe login")
    def get_context_data(self, **kwargs):
        print("Renderizando para login")
        context = super().get_context_data(**kwargs)
        context['status'] = self.request.GET.get('status')
        return context

class ValidaLoginView(View):
    def post(self, request):
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        print(f"Email: {email} Senha: {senha}")

        senha_hashed = sha256(senha.encode()).hexdigest()
        usuario = Usuario.objects.filter(email=email).filter(senha=senha_hashed)

        query_string = QueryDict(mutable=True)

        if len(usuario) == 0:
            print("Usuário não encontrado ou senha incorreta")
            query_string['status'] = 1
            url = f"{reverse('usuarios:login')}?{query_string.urlencode()}"
            return redirect(url)
        elif len(usuario) > 0:
            request.session['usuario'] = usuario[0].id
            print("Usuário autenticado com sucesso")
            query_string['status'] = 0
            url = f"{reverse('produto:produto_list')}?{query_string.urlencode()}"
            return redirect(url)




class CadastroView(TemplateView):
    model = Usuario
    template_name = "usuarios/cadastro.html"
    context_object_name = 'usuarioss'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status'] = self.request.GET.get('status')
        return context

class ValidaCadastroView(View):
    def post(self, request):
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        usuario = Usuario.objects.filter(email=email).first()

        query_string = QueryDict(mutable=True)

        if not nome.strip() or not email.strip():
            query_string['status'] = 1
            url = f"{reverse('usuarios:cadastro')}?{query_string.urlencode()}"
            return redirect(url)
        if len(senha) < 8:
            query_string['status'] = 2
            url = f"{reverse('usuarios:cadastro')}?{query_string.urlencode()}"
            return redirect(url)
        if usuario:
            query_string['status'] = 3
            url = f"{reverse('usuarios:cadastro')}?{query_string.urlencode()}"
            return redirect(url)

        try:
            senha_hashed = sha256(senha.encode()).hexdigest()
            usuario = Usuario(nome=nome, email=email, senha=senha_hashed)
            usuario.save()
            query_string['status'] = 0
            url = f"{reverse('usuarios:cadastro')}?{query_string.urlencode()}"
            return redirect(url)
        except:
            query_string['status'] = 4
            url = f"{reverse('usuarios:cadastro')}?{query_string.urlencode()}"
            return redirect(url)

class SairView(View):
    def get(self, request):
        request.session.flush() # Desloga e limpa completamente
        return redirect('usuarios:login')
       
    

