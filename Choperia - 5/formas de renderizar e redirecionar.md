Em uma classe de uma views.py em um projeto Django, você pode utilizar 
as seguintes formas de renderizar e redirecionar:

Renderizar um template:

Usando a função render() do Django:

from django.shortcuts import render

class MyView(View):
    def get(self, request):
        return render(request, 'my_template.html', {'my_data': 'some_data'})
Usando o método render() da classe genérica TemplateView:

from django.views.generic import TemplateView

class MyView(TemplateView):
    template_name = 'my_template.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_data'] = 'some_data'
        return context
Redirecionar para outra URL:

Usando a função redirect() do Django:

from django.shortcuts import redirect

class MyView(View):
    def post(self, request):
        # Alguma lógica de processamento
        return redirect('my_named_url')
Usando o método redirect() da classe genérica RedirectView:

from django.views.generic import RedirectView

class MyRedirectView(RedirectView):
    url = 'my_named_url'
Redirecionar para a URL de uma view específica:

Usando a função reverse() do Django para gerar a URL:

from django.shortcuts import redirect
from django.urls import reverse

class MyView(View):
    def post(self, request):
        # Alguma lógica de processamento
        return redirect(reverse('my_named_url'))
Redirecionar para a URL de uma view específica, passando argumentos:

Usando a função reverse() do Django e passando os argumentos:

from django.shortcuts import redirect
from django.urls import reverse

class MyView(View):
    def post(self, request, pk):
        # Alguma lógica de processamento
        return redirect(reverse('my_named_url', args=[pk]))
Essas são as principais formas de renderizar templates e redirecionar 
em uma classe de uma views.py em um projeto Django. 
A escolha da abordagem dependerá do contexto e das necessidades específicas da sua aplicação.