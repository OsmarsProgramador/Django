# produto/htmx_views.py
from django.views import View
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from .models import Produto, Categoria
from .forms import ProdutoForm, CategoriaForm
from django.http import QueryDict

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

def get_put_data(request):
    # Cria um QueryDict a partir dos dados do corpo da requisição
    return QueryDict(request.body)

@method_decorator(csrf_exempt, name='dispatch')
class EditProdutoView(View):
    def get(self, request, id):
        produto = get_object_or_404(Produto, id=id)
        form = ProdutoForm(instance=produto)
        categorias = Categoria.objects.all()
        return render(request, 'produto/partials/htmx_componentes/edit_produto_form.html', {
            'form': form,
            'produto': produto,
            'categorias': categorias
        })

    def put(self, request, id):
        produto = get_object_or_404(Produto, id=id)
        put_data = get_put_data(request)
        form = ProdutoForm(put_data, instance=produto)
        if form.is_valid():
            form.save()
            produtos_list = Produto.objects.all().order_by('nome_produto')
            paginator = Paginator(produtos_list, 10)  # 10 produtos por página
            page_number = request.GET.get('page', 1)
            page_obj = paginator.get_page(page_number)
            
            return render(request, 'produto/partials/htmx_componentes/list_all_produtos.html', {
                'produtos': page_obj.object_list,
                'page_obj': page_obj,
                'is_paginated': page_obj.has_other_pages(),
            })
        return render(request, 'produto/partials/htmx_componentes/edit_produto_form.html', {
            'form': form,
            'produto': produto,
            'categorias': Categoria.objects.all()
        })
    
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
    
def search_produto(request):
    search_text = request.POST.get('search', '')

    produtos_list = Produto.objects.filter(nome_produto__icontains=search_text).order_by('nome_produto')

    paginator = Paginator(produtos_list, 10)  # 10 produtos por página
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    print(f'paginator = {paginator}\npage_number = {page_number}\npage_obj = {page_obj}\nprodutos = {page_obj.object_list}\nis_paginated = {page_obj.has_other_pages()}')

    return render(request, 'produto/partials/htmx_componentes/list_all_produtos.html', {
        'produtos': page_obj.object_list,
        'page_obj': page_obj,
        'is_paginated': page_obj.has_other_pages(),
    })


    
