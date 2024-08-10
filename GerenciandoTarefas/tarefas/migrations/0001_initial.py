# Generated by Django 5.1 on 2024-08-09 14:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tarefa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descricao', models.TextField(blank=True)),
                ('completa', models.BooleanField(default=False)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tarefas', to='tarefas.categoria')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tarefas', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
