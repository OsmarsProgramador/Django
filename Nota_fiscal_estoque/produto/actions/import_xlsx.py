# produto/actions/import_xlsx.py
import pandas as pd
from produto.models import Categoria, Produto

def import_xlsx(file_path):
    '''
    Importa planilhas xlsx.
    '''
    # Leia o arquivo Excel usando pandas e openpyxl
    df = pd.read_excel(file_path, engine='openpyxl')
    
    # Supondo que as colunas estão na ordem correta
    fields = ('produto', 'ncm', 'importado', 'preco', 'estoque', 'estoque_minimo', 'categoria')

    # Atualizar categorias
    categorias = df['categoria'].dropna().unique()
    categorias_objs = [Categoria(categoria=categoria) for categoria in categorias]

    Categoria.objects.all().delete()  # CUIDADO
    Categoria.objects.bulk_create(categorias_objs)

    aux = []
    for _, row in df.iterrows():
        produto = row['produto']
        ncm = int(row['ncm'])
        importado = True if row['importado'] == 'True' else False
        preco = row['preco']
        estoque = row['estoque']
        estoque_minimo = row['estoque_minimo']
        categoria_nome = row['categoria']
        
        categoria = Categoria.objects.filter(categoria=categoria_nome).first()

        produto = dict(
            produto=produto,
            ncm=ncm,
            importado=importado,
            preco=preco,
            estoque=estoque,
            estoque_minimo=estoque_minimo,
        )

        if categoria:
            obj = Produto(categoria=categoria, **produto)
        else:
            obj = Produto(**produto)

        aux.append(obj)

    Produto.objects.all().delete()  # CUIDADO
    Produto.objects.bulk_create(aux)
