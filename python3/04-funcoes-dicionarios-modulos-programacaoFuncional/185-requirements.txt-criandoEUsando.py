#

# Replicando ambientes
# No início do artigo falamos sobre os ambientes virtuais trazerem a simplicidade de replicar o ambiente em outras máquinas e isso se deve a possibilidade de exportarmos um arquivo com todas bibliotecas que o nosso projeto contém. Veja como é simples:

pip freeze > requirements.txt


# Com o comando acima, será criado um arquivo com todas as bibliotecas presentes em nosso ambiente virtual. Por exemplo:

flake8==3.7.9
Flask==1.1.2
Flask-API==2.0


# Criando e usando um requirements.txt
# pip freeze > requirements.txt
# Instalando tudo do requirements.txt
pip install -r requirements.txt

# Com o comando acima, será instalado de forma automática todas as bibliotecas presentes no arquivo requirements.txt


# E por fim, para desativar o ambiente virtual:

deactivate