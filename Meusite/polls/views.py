from django.shortcuts import get_object_or_404, render
# from django.http import Http404
# from django.template import loader
from django.db.models import F
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Question, Choice


"""def index(request):
    return HttpResponse("Olá Mundo. Você está no índice de pesquisas.")"""

"""def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.question_text for q in latest_question_list])
    return HttpResponse(output)"""

"""def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))"""

"""def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)"""

"""def detail(request, question_id):
    return HttpResponse("Você está vendo a pergunta %s." % question_id)"""

"""def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})"""

"""def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})"""

"""def results(request, question_id):
    response = "Você está vendo os resultados da pergunta %s."
    return HttpResponse(response % question_id)
"""

"""def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})"""

"""def vote(request, question_id):
    return HttpResponse("Você está votando na pergunta %s." % question_id)"""

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Reexibir formulário de votação de pergunta.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "Você não selecionou uma opção.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Sempre retorne um HttpResponseRedirect após negociar com sucesso
        # com dados POST. Isso evita que os dados sejam lançados duas vezes se um
        # usuário clica no botão Voltar.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))