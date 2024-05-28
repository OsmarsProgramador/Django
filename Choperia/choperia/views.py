from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, redirect

from usuarios.models import Usuario

from .models import Categoria, Produto


"""
#3 27:16
def index(request):
    lista_ultima_categoria = Categoria.objects.order_by("-data_criacao")[:5]
    template = loader.get_template("choperia/index.html")
    context = {
        "lista_ultima_categoria": lista_ultima_categoria,
    }
    return HttpResponse(template.render(context, request))"""
"""
def index(request):
    lista_ultima_categoria = Categoria.objects.order_by("-data_criacao")[:5]
    output = ", ".join([q.categoria_text for q in lista_ultima_categoria])
    return HttpResponse(output)
"""

def cadastrar(request):
    return HttpResponse("Olá Mundo. Você está no índice de pesquisas.")


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
        status = request.GET.get('status')
        usuario = Usuario.objects.get(id=request.session['usuario']) 
        produto = Produto.objects.all() # traz todos os produtos do BD
        # return HttpResponse(f"Olá {usuario} Seus produto são: {produto}") 
        return render(request, 'home.html', {'status': status})  # Adicione o 'return' aqui
    else:
        return redirect('/auth/login/?status=2')
    
def tabela_produtos(request):
    produtos = Produto.objects.all()  # Obtém todos os produtos do banco de dados
    status = request.GET.get('status')
    
    """ Criando um dicionário chamado context que será utilizado como contexto ao renderizar um template em uma aplicação Django:

    context = { ... }: Aqui você está criando um novo dicionário em Python chamado context que será passado como contexto para o template durante a renderização.

    'produtos': produtos: Nesta linha, você está adicionando uma chave 'produtos' ao dicionário context.

    'produtos' é a chave que será usada para acessar a lista de produtos no template.
    produtos é a variável que contém a lista de objetos de produto obtidos da consulta ao banco de dados por meio de Produto.objects.all(). 
    Essa variável será associada à chave 'produtos' no contexto.
    'status': status: Nesta linha, você está adicionando outra chave 'status' ao dicionário context.

    'status' é a chave que será usada para acessar o valor do status no template.
    status é a variável que contém o valor do status, que foi obtido através de request.GET.get('status'). 
    Essa variável será associada à chave 'status' no contexto.

    Resumindo, ao criar o dicionário context, você está reunindo as informações necessárias que deseja 
    disponibilizar para o template 'tabela_produtos.html'. Dessa forma, no template, você poderá acessar 
    os produtos através da chave 'produtos' e o status através da chave 'status' para exibir 
    e manipular esses dados conforme necessário na interface do usuário."""
    context = {
        'produtos': produtos,
        'status': status,
    }

    return render(request, 'tabela_produtos.html', context)


