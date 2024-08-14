# mesa/forms.py
from django import forms
from .models import Mesa

class MesaForm(forms.ModelForm):
    class Meta:
        model = Mesa
        fields = ['nome']

    def clean_nome(self):
        nome = self.cleaned_data['nome']
        if nome.isdigit():
            nome = str(nome).zfill(2)
        if Mesa.objects.filter(nome=nome).exists():
            raise forms.ValidationError("Já existe uma mesa com este nome.")
        return nome
