from . import views
from django.urls import path


urlpatterns = [
    path("landing/", views.landing, name="landing"),
    path("exam/", views.exam, name="exam"),
]
