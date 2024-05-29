# Relações entre classes: associação, agregação e composição

# Composição é uma especialização da agregação.
# Mas nela, quando o objeto "pai" for apagado, todas
# as referências dos objetos filhos também são
# apagadas.

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))

    def inserir_endereco_externo(self, endereco):
        self.enderecos.append(endereco)

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)

    # metodo chamado automaticamente quando o objeto está para ser apagado
    def __del__(self):
        print('APAGANDO,', self.nome)


class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

    # metodo chamado automaticamente quando o objeto está para ser apagado
    def __del__(self):
        print('APAGANDO,', self.rua, self.numero)


cliente1 = Cliente('Maria')
cliente1.inserir_endereco('Av Brasil', 54)
cliente1.inserir_endereco('Rua B', 6745)
endereco_externo = Endereco('Av Saudade', 123213)
cliente1.inserir_endereco_externo(endereco_externo)
cliente1.listar_enderecos()
# Av Brasil 54
# Rua B 6745
# Av Saudade 123213

# observe que os enderecos criados por dentro da classe com o metodo inserir_endereco foram apagados assim que o cliente foi apagado, o que caracteriza a relacao de composicao entre eles
del cliente1
# APAGANDO, Maria
# APAGANDO, Rua B 6745
# APAGANDO, Av Brasil 54


print(endereco_externo.rua, endereco_externo.numero) # Av Saudade 123213
print('######################## AQUI TERMINA MEU CÓDIGO')

# observe tambem que o endereco criado 'por fora' da classe com o metodo inserir_endereco_externo so foi apagado apos o fim do programa e nao quando o objeto cliente1 foi apagado

# APAGANDO, Av Saudade 123213