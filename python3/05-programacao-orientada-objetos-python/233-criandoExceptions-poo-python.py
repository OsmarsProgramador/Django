# Criando Exceptions em Python Orientado a Objetos

# Para criar uma Exception em Python, você só
# precisa herdar de alguma exceção da linguagem.

# A recomendação da doc é herdar de Exception.
# https://docs.python.org/3/library/exceptions.html

# Criando exceções (comum colocar Error ao final)
# Levantando (raise) / Lançando (throw) exceções
# Relançando exceções
# Adicionando notas em exceções (3.11.0)

# convencao de python colocar a palavra 'Error' no final das exceçoes para comunicar um error. herda o Exception, criada a excecao personalizada em python
class MeuError(Exception):
    ...