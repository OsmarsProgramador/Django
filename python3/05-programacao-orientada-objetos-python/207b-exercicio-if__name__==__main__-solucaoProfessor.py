import json

CAMINHO_ARQUIVO = '.\\05-programacao-orientada-objetos-python\\207-json-arquivoAuxiliar.json'



def fazer_dump():
    with open(CAMINHO_ARQUIVO, 'w') as arquivo:
        print('FAZENDO DUMP')
        json.dump(bd, arquivo, ensure_ascii=False, indent=2)

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# fazer_dump()

with open(CAMINHO_ARQUIVO, 'r') as arquivo:
    pessoas = json.load(arquivo)
    p1 = Pessoa(**pessoas[0])
    p2 = Pessoa(**pessoas[1])
    p3 = Pessoa(**pessoas[2])

    print(p1.nome, p1.idade)
    print(p2.nome, p2.idade)
    print(p3.nome, p3.idade)

    bd = [vars(p1), p2.__dict__, vars(p3)]