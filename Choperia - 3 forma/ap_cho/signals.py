"""
O objetivo do código fornecido é usar o sinal post_migrate do Django para criar instâncias iniciais no banco de dados assim que as migrações forem aplicadas.
post_migrate: Um sinal disparado após a aplicação das migrações.
receiver: Um decorador usado para conectar funções a sinais.
Mesa: O modelo que queremos criar instâncias iniciais.

"""

from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Mesa, Categoria

@receiver(post_migrate)
def create_initial_mesas(sender, **kwargs):
    if sender.name == 'ap_cho':
        if Mesa.objects.count() == 0:
            for i in range(1, 11):
                Mesa.objects.create(nome=f'{i}')

@receiver(post_migrate)
def create_initial_categories(sender, **kwargs):
    if sender.name == 'ap_cho':
        initial_categories = ['Suco', 'Cerveja', 'Balde', 'Pizza', 'Lanches', 'Tapioca', 'Refrigerante']
        for category in initial_categories:
            Categoria.objects.get_or_create(nome=category)


          