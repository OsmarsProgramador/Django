# mesa/views.py
from django.views.generic import ListView, DetailView
from .models import Mesa
from django.contrib.auth.mixins import LoginRequiredMixin

class MesaListView(LoginRequiredMixin, ListView):
    model = Mesa
    template_name = 'mesa/mesa_list.html'
    context_object_name = 'mesas'
    paginate_by = 10

class MesaDetailView(LoginRequiredMixin, DetailView):
    model = Mesa
    template_name = 'mesa/mesa_detail.html'
    context_object_name = 'mesa'

