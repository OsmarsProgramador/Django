# core/views.py
# from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin # Serve para verificar se um usuario está logado

class IndexView(LoginRequiredMixin, TemplateView): # TemplateView funciona só para renderizar
    template_name = 'core/index.html'


