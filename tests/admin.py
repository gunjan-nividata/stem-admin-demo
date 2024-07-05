from django.contrib import admin
from .models import Strategy, Test, TestSubject, TestSection, TestTopic, TestType


class TestTopicAdmin(admin.ModelAdmin):
    def get_model_perms(self, request): return {}


class TopicInline(admin.StackedInline):
    model = TestTopic
    filter_horizontal = ['questions']
    extra = 1
    show_change_link = True


class TestSectionAdmin(admin.ModelAdmin):
    inlines = [TopicInline]

    def get_model_perms(self, request): return {}


class SectionInline(admin.StackedInline):
    model = TestSection
    extra = 1
    show_change_link = True


class TestSubjectAdmin(admin.ModelAdmin):
    inlines = [SectionInline]

    def get_model_perms(self, request): return {}


class TestSubjectInline(admin.TabularInline):
    model = TestSubject
    extra = 1
    inlines = [SectionInline]
    show_change_link = True


class TestAdmin(admin.ModelAdmin):
    inlines = [TestSubjectInline]
    list_display = ['name', 'course', 'type', 'duration', 'publish_date', 'end_date', 'is_published']
    search_fields = ['name', 'course__name', 'type']


admin.site.register(Test, TestAdmin)
admin.site.register(Strategy)
admin.site.register(TestSubject, TestSubjectAdmin)
admin.site.register(TestSection, TestSectionAdmin)
admin.site.register(TestTopic, TestTopicAdmin)
admin.site.register(TestType)
