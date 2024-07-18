# mesa/views.py
from django.views.generic import ListView, View
from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404, render
from .models import Mesa
from produto.models import Produto
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse

from django.views.generic.edit import CreateView
from .forms import MesaForm

# pip install reportlab - para imprimir comanda
# from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


""" 
Resumo Visual do Passo a Passo
Template URL Tag: {% url 'mesa:mesa_list' %}
Resolução da URL: Encontrar a URL correspondente em urls.py
Mapeamento para View: views.MesaListView.as_view()
Chamada de as_view: Criação da função de view
Método dispatch: Determinar o método HTTP e chamar get
Método get: Chamar get_context_data
Método get_context_data: Adicionar dados ao contexto
Renderização: Renderizar o template com o contexto
Isso mostra como Django sabe como chegar ao método get_context_data quando você clica no link "Listar mesas".
"""
"""O uso do LoginRequiredMixin tem como objetivo garantir que apenas usuários autenticados possam acessar essa view."""

class MesaListView(LoginRequiredMixin, ListView):
    model = Mesa
    template_name = 'mesa/mesa_list.html'
    context_object_name = 'mesas'
    paginate_by = 10

    def get_queryset(self):
        # Ordena o queryset antes da paginação
        return Mesa.objects.all().order_by('nome')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mesas_abertas'] = Mesa.objects.filter(status='Aberta').order_by('nome')
        context['mesas_fechadas'] = Mesa.objects.filter(status='Fechada').order_by('nome')
        return context

class AbrirMesaView(View):
    def get(self, request, pk):
        mesa = get_object_or_404(Mesa, pk=pk)
        usuarios = User.objects.exclude(username='admin')
        produtos = Produto.objects.all()
        return render(request, 'mesa/abrir_mesa.html', {'mesa': mesa, 'usuarios': usuarios, 'produtos': produtos})

class UpdateUserView(View):
    def post(self, request, pk):
        mesa = get_object_or_404(Mesa, pk=pk)
        usuario_id = request.POST.get('usuario')
        usuario = get_object_or_404(User, pk=usuario_id)

        # Debugging
        print(f"Received user ID: {usuario_id}")
        print(f"Usuario: {usuario.username}")
        print(f"Mesa: {mesa.nome}")

        mesa.usuario = usuario
        mesa.save()

        # Debugging
        print(f"Updated Mesa: {mesa.nome}, New User: {mesa.usuario.username}")

        return redirect('mesa:abrir_mesa', pk=pk)
    

class GerarComandaPDFView(LoginRequiredMixin, View):
    def get(self, request, mesa_id):
        mesa = get_object_or_404(Mesa, pk=mesa_id)

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="comanda_{mesa_id}.pdf"'

        p = canvas.Canvas(response)

        y = 800  # Starting position for the first line
        p.drawString(100, y, f"Comanda de Pedido: {mesa.pedido}")
        y -= 20

        for item in mesa.itens:
            p.drawString(100, y, f"{item['nome_produto']} - {item['quantidade']} - R${item['preco_unitario']:.2f}")
            y -= 20

        p.showPage()
        p.save()
        return response


class MesaCreateView(LoginRequiredMixin, CreateView):
    model = Mesa
    form_class = MesaForm
    template_name = 'mesa/mesa_form.html'
    success_url = reverse_lazy('mesa:mesa_list')



class ExcluirItemView(LoginRequiredMixin, View):
    def post(self, request, pk):
        mesa = get_object_or_404(Mesa, pk=pk)
        item_codigo = request.POST.get('item_codigo')
        quantidade = int(request.POST.get('quantidade', 1))

        item_removido = False
        for item in mesa.itens:
            if item['codigo'] == item_codigo:
                if item['quantidade'] > quantidade:
                    item['quantidade'] -= quantidade
                else:
                    mesa.itens.remove(item)
                item_removido = True
                break

        if item_removido:
            try:
                produto = Produto.objects.get(codigo=item_codigo)
                produto.estoque += quantidade
                produto.save()
            except Produto.DoesNotExist:
                pass

            total_itens = sum(item['quantidade'] for item in mesa.itens)

            if total_itens <= 0:
                mesa.itens = []
                mesa.status = 'Fechada'
                mesa.pedido = 0

            mesa.save()

        return redirect('mesa:abrir_mesa', pk=pk)

    
from django.template.loader import render_to_string

class AdicionarProdutoView(View):
    def post(self, request, mesa_id, produto_id):
        print("Iniciando AdicionarProdutoView...")  # Debugging inicial
        mesa = get_object_or_404(Mesa, pk=mesa_id)
        produto = get_object_or_404(Produto, pk=produto_id)
        quantidade = int(request.POST.get('quantidade', 1))

        print(f"Produto: {produto.nome_produto}, Quantidade: {quantidade}")  # Debugging
        print(f"Estoque disponível: {produto.estoque}")

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
            
            context = {
                'mesa': mesa
            }
            item_list_html = render_to_string('mesa/partials/item_list.html', context)
            print("Produto adicionado com sucesso!")  # Debugging
            return JsonResponse({'success': True, 'item_list_html': item_list_html})
        else:
            print("Estoque insuficiente.")  # Debugging
            return JsonResponse({'success': False, 'error': 'Estoque insuficiente'})

