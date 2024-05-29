# Abstração
class Log:
    def log(self, msg):
        raise NotImplementedError('Implemente o método log')


class LogFileMixin(Log):
    def log(self, msg):
        print(msg)

# nesse caso só irá executar caso a execucao seja feita diretamente no modulo log.py, caso seja em algum outro modulo que importa log ele nao efetuara os comandos abaixo como rodar o main.py
if __name__ == '__main__':
    l = LogFileMixin()
    l.log('qualquer coisa')