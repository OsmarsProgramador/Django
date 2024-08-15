# mesa/htmx_views.py
from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from .models import Mesa
from .forms import MesaForm
from produto.models import Produto

from .forms import AdicionarItemForm

def adicionar_item(request, mesa_id):
    mesa = get_object_or_404(Mesa, id=mesa_id)

    if request.method == 'POST':
        produto_id = request.POST.get('produto_id')
        quantidade = int(request.POST.get('quantidade', 1))

        produto = get_object_or_404(Produto, id=produto_id)

        if produto.estoque >= quantidade:
            produto.estoque -= quantidade
            produto.save()

            encontrou = False
            for item in mesa.itens:
                if item['codigo'] == produto.codigo:
                    item['quantidade'] += quantidade
                    encontrou = True
                    break

            if not encontrou:
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
                    'preco_unitario': float(produto.venda)
                })

            mesa.status = 'Aberta'
            if mesa.pedido == 0:
                ultimo_pedido = Mesa.objects.order_by('-pedido').first()
                mesa.pedido = (ultimo_pedido.pedido + 1) if ultimo_pedido else 1
            mesa.save()

    return redirect('mesa:abrir_mesa', mesa_id=mesa_id)

""" implementar a lógica para adicionar produtos à mesa, considerando a manipulação do estoque e a atualização da lista de itens da mesa. """   
class AdicionarItemView(View):
    def get(self, request, mesa_id):
        mesa = get_object_or_404(Mesa, pk=mesa_id)
        produtos = Produto.objects.all()  # Obtém todos os produtos
        return render(request, 'mesa/adicionar_item.html', {'mesa': mesa, 'produtos': produtos})
       

    def post(self, request, mesa_id, produto_id):
        mesa = get_object_or_404(Mesa, pk=mesa_id)
        produto = get_object_or_404(Produto, pk=produto_id)
        quantidade = int(request.POST.get('quantidade', 1))

        if produto.estoque >= quantidade:
            produto.estoque -= quantidade
            produto.save()

            encontrou = False
            for item in mesa.itens:
                if item['codigo'] == produto.codigo:
                    item['quantidade'] += quantidade
                    encontrou = True
                    break

            if not encontrou:
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
                    'preco_unitario': float(produto.venda)
                })

            mesa.status = 'Aberta'

            if mesa.pedido == 0:
                ultimo_pedido = Mesa.objects.order_by('-pedido').first()
                mesa.pedido = (ultimo_pedido.pedido + 1) if ultimo_pedido else 1

            mesa.save()

            return redirect('mesa:abrir_mesa', id_mesa=mesa.id)
        else:
            return render(request, 'mesa/adicionar_item.html', {
                'mesa': mesa,
                'produtos': Produto.objects.all(),  # Recarregar os produtos para exibir a lista novamente
                'error': 'Estoque insuficiente'
            })

class AdicionarProdutoView(View):
    def post(self, request, mesa_id, produto_id):
        # Obter a mesa e o produto correspondentes
        mesa = get_object_or_404(Mesa, pk=mesa_id)
        produto = get_object_or_404(Produto, pk=produto_id)
        
        # Obter a quantidade de produtos a serem adicionados
        quantidade = int(request.POST.get('quantidade', 1))

        # Verificar se o estoque é suficiente
        if produto.estoque >= quantidade:
            # Atualizar o estoque do produto
            produto.estoque -= quantidade
            produto.save()

            # Adicionar ou atualizar o item na mesa
            encontrou = False
            for item in mesa.itens:
                if item['codigo'] == produto.codigo:
                    item['quantidade'] += quantidade
                    encontrou = True
                    break
            
            if not encontrou:
                # Adicionar novo item se ainda não existir na mesa
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
                    'preco_unitario': float(produto.venda)
                })

            mesa.status = 'Aberta'

            if mesa.pedido == 0:
                ultimo_pedido = Mesa.objects.filter().order_by('-pedido').first()
                if ultimo_pedido:
                    mesa.pedido = ultimo_pedido.pedido + 1
                else:
                    mesa.pedido = 1
            
            # Salvar a mesa com os novos itens
            mesa.save()

            # Renderiza apenas a lista de itens da mesa
            return render(request, 'mesa/partials/htmx_componentes/item_list.html', {'mesa': mesa})
        else:
            return JsonResponse({'success': False, 'error': 'Estoque insuficiente'}, status=400)

"""class MesaCreateView(LoginRequiredMixin, CreateView):
    model = Mesa
    form_class = MesaForm
    template_name = 'mesa/mesa_form.html'
    success_url = reverse_lazy('mesa:list_mesa')"""

class MesaCreateView(LoginRequiredMixin, CreateView):
    model = Mesa
    form_class = MesaForm
    template_name = 'mesa/mesa_form.html'

    def form_valid(self, form):
        # Verifica se a requisição é feita via HTMX pelo cabeçalho HX-Request
        if self.request.headers.get('HX-Request'):
            response = super().form_valid(form)
            mesas_abertas = Mesa.objects.filter(status='Aberta')
            mesas_fechadas = Mesa.objects.filter(status='Fechada')             
                
            return render(self.request, 'mesa/partials/htmx_componentes/lista_mesas.html', {
                'mesas_abertas': mesas_abertas,
                'mesas_fechadas': mesas_fechadas,
            })
        else:
            return super().form_valid(form)

    def get_success_url(self):
        # Caso a requisição seja HTMX, não faça redirecionamento
        if self.request.headers.get('HX-Request'):
            return ''
        return reverse_lazy('mesa:list_mesa')

