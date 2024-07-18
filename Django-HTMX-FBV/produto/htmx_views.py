# produto/htmx_views.py
from .models import Produto
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

