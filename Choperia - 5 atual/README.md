Bom dia! Me responda em português. Preciso de um sistema de choperia baseado em classes em suas views, e tem objetivo criar um gerenciamento de notas fiscais/comandas, para prover o gerenciamento de notas fiscais de uma empresa e comandas de mesas. Escolha um local para implementar essa lógica. 

Esse projeto deverá ter um controle para que as páginas dos aplicativos empresa, produto, mesa, estoque sejam acessadas se um usuário estiver conectado.

Outros modelos que o projeto deve ter é o de Categoria (nome), Produto com os atributos (nome_produto, categoria, descricao, custo, venda, codigo, estoque, estoque_total e imagem com caminho upload_to='imagens/') e Mesa (id, nome, itens (default=list), status (default='Fechada') e pedido(default=0). Onde itens, será cada produto que for adicionado a mesa

**O nome do projeto**
    - choperia
    será representado por choperia (urls.py para as rotas que chegarao aos app)

**Os aplicativos**
   - core (base.html, index.html)
    A base.html deverá ter uma nav do bootstrep 5.3.3, com links para a página principal index.html e também um link para cada templates dos aplicativos empresa, produto, mesa, estoque. Se um aplicativo tiver mais de um template, deverá ser um dropdow. Toda teg deverá acessar a URL por meio de um namespace.
    A model dde core terá campos para controle de entrada e saída de estoque.
        # core/models.py
        from django.db import models # type: ignore


        class TimeStampedModel(models.Model):
            created = models.DateTimeField(
                'criado em',
                auto_now_add=True,
                auto_now=False
            )
            modified = models.DateTimeField(
                'modificado em',
                auto_now_add=False,
                auto_now=True
            )

            class Meta:
                abstract = True


   - usuario (para autenticação e cadastro)
    # usuario/models.py
    from django.db import models

    class Usuario(models.Model):
        nome = models.CharField(max_length=30)
        email = models.EmailField()
        senha = models.CharField(max_length=64) # sha256 vai transforma em uma hash unica e exclusiva de 64 caracteres
        ativo = models.BooleanField(default=False)

        def __str__(self) -> str:
            return self.nome

   - estoque com entrada e saída
    # estoque/models.py
    from django.db import models
    from core.models import TimeStampedModel

    class Estoque(TimeStampedModel):
        empresa = models.ForeignKey('empresa.Empresa', on_delete=models.CASCADE, related_name='estoques')
        produto = models.ForeignKey('produto.Produto', on_delete=models.CASCADE, related_name='entradas_saidas')
        quantidade = models.PositiveIntegerField()
        tipo = models.CharField(max_length=10)  # 'entrada' ou 'saída'
        data = models.DateField()

        def __str__(self):
            return f'{self.produto.nome_produto} - {self.quantidade} ({self.tipo})'

   - produto
    # produto/models.py
    from django.db import models

    class Categoria(models.Model):
        nome = models.CharField(max_length=255)

        def __str__(self):
            return self.nome


    class Produto(models.Model):
        nome_produto = models.CharField(max_length=255)
        categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
        descricao = models.TextField(blank=True, null=True)
        custo = models.DecimalField(max_digits=10, decimal_places=2)
        venda = models.DecimalField(max_digits=10, decimal_places=2)
        codigo = models.CharField(max_length=20, unique=True)
        estoque = models.PositiveIntegerField()
        estoque_total = models.PositiveIntegerField()
        imagem = models.ImageField(upload_to='imagens/', blank=True, null=True)

        def __str__(self):
            return self.nome_produto



   - mesa com criação de 10 mesas iniciais 
        # mesa/models.py
        from django.db import models

        class Mesa(models.Model):
            nome = models.CharField(max_length=50)
            itens = models.JSONField(default=list)
            status = models.CharField(max_length=10, default='Fechada')
            pedido = models.PositiveIntegerField(default=0)

            def __str__(self):
                return self.nome

   


**Campos da Nota Fiscal**

- Empresa (deve ter uma entidade própria)
- Série (alfanumerico)
- Número (numérico)
- Nome/Descrição
- Data

Crie uma página para exibir a listagem de empresas. Ao abrir os detalhes da empresa deve ser aberta a listagem de notas fiscais daquela empresa.

- [x] Adicione à listagem de notas fiscais um campo de busca por número, nome do produto e data. A busca deve funcionar via GET.

- [x] Paginação é bem vinda, mas não necessária para o teste.
Você pode usar qualquer formato de Django views para este teste (CBV ou FBV)

Para a apresentação cadastre ao menos 10 empresas com 20 notas fiscais cada uma. O nome de cada empresa pode ser gerado com um lorem ipsum e os dados das notas fiscais podem ser randomicos, porém válidos, com dados do Brasil e escrito em português.

- [x] Inclua o script de geração das empresas no anexo do projeto
- [x] Utilize arquivos externos para os dados de entrada
- [x] Inclua um CSS à página para uma aparencia agradável (pode ser Bootstrap 5.3.3)
- [x] A listagem de notas fiscais deve ser feita em uma tabela (HTML/boostrep 5.3.3)

Para popular o banco de dados da aplicação utilizamos a biblioteca [Faker]. Os scripts de geração das empresas se encontram no diretório scripts, com dados do Brasil e escrito em português.

Outros diretórios deverão está na raiz do projeto , tais como: além de scripts, media e static


Use Django CRUD (criar, recuperar, atualizar, excluir) visualizações genéricas baseadas em classe: -

CreateView – Visualizações baseadas em classe Django
DetailView – Visualizações baseadas em classe Django
UpdateView – Visualizações baseadas em classe Django
DeleteView – Visualizações baseadas em classe Django
FormView – Visualizações baseadas em classe Django



Se achar necessário use Apps de terceiros:
    'django_extensions', # pip install django_extensions
    'widget_tweaks', # pip install widget_tweaks   
    'bootstrapform', # pip install django-bootstrap-form

O projeto deverá ter a seguinte Estrutura:
.
├── .gitignore
├── Planilha de Controle de Estoque.xlsx
├── choperia/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── core/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   │   ├── __init__.py
│   ├── models.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
├── db.sqlite3
├── empresa/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   │   ├── 0001_initial.py
│   │   ├── __init__.py
│   ├── models.py
│   ├── templates/
│   │   ├── empresa/
│   │   │   ├── empresa_detail.html
│   │   │   ├── empresa_list.html
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
├── estoque/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   │   ├── 0001_initial.py
│   │   ├── __init__.py
│   ├── models.py
│   ├── templates/
│   │   ├── estoque/
│   │   │   ├── estoque_entrada_list.html
│   │   │   ├── estoque_saida_list.html
│   │   │   ├── protocolo_entrega_list.html
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
├── list_structure_clean.py
├── manage.py
├── media/
│   ├── imagens/
├── mesa/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   │   ├── 0001_initial.py
│   │   ├── __init__.py
│   ├── models.py
│   ├── templates/
│   │   ├── mesa/
│   │   │   ├── abrir_mesa.html
│   │   │   ├── mesa_list.html
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
├── popular os bancos.txt
├── produto/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   │   ├── 0001_initial.py
│   │   ├── __init__.py
│   ├── models.py
│   ├── tabelas/
│   │   ├── produtos.xlsx
│   ├── templates/
│   │   ├── produto/
│   │   │   ├── index.html
│   │   │   ├── produto_list.html
│   │   │   ├── produto_list_cards.html
│   │   │   ├── produto_list_fragment.html
│   │   │   ├── produto_list_table.html
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
├── scripts/
│   ├── gerar_dados.py
├── static/
│   ├── css/
│   │   ├── style.css
│   ├── img/
│   ├── js/
│   │   ├── script.js
├── testes.py
├── usuarios/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   │   ├── 0001_initial.py
│   │   ├── __init__.py
│   ├── models.py
│   ├── templates/
│   │   ├── cadastro.html
│   │   ├── login.html
│   ├── tests.py
│   ├── urls.py
│   ├── views.py


Podemos usar base.html:
<!-- https://getbootstrap.com/docs/4.0/getting-started/introduction/#starter-template -->
{% load static %}
<!doctype html>
<html lang="pt-BR">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="shortcut icon" href="https://www.djangoproject.com/favicon.ico">
    <title>Choperia</title>

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <!-- Font-awesome -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">

    <!-- Select2 -->
    <link href="https://cdnjs.cloudflare.com/ajax/libs/select2/4.0.6-rc.0/css/select2.min.css" rel="stylesheet" />

    <link rel="stylesheet" href="{% static 'css/style.css' %}">

    {% block css %}{% endblock css %}

  </head>
  <body>

    <nav class="navbar navbar-expand-md navbar-dark bg-dark fixed-top">
      <a class="navbar-brand" href="#">Choperia</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarsExampleDefault" aria-controls="navbarsExampleDefault" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
    
      <div class="collapse navbar-collapse" id="navbarsExampleDefault">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item active">
            <a class="nav-link" href="{% url 'core:index' %}">Home <span class="sr-only">(current)</span></a>
          </li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" id="dropdown01" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Produtos</a>
            <div class="dropdown-menu" aria-labelledby="dropdown01">
              <a class="dropdown-item" href="{% url 'produto:produto_list' %}">Produtos</a>
              
            </div>
          </li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" id="dropdown02" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Estoque</a>
            <div class="dropdown-menu" aria-labelledby="dropdown02">
              <a class="dropdown-item" href="{% url 'estoque:estoque_entrada_list' %}">Entrada</a>
              <a class="dropdown-item" href="{% url 'estoque:estoque_saida_list' %}">Saída</a>
            </div>
          </li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" id="dropdown03" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Protocolo de Entrega</a>
            <div class="dropdown-menu" aria-labelledby="dropdown03">
              <a class="dropdown-item" href="{% url 'estoque:protocolo_de_entrega_list' %}">Entrega</a>
            </div>
          </li>
        </ul>
        {% if user.is_authenticated %}
          <ul class="navbar-nav px-3">
            <li class="nav-item text-nowrap">
              <a href="{% url 'logout' %}" class="nav-link">Sair</a>
            </li>
          </ul>
        {% endif %}
      </div>
    </nav>

    <div class="container mb-2 p-2">
      <br>
      {% block content %}{% endblock content %}
    </div>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
    <!-- Select2 -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/select2/4.0.6-rc.0/js/select2.min.js"></script>

    {% block js %}{% endblock js %}
  </body>
</html>

index.html: {% extends "base.html" %}

{% block content %}

  <div class="jumbotron">
    <div class="container">
      <h1>Bem-vindo!</h1>
      <p>Este é um sistema para controle de estoque para Choperia.</p>
      <p>
        <a href="https://github.com/rg3915/estoque">Veja no GitHub</a>
      </p>
    </div>
  </div>

{% endblock content %}

