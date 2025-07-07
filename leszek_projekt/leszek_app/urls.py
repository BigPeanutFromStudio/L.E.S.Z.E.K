from . import views
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path("", views.landing, name="landing"),
    # path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path("exam/", views.exam, name="exam"),
    path("results", views.post_exam_results, name="post_exam_results"),
    path("getResults", views.display_exam_results, name="display_exam_results"),
    path('application-form/<str:code>',views.application_form_view,name = 'application_form'),
    path('logout/', views.logout_view, name="logout"),
    path('updateQuestion',views.save_correct_answer, name='save_correct_answer'),
    path('cke/login/',views.cke_login,name='cke_login'),
    path('cke/egzamin/',views.cke_exam,name='cke_exam'),
    path('cke/odpowiedz/',views.cke_answer,name='cke_answer'),
    path('cke/exam_instrukcja',views.cke_exam_instruction, name='cke_exam_instruction'),
    path('polityka-prywatnosci/',views.privacy_policy,name='privacy_policy')
] + debug_toolbar_urls()
