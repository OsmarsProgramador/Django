import json

pessoa = {
    'nome': 'Luiz Otávio 2',
    'sobrenome': 'Miranda',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.8,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None,
}

# o caminho esta sendo usado a partir do diretorio raiz do curso python3, pois assim venho abrindo pelo github desktop
caminhoArquivoJson='.\\04-funcoes-dicionarios-modulos-programacaoFuncional\\190-json-arquivoAuxiliar.json'

# ensure_ascii=False mostra os caracteres especiais no arquivo em vez de codificação
# indent=2 formata o arquivo de maneira a ficar mais facil seu entendimento (em varias linhas em vez de tudo em uma)
with open(caminhoArquivoJson, 'w', encoding='utf8') as arquivo:
    json.dump(
        pessoa,
        arquivo,
        ensure_ascii=False,
        indent=2,
    )

with open(caminhoArquivoJson, 'r', encoding='utf8') as arquivo:
    pessoa1 = json.load(arquivo)
    print(pessoa1)
    print(type(pessoa1))
    print(pessoa1['nome']) 