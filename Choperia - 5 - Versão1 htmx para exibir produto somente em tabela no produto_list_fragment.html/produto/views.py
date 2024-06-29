# produto/views.py
import os
import pandas as pd
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Categoria, Produto
from django.views.generic import ListView
from django.conf import settings
from django.http import JsonResponse

class ProdutoListView(ListView):
    model = Produto
    template_name = 'produto/produto_list.html'
    context_object_name = 'produtos'

def import_xlsx(request):
    file_path = os.path.join(settings.BASE_DIR, 'produto', 'produtos.xlsx')
    df = pd.read_excel(file_path, header=1)  # Lendo o cabeçalho a partir da linha 2

    for _, row in df.iterrows():
        categoria_nome = row['categoria']
        categoria, created = Categoria.objects.get_or_create(nome=categoria_nome)

        Produto.objects.create(
            nome_produto=row['nome_produto'],
            categoria=categoria,
            descricao=row['descricao'],
            custo=row['custo'],
            venda=row['venda'],
            codigo=row['codigo'],
            estoque=row['estoque'],
            estoque_total=row['estoque_total'],
            imagem=row['imagem']
        )

    produtos = Produto.objects.all()
    return render(request, 'produto/produto_list_fragment.html', {'produtos': produtos})

def produto_list(request):
    produtos = Produto.objects.all()
    return render(request, 'produto/produto_list.html', {'produtos': produtos})