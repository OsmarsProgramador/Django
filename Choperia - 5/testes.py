def gerar_comanda_pdf(request, mesa_id):
    mesa = get_object_or_404(Mesa, id=mesa_id)
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="comanda_{mesa.nome}.pdf"'
    
    p = canvas.Canvas(response, pagesize=letter)
    p.drawString(100, 750, f'Comanda da Mesa: {mesa.nome}')
    p.drawString(100, 730, f'Pedido: {mesa.pedido}')
    p.drawString(100, 710, 'Itens:')

    y = 690
    for item in mesa.itens:
        p.drawString(100, y, f'{item["nome_produto"]} - {item["quantidade"]}x - R${item["preco_unitario"]}')
        y -= 20

    p.showPage()
    p.save()
    return response

def cadastrar_produto(request):
    context = {
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

        # Verificar se a categoria existe e criar se não existir
        if Categoria.objects.filter(nome=nome_categoria).exists():
            categoria = Categoria.objects.get(nome=nome_categoria)
        else:
            categoria = Categoria.objects.create(nome=nome_categoria)

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
            
            return redirect('tabela_produtos')
            # return render(request, 'ap_cho/produto/partial_produtos_table.html', context)
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
    produto = get_object_or_404(Produto, id=produto_id)
    if request.method == "POST":
        produto.nome_produto = request.POST.get('nome_produto')
        produto.descricao = request.POST.get('descricao')
        produto.custo = request.POST.get('custo')
        produto.venda = request.POST.get('venda')
        produto.codigo = request.POST.get('codigo')
        produto.estoque = request.POST.get('estoque')
        produto.estoque_total = request.POST.get('estoque_total')
        produto.categoria = request.POST.get('categoria')
        
        if 'imagem' in request.FILES:
            produto.imagem = request.FILES['imagem']

        try:
            produto.save()
            return redirect('tabela_produtos')
        except:
            return HttpResponse("Não foi possível realizar a edição do produto")
    context = {
        'produto_id': produto_id,
        'produto': produto,
    }
    return render(request, 'ap_cho/produto/editar_produto.html', context)

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

def deletar_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
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
    
def lista_mesas(request):
    # Obtém todas as mesas do banco de dados
    mesas_aberta = Mesa.objects.filter(status='Aberta')
    mesas_fechada = Mesa.objects.filter(status='Fechada')
    context = {
        'mesas_abertas': mesas_aberta,
        'mesas_fechadas': mesas_fechada
    }
    return render(request, 'ap_cho/mesa/lista_mesas.html', context)

def abrir_mesa(request, mesa_id):
    try:
        mesa = Mesa.objects.get(id=mesa_id)
    except Mesa.DoesNotExist:
        return HttpResponse("Mesa não encontrada", status=404)

    usuario_id = request.session.get('usuario')
    if not usuario_id:
        return HttpResponse("Usuário não autenticado", status=401)

    try:
        usuario = Usuario.objects.get(id=usuario_id)
    except Usuario.DoesNotExist:
        return HttpResponse("Usuário não encontrado", status=404)

    usuarios = Usuario.objects.all()  # Obtenha todos os usuários para o dropdown
    produtos = Produto.objects.all()  # Obtenha todos os produtos para o modal

    context = {
        'mesa': mesa,
        'usuario': usuario,
        'usuarios': usuarios,
        'produtos': produtos,
    }
    return render(request, 'ap_cho/mesa/abrir_mesa.html', context)

def update_user(request, mesa_id):
    if request.method == 'POST':
        usuario_id = request.POST.get('usuario')
        try:
            usuario = Usuario.objects.get(id=usuario_id)
            request.session['usuario'] = usuario.id
        except Usuario.DoesNotExist:
            return HttpResponse("Usuário não encontrado", status=404)
        
        return redirect('abrir_mesa', mesa_id=mesa_id)

    return HttpResponse("Método não permitido", status=405)

"""def adicionar_produto(request, mesa_id):
    mesa = get_object_or_404(Mesa, id=mesa_id)
    categorias = Categoria.objects.all()
    produtos = Produto.objects.all()
    return render(request, 'ap_cho/produto/adicionar_produto.html', {'mesa': mesa, 'categorias': categorias, 'produtos': produtos})
"""
from decimal import Decimal
from django.core.exceptions import ValidationError

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
                'categoria': produto.categoria.nome,
                'custo': float(produto.custo),
                'venda': float(produto.venda),
                'codigo': produto.codigo,
                'estoque': produto.estoque,
                'estoque_total': produto.estoque_total,
                'descricao': produto.descricao,
                'imagem': produto.imagem.url if produto.imagem else '',
                'quantidade': quantidade,
                'preco_unitario': float(produto.venda)  # Convertendo Decimal para float
            })

        mesa.status = 'Aberta'

        if mesa.pedido == 0:
            ultimo_pedido = Mesa.objects.filter().order_by('-pedido').first()
            if ultimo_pedido:
                mesa.pedido = ultimo_pedido.pedido + 1
            else:
                mesa.pedido = 1

        mesa.save()
        return redirect('abrir_mesa', mesa_id=mesa.id)
    else:
        return HttpResponse('Estoque insuficiente para o produto solicitado.')
    
