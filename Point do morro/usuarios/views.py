from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario
from django.shortcuts import redirect
from hashlib import sha256


def login(request):
    return render(request, "login.html")

"""
Os métodos POST e GET são dois dos principais métodos HTTP utilizados para enviar dados de um cliente (navegador) para um servidor web.

### Método GET:
- O método GET é usado para solicitar dados de um recurso específico no servidor.
- Os dados são enviados no URL da requisição, visíveis para todos (por exemplo, em links ou bookmarks).
- É adequado para solicitações que recuperam dados, como pesquisas ou navegação em páginas.
- No Django, os parâmetros GET são acessados através de `request.GET.get('nome_do_parametro')`.

### Método POST:
- O método POST é usado para enviar dados para o servidor para serem processados.
- Os dados são enviados no corpo da requisição, não visíveis na URL.
- É adequado para envio de formulários ou dados sensíveis, pois os dados não são visíveis.
- No Django, os parâmetros POST são acessados através de `request.POST.get('nome_do_parametro')`.

### Explicação dos métodos nos trechos de código fornecidos:
1. **Função `cadastro(request)`**:
   - Utiliza o método GET para obter o parâmetro 'status' da URL.
   - O valor de 'status' é passado para o template "cadastro.html" via contexto.

2. **Função `valida_cadastro(request)`**:
   - Utiliza o método POST para obter os dados do formulário de cadastro (nome, senha, email).
   - Realiza validações nos dados recebidos e redireciona com um parâmetro 'status' na URL em caso de erro ou sucesso.

3. **Função `validar_login(request)`**:
   - Utiliza o método POST para obter os dados de email e senha do formulário de login.
   - Realiza uma consulta no banco de dados com os dados fornecidos e redireciona com um parâmetro 'status' na URL com base no resultado.

Esses métodos são essenciais para a comunicação entre o cliente e o servidor em aplicações web, permitindo a troca de informações de forma segura e eficiente.
"""

def cadastro(request):
    status = request.GET.get('status')
    return render(request, "cadastro.html", {'status': status})

def valida_cadastro(request):
    nome = request.POST.get('nome')
    senha = request.POST.get('senha')
    email = request.POST.get('email')

    """ Faz uma busca antes no BD e armazena em 'usuario' se encontrar"""
    usuario = Usuario.objects.filter(email = email)

    if len(nome.strip()) == 0 or len(email.strip()) == 0:
        return redirect('/auth/cadastro/?status=1')

    if len(senha) < 8:
        return redirect('/auth/cadastro/?status=2')

    if len(usuario) > 0:
        return redirect('/auth/cadastro/?status=3')

    try:
        senha = sha256(senha.encode()).hexdigest()
        usuario = Usuario(nome = nome,
                          senha = senha,
                          email = email)
        usuario.save()

        return redirect('/auth/cadastro/?status=0')
    except:
        return redirect('/auth/cadastro/?status=4')


def validar_login(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    senha = sha256(senha.encode()).hexdigest()

    usuario = Usuario.objects.filter(email = email).filter(senha = senha)

    if len(usuario) == 0:
        return redirect('/auth/login/?status=1')
    elif len(usuario) > 0:
        request.session['usuario'] = usuario[0].id
        return redirect(f'/choperia/')

    return HttpResponse(f"{email} {senha}")


def sair(request):
    request.session.flush()
    return redirect('/auth/login/')