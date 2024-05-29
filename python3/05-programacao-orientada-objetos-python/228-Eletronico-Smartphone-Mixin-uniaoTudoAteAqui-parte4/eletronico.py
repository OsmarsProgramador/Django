from log import LogFileMixin


class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    def ligar(self):
        if not self._ligado:
            self._ligado = True

    def desligar(self):
        if self._ligado:
            self._ligado = False

# a ordem das classes na heranca fazem diferenca, no caso de termos metodos de mesmo nome em ambas as superclasses sera herdada o metodo da superclasse a esquerda por exemplo
class Smartphone(Eletronico, LogFileMixin):
    def ligar(self):
        super().ligar() # está utilizando o metodo original da superclasse

        if self._ligado:
            msg = f'{self._nome} está ligado'
            self.log_success(msg)

    def desligar(self):
        super().desligar() # está utilizando o metodo original da superclasse

        if not self._ligado:
            msg = f'{self._nome} está desligado'
            self.log_error(msg)