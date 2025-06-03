from datetime import datetime
from django.shortcuts import render, redirect
from random import sample, randint  
from .models import Question, Code, QuestionApplication
from json import dumps, loads
from django.db.models import Count
from django.core.serializers import serialize
from django.http.request import HttpRequest
from django.http.response import HttpResponse, JsonResponse 
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def landing(request: HttpRequest):
    classifications = Code.objects.all()
    classifications_quantities = {}
    for c in classifications:
        classifications_quantities[c.code_name] = Question.objects.filter(code_id=c).count()
    # question_quantities = Question.objects.values('code_id__code_name').annotate(count=Count('code_id'))
    # print(list(Question.objects.values('code_id__code_name').annotate(count=Count('code_id'))))
    # print(classifications_quantities)  # Debugging
    context = {"classifications": classifications_quantities}
    return render(request, "landing.html", context)


def exam(request: HttpRequest):
    examCode = request.GET.get("code")
    count = Question.objects.filter(code_id=Code.objects.get(code_name=examCode)).count()
    if count:
        questions = []
        numbers = sample(range(1, count + 1), 40)
        for n in numbers:
            questions.append(Question.objects.get(id=n).prepare())
    
    context = {"examCode": examCode, "questions": dumps(questions)}
    return render(request, "exam.html", context)


def postExamResults(request: HttpRequest):
    questions = loads(request.body)["questions"]
    score = 0
    questionsList = []
    for questionIndex in questions:
      currentQuestion = Question.objects.filter(id=questionIndex)
      currentQuestion = loads(serialize("json", currentQuestion))[0]
      currentQuestion['fields']['selected_answer'] = questions[questionIndex] 
      if(questions[questionIndex] == currentQuestion['fields']['correct_answer']):
          score += 1
      questionsList.append(currentQuestion)
    request.session['score'] = score
    request.session['questions'] = questionsList
    request.session['date'] = datetime.now().strftime("%d/%m/%Y %H:%M")


    return HttpResponse(serialize("json", [])) 

def displayExamResults(request: HttpRequest):
    if request.session.has_key("score"):
        results = dumps({"msg": "Success", "questions": request.session['questions'], "score": request.session['score'],"date":request.session['date']})
    else:
        results = {"msg": "Brak wyników ostatniego egzaminu"}

    return render(request, "results.html", {"results": results})



@login_required(login_url="/login/")
def application_form_view(request, code):
    unanswered_questions = Question.objects.filter(code_id=Code.objects.get(code_name=code),correct_answer__isnull=True).all()
    random_q = unanswered_questions.exclude(question__in=QuestionApplication.objects.all().values('question_id__question')).order_by('?').first()
    # DEBUG
    # print(unanswered_questions.exclude(question__in=QuestionApplication.objects.all().values('question_id__question')).count())
    return render(request, "application_form.html", {"code": code,"question":random_q,"question_json":dumps(random_q.prepare())})

@login_required(login_url="/login/")
def save_correct_answer(request: HttpRequest):
    question = Question.objects.get(id = loads(request.body)["question"]["id"])
    correct_answer = loads(request.body)["question"]["correct_answer"]

    question_aplication = QuestionApplication(question_id = question,correct_answer = correct_answer,user_id=request.user,sent_at = datetime.now())
    question_aplication.save()
    return JsonResponse({"success": True})


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
