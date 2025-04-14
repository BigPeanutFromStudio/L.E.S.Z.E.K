from . import views
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.landing, name="landing"),
    path("exam/", views.exam, name="exam"),
    path("getExam/<str:examCode>", views.getExam, name="getExam"),
    path("results", views.examResults, name="examResults"),
    path("getResults", views.displayExamResults, name="displayExamResults"),
    path("getExamResults", views.getExamResults, name="getExamResults")
]