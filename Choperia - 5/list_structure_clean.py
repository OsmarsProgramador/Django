import os

def list_files(startpath, prefix=''):
    for item in sorted(os.listdir(startpath)):
        if item in ['venv', '__pycache__', ] or item.endswith(('.jpg', '.png')):  # Ignora as pastas venv, __pycache__ e arquivos .jpg e .png
            continue
        path = os.path.join(startpath, item)
        if os.path.isdir(path):
            print(f"{prefix}├── {item}/")
            list_files(path, prefix + '│   ')
        else:
            print(f"{prefix}├── {item}")
            
print(".")
list_files('.')

"""
Estrutura do meu projeto:

.
├── .gitignore
├── Planilha de Controle de Estoque.xlsx
├── README.md
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
│   │   ├── core/
│   │   │   ├── base.html
│   │   │   ├── index.html
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
│   │   │   ├── estoque_form.html
│   │   │   ├── estoque_list.html
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
├── formas de renderizar e redirecionar.md
├── funcionalidades pendentes
├── list_structure_clean.py
├── manage.py
├── media/
│   ├── imagens/
├── mesa/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations/
│   │   ├── 0001_initial.py
│   │   ├── __init__.py
│   ├── models.py
│   ├── templates/
│   │   ├── mesa/
│   │   │   ├── abrir_mesa.html
│   │   │   ├── mesa_form.html
│   │   │   ├── mesa_list.html
│   │   │   ├── partials/
│   │   │   │   ├── item_list.html
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
├── popular os bancos.txt
├── produto/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── htmx_views.py
│   ├── migrations/
│   │   ├── 0001_initial.py
│   │   ├── __init__.py
│   ├── models.py
│   ├── tabelas/
│   │   ├── produtos.xlsx
│   ├── templates/
│   │   ├── produto/
│   │   │   ├── categoria_list.html
│   │   │   ├── list_produto.html
│   │   │   ├── partials/
│   │   │   │   ├── htmx_componentes/
│   │   │   │   │   ├── add_categoria_form.html
│   │   │   │   │   ├── check_produto.html
│   │   │   │   │   ├── edit_produto.html
│   │   │   │   │   ├── list_all_produtos.html
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
├── t2.html
├── teste.html
├── testes.py
├── usuario/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations/
│   │   ├── 0001_initial.py
│   │   ├── __init__.py
│   │   ├── templates/
│   │   │   ├── usuario/
│   │   │   │   ├── cadastro.html
│   │   │   │   ├── login.html
│   ├── models.py
│   ├── templates/
│   │   ├── usuario/
│   │   │   ├── cadastro.html
│   │   │   ├── login.html
│   ├── tests.py
│   ├── urls.py
│   ├── views.py




"""