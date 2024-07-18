# produto/views.py
from django.shortcuts import render
from django.views import View
from .models import Produto

# Views que recebe a requisição do próprio usuario que acessou o navegador
"""def list_produto(request):
    produtos = Produto.objects.all()
    return render(request, 'produto/list_produto.html', {'produtos': produtos})"""

class ListProdutoView(View):
    def get(self, request):
        produtos = Produto.objects.all()
        return render(request, 'produto/list_produto.html', {'produtos': produtos})


