# produto/htmx_views.py
from django.views import View
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from .models import Produto, Categoria
from .forms import ProdutoForm, CategoriaForm

class CheckProdutoView(View):
    def get(self, request):
        produto = request.GET.get('nome_produto')
        produtos = Produto.objects.filter(nome_produto__icontains=produto)
        return render(request, 'produto/partials/htmx_componentes/check_produto.html', {'produtos': produtos})
    
class CheckCategoriaView(View):
    def get(self, request):
        categoria = request.GET.get('nome')
        categorias = Categoria.objects.filter(nome__icontains=categoria)
        return render(request, 'produto/partials/htmx_componentes/check_categoria.html', {'categorias': categorias})

class CreateProdutoView(View): # equivalente a SaveProdutoView
    def post(self, request):
        form = ProdutoForm(request.POST)
        nome = request.POST.get('nome_produto')
        if Produto.objects.filter(nome_produto=nome).exists():
            produtos = Produto.objects.filter(nome_produto__icontains=nome)
            return render(request, 'produto/partials/htmx_componentes/check_produto.html', {'produtos': produtos})
        if form.is_valid():
            form.save()
            produtos = Produto.objects.all()
            return render(request, 'produto/partials/htmx_componentes/list_all_produtos.html', {'produtos': produtos})
        return JsonResponse({'error': form.errors}, status=400)

"""class EditProdutoView(View):
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
        return JsonResponse({'error': form.errors}, status=400)"""

class EditProdutoView(View):
    def get(self, request, id):
        produto = get_object_or_404(Produto, id=id)
        form = ProdutoForm(instance=produto)
        return render(request, 'produto/partials/htmx_componentes/edit_produto_form.html', {'form': form, 'produto_id': id})

class UpdateProdutoView(View):
    def post(self, request):
        produto_id = request.POST.get('produto_id')
        produto = get_object_or_404(Produto, id=produto_id)
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            # Paginação
            page_number = request.POST.get('page', 1)
            produtos_list = Produto.objects.all()
            paginator = Paginator(produtos_list, 10)  # 10 produtos por página
            page_obj = paginator.get_page(page_number)
            return render(request, 'produto/partials/htmx_componentes/list_all_produtos.html', {'produtos': page_obj})
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
    def post(self, request):
        print('Add cat dentro de def')
        form = CategoriaForm(request.POST)
        if form.is_valid():
            print('Formulário válido')
            form.save()
            categorias = Categoria.objects.all()
            return render(request, 'produto/partials/htmx_componentes/list_all_categoria.html', {'categorias': categorias})
        print('Formulário não válido')
        return JsonResponse({'error': form.errors}, status=400)
    

