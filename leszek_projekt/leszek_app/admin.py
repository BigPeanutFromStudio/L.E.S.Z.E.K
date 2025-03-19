from django.contrib import admin

# Register your models here.
from .models import Code , Question, QuestionApplication

admin.site.register([Code, Question, QuestionApplication])
