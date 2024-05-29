# Abra a pasta do seu projeto no terminal
# e digite:
# python -m venv nome_do_ambiente_virtual
#

# Ativando e desativando meu ambiente virtual

Windows: .\venv\Scripts\activate
Linux e Mac: source venv/bin/activate
Desativar: deactivate
#


# Replicando ambientes
# No início do artigo falamos sobre os ambientes virtuais trazerem a simplicidade de replicar o ambiente em outras máquinas e isso se deve a possibilidade de exportarmos um arquivo com todas bibliotecas que o nosso projeto contém. Veja como é simples:

pip freeze > requirements.txt


# Com o comando acima, será criado um arquivo com todas as bibliotecas presentes em nosso ambiente virtual. Por exemplo:

flake8==3.7.9
Flask==1.1.2
Flask-API==2.0


# Agora, se quisermos rodar o nosso projeto em outra máquina, não será necessário baixar as dependências uma a uma, basta fazer:

pip install -r requirements.txt  

# Com o comando acima, será instalado de forma automática todas as bibliotecas presentes no arquivo requirements.txt


# E por fim, para desativar o ambiente virtual:

deactivate