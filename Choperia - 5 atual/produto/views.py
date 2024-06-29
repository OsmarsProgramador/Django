# produto/views.py
from django.shortcuts import render, redirect
from django.conf import settings
from .models import Categoria, Produto
from django.views.generic import ListView
import os
import pandas as pd

class ProdutoListView(ListView):
    print('Fui chamado na classe!')
    model = Produto
    template_name = 'produto/produto_list.html'
    context_object_name = 'produtos'

    def get_template_names(self):
        print('Fui chamado na função da classe!')
        mode = self.request.GET.get('mode', 'table')
        print(f'Modo em classe: {mode}')
        if mode == 'cards':
            return ['produto/produto_list_cards.html']
        else:
            return ['produto/produto_list_table.html']

def import_xlsx(request):
    print('Fui chamado na função da import_xlsx!')
    if Produto.objects.exists():
        return redirect('produto:produto_list')
    else:
        file_path = os.path.join(settings.BASE_DIR, 'produto', 'tabelas/produtos.xlsx')
        df = pd.read_excel(file_path, header=1)  # Lendo o cabeçalho a partir da linha 2

        for _, item in df.iteritems():
            categoria_nome = item['categoria']
            categoria, created = Categoria.objects.get_or_create(nome=categoria_nome)
            Produto.objects.create(
                nome_produto=item['nome_produto'],
                categoria=categoria,
                descricao=item['descricao'],
                custo=item['custo'],
                venda=item['venda'],
                codigo=item['codigo'],
                estoque=item['estoque'],
                estoque_total=item['estoque_total'],
                imagem=item['imagem']
            )
        # Redirecionar para a listagem de produtos na visualização de cards após a importação
        return redirect('prodoto:produto_list')

"""def produto_list(request):
    mode = request.GET.get('mode', 'table')
    print(f'Modo em list_produto: {mode}')
    produtos = Produto.objects.all()
    return render(request, 'produto/produto_list.html', {'produtos': produtos, 'mode': mode})"""



