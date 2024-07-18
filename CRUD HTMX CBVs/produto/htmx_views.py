# produto/htmx_views.py
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Produto
from .forms import ProdutoForm

class CheckProdutoView(View):
    def get(self, request):
        produto = request.GET.get('nome')
        produtos = Produto.objects.filter(nome__icontains=produto)
        return render(request, 'partials/htmx_componentes/check_produto.html', {'produtos': produtos})

class CreateProdutoView(View): # equivalente a SaveProdutoView
    def post(self, request):
        form = ProdutoForm(request.POST)
        nome = request.POST.get('nome')
        if Produto.objects.filter(nome=nome).exists():
            produtos = Produto.objects.filter(nome__icontains=nome)
            return render(request, 'partials/htmx_componentes/check_produto.html', {'produtos': produtos})
        if form.is_valid():
            form.save()
            produtos = Produto.objects.all()
            return render(request, 'partials/htmx_componentes/list_all_produtos.html', {'produtos': produtos})
        return JsonResponse({'error': form.errors}, status=400)

class EditProdutoView(View):
    def get(self, request, id):
        produto = get_object_or_404(Produto, id=id)
        return render(request, 'partials/htmx_componentes/edit_produto.html', {'produto': produto})
    
class UpdateProdutoView(View):
    def post(self, request, id):
        produto = get_object_or_404(Produto, id=id)
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            produtos = Produto.objects.all()
            return render(request, 'partials/htmx_componentes/list_all_produtos.html', {'produtos': produtos})
        return JsonResponse({'error': form.errors}, status=400)

    
class SaveProdutoView(View):
    def post(self, request):
        nome = request.POST.get('produto')
        preco = request.POST.get('preco')

        produto = Produto(nome=nome, preco=preco)
        produto.save()

        produtos = Produto.objects.all()
        return render(request, 'partials/htmx_componentes/list_all_produtos.html', {'produtos': produtos})

@method_decorator(csrf_exempt, name='dispatch')
class DeleteProdutoView(View):
    def delete(self, request, id):
        produto = Produto.objects.get(id=id)
        produto.delete()
        produtos = Produto.objects.all()
        return render(request, 'partials/htmx_componentes/list_all_produtos.html', {'produtos': produtos})


