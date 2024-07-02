from django.contrib import admin
from .models import Mesa

@admin.register(Mesa)
class MesaAdmin(admin.ModelAdmin):
    list_display = ['nome']  
    list_filter = ['nome']  
    search_fields = ['nome']