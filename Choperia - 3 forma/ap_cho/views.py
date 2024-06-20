from pyexpat.errors import messages
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from usuarios.models import Usuario

from .models import Categoria, Produto, Mesa
import json


def index(request):
    return render(request, "ap_cho/index.html")    

def home(request):
    context = {
        'status': request.GET.get('status')
    }
    if request.session.get('usuario'):  # Verifica se o usuário está autenticado        
        usuario = Usuario.objects.get(id=request.session['usuario']) 
        produto = Produto.objects.all() # traz todos os produtos do BD
        # return HttpResponse(f"Olá {usuario} Seus produto são: {produto}") 
        return render(request, 'ap_cho/home.html', context)  # Adicione o 'return' aqui
    else:
        return redirect('/auth/login/?status=2')

def cadastrar_produto(request):
    context = {
        'status': request.GET.get('status'),
        'categorias': Categoria.objects.all()
    }   
    
    return render(request, "ap_cho/produto/cadastrar_produto.html", context)

        

def valida_cadastro_produto(request):
    if request.method == 'POST':
        nome_categoria = request.POST.get('categoria')
        nome_produto = request.POST.get('nome_produto')
        descricao = request.POST.get('descricao')
        custo = request.POST.get('custo')
        venda = request.POST.get('venda')
        codigo = request.POST.get('codigo')
        estoque = request.POST.get('estoque')
        estoque_total = request.POST.get('estoque_total')
        imagem = request.FILES.get('imagem')

        # Criar a categoria se ela não existir
        categoria, created = Categoria.objects.get_or_create(nome=nome_categoria)

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
            
            # Renderizar o template parcial da tabela com os produtos atualizados
            produtos = Produto.objects.all()
            context = {
                'produtos': produtos,
            }
            
            return render(request, 'ap_cho/produto/partial_produtos_table.html', context)
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=400)
    else:
        return JsonResponse({'success': False, 'message': 'Método não permitido'}, status=405)
            
            

