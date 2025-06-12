from django.contrib import admin
from django.http import HttpRequest
from django.db.models import QuerySet

# Register your models here.
from .models import Code, Question, QuestionApplication

# TODO: Add import button

admin.site.register([Code])

@admin.action(description='Zatwierdź')
def aprove_application(self: admin.ModelAdmin, request: HttpRequest, queryset):
    for query in queryset:
        print(query.question_id.id)
        question = Question.objects.get(id= query.question_id.id)
        question.correct_answer = query.correct_answer
        question.save()
        query.delete()


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'code_id', 'media', 'question')
    search_fields = ('question', 'answer_a', 'answer_b', 'answer_c', 'answer_d')
    list_filter = ('code_id',('correct_answer',admin.EmptyFieldListFilter))

@admin.register(QuestionApplication)
class QuestionApplicationAdmin(admin.ModelAdmin):
    list_display = ('question_id', 'user_id', 'question_id__question', 'correct_answer', 'sent_at')
    search_fields = ('question_id__question', 'user_id__username')
    list_filter = ('sent_at', 'question_id__code_id',)
    actions = [aprove_application]

