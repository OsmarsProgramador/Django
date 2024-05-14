from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, redirect

from usuarios.models import Usuario

from .models import Categoria, Produto


def index(request):
    lista_ultima_categoria = Categoria.objects.order_by("-data_criacao")[:5]
    template = loader.get_template("choperia/formulario.html")
    context = {
        "lista_ultima_categoria": lista_ultima_categoria,
    }
    return HttpResponse(template.render(context, request))
"""
def index(request):
    lista_ultima_categoria = Categoria.objects.order_by("-data_criacao")[:5]
    output = ", ".join([q.categoria_text for q in lista_ultima_categoria])
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
        categoria_nome = request.POST.get('categoria')  # Obtém o nome da categoria do formulário

        categoria, created = Categoria.objects.get_or_create(nome=categoria_nome)  # Obtém ou cria a instância da Categoria

        imagem = request.FILES['imagem']

        produto = Produto(
            nome_produto=nome_produto,
            descricao=descricao,
            custo=custo,
            venda=venda,
            codigo=codigo,
            estoque=estoque,
            estoque_total=estoque_total,
            categoria=categoria,  # Atribui a instância da Categoria ao campo categoria
            imagem=imagem
        )
        produto.save()

        return HttpResponseRedirect('/sucesso/')  # Redireciona para uma página de sucesso
    return render(request, 'cadastrar_produto.html')

def home(request):
    if request.session.get('usuario'):  
        usuario = Usuario.objects.get(id = request.session['usuario'])
        
    return redirect('/auth/login/?status=2')
