from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, redirect

from usuarios.models import Usuario

from .models import Produto


def cadastrar_produto(request):    
    status = request.GET.get('status')
    return render(request, "choperia/cadastrar_produto.html", {'status': status})

        

def valida_cadastro_produto(request):
    nome_produto = request.POST.get('nome_produto')
    descricao = request.POST.get('descricao')
    custo = request.POST.get('custo')
    venda = request.POST.get('venda')
    codigo = request.POST.get('codigo')
    estoque = request.POST.get('estoque')
    estoque_total = request.POST.get('estoque_total')
    categoria = request.POST.get('categoria') 

    #categoria = Categoria.objects.get_or_create(nome=categoria_nome)  # Obtém ou cria a instância da Categoria
    print(f"Categoria: {categoria}")

    imagem = request.FILES['imagem']
    print(imagem)
    try:
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
        print('salvou')
        produto.save()
        return redirect('/choperia/cadastrar_produto/?status=0')
    except:
        # return redirect('/choperia/home/?status=1')
        return HttpResponse(f"{nome_produto} {descricao} {custo} {venda} {codigo} {estoque} {estoque_total} {imagem}")
    

def home(request):
    if request.session.get('usuario'):  # Verifica se o usuário está autenticado
        status = request.GET.get('status')
        usuario = Usuario.objects.get(id=request.session['usuario']) 
        produto = Produto.objects.all() # traz todos os produtos do BD
        # return HttpResponse(f"Olá {usuario} Seus produto são: {produto}") 
        return render(request, 'choperia/home.html', {'status': status})  # Adicione o 'return' aqui
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

    return render(request, 'choperia/tabela_produtos.html', context)


