from django.db import models
from froala_editor.fields import FroalaField

from configuration.models import Course
from questions.models import Question





class TestView(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    type = models.ForeignKey('tests.TestType', on_delete=models.CASCADE)
    duration = models.IntegerField(help_text='Enter duration in minutes')
    publish_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_published = models.BooleanField(default=False)
    instructions = FroalaField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Test'
        verbose_name_plural = 'Tests'


class TestViewSubject(models.Model):
    name = models.CharField(max_length=100)
    test = models.ForeignKey(TestView, related_name='viewsubjects', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'TestView Subject'
        verbose_name_plural = 'TestView Subjects'


class TestViewSection(models.Model):
    name = models.CharField(max_length=100)
    subject = models.ForeignKey(TestViewSubject, related_name='viewsections', on_delete=models.CASCADE)
    strategy = models.ForeignKey('tests.Strategy', on_delete=models.CASCADE)
    questions = models.ManyToManyField(Question, related_name='viewsections')


    def __str__(self):
        return f'{self.name} - {self.subject}'

    class Meta:
        verbose_name = 'TestView Section'
        verbose_name_plural = 'TestView Sections'

