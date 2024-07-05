from django.contrib import admin
from .models import TestView, TestViewSubject, TestViewSection


class TestViewSectionAdmin(admin.ModelAdmin):
    # inlines = [TopicInline]

    def get_model_perms(self, request): return {}


class SectionInline(admin.StackedInline):
    model = TestViewSection
    extra = 1
    show_change_link = True


class TestViewSubjectAdmin(admin.ModelAdmin):
    inlines = [SectionInline]

    def get_model_perms(self, request): return {}


class TestSubjectInline(admin.TabularInline):
    model = TestViewSubject
    extra = 1
    inlines = [SectionInline]
    show_change_link = True


class TestViewAdmin(admin.ModelAdmin):
    inlines = [TestSubjectInline]
    list_display = ['name', 'course', 'type', 'duration', 'publish_date', 'end_date', 'is_published']
    search_fields = ['name', 'course__name', 'type']


admin.site.register(TestView, TestViewAdmin)
admin.site.register(TestViewSubject, TestViewSubjectAdmin)
admin.site.register(TestViewSection, TestViewSectionAdmin)


