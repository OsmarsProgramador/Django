# script_populacao.py
import os
import django
import random
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sistema_notas_fiscais.settings')
django.setup()

from empresa.models import Empresa
from notafiscal.models import NotaFiscal

fake = Faker()

def criar_empresas_notas_fiscais():
    for _ in range(10):
        empresa = Empresa.objects.create(
            nome=fake.company(),
            cnpj=fake.ssn()
        )
        for _ in range(20):
            NotaFiscal.objects.create(
                empresa=empresa,
                serie=fake.bothify(text='??####'),
                numero=fake.random_number(digits=5),
                descricao=fake.catch_phrase(),
                peso=fake.random_number(digits=4),
                cubagem=fake.random_number(digits=2, fix_len=True) / 100,
                data_emissao=fake.date_this_decade()
            )

if __name__ == '__main__':
    criar_empresas_notas_fiscais()
