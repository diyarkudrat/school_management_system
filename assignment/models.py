from django.db import models

# Create your models here.


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    slug = models.SlugField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Assignment(models.Model):
    title = models.CharField(max_length=100)
    students = models.ManyToManyField(Student, through='Grade')
    date_assigned = models.DateField()
    date_due = models.DateField()
    date_submitted = models.DateField()
    slug = models.SlugField()

    def __str__(self):
        return self.title

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    work = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    grade = models.PositiveIntegerField()
    date_submitted = models.DateField()

    def __str__(self):
        return self.student.first_name + ' ' + self.student.last_name + ': ' + self.work.title
