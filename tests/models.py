from django.db import models
from froala_editor.fields import FroalaField

from configuration.models import Course
from questions.models import Question


class Strategy(models.Model):
    name = models.CharField(max_length=100)
    question_type = models.CharField(max_length=50, choices=[('MCQ', 'MCQ'), ('IBQ', 'IBQ')])
    total_questions = models.IntegerField()
    minimum_questions = models.IntegerField()
    marks_per_question = models.FloatField()
    negative_marks = models.FloatField(default=0)
    instructions = models.TextField()

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Strategy"
        verbose_name_plural = "Strategies"


class TestType(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Test Type'
        verbose_name_plural = 'Test Types'

    def __str__(self):
        return self.name


class Test(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    type = models.ForeignKey(TestType, on_delete=models.CASCADE)
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


class TestSubject(models.Model):
    name = models.CharField(max_length=100)
    test = models.ForeignKey(Test, related_name='subjects', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Test Subject'
        verbose_name_plural = 'Test Subjects'


class TestSection(models.Model):
    name = models.CharField(max_length=100)
    subject = models.ForeignKey(TestSubject, related_name='sections', on_delete=models.CASCADE)
    strategy = models.ForeignKey(Strategy, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.subject}'

    class Meta:
        verbose_name = 'Test Section'
        verbose_name_plural = 'Test Sections'


class TestTopic(models.Model):
    name = models.CharField(max_length=100)
    section = models.ForeignKey(TestSection, related_name='topics', on_delete=models.CASCADE)
    questions = models.ManyToManyField(Question, related_name='sections')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Topic'
        verbose_name_plural = 'Topics'
