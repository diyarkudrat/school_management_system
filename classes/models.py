from django.db import models
from assignment.models import Student, Grade

class Class(models.Model):
    name = models.CharField(max_length=150)
    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.name
