# Generated by Django 5.0.6 on 2024-06-26 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mesa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('itens', models.JSONField(default=list)),
                ('status', models.CharField(default='Fechada', max_length=10)),
                ('pedido', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
