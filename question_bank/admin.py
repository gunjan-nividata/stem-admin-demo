from django.contrib import admin
from .models import Heading, Topic, Module
from questions.models import Question


class TopicInline(admin.TabularInline):
    model = Topic
    extra = 0
    show_change_link = True


class HeadingAdmin(admin.ModelAdmin):
    list_display = ['name', 'course', 'subject']
    inlines = [TopicInline]


class QuestionInline(admin.StackedInline):
    model = Question


class ModuleInline(admin.StackedInline):
    model = Module
    show_change_link = True
    filter_horizontal = ['questions']
    extra = 0
    inlines = [QuestionInline]


class TopicAdmin(admin.ModelAdmin):
    inlines = [ModuleInline]


class ModuleAdmin(admin.ModelAdmin):
    list_display = ['topic']
    filter_horizontal = ['questions']
    search_fields = ['questions__question_id']


admin.site.register(Heading, HeadingAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Module, ModuleAdmin)
