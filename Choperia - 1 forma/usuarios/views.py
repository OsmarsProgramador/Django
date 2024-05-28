from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario
from django.shortcuts import redirect
from hashlib import sha256


def login(request):
    """if request.session.get('usuario'):
        return redirect('/choperia/home/')"""
    """ O tipo do método de envio através da url é o GET """
    status = request.GET.get('status')
    return render(request, "login.html", {'status': status})

def valida_login(request):
    """
    é responsável por verificar as credenciais de login (email e senha) enviadas por um formulário HTML via método POST. 
    Ela primeiro obtém o email e a senha do objeto request, em seguida, criptografa a senha usando o algoritmo SHA-256 e 
    busca por um usuário com o email e a senha fornecidos no banco de dados. Se nenhum usuário for encontrado, 
    o código redireciona o usuário de volta para a página de login com um parâmetro status=1 na URL. Caso contrário, 
    se um usuário for encontrado, o código armazena o ID do usuário na sessão do request e redireciona o usuário para 
    a página '/choperia/'.
    """
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    senha = sha256(senha.encode()).hexdigest()
    
    usuario = Usuario.objects.filter(email = email).filter(senha = senha)
    
    if len(usuario) == 0:
        return redirect('/auth/login/?status=1')
    elif len(usuario) > 0:
        request.session['usuario'] = usuario[0].id
        return redirect(f'/choperia/home/?status=0')

    # return HttpResponse(f"{email} {senha}")

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