# filter é um filtro funcional

# funcao para impressao de um iterator de forma mais organizada
def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]


def filtrar_preco(produto):
    return produto['preco'] > 100


# fazendo com list comprehension, filtrando produtos com precos maiores de $100
novos_produtos = [
    p for p in produtos
    if p['preco'] > 100
]

# fazendo com filter (retorna um filter object, para sair lista precisa envolver em lista)
novos_produtos2 = filter(
    # lambda produto: produto['preco'] > 100,
    filtrar_preco,
    produtos
)


print_iter(produtos)

print('--------------------------------')
print_iter(novos_produtos) # {'nome': 'Produto 2', 'preco': 105.87}

print('--------------------------------')
print_iter(novos_produtos2) # {'nome': 'Produto 2', 'preco': 105.87}

print('--------------------------------')
print(novos_produtos) # [{'nome': 'Produto 2', 'preco': 105.87}]

print('--------------------------------')
print(novos_produtos2) # <filter object at 0x0000012B54780F70>