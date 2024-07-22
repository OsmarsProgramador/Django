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
├── core/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── db.sqlite3
├── gitignore
├── list_structure_clean.py
├── manage.py
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
│   ├── templates/
│   │   ├── base.html
│   │   ├── produto/
│   │   │   ├── categoria_list.html
│   │   │   ├── index.html
│   │   │   ├── list_produto.html
│   │   │   ├── partials/
│   │   │   │   ├── htmx_componentes/
│   │   │   │   │   ├── add_categoria.html
│   │   │   │   │   ├── categoria_table.html
│   │   │   │   │   ├── check_produto.html
│   │   │   │   │   ├── edit_produto.html
│   │   │   │   │   ├── list_all_produtos.html
│   ├── tests.py
│   ├── urls.py
│   ├── views.py


"""