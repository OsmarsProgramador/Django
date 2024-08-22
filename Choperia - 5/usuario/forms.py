# usuario/forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
            usuario = Usuario.objects.create(user=user, nome=user.username)
        return user

class PasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput, label='Senha')
