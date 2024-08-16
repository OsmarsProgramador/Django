# mesa/views.py
from django.views.generic import ListView, View
from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404, render
from .models import Mesa
from produto.models import Produto
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.utils import timezone

# pip install reportlab - para imprimir comanda
# from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

""" 
Resumo Visual do Passo a Passo
Template URL Tag: {% url 'mesa:list_mesa' %}
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
    template_name = 'mesa/list_mesa.html'
    context_object_name = 'mesas'
    paginate_by = 10

    def get_queryset(self):
        # Ordena o queryset antes da paginação
        return Mesa.objects.all().order_by('nome')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mesas_abertas'] = Mesa.objects.filter(status='Aberta').order_by('nome')
        context['mesas_fechadas'] = Mesa.objects.filter(status='Fechada').order_by('nome')
        
        # Obtém as mesas já existentes no banco de dados
        mesas_existentes = set(Mesa.objects.values_list('nome', flat=True))

        # Gera uma lista de mesas entre 1 e 30 que não estão no banco de dados
        context['mesas_disponiveis'] = [f'{str(i).zfill(2)}' for i in range(1, 31) if f'{str(i).zfill(2)}' not in mesas_existentes]

        return context


class AbrirMesaView(View):
    def get(self, request, id_mesa):
        print(f'Abrindo mesa na função AbrirMesaView')
        mesa = get_object_or_404(Mesa, id=id_mesa)
        usuarios = User.objects.exclude(username='admin')
        produtos = Produto.objects.all()

        # Cálculo do total de cada item e o total geral no backend
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

        return render(request, 'mesa/abrir_mesa.html', {
            'mesa': mesa, 
            'usuarios': usuarios, 
            'produtos': produtos,
            'itens_calculados': itens_calculados,  # Enviar os itens calculados para o template
            'total_geral': total_geral,  # Enviar o total geral para o template
            'now': now,  # Passar a data e hora atual para o template
        })


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

