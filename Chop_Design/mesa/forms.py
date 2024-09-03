# mesa/forms.py
from django import forms
from django.contrib.auth.models import User
from .models import Pedido, Produto
from .models import Mesa

class SelecionarUsuarioForm(forms.Form):
    usuario = forms.ModelChoiceField(queryset=User.objects.all(), label="Selecione o Usuário")
    senha = forms.CharField(widget=forms.PasswordInput, label="Senha")

    def clean(self):
        cleaned_data = super().clean()
        usuario = cleaned_data.get('usuario')
        senha = cleaned_data.get('senha')

        if usuario and not usuario.check_password(senha):
            raise forms.ValidationError("Senha incorreta. Tente novamente.")
        return cleaned_data

class AdicionarProdutoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['produto', 'quantidade']
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['produto'].queryset = Produto.objects.filter(estoque__gt=0)

class MesaForm(forms.ModelForm):
    class Meta:
        model = Mesa
        fields = ['numero', 'capacidade', 'usuario']
        