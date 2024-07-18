# produto/htmx_views.py
from django.shortcuts import render
from django.views import View
from .models import Produto
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

class CheckProdutoView(View):
    def get(self, request):
        produto = request.GET.get('produto')
        produtos = Produto.objects.filter(nome__icontains=produto)
        return render(request, 'partials/htmx_componentes/check_produto.html', {'produtos': produtos})

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

"""from .models import Produto
from django.http import HttpResponse
from django.shortcuts import render

def check_produto(request):
    produto = request.GET.get('produto') # Corrigido: request.GET em vez de request.Get
    produtos = Produto.objects.filter(nome__icontains=produto) # Use icontains para buscar nomes que contenham a string
    return render(request, 'partials/htmx_componentes/check_produto.html', {'produtos': produtos})

def save_produto(request):
    nome = request.POST.get('produto')
    preco = request.POST.get('preco')

    produto = Produto(
        nome=nome,
        preco=preco,
    )
    produto.save()
    produtos = Produto.objects.all()

    return render(request, 'partials/htmx_componentes/list_all_produtos.html', {'produtos': produtos})
    
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@require_http_methods(['DELETE'])
def delete_produto(request, id):
    produto = Produto.objects.get(id=id)
    produto.delete()
    produtos = Produto.objects.all()
    return render(request, 'partials/htmx_componentes/list_all_produtos.html', {'produtos': produtos})
"""

