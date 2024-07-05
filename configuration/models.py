from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100)
    subjects = models.ManyToManyField('Subject', related_name='courses')

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=100)
    prefix = models.CharField(max_length=3)

    def __str__(self):
        return self.name



