# notafiscal/views.py
from django.shortcuts import render
from django.views.generic import ListView
from .models import NotaFiscal
from django.db.models import Q # Importar Q da biblioteca django.db.models para usar consultas complexas.

class NotaFiscalListView(ListView):
    model = NotaFiscal
    template_name = 'notafiscal/notafiscal_list.html'
    context_object_name = 'notas_fiscais'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return NotaFiscal.objects.filter(Q(numero__icontains=query) | Q(descricao__icontains=query) | Q(data_emissao__icontains=query))
        return NotaFiscal.objects.all()


