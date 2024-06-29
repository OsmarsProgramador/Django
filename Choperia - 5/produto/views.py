# produto/views.py
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Produto, Categoria
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class ProdutoListView(LoginRequiredMixin, ListView):
    model = Produto
    template_name = 'produto/produto_list.html'
    context_object_name = 'produtos'
    paginate_by = 10

class ProdutoCreateView(LoginRequiredMixin, CreateView):
    model = Produto
    fields = '__all__'
    template_name = 'produto/produto_form.html'
    success_url = reverse_lazy('produto:produto_list')

class ProdutoUpdateView(LoginRequiredMixin, UpdateView):
    model = Produto
    fields = '__all__'
    template_name = 'produto/produto_form.html'
    success_url = reverse_lazy('produto:produto_list')

class ProdutoDeleteView(LoginRequiredMixin, DeleteView):
    model = Produto
    template_name = 'produto/produto_confirm_delete.html'
    success_url = reverse_lazy('produto:produto_list')

class CategoriaListView(LoginRequiredMixin, ListView):
    model = Categoria
    template_name = 'produto/categoria_list.html'
    context_object_name = 'categorias'
    paginate_by = 10

