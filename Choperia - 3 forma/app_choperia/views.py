from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from usuarios.models import Usuario

from .models import Produto


def index(request):
    return render(request, "app_choperia/index.html")    

def home(request):
    context = {
        'status': request.GET.get('status')
    }
    if request.session.get('usuario'):  # Verifica se o usuário está autenticado        
        usuario = Usuario.objects.get(id=request.session['usuario']) 
        produto = Produto.objects.all() # traz todos os produtos do BD
        # return HttpResponse(f"Olá {usuario} Seus produto são: {produto}") 
        return render(request, 'app_choperia/home.html', context)  # Adicione o 'return' aqui
    else:
        return redirect('/auth/login/?status=2')

def cadastrar_produto(request):
    context = {
        'sidebar_expanded': request.session.get('sidebar.expand', False),
        'status': request.GET.get('status')
    }   
    
    return render(request, "app_choperia/cadastrar_produto.html", context)

        

def valida_cadastro_produto(request):
    nome_produto = request.POST.get('nome_produto')
    descricao = request.POST.get('descricao')
    custo = request.POST.get('custo')
    venda = request.POST.get('venda')
    codigo = request.POST.get('codigo')
    estoque = request.POST.get('estoque')
    estoque_total = request.POST.get('estoque_total')
    categoria = request.POST.get('categoria') 

    imagem = request.FILES['imagem']
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
        produto.save()
        return redirect('/app_choperia/cadastrar_produto/?status=0')
    except:
        # return redirect('/choperia/home/?status=1')
        return HttpResponse(f"Não foi possivel realizar o cadastro")
    
def tabela_produtos(request):
    produtos = Produto.objects.all()  # Obtém todos os produtos do banco de dados
    status = request.GET.get('status')
    # total_reposicao_estoque = 0
    
    total_estoque = sum(produto.estoque for produto in produtos)
    total_valor_estoque = sum(produto.venda for produto in produtos)
    total_custo_estoque = sum(produto.custo for produto in produtos)
    total_estoque_zerado = sum(1 for produto in produtos if produto.estoque == 0)
    total_reposicao_estoque = sum(1 for produto in produtos if produto.estoque < produto.estoque_total)
    total_valor_estoque_total = sum(produto.estoque_total for produto in produtos)


    """ Criando um dicionário chamado context que será utilizado como contexto ao renderizar um template em uma aplicação Django: """
    context = {
        'produtos': produtos,
        'total_estoque': total_estoque,
        'total_valor_estoque': total_valor_estoque,
        'total_custo_estoque': total_custo_estoque,
        'total_reposicao_estoque': total_reposicao_estoque,
        'total_estoque_zerado': total_estoque_zerado,
        'total_valor_estoque_total': total_valor_estoque_total,
    }

    return render(request, 'app_choperia/tabela_produtos.html', context)


def editar_produto(request, produto_id):
    produto = Produto.objects.get(id=produto_id)
    status = request.GET.get('status')
    context = {
        'produto_id': produto_id,
        'produto': produto,
        'status': status,
    }

    return render(request, 'app_choperia/editar_produto.html', context)


def deletar_produto(request, produto_id):
    # Obtém o objeto do Produto a ser deletado
    produto = get_object_or_404(Produto, id=produto_id)
    status = request.GET.get('status')
    
    context = {
        'produto_id': produto_id,
        'produto': produto,
    }

    return render(request, 'app_choperia/deletar_produto.html', context)

def deletar_produto_confirmacao(request, produto_id): # O parâmetro para o produto.id, foi enviado através do caminho da url
    # Obtém o objeto do Produto a ser deletado
    produto = get_object_or_404(Produto, id=produto_id)
    print(produto_id)
    # Exclui o produto do banco de dados
    produto.delete()

    # Obtem todos os produtos
    produto = Produto.objects.all()
    context = {
        'produtos': produto,
    }

    # Redireciona para a página de tabela de produtos após a exclusão
    return render(request, 'app_choperia/tabela_produtos.html', context)

def valida_edicao_produto(request, produto_id):
    produto = Produto.objects.get(id=produto_id)  # Obtenha o produto existente a ser editado

    # Atualize os campos do produto com os novos valores fornecidos
    produto.nome_produto = request.POST.get('nome_produto')
    produto.descricao = request.POST.get('descricao')
    produto.custo = request.POST.get('custo')
    produto.venda = request.POST.get('venda')
    produto.codigo = request.POST.get('codigo')
    produto.estoque = request.POST.get('estoque')
    produto.estoque_total = request.POST.get('estoque_total')
    produto.categoria = request.POST.get('categoria')
    
    # Verifique se uma nova imagem foi enviada
    if 'imagem' in request.FILES:
        produto.imagem = request.FILES['imagem']

    try:
        produto.save()  # Salve as alterações no banco de dados
        return redirect('/app_choperia/tabela_produtos/')
    except:
        return HttpResponse("Não foi possível realizar a edição do produto")
