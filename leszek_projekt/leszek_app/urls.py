from . import views
from django.urls import path, include

urlpatterns = [
    path("", views.landing, name="landing"),
    # path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path("exam/", views.exam, name="exam"),
    path("results", views.postExamResults, name="postExamResults"),
    path("getResults", views.displayExamResults, name="displayExamResults"),
    path('application_form/<str:code>',views.application_form_view,name = 'application_form'),
    path('logout/', views.logout_view, name="logout"),
    path('updateQuestion',views.save_correct_answer, name='save_correct_answer'),
    path('cke/zdajacy/',views.cke_zdajacy,name='cke_zdajacy'),
    path('cke/exam/',views.cke_exam,name='cke_exam'),
    path('cke/answer/',views.cke_answer,name='cke_answer'),
    path('cke/exam_instrukcja',views.cke_exam_instruction, name='cke_exam_instruction')
]
