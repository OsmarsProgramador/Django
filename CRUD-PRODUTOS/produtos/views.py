# produtos/views.py
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from .models import Produto
from .forms import ProdutoForm

class ProdutoListView(ListView):
    model = Produto
    template_name = 'produtos/produto_list.html'
    context_object_name = 'produtos'
    paginate_by = 5

    def get_queryset(self):
        return Produto.objects.all().order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = Paginator(self.get_queryset(), self.paginate_by)
        page = self.request.GET.get('page')

        try:
            produtos = paginator.page(page)
        except PageNotAnInteger:
            produtos = paginator.page(1)
        except EmptyPage:
            produtos = paginator.page(paginator.num_pages)
        except TypeError:
            produtos = paginator.page(1)

        context['produtos'] = produtos
        return context

class ProdutoCreateView(CreateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'produtos/produto_form.html'
    success_url = reverse_lazy('produto_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.htmx:
            return JsonResponse({
                'id': self.object.id,
                'nome': self.object.nome,
                'descricao': self.object.descricao,
                'preco': self.object.preco,
                'quantidade': self.object.quantidade,
            })
        return response

class ProdutoUpdateView(UpdateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'produtos/produto_form.html'
    success_url = reverse_lazy('produto_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.htmx:
            return JsonResponse({
                'id': self.object.id,
                'nome': self.object.nome,
                'descricao': self.object.descricao,
                'preco': self.object.preco,
                'quantidade': self.object.quantidade,
            })
        return response

class ProdutoDeleteView(DeleteView):
    model = Produto
    template_name = 'produtos/produto_confirm_delete.html'
    success_url = reverse_lazy('produto_list')

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        if self.request.htmx:
            return JsonResponse({'id': self.object.id})
        return response


