# empresa/views.py
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Empresa, NotaFiscal
from django.db.models import Q  # Importar Q para consultas complexas

class EmpresaListView(ListView):
    model = Empresa
    template_name = 'empresa/empresa_list.html'

class EmpresaDetailView(DetailView):
    model = Empresa
    template_name = 'empresa/empresa_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['notas'] = self.object.notas.all()
        return context

class NotaFiscalListView(ListView):
    model = NotaFiscal
    template_name = 'empresa/nota_list.html'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return NotaFiscal.objects.filter(
                Q(numero__icontains=query) | Q(descricao__icontains=query)
            )
        return NotaFiscal.objects.all()


