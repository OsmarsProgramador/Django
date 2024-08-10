# produto/views.py
from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Produto, Categoria
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class ProdutoListView(LoginRequiredMixin, ListView):
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

'''class ProdutoCreateView(LoginRequiredMixin, CreateView):
    """
    Essa view herda de LoginRequiredMixin e CreateView.
    O LoginRequiredMixin garante que apenas usuários autenticados possam acessar essa view.
    A CreateView é responsável por exibir o formulário de criação de um novo produto e salvar os dados no banco de dados.
    O model define o modelo a ser usado (nesse caso, Produto).
    fields = '__all__' significa que todos os campos do modelo serão exibidos no formulário.
    template_name especifica o template a ser usado para renderizar o formulário.
    success_url define a URL para a qual o usuário será redirecionado após a criação bem-sucedida de um produto.
    """
    model = Produto
    fields = '__all__'
    template_name = 'produto/produto_form.html'
    success_url = reverse_lazy('produto:list_produto')

class ProdutoUpdateView(LoginRequiredMixin, UpdateView):
    """
    O model define o modelo a ser usado (nesse caso, Produto).
    fields = '__all__' significa que todos os campos do modelo serão exibidos no formulário de edição.
    template_name especifica o template a ser usado para renderizar o formulário de edição.
    success_url define a URL para a qual o usuário será redirecionado após a atualização bem-sucedida de um produto.
    """

    model = Produto
    fields = '__all__'
    template_name = 'produto/produto_form.html'
    success_url = reverse_lazy('produto:list_produto')

class ProdutoDeleteView(LoginRequiredMixin, DeleteView):
    """
    O model define o modelo a ser usado (nesse caso, Produto).
    template_name especifica o template a ser usado para renderizar a página de confirmação de exclusão.
    success_url define a URL para a qual o usuário será redirecionado após a exclusão bem-sucedida de um produto.
    """
    model = Produto
    template_name = 'produto/produto_confirm_delete.html'
    success_url = reverse_lazy('produto:list_produto')'''

class CategoriaListView(LoginRequiredMixin, ListView):
    model = Categoria
    template_name = 'produto/categoria_list.html'
    context_object_name = 'categorias'
    paginate_by = 10

    def get_queryset(self): # garantir que os objetos sejam ordenados antes de serem paginados.
        return Categoria.objects.all().order_by('nome')

