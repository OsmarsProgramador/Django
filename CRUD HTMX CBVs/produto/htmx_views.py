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

def get_put_data(request):
    # Cria um QueryDict a partir dos dados do corpo da requisição
    return QueryDict(request.body)

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

class CreateProdutoView(View):
    def post(self, request):
        form = ProdutoForm(request.POST)
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
        return JsonResponse({'error': form.errors}, status=400)

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
    def post(self, request):
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            categorias_list = Categoria.objects.all().order_by('nome')
            paginator = Paginator(categorias_list, 10)  # 10 categorias por página
            page_number = request.GET.get('page', 1)
            page_obj = paginator.get_page(page_number)
            
            return render(request, 'produto/partials/htmx_componentes/list_all_categoria.html', {
                'categorias': page_obj.object_list,
                'page_obj': page_obj,
                'is_paginated': page_obj.has_other_pages(),
            })
        return JsonResponse({'error': form.errors}, status=400)
    
@method_decorator(csrf_exempt, name='dispatch')
class EditCategoriaView(View):
    def get(self, request, id):
        categoria = get_object_or_404(Categoria, id=id)
        return JsonResponse({
            'nome': categoria.nome,
            'action': f"/produto/edit_categoria/{categoria.id}/"
        })

    def put(self, request, id):
        categoria = get_object_or_404(Categoria, id=id)
        put_data = get_put_data(request)
        form = CategoriaForm(put_data, instance=categoria)
        if form.is_valid():
            form.save()
            categorias_list = Categoria.objects.all().order_by('nome')
            paginator = Paginator(categorias_list, 10)  # 10 categorias por página
            page_number = request.GET.get('page', 1)
            page_obj = paginator.get_page(page_number)
            
            return render(request, 'produto/partials/htmx_componentes/list_all_categoria.html', {
                'categorias': page_obj.object_list,
                'page_obj': page_obj,
                'is_paginated': page_obj.has_other_pages(),
            })
        return JsonResponse({'error': form.errors}, status=400)

@method_decorator(csrf_exempt, name='dispatch')
class DeleteCategoriaView(View):
    def delete(self, request, id):
        categoria = Categoria.objects.get(id=id)
        categoria.delete()
        categorias_list = Categoria.objects.all().order_by('nome')
        paginator = Paginator(categorias_list, 10)  # 10 categorias por página
        page_number = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)
        
        return render(request, 'produto/partials/htmx_componentes/list_all_categoria.html', {
            'categorias': page_obj.object_list,
            'page_obj': page_obj,
            'is_paginated': page_obj.has_other_pages(),
        })
    
class CheckProdutoView(View):
    def get(self, request):
        produto = request.GET.get('nome_produto')
        produtos = Produto.objects.filter(nome_produto__icontains=produto)
        return render(request, 'produto/partials/htmx_componentes/check_produto.html', {'produtos': produtos})
    
class SearchProdutoView(View):
    def get(self, request):
        query = request.GET.get('query', '')
        if not query:
            print("Nenhum parâmetro de consulta fornecido.")
        else:
            print(f"Query: {query}")  # Verifique o valor de query
        
        produtos_list = Produto.objects.filter(nome_produto__icontains=query).order_by('nome_produto')
        print(f"Produtos encontrados: {produtos_list}")  # Verifique os produtos filtrados
        
        paginator = Paginator(produtos_list, 10)  # 10 produtos por página
        page_number = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)
        
        return render(request, 'produto/partials/htmx_componentes/list_all_produtos.html', {
            'produtos': page_obj.object_list,
            'page_obj': page_obj,
            'is_paginated': page_obj.has_other_pages(),
        })


