from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.shortcuts import render

from .models import Categoria, Produto


def index(request):
    latest_categoria_list = Categoria.objects.order_by("-data_pub")[:5]
    template = loader.get_template("choperia/detail.html")
    context = {
        "latest_categoria_list": latest_categoria_list,
    }
    return HttpResponse(template.render(context, request))
"""
def index(request):
    latest_categoria_list = Categoria.objects.order_by("-data_pub")[:5]
    output = ", ".join([q.categoria_text for q in latest_categoria_list])
    return HttpResponse(output)

def index(request):
    return HttpResponse("Olá Mundo. Você está no índice de pesquisas.")"""

def detail(request, categoria_id):
    return HttpResponse("Você está vendo a pergunta %s." % categoria_id)


def results(request, categoria_id):
    response = "Você está vendo os resultados da pergunta %s."
    return HttpResponse(response % categoria_id)


def vote(request, categoria_id):
    return HttpResponse("Você está votando na pergunta %s." % categoria_id)

def cadastrar_produto(request):
    if request.method == 'POST':
        nome_produto = request.POST.get('nome_produto')
        descricao = request.POST.get('descricao')
        custo = request.POST.get('custo')
        venda = request.POST.get('venda')
        codigo = request.POST.get('codigo')
        estoque = request.POST.get('estoque')
        estoque_total = request.POST.get('estoque_total')
        categoria = request.POST.get('categoria')
        imagem = request.FILES['imagem']

        produto = Produto(
            nome_produto=nome_produto,
            descricao=descricao,
            custo=custo,
            venda=venda,
            codigo=codigo,
            estoque=estoque,
            estoque_total=estoque_total,
            categoria=categoria,
            imagem=imagem
        )
        produto.save()

        return HttpResponseRedirect('/sucesso/')  # Redireciona para uma página de sucesso
    return render(request, 'cadastrar_produto.html')