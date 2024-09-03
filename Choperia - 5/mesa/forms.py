# mesa/forms.py
from django import forms
from .models import Mesa
from produto.models import Produto

class MesaForm(forms.ModelForm):
    class Meta:
        model = Mesa
        # fields = ['nome']
        fields = ['nome', 'itens', 'status', 'pedido', 'usuario']  # Certifique-se de usar campos válidos

    def clean_nome(self):
        nome = self.cleaned_data['nome']
        if nome.isdigit():
            nome = str(nome).zfill(2)
        if Mesa.objects.filter(nome=nome).exists():
            raise forms.ValidationError("Já existe uma mesa com este nome.")
        return nome

""" Criar o Formulário para Adicionar Itens
Este formulário permitirá que o usuário selecione um produto 
e a quantidade a ser adicionada à mesa.
Nesse caso uma pagina seria renderizada no formato de formulário """
class AdicionarItemForm(forms.Form):
    produto = forms.ModelChoiceField(queryset=Produto.objects.all(), label="Produto")
    quantidade = forms.IntegerField(min_value=1, initial=1, label="Quantidade")