def excluir_item_mesa(request, mesa_id, item_codigo):
    mesa = get_object_or_404(Mesa, id=mesa_id)
    quantidade = int(request.POST.get('quantidade', 1))
    
    item_removido = False
    for item in mesa.itens:
        if item['codigo'] == item_codigo:
            if item['quantidade'] > 0:
                item['quantidade'] -= quantidade
            else:
                mesa.itens.remove(item)
            item_removido = True
            break
    
    if item_removido:
        # Atualizar o estoque do produto correspondente
        try: # tenta adicionar produto ao estoque
            produto = Produto.objects.get(codigo=item_codigo)
            produto.estoque += quantidade
            produto.save()
        except Produto.DoesNotExist:
            pass  # Não fazer nada se o produto não existir

        # Verifica se a quantidade de itens é menor ou igual a zero
        total_itens = sum(item['quantidade'] for item in mesa.itens)

        # Aplica o estado inicial de cadastro
        if total_itens <= 0:
            mesa.itens = []
            mesa.status = 'Fechada'
            mesa.pedido = 0
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


# resgata usuário admin
@login_required
def get_user_info_adm(request):
    user = request.user
    user_info = {
        'username': user.username,
        'email': user.email,
        # Adicione outras informações necessárias
    }
    return JsonResponse(user_info)

#Resgata usuarios do app
@login_required
def get_user_info(request):
    user = request.user
    usuario = Usuario.objects.get(user=user)
    user_info = {
        'username': usuario.nome,
        'email': usuario.email,
        # Adicione mais campos conforme necessário
    }
    return JsonResponse(user_info)



<!-- usuarios/templates/usuarios/login.html -->
{% extends 'base.html' %}

{% load static %}

{% block 'titulo' %}Login{% endblock %}

{% block 'content' %}

  <div class="container">
      <br>
      {% if status == '1' %}
      <div class="alert alert-danger" role="alert">
          Email ou senha inválidos
        </div>
        
      {% endif %}

      {% if status == '2' %}
      <div class="alert alert-danger" role="alert">
          Faça login antes de tentar acessar o sistema
        </div>
        
      {% endif %}
      <div class="row">

          <div class="col-md-3">

          </div>

          <div class="col-md">
            <h1>Login</h1>
            <hr>

            <form method="POST" action="{% url 'usuarios:valida_login' %}">{% csrf_token %}
                  <label>Email</label>
                  <input name="email" class="form-control" type="text" placeholder="Email...">
                  <br>
                  <label>Senha</label>
                  <input name="senha" class="form-control" type="password" placeholder="Senha...">
                  <br>
                  <input class="btn btn-info btn-lg" type="submit" value="Enviar">
                  <a href="{% url 'usuarios:cadastro' %}" class="btn btn-warning btn-lg">Cadastro</a>


            </form>
          </div>

          <div class="col-md-3">

          </div>


      </div>

  </div>

{% endblock 'content' %}


            


