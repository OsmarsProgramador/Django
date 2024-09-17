# mesa/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Mesa, Pedido
from produto.models import Produto  # Importando o modelo Produto
from .forms import SelecionarUsuarioForm, AdicionarProdutoForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login  # Importação correta do login
from .forms import MesaForm


@login_required
def index(request):
    mesas = Mesa.objects.all()
    return render(request, 'mesa/mesa.html', {'mesas': mesas})

@login_required
def abrir_mesa(request, numero_mesa):
    mesa = get_object_or_404(Mesa, numero=numero_mesa)
    if request.method == 'POST':
        form = SelecionarUsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['usuario']
            login(request, usuario)
            mesa.usuario = usuario
            mesa.save()
            return redirect('mesa:detalhes_mesa', numero_mesa=mesa.numero)
    else:
        form = SelecionarUsuarioForm()
    
    return render(request, 'mesa/abrir_mesa.html', {'form': form, 'mesa': mesa})

@login_required
def detalhes_mesa(request, numero_mesa):
    mesa = get_object_or_404(Mesa, numero=numero_mesa)
    pedidos = Pedido.objects.filter(mesa=mesa)

    if request.method == 'POST':
        if 'adicionar_produto' in request.POST:
            form = AdicionarProdutoForm(request.POST)
            if form.is_valid():
                pedido = form.save(commit=False)
                pedido.mesa = mesa
                produto = pedido.produto
                produto.estoque -= pedido.quantidade  # Reduz o estoque do produto
                produto.save()
                pedido.save()
                return redirect('mesa:detalhes_mesa', numero_mesa=numero_mesa)
        elif 'remover_produto' in request.POST:
            pedido_id = request.POST.get('pedido_id')
            pedido = get_object_or_404(Pedido, id=pedido_id)
            produto = pedido.produto
            produto.estoque += pedido.quantidade  # Devolve a quantidade ao estoque do produto
            produto.save()
            pedido.delete()
            return redirect('mesa:detalhes_mesa', numero_mesa=numero_mesa)
    else:
        form = AdicionarProdutoForm()

    return render(request, 'mesa/detalhes_mesa.html', {
        'mesa': mesa,
        'pedidos': pedidos,
        'form': form
    })

def mesa_list(request):
    # Filtra as mesas abertas (sem produtos) e fechadas (com produtos)
    mesas_abertas = Mesa.objects.filter(produtos__isnull=False).distinct()
    mesas_fechadas = Mesa.objects.filter(produtos__isnull=True).distinct()

    return render(request, 'mesa/mesa_list.html', {
        'mesas_abertas': mesas_abertas,
        'mesas_fechadas': mesas_fechadas,
    })

def mesa_create(request):
    if request.method == 'POST':
        form = MesaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mesa:mesa_list')
    else:
        form = MesaForm()
    return render(request, 'mesa/mesa_form.html', {'form': form})

def mesa_update(request, pk):
    mesa = get_object_or_404(Mesa, pk=pk)
    if request.method == 'POST':
        form = MesaForm(request.POST, instance=mesa)
        if form.is_valid():
            form.save()
            return redirect('mesa:mesa_list')
    else:
        form = MesaForm(instance=mesa)
    return render(request, 'mesa/mesa_form.html', {'form': form})

def mesa_delete(request, pk):
    mesa = get_object_or_404(Mesa, pk=pk)
    if request.method == 'POST':
        mesa.delete()
        return redirect('mesa:mesa_list')
    return render(request, 'mesa/mesa_confirm_delete.html', {'mesa': mesa})

