from django import forms

class AdicionarItemForm(forms.Form):
    produto_codigo = forms.CharField(label='Código do Produto', max_length=100)
    quantidade = forms.IntegerField(label='Quantidade')
