from django.shortcuts import render, get_object_or_404, redirect
from .models import Produto, Categoria
from .forms import ProdutoForm, CategoriaForm
from django.contrib.auth.decorators import login_required

def index(request):
    produtos = Produto.objects.all()
    return render(request, 'produto/produto.html', {'produtos': produtos})
# View para listar categorias
@login_required
def categoria_list(request):
    if request.user.is_superuser:
        return redirect('/admin/')  # Redireciona para o admin se o usuário for superuser
    categorias = Categoria.objects.all()
    return render(request, 'produto/categoria_list.html', {'categorias': categorias})

# View para criar uma nova categoria
@login_required
def categoria_create(request):
    if request.user.is_superuser:
        return redirect('/admin/')  # Redireciona para o admin se o usuário for superuser
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produto:categoria_list')
    else:
        form = CategoriaForm()
    return render(request, 'produto/categoria_form.html', {'form': form})

# View para listar todos os produtos
@login_required
def produto_list(request):
    if request.user.is_superuser:
        return redirect('/admin/')  # Redireciona para o admin se o usuário for superuser
    produtos = Produto.objects.all()
    return render(request, 'produto/produto_list.html', {'produtos': produtos})

# View para criar um novo produto
@login_required
def produto_create(request):
    if request.user.is_superuser:
        return redirect('/admin/')  # Redireciona para o admin se o usuário for superuser
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('produto:produto_list')
    else:
        form = ProdutoForm()
    return render(request, 'produto/produto_form.html', {'form': form})

# View para atualizar um produto existente
@login_required
def produto_update(request, pk):
    if request.user.is_superuser:
        return redirect('/admin/')  # Redireciona para o admin se o usuário for superuser
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('produto:produto_list')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'produto/produto_form.html', {'form': form})

# View para excluir um produto
@login_required
def produto_delete(request, pk):
    if request.user.is_superuser:
        return redirect('/admin/')  # Redireciona para o admin se o usuário for superuser
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        produto.delete()
        return redirect('produto:produto_list')
    return render(request, 'produto/produto_confirm_delete.html', {'produto': produto})
