# mesa/views.py
from django.views.generic import ListView, DetailView, View
from django.shortcuts import redirect, get_object_or_404
from .models import Mesa
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mesas_abertas'] = Mesa.objects.filter(status='Aberta')
        context['mesas_fechadas'] = Mesa.objects.filter(status='Fechada')
        return context

class AbrirMesaView(LoginRequiredMixin, DetailView):
    model = Mesa
    template_name = 'mesa/abrir_mesa.html'
    context_object_name = 'mesa'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # passa todos os usuários ativos para o contexto.
        # Exclui o usuário administrador
        context['usuarios'] = User.objects.exclude(is_superuser=True)
        return context
        return context

class UpdateUserView(LoginRequiredMixin, View):
    def post(self, request, pk):
        mesa = get_object_or_404(Mesa, pk=pk)
        usuario_id = request.POST.get('usuario')
        usuario = get_object_or_404(User, pk=usuario_id)
        mesa.usuario = usuario
        mesa.save()
        return redirect('mesa:abrir_mesa', pk=pk)
    

class GerarComandaPDFView(LoginRequiredMixin, View):
    def get(self, request, pk):
        mesa = get_object_or_404(Mesa, pk=pk)
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="comanda_{mesa.id}.pdf"'
        p = canvas.Canvas(response)
        p.drawString(100, 800, f"Comanda da Mesa {mesa.nome}")
        p.drawString(100, 780, f"Pedido: {mesa.pedido}")
        y = 760
        for item in mesa.itens:
            p.drawString(100, y, f"{item.nome_produto} - {item.quantidade} - R${item.preco_unitario}")
            y -= 20
        p.showPage()
        p.save()
        return response


class ExcluirItemView(LoginRequiredMixin, View):
    def post(self, request, pk):
        mesa = get_object_or_404(Mesa, pk=pk)
        item_codigo = request.POST.get('item_codigo')
        item = mesa.itens.filter(codigo=item_codigo).first()
        if item:
            item.delete()
        return redirect('mesa:abrir_mesa', pk=pk)