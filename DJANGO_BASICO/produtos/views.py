from django.shortcuts import render
from django.http import HttpResponse
from . models import Pessoas, Produtos


def ver_produto(request):
    if request.method == "GET":
        nome = 'Osmar'
        return render(request, "ver_produto.html", {'nome': nome})
    elif request.method == "POST":
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
        pessoa = Pessoas(nome=nome, idade=idade)

        # pessoa = Pessoas.objects.all() # traz todas as pessoas do banco
        # pessoa = Pessoas.objects.filter(nome=nome) # traz todas as pessoas do banco que tem o nome igual a nome

        pessoa.save()
        return HttpResponse(f'Meu nome é {nome} e minha idade é {idade} anos')

def inserir_produto(request):
    return render(request, "inserir_produto.html")
    # return HttpResponse('Estou no inserir produto!')