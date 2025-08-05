from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from unfold.admin import ModelAdmin
from django.http import HttpRequest
from django.db.models import QuerySet
# Register your models here.
from .models import Code, Question, QuestionApplication
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group
from unfold.decorators import action
from unfold.contrib.import_export.forms import ExportForm, ImportForm, SelectableFieldsExportForm

from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm

from unfold.contrib.filters.admin import (
    AutocompleteSelectFilter,
    AutocompleteSelectMultipleFilter
)


admin.site.unregister(User)
admin.site.unregister(Group)

@action(description='Zatwierdź')
def aprove_application(self: ModelAdmin, request: HttpRequest, queryset):
    for query in queryset:
        print(query.question_id.id)
        question = Question.objects.get(id= query.question_id.id)
        question.correct_answer = query.correct_answer
        question.save()
        query.delete()


@admin.register(Question)
class QuestionAdmin(ModelAdmin, ImportExportModelAdmin):
    list_display = ('id', 'code_id', 'media', 'question')
    search_fields = ('question', 'answer_a', 'answer_b', 'answer_c', 'answer_d')
    list_filter = ('code_id',('correct_answer',admin.EmptyFieldListFilter))
    import_form_class = ImportForm
    export_form_class = ExportForm

@admin.register(QuestionApplication)
class QuestionApplicationAdmin(ModelAdmin):
    list_display = ('question_id', 'user_id', 'question_id__question', 'correct_answer', 'sent_at')
    search_fields = ('question_id__question', 'user_id__username')
    list_filter = ('sent_at', 'question_id__code_id',)
    actions = [aprove_application]

@admin.register(Code)
class CodeAdmin(ModelAdmin):
    ...

@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    # Forms loaded from `unfold.forms`
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm


