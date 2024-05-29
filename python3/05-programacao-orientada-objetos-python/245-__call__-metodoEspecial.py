# Método especial __call__
# callable é algo que pode ser executado com parênteses
# Em classes normais, __call__ faz a instância de uma
# classe "callable".

class CallMe:
    def __init__(self, phone):
        self.phone = phone

    # faz com que a instacia de cada objeto da classe acima (CallMe) seja chamavel como uma funcao
    # cancela o erro 'object is not callable'
    def __call__(self, nome):
        print(nome, 'está chamando', self.phone)
        return 2134


call1 = CallMe('23945876545')

# aqui chamamos a instacia call1 passando o argumento 'Luiz Otávio'
retorno = call1('Luiz Otávio') # Luiz Otávio está chamando 23945876545

print(retorno) # 2134