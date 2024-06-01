from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse

def index(request):
    return render(request, "app_quitanda/index.html", {})

def login(request):
    return render(request, "app_quitanda/login.html", {})

def contato(request):
    return render(request, "app_quitanda/contato.html", {})


def confirmarcadastro(request):
    return render(request, "app_quitanda/confirmarcadastro.html")

def cadastrarnovasenha(request):
    return render(request, "app_quitanda/cadastrarnovasenha.html")

def cadastro(request):
    return render(request, "app_quitanda/cadastro.html", {})

def valida_cadastro(request):
    """nome = request.POST.get('nome')
    senha = request.POST.get('senha')
    email = request.POST.get('email')    

    # Faz uma busca antes no BD e armazena em 'usuario' se encontrar
    usuario = Usuario.objects.filter(email = email)

    # uma variável chamada 'status' é criada para controlar a validação e autenticação do usuário
    if len(nome.strip()) == 0 or len(email.strip()) == 0:
        return redirect('/auth/cadastro/?status=1')

    if len(senha) < 8:
        return redirect('/auth/cadastro/?status=2')

    if len(usuario) > 0:
        return redirect('/auth/cadastro/?status=3')

    try:
        ''' utilizando a função sha256 do módulo hashlib para codificar a senha antes de 
        salvar no banco de dados. Aqui está uma explicação passo a passo do que está acontecendo:

        senha.encode(): A senha fornecida é convertida para uma sequência de bytes, 
        que é necessária para realizar a codificação SHA-256.

        sha256(senha.encode()): A função sha256 calcula o hash SHA-256 dos bytes 
        da senha, produzindo um objeto de hash.

        .hexdigest(): Este método converte o objeto de hash em uma string legível e utilizável. 
        Aqui, está sendo usada para obter a representação hexadecimal do hash SHA-256 da senha. 
        
        Portanto ao cadastrar a senha ela não será visível no admin '''
        senha = sha256(senha.encode()).hexdigest()
        usuario = Usuario(nome = nome,
                          senha = senha,
                          email = email)
        usuario.save()

        return redirect('/auth/cadastro/?status=0')
    except:"""
    return redirect('/proj_quitanda')

def carrinho(request):
    return render(request, "app_quitanda/carrinho.html")

def cliente(request):
    return render(request, "app_quitanda/cliente.html")

def privacidade(request):
    return render(request, "app_quitanda/privacidade.html")

def quemsomos(request):
    return render(request, "app_quitanda/quemsomos.html")

def termos(request):
    return render(request, "app_quitanda/termos.html")

def trocas(request):
    return render(request, "app_quitanda/trocas.html")

def cliente_contatos(request):
    return render(request, "app_quitanda/cliente_contatos.html")

def cliente_dados(request):
    return render(request, "app_quitanda/cliente_dados.html")

def cliente_endereco(request):
    return render(request, "app_quitanda/cliente_endereco.html")

def cliente_favoritos(request):
    return render(request, "app_quitanda/cliente_favoritos.html")

def cliente_pedidos(request):
    return render(request, "app_quitanda/cliente_pedidos.html")

def cliente_senha(request):
    return render(request, "app_quitanda/cliente_senha.html")

def confirmcadastrosenha(request):
    return render(request, "app_quitanda/confirmcadastrosenha.html")

def confirmcontato(request):
    return render(request, "app_quitanda/confirmcontato.html")

def confirmrecupsenha(request):
    return render(request, "app_quitanda/confirmrecupsenha.html")

def fechamento_endereco(request):
    return render(request, "app_quitanda/fechamento_endereco.html")

def fechamento_itens(request):
    return render(request, "app_quitanda/fechamento_itens.html")

def fechamento_pagamento(request):
    return render(request, "app_quitanda/fechamento_pagamento.html")

def fechamento_pedido(request):
    return render(request, "app_quitanda/fechamento_pedido.html")

def produto(request):
    return render(request, "app_quitanda/produto.html")

def recuperarsenha(request):
    return render(request, "app_quitanda/recuperarsenha.html")