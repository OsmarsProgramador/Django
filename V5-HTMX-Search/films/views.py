# films/views.py
from django.http.response import HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView, View
from django.contrib.auth import get_user_model, logout
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from films.forms import RegisterForm
from films.models import Film
from django.views.generic.list import ListView

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'
    
class Login(LoginView):
    template_name = 'registration/login.html'

class CustomLogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect('login')
    
class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()  # save the user
        return super().form_valid(form)


class FilmList(LoginRequiredMixin, ListView):
    template_name = 'films.html'
    model = Film
    context_object_name = 'films'

    def get_queryset(self):
        user = self.request.user
        return user.films.all()


def check_username(request):
    username = request.POST.get('username')
    if get_user_model().objects.filter(username=username).exists():
        return HttpResponse("<div id='username-error' class='error'>This username already exists</div>")
    else:
        return HttpResponse("<div id='username-error' class='success'>This username is available</div>")

@login_required
def add_film(request):
    name = request.POST.get('filmname')
    
    # Adicionar filme
    film, created = Film.objects.get_or_create(name=name)
    
    # Adicionar o filme à lista do usuário
    request.user.films.add(film)

    # Adicionar mensagem de sucesso
    messages.success(request, f"{name} adicionado à lista de filmes")
    
    # Retornar fragmento do modelo com todos os filmes do usuário
    films = request.user.films.all()
    return render(request, 'partials/film-list.html', {'films': films, 'show_messages': True})


@require_http_methods(['DELETE'])
@login_required
def delete_film(request, pk):
    try:
        film = request.user.films.get(pk=pk)
        film.delete()
        messages.success(request, "Filme deletado com sucesso")
    except Film.DoesNotExist:
        messages.error(request, "Filme não encontrado")

    # retornar fragmento de modelo com todos os filmes do usuário
    films = request.user.films.all()
    return render(request, 'partials/film-list.html', {'films': films})


"""@login_required
def search_film(request):
    search_text = request.POST.get('search', '')
    
    # procurar todos os filmes que contenham o texto
    # excluir filmes do usuário
    userfilms = request.user.films.all()
    results = Film.objects.filter(name__icontains=search_text)
    context = {"results": results}
    # return render(request, 'partials/search-results.html', context)
    return render(request, 'partials/film-list.html', context)"""

@login_required
def search_film(request):
    search_text = request.POST.get('search', '')
    # Procurar todos os filmes que contenham o texto no campo 'name'
    # e que estão associados ao usuário atual
    # films = request.user.films.filter(name__icontains=search_text)
    
    # Procurar todos os filmes que contenham o texto
    films = Film.objects.filter(name__icontains=search_text)
    context = {"films": films}
    return render(request, 'partials/film-list.html', context)


def clear(request):
    return HttpResponse("")




