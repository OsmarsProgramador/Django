"""
Closure e funções que retornam outras funções
"""


def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar

# aqui ficara salva na variavel a funcao saudar, no entanto com a saudacao ja salva que foi passada, sendo assim poderemos chamar a funcao falar_bom_dia e falar_boa_noite com os argumentos do nome e ela lembrara da mensagem de saudacao enviada inicialmente
falar_bom_dia = criar_saudacao('Bom dia') 
falar_boa_noite = criar_saudacao('Boa noite')

for nome in ['Maria', 'Joana', 'Luiz']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))