# mesa/views.py
from django.views.generic import ListView, DetailView
from .models import Mesa

""" Resumo Visual do Passo a Passo
Template URL Tag: {% url 'mesa:mesa_list' %}
Resolução da URL: Encontrar a URL correspondente em urls.py
Mapeamento para View: views.MesaListView.as_view()
Chamada de as_view: Criação da função de view
Método dispatch: Determinar o método HTTP e chamar get
Método get: Chamar get_context_data
Método get_context_data: Adicionar dados ao contexto
Renderização: Renderizar o template com o contexto
Isso mostra como Django sabe como chegar ao método get_context_data quando você clica no link "Listar mesas".
 """
class MesaListView(ListView):
    model = Mesa
    template_name = 'mesa/mesa_list.html'
    context_object_name = 'mesas'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mesas_abertas'] = Mesa.objects.filter(status='Aberta')
        context['mesas_fechadas'] = Mesa.objects.filter(status='Fechada')
        return context
    
class MesaDetailView(DetailView):
    model = Mesa
    template_name = 'mesa/abrir_mesa.html'  # Crie este template conforme necessário

