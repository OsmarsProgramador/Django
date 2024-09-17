# produto/forms.py
from django import forms
from .models import Produto, Categoria

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'preco', 'venda', 'codigo', 'estoque', 'estoque_total', 'imagem', 'categoria']  # Incluímos 'categoria'

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome']  # Incluímos apenas o campo 'nome'

