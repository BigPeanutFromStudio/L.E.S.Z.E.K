from django.contrib import admin

# Register your models here.
from .models import Code , Question, QuestionApplication

admin.site.register([Code])

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'code_ID', 'media', 'question')
    search_fields = ('question', 'answer_a', 'answer_b', 'answer_c', 'answer_d')
    list_filter = ('code_ID',)

@admin.register(QuestionApplication)
class QuestionApplicationAdmin(admin.ModelAdmin):
    list_display = ('questionID', 'user_ID', 'correct_answer', 'sent_at')
    search_fields = ('questionID__question', 'user_ID__username')
    list_filter = ('sent_at',)
