# try, except, else e finally
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

# o finally sempre é executado, com erro ou sem erro no try

try:
    print('ABRIR ARQUIVO')
    8/0
    # print(c)
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
    print('DIVIDIU ZERO')
except IndexError as error:
    print('IndexError')
    print(error)
except (NameError, ImportError):
    print('NameError, ImportError')
# o else so executa se o codigo nao der erros
else:
    print('Não deu erro')
# o finally sempre é executado, com erro ou sem erro no try
finally:
    print('FECHAR ARQUIVO')