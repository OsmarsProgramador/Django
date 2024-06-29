# mesa/views.py
from django.views.generic import ListView
from .models import Mesa

class MesaListView(ListView):
    model = Mesa
    template_name = 'mesa/mesa_list.html'
    context_object_name = 'mesas'
