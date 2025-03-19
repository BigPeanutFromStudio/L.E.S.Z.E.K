from . import views
from django.urls import path


urlpatterns = [
    path("", views.landing, name="landing"),
    path("exam/", views.exam, name="exam"),
    path("getExam/<str:examCode>", views.getExam, name="getExam")
]
