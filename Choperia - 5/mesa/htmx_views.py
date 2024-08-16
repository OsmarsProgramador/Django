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

from django.utils import timezone
from .forms import AdicionarItemForm

""" implementar a lógica para adicionar produtos à mesa, considerando a manipulação do estoque e a atualização da lista de itens da mesa. """   
class AdicionarItemView(View):
    def get(self, request, mesa_id):
        mesa = get_object_or_404(Mesa, pk=mesa_id)
        produtos = Produto.objects.all()
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

            # Cálculo do total de cada item e do total geral
            itens_calculados = []
            total_geral = 0
            
            for item in mesa.itens:
                total_item = item['quantidade'] * item['preco_unitario']
                itens_calculados.append({
                    'nome_produto': item['nome_produto'],
                    'quantidade': item['quantidade'],
                    'preco_unitario': item['preco_unitario'],
                    'total_item': total_item,
                })
                total_geral += total_item

            # Obter a data e hora atual
            now = timezone.now()

            # Se a requisição for via HTMX, renderizar apenas o componente parcial
            if request.headers.get('HX-Request'):
                return render(request, 'mesa/partials/htmx_componentes/item_list.html', {
                    'mesa': mesa,
                    'itens_calculados': itens_calculados,  # Enviar os itens calculados para o template
                    'total_geral': total_geral,  # Enviar o total geral para o template
                    'now': now,  # Passar a data e hora atual para o template
                })
            else:
                return redirect('mesa:abrir_mesa', id_mesa=mesa.id)
        else:
            return render(request, 'mesa/adicionar_item.html', {
                'mesa': mesa,
                'produtos': Produto.objects.all(),
                'error': 'Estoque insuficiente'
            })
 

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

