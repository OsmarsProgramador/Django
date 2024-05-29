import json

caminhoArquivoJson='.\\05-programacao-orientada-objetos-python\\206-json-arquivoAuxiliar.json'

try:
    with open(caminhoArquivoJson, 'r', encoding='utf8') as arquivo:
        arquivoJson = json.load(arquivo)

except:
    print('Arquivo JSON não localizado, lista inicial de tarefas será vazia.\n')
    arquivoJson={}


class Pessoa:
    def __init__(self,nome,idade,email,profissao) -> None:
        self.nome=nome
        self.idade=idade
        self.email=email
        self.profissao=profissao


listaPessoas=[]

# podemos colocar atributo por atributo mas tambem expandir o dicionario que esta na lista pessoas
for pessoa in arquivoJson['pessoas']:
    # listaPessoas.append(Pessoa(pessoa['nome'],pessoa['idade'],pessoa['email'],pessoa['profissao']))
    listaPessoas.append(Pessoa(**pessoa))
    


for pessoa in listaPessoas:
    print(pessoa.__dict__)
    print()




# abaixo temos a retirada dos dados no formato string onde eu havia feito errado, foi tao trabalhoso que nao tive coragem de apagar rs

# listaPessoas=[]
# for pessoa in arquivoJson['pessoas']:
#     pessoa=pessoa.replace('{','').replace('}','').replace("'",'').replace(': ',':').strip()
#     listaPessoa=pessoa.split(',')
#     for item in listaPessoa:
#         if 'nome' in item:
#             nome=item[item.find(':')+1:]
#         elif 'idade' in item:
#             idade=item[item.find(':')+1:]
#         elif 'email' in item:
#             email=item[item.find(':')+1:]
#         elif 'profissao' in item:
#             profissao=item[item.find(':')+1:]
#     listaPessoas.append(Pessoa(nome,idade,email,profissao))


# for pessoa in listaPessoas:
#     print(pessoa.__dict__)

