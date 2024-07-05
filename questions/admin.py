from django.contrib import admin
from .models import Question


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['title', 'subject', 'question_id']
    search_fields = ['title', 'question_id']
    list_filter = ['subject']


admin.site.register(Question, QuestionAdmin)
