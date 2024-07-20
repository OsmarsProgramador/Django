# produto/views.py
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Produto, Categoria
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class ProdutoListView(LoginRequiredMixin, ListView):
    """
    -model: Especifica o modelo a ser listado (neste caso, Produto).
    -template_name: Indica o template a ser usado para renderizar a listagem.
    -context_object_name: Define o nome do objeto a ser passado para o template.
    -paginate_by: Determina a quantidade de itens a serem exibidos por página.
    """
    model = Produto
    template_name = 'produto/produto_list.html'
    context_object_name = 'produtos'
    paginate_by = 10

    def get_queryset(self): # garantir que os objetos sejam ordenados antes de serem paginados.
        return Produto.objects.all().order_by('nome_produto')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        return context

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
    success_url = reverse_lazy('produto:produto_list')

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
    success_url = reverse_lazy('produto:produto_list')

class ProdutoDeleteView(LoginRequiredMixin, DeleteView):
    """
    O model define o modelo a ser usado (nesse caso, Produto).
    template_name especifica o template a ser usado para renderizar a página de confirmação de exclusão.
    success_url define a URL para a qual o usuário será redirecionado após a exclusão bem-sucedida de um produto.
    """
    model = Produto
    template_name = 'produto/produto_confirm_delete.html'
    success_url = reverse_lazy('produto:produto_list')'''

class CategoriaListView(LoginRequiredMixin, ListView):
    model = Categoria
    template_name = 'produto/categoria_list.html'
    context_object_name = 'categorias'
    paginate_by = 10

    def get_queryset(self): # garantir que os objetos sejam ordenados antes de serem paginados.
        return Categoria.objects.all().order_by('nome')

