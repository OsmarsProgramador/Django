from django.shortcuts import render
from django.shortcuts import redirect

def index(request):
    return render(request, "index.html", {})

def login(request):
    return render(request, "login.html")

def contato(request):
    return render(request, "contato.html")

"""def cadastrarnovasenha(request):
    return render(request, "cadastrarnovasenha.html")

def cadastro(request):
    return render(request, "cadastro.html")

def carrinho(request):
    return render(request, "carrinho.html")

def cliente(request):
    return render(request, "cliente.html")"""
