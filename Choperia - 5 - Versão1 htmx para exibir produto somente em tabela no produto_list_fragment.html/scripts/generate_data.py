# scripts/generate_data.py
import os
import sys
import django
import random
from faker import Faker
from validate_docbr import CNPJ

# Adicione o caminho do diretório do projeto ao sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'choperia.settings')
django.setup()

from empresa.models import Empresa, NotaFiscal
from produto.models import Categoria, Produto
from mesa.models import Mesa
from estoque.models import Estoque

fake = Faker('pt_BR')
cnpj_generator = CNPJ()

def create_empresas_and_notas():
    for _ in range(10):
        cnpj = cnpj_generator.generate()
        empresa = Empresa.objects.create(
            nome=fake.company(),
            endereco=fake.address(),
            telefone=fake.phone_number(),
            email=fake.email(),
            cnpj=cnpj
        )
        for _ in range(20):
            NotaFiscal.objects.create(
                empresa=empresa,
                serie=fake.bothify(text='??###'),
                numero=fake.random_int(min=1000, max=9999),
                descricao=fake.text(max_nb_chars=200),
                data=fake.date_this_decade()
            )

def create_categorias():
    categorias_nomes = [
        'Refrigerantes', 'Sucos', 'Porções', 'Alcoólicas',
        'Baldes', 'Pizzas', 'Lanches', 'Sobremesas', 'Tapiocas'
    ]
    categorias = []
    for nome in categorias_nomes:
        categoria = Categoria.objects.create(nome=nome)
        categorias.append(categoria)
    return categorias

def create_produtos(categorias):
    produtos_nomes = [
        'Coca-Cola', 'Guaraná', 'Suco de Laranja', 'Suco de Uva',
        'Batata Frita', 'Azeitonas', 'Cerveja', 'Chopp', 'Balde de Cerveja',
        'Pizza Margherita', 'Pizza Pepperoni', 'Hambúrguer', 'Cheeseburger',
        'Pudim', 'Sorvete', 'Tapioca de Coco', 'Tapioca de Queijo'
    ]
    for nome in produtos_nomes:
        categoria = random.choice(categorias)
        Produto.objects.create(
            nome_produto=nome,
            categoria=categoria,
            descricao=fake.text(max_nb_chars=200),
            custo=fake.random_number(digits=5, fix_len=True) / 100,
            venda=fake.random_number(digits=5, fix_len=True) / 100,
            codigo=fake.bothify(text='PROD-#####'),
            estoque=fake.random_int(min=0, max=100),
            estoque_total=fake.random_int(min=0, max=200)
        )

def create_mesas():
    for i in range(1, 11):
        Mesa.objects.create(nome=f'Mesa {i}')

def add_produtos_to_mesas():
    produtos = list(Produto.objects.all())
    for mesa in Mesa.objects.all():
        itens = random.sample(produtos, k=random.randint(1, 5))
        mesa.itens = [{"produto_id": produto.id, "quantidade": random.randint(1, 5)} for produto in itens]
        mesa.save()

def create_estoque():
    empresas = list(Empresa.objects.all())
    produtos = list(Produto.objects.all())
    for _ in range(100):
        empresa = random.choice(empresas)
        produto = random.choice(produtos)
        tipo = random.choice(['entrada', 'saida'])
        quantidade = fake.random_int(min=1, max=50)
        Estoque.objects.create(
            empresa=empresa,
            produto=produto,
            quantidade=quantidade,
            tipo=tipo,
            data=fake.date_this_year()
        )

if __name__ == '__main__':
    create_empresas_and_notas()
    categorias = create_categorias()
    create_produtos(categorias)
    create_mesas()
    add_produtos_to_mesas()
    create_estoque()
