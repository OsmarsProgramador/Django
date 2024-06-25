# empresa/views.py
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Empresa


def index(request):
    return render(request, 'index.html')

class EmpresaListView(ListView):
    model = Empresa
    template_name = 'empresa/empresa_list.html'
    context_object_name = 'empresas'

class EmpresaDetailView(DetailView):
    model = Empresa
    template_name = 'empresa/empresa_detail.html'
    context_object_name = 'empresa'


