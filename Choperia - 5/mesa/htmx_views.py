# mesa/htmx_views.py
from django.views import View
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from .models import Mesa
from .forms import MesaForm
from produto.models import Produto

class AdicionarProdutoView(View):
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
                ultimo_pedido = Mesa.objects.filter().order_by('-pedido').first()
                if ultimo_pedido:
                    mesa.pedido = ultimo_pedido.pedido + 1
                else:
                    mesa.pedido = 1
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