def criar_categoria(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        nome_categoria = data.get('nome')
        if nome_categoria:
            categoria = Categoria.objects.create(nome=nome_categoria)
            return JsonResponse({'success': True, 'categoria_id': categoria.id, 'categoria_nome': categoria.nome})
        else:
            return JsonResponse({'success': False, 'message': 'Nome da categoria é obrigatório'})
    return JsonResponse({'success': False, 'message': 'Método não permitido'})

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

    return render(request, 'ap_cho/produto/tabela_produtos.html', context)


def editar_produto(request, produto_id):
    produto = Produto.objects.get(id=produto_id)
    status = request.GET.get('status')
    context = {
        'produto_id': produto_id,
        'produto': produto,
        'status': status,
    }

    return render(request, 'ap_cho/produto/editar_produto.html', context)


def deletar_produto(request, produto_id):
    # Obtém o objeto do Produto a ser deletado
    produto = get_object_or_404(Produto, id=produto_id)
    status = request.GET.get('status')
    
    context = {
        'produto_id': produto_id,
        'produto': produto,
    }

    return render(request, 'ap_cho/produto/deletar_produto.html', context)

def deletar_produto_confirmacao(request, produto_id): # O parâmetro para o produto.id, foi enviado através do caminho da url
    # Obtém o objeto do Produto a ser deletado
    produto = get_object_or_404(Produto, id=produto_id)
    # Exclui o produto do banco de dados
    produto.delete()

    """# Obtem todos os produtos
    produto = Produto.objects.all()
    context = {
        'produtos': produto,
    }

    # Redireciona para a página de tabela de produtos após a exclusão
    return render(request, 'ap_cho/produto/tabela_produtos.html', context)"""
    return redirect('tabela_produtos')
    # return redirect('/ap_cho/produto/tabela_produtos/')

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
        # return redirect('/ap_cho/produto/tabela_produtos/')
        return redirect('tabela_produtos')
    except:
        return HttpResponse("Não foi possível realizar a edição do produto")
    
def lista_mesas(request):
    # Obtém todas as mesas do banco de dados
    mesas_aberta = Mesa.objects.filter(status='Aberta')
    mesas_fechada = Mesa.objects.filter(status='Fechada')
    context = {
        'mesas_abertas': mesas_aberta,
        'mesas_fechadas': mesas_fechada
    }
    return render(request, 'ap_cho/mesa/lista_mesas.html', context)

def cadastrar_mesa(request):
    return render(request, 'ap_cho/mesa/cadastrar_mesa.html')

def valida_cadastro_mesa(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        
        # Verificar se a mesa com o mesmo nome já existe
        if Mesa.objects.filter(nome=nome).exists():
            return JsonResponse({'success': False, 'message': 'Mesa já existe'})
        
        # Cria a nova mesa
        nova_mesa = Mesa(nome=nome, status='Fechada')
        nova_mesa.save()
        
        # Atualizar a lista de mesas
        mesas_aberta = Mesa.objects.filter(status='Aberta')
        mesas_fechada = Mesa.objects.filter(status='Fechada')
        context = {
            'mesas_abertas': mesas_aberta,
            'mesas_fechadas': mesas_fechada
        }
        
        return render(request, 'ap_cho/mesa/partial_lista_mesas.html', context)
    
    return JsonResponse({'success': False, 'message': 'Método não permitido'}, status=405)

def abrir_mesa(request, mesa_id):
    mesa = get_object_or_404(Mesa, id=mesa_id)
    mesa_numero = str(mesa.id).zfill(2)
    print(mesa_numero)
    return render(request, 'ap_cho/mesa/abrir_mesa.html', {'mesa': mesa, 'mesa_numero': mesa_numero})


def adicionar_produto(request, mesa_id):
    mesa = get_object_or_404(Mesa, id=mesa_id)
    categorias = Categoria.objects.all()
    produtos = Produto.objects.all()
    return render(request, 'ap_cho/produto/adicionar_produto.html', {'mesa': mesa, 'categorias': categorias, 'produtos': produtos})

def adicionar_item_mesa(request, mesa_id, produto_id):
    mesa = get_object_or_404(Mesa, id=mesa_id)
    produto = get_object_or_404(Produto, id=produto_id)
    quantidade = int(request.POST.get('quantidade', 1))

    if produto.estoque >= quantidade:
        produto.estoque -= quantidade
        produto.save()
        
        item_ja_existente = False
        for item in mesa.itens:
            if item['codigo'] == produto.codigo:
                item['quantidade'] += quantidade
                item_ja_existente = True
                break
        if not item_ja_existente:
            mesa.itens.append({
                'nome_produto': produto.nome_produto,
                'codigo': produto.codigo,
                'quantidade': quantidade,
                'preco_unitario': produto.venda
            })
        mesa.status = 'Aberta'
        mesa.pedido += 1
        mesa.save()
        messages.success(request, 'Produto adicionado com sucesso!')
    else:
        messages.error(request, 'Estoque insuficiente para o produto solicitado.')
    
    return redirect('abrir_mesa', mesa_id=mesa.id)

def excluir_item_mesa(request, mesa_id, item_codigo):
    mesa = get_object_or_404(Mesa, id=mesa_id)
    mesa.itens = [item for item in mesa.itens if item['codigo'] != item_codigo]
    mesa.save()
    return redirect('abrir_mesa', mesa_id=mesa.id)

def finalizar_pagamento(request, mesa_id):
    mesa = get_object_or_404(Mesa, id=mesa_id)
    mesa.itens.clear()
    mesa.status = 'Fechado'
    mesa.pedido = 0
    mesa.save()
    messages.success(request, 'Pagamento finalizado e mesa liberada para novo pedido.')
    return redirect('/ap_cho/mesa/listar_mesas/')


