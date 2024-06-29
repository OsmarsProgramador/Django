import os

def list_files(startpath, prefix=''):
    for item in sorted(os.listdir(startpath)):
        if item in ['venv', '__pycache__', 'imagens']:  # Ignora as pastas venv e __pycache__
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
.
├── .gitignore
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
│   │   │   ├── mesa_list.html
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
├── popular os bancos.txt
├── produto/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── imagens
│   ├── migrations/
│   │   ├── 0001_initial.py
│   │   ├── __init__.py
│   ├── models.py
│   ├── produtos.xlsx
│   ├── templates/
│   │   ├── produto/
│   │   │   ├── index.html
│   │   │   ├── produto_list.html
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
├── scripts/
│   ├── generate_data.py
├── static/
│   ├── css/
│   │   ├── style.css
"""



"""eu tenho que ├── produto/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── imagens
│   ├── migrations/
│   │   ├── 0001_initial.py
│   │   ├── __init__.py
│   ├── models.py
│   ├── produtos.xlsx

"""