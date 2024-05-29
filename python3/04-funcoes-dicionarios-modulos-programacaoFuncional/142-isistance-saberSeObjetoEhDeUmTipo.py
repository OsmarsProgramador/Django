# isinstace - para saber se objeto é de determinado tipo

# caracterista de boolean -  


lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {'nome': 'Luiz'},
]

for item in lista:
    if isinstance(item, set):
        print('\nSET')
        item.add(5)
        print(item, isinstance(item, set))

    elif isinstance(item, str):
        print('\nSTR')
        print(item.upper())

    elif isinstance(item, (int, float)):
        print('\nNUM')
        print(item, item * 2)

    else:
        print('\nOUTRO')
        print(item, type(item))