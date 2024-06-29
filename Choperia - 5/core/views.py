# core/views.py
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'core/index.html'


"""from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request, 'index.html')
"""

