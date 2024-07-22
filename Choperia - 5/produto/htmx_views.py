# produto/htmx_views.py
from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Produto, Categoria
from .forms import ProdutoForm, CategoriaForm

class CheckProdutoView(View):
    def get(self, request):
        produto_nome = request.GET.get('nome_produto')
        produtos = Produto.objects.filter(nome_produto__icontains=produto_nome)
        return render(request, 'produto/partials/htmx_componentes/check_produto.html', {'produtos': produtos})

class CreateProdutoView(View): # equivalente a SaveProdutoView
    def post(self, request):
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            produtos = Produto.objects.all()
            return render(request, 'produto/partials/htmx_componentes/list_all_produtos.html', {'produtos': produtos})
        return JsonResponse({'error': form.errors}, status=400)

class EditProdutoView(View):
    def get(self, request, id):
        produto = get_object_or_404(Produto, id=id)
        categorias = Categoria.objects.all()
        return render(request, 'produto/partials/htmx_componentes/edit_produto.html', 
            {'produto': produto,
            'categorias': categorias
        })
    
class UpdateProdutoView(View):
    def post(self, request, id):
        produto = get_object_or_404(Produto, id=id)
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            produtos = Produto.objects.all()
            return render(request, 'produto/partials/htmx_componentes/list_all_produtos.html', {'produtos': produtos})
        return JsonResponse({'error': form.errors}, status=400)

    
class SaveProdutoView(View):
    def post(self, request):
        nome = request.POST.get('produto')
        preco = request.POST.get('preco')

        produto = Produto(nome=nome, preco=preco)
        produto.save()

        produtos = Produto.objects.all()
        return render(request, 'produto/partials/htmx_componentes/list_all_produtos.html', {'produtos': produtos})

@method_decorator(csrf_exempt, name='dispatch')
class DeleteProdutoView(View):
    def delete(self, request, id):
        produto = Produto.objects.get(id=id)
        produto.delete()
        produtos = Produto.objects.all()
        return render(request, 'produto/partials/htmx_componentes/list_all_produtos.html', {'produtos': produtos})

class AddCategoriaModalView(View):
    def get(self, request):
        form = CategoriaForm()
        return render(request, 'produto/partials/htmx_componentes/add_categoria_form.html', {'form': form})

    def post(self, request):
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            categorias = Categoria.objects.all()
            return render(request, 'produto/categoria_list.html', {'categorias': categorias})
        return render(request, 'produto/partials/htmx_componentes/add_categoria_form.html', {'form': form})

    
