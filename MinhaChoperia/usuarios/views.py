from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario
from django.shortcuts import redirect
from hashlib import sha256


def login(request):
    """if request.session.get('usuario'):
        return redirect('/app_choperia/home/')"""
    """ O tipo do método de envio através da url é o GET """
    status = request.GET.get('status')
    return render(request, "login.html", {'status': status})

def valida_login(request):

    email = request.POST.get('email')
    senha = request.POST.get('senha')

    senha = sha256(senha.encode()).hexdigest()
    
    usuario = Usuario.objects.filter(email = email).filter(senha = senha)
    
    if len(usuario) == 0:
        return redirect('/auth/login/?status=1')
    elif len(usuario) > 0:
        request.session['usuario'] = usuario[0].id
        return redirect(f'/app_choperia/home/?status=0')

    # return HttpResponse(f"{email} {senha}")

def cadastro(request):
    status = request.GET.get('status')
    return render(request, "cadastro.html", {'status': status})

def valida_cadastro(request):
    nome = request.POST.get('nome')
    senha = request.POST.get('senha')
    email = request.POST.get('email')    

    """ Faz uma busca antes no BD e armazena em 'usuario' se encontrar """
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
    except:
        return redirect('/auth/cadastro/?status=4')


def sair(request):
    """ 
    é responsável por encerrar a sessão do usuário, deslogando-o. Ao chamar request.session.flush(), 
    todos os dados da sessão atual são removidos, efetivamente deslogando o usuário, e então 
    o código redireciona o usuário de volta para a página de login ('/auth/login/'). 
    """
    request.session.flush() # Desloga e limpa completamente
    return redirect('/auth/login/')