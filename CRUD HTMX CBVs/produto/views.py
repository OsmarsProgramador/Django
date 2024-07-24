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
        return Produto.objects.all().order_by('nome_produto')

    def get(self, request):
        produtos_list = self.get_queryset()
        categorias = Categoria.objects.all()
        
        paginator = Paginator(produtos_list, 10)  # 10 produtos por página
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        return render(request, 'produto/list_produto.html', {
            'produtos': page_obj.object_list,
            'categorias': categorias,
            'page_obj': page_obj,
            'is_paginated': page_obj.has_other_pages(),
        })
    
    

class CategoriaListView(ListView):
    model = Categoria
    template_name = 'produto/list_categoria.html'
    context_object_name = 'categorias'
    paginate_by = 10

    def get_queryset(self): # garantir que os objetos sejam ordenados antes de serem paginados.
        return Categoria.objects.all().order_by('nome')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = Paginator(self.get_queryset(), self.paginate_by)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['is_paginated'] = page_obj.has_other_pages()
        context['page_obj'] = page_obj
        return context

