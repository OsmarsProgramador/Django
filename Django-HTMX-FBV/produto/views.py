# produto/views.py
from django.shortcuts import render
from .models import Produto

# Views que recebe a requisição do próprio usuario que acessou o navegador
def list_produto(request):
    produtos = Produto.objects.all()
    return render(request, 'produto/list_produto.html', {'produtos': produtos})


