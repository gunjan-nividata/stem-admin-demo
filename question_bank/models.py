from django.db import models
from froala_editor.fields import FroalaField


class Heading(models.Model):
    name = models.CharField(max_length=50)
    course = models.ForeignKey('configuration.Course', on_delete=models.CASCADE)
    subject = models.ForeignKey('configuration.Subject', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'heading'
        verbose_name_plural = 'headings'

    def __str__(self):
        return f'{self.name} - {self.course} - {self.subject}'


class Topic(models.Model):
    name = models.CharField(max_length=50)
    heading = models.ForeignKey(Heading, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.heading}'


class Module(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(verbose_name='module_image')
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    key_topics = FroalaField()
    access_type = models.CharField(max_length=10, choices=[('Free', 'Free'), ('Pro', 'Pro')])
    questions = models.ManyToManyField('questions.Question', related_name='modules')

    def __str__(self):
        return f'{self.name}'



