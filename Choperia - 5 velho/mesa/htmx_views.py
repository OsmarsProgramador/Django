# mesa/htmx_views.py
from django.views import View
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Mesa
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

            # Adicionar o cabeçalho HTMX para a resposta
            response = render(request, 'mesa/partials/item_list.html', {'mesa': mesa})
            response['HX-Trigger'] = 'updateItems'  # Dispara um evento HTMX personalizado, se necessário
            return response
        else:
            return JsonResponse({'success': False, 'error': 'Estoque insuficiente'})
        
        
