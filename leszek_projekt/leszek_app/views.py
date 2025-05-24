from django.shortcuts import render, redirect
from random import sample
from .models import Question, Code
from json import dumps, loads
from django.core.serializers import serialize
from django.http.request import HttpRequest
from django.http.response import HttpResponse, JsonResponse 
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

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

def examResults(request: HttpRequest):
    questions = loads(request.body)["questions"]
    score = 0
    questionsList = []
    # TODO: pass selected answer as well
    for questionIndex in questions:
      currentQuestion = Question.objects.filter(id=questionIndex)
      currentQuestion = loads(serialize("json", currentQuestion))[0]
      currentQuestion['fields']['selected_answer'] = questions[questionIndex] 
      if(questions[questionIndex] == currentQuestion['fields']['correct_answer']):
          score += 1
      questionsList.append(currentQuestion)
    request.session['score'] = score
    request.session['questions'] = questionsList
    return HttpResponse(serialize("json", [])) 

def displayExamResults(request: HttpRequest):
    return render(request, "results.html")

def getExamResults(request: HttpRequest):
    if request.session.has_key("score"):
        return JsonResponse({"msg": "Success", "questions": request.session['questions'], "score": request.session['score']})
    else:
        return JsonResponse({"msg": "Brak wyników ostatniego egzaminu"})
    

@login_required(login_url="/login/")
def application_form_view(request, code):
    return render(request, "application_form.html", {"code": code})


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            if "next" in request.POST:
                return redirect(request.POST.get('next'))
            return redirect("/")
    else:
        form = UserCreationForm()
    return render(request, "user/register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if "next" in request.POST:
                return redirect(request.POST.get('next'))
            return redirect("/")
    else:
        form = AuthenticationForm()
    return render(request, "user/login.html", {"form": form})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("/")
