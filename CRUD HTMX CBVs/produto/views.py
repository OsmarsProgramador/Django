# produto/views.py
from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views import View
from .models import Produto, Categoria

class IndexView(TemplateView): # TemplateView funciona só para renderizar
    template_name = 'produto/index.html'
    
# Views que recebe a requisição do próprio usuario que acessou o navegador
class ListProdutoView(View):
    def get_queryset(self):
        # Garantir que os objetos sejam ordenados antes de serem paginados
        return Produto.objects.all().order_by('nome_produto')

    def get(self, request):
        produtos_list = self.get_queryset()  # Usar a queryset ordenada
        categorias = Categoria.objects.all()
        
        # Configuração da paginação
        paginator = Paginator(produtos_list, 10)  # 10 produtos por página
        page_number = request.GET.get('page')
        produtos = paginator.get_page(page_number)        
        
        return render(request, 'produto/list_produto.html', {
            'produtos': produtos, 
            'categorias': categorias
        })
    
    

class CategoriaListView(ListView):
    model = Categoria
    template_name = 'produto/list_categoria.html'
    context_object_name = 'categorias'
    paginate_by = 10

    def get_queryset(self): # garantir que os objetos sejam ordenados antes de serem paginados.
        return Categoria.objects.all().order_by('nome')
