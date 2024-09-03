# mesa/admin.py
from django.contrib import admin
from .models import Mesa, Pedido

admin.site.register(Mesa)
admin.site.register(Pedido)

