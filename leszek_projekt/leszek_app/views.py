from django.shortcuts import render
from random import sample
from .models import Question, Code
from json import dumps
from django.core.serializers import serialize
from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponseNotFound


# Create your views here.
def landing(request: HttpRequest):
    classifications = Code.objects.all()
    context = {"classifications": classifications}
    return render(request, "landing.html", context)


def exam(request: HttpRequest):
    examCode = request.GET.get("code")
    context = {"examCode": examCode}
    return render(request, "exam.html", context)


def getExam(request: HttpRequest, examCode):
    count = Question.objects.filter(code_ID=Code.objects.get(codeName=examCode)).count()
    if count:
        questions = []
        numbers = sample(range(1, count + 1), 40)
        for n in numbers:
            questions.append(Question.objects.get(id=n).prepare())
        return HttpResponse(dumps(questions))
    else:
        # we know it should be 404 but ... it is easier
        return HttpResponse(serialize("json",[]))
