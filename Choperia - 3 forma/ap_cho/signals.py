from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Mesa

@receiver(post_migrate)
def create_initial_mesas(sender, **kwargs):
    if sender.name == 'ap_cho':
        if Mesa.objects.count() == 0:
            for i in range(1, 11):
                Mesa.objects.create(nome=f'{i}')
