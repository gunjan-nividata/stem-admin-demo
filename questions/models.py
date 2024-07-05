from django.db import models
from froala_editor.fields import FroalaField


class Question(models.Model):
    title = models.CharField(max_length=255)
    description = FroalaField(null=True)
    subject = models.ForeignKey('configuration.Subject', on_delete=models.CASCADE, null=True)
    answer = models.CharField(max_length=50, null=True)
    explanation = FroalaField()
    question_id = models.CharField(max_length=100, unique=True, null=True)
    question_type = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title
