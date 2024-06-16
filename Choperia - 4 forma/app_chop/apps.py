from django.apps import AppConfig
from django.db.models.signals import post_migrate

def create_initial_mesas(sender, **kwargs):
    from .models import Mesa
    if Mesa.objects.count() == 0:
        for i in range(1, 11):
            Mesa.objects.create(nome=f'Mesa {i}')

class AppChopConfig(AppConfig):
    name = 'app_chop'

    def ready(self):
        post_migrate.connect(create_initial_mesas, sender=self)
