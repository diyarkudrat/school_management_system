"""models.py"""
from django.contrib.auth.models import User
from django.db import models


A = "A"
B = "B"
C = "C"
D = "D"
F = "F"
PASS = "PASS"
FAIL = "FAIL"

GRADE = (
    (A, 'A'),
    (B, 'B'),
    (C, 'C'),
    (D, 'D'),
    (F, 'F'),
)

FIRST = "First"
SECOND = "Second"

SEMESTER = (
        (FIRST, "First"),
        (SECOND, "Second"),
)


class User(User):
    student_access = models.BooleanField(default=False)
    teacher_access = models.BooleanField(default=False)

    def get_full_name(self):
        full_name = self.username
        if self.first_name and self.last_name:
            full_name = self.first_name + " " + self.last_name
        return full_name

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id_number = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.id_number

class Session(models.Model):
    session = models.CharField(max_length=200, unique=True)
    is_current_session = models.BooleanField(default=False, blank=True, null=True)
    next_session_begins = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.session

class Semester(models.Model):
    semester = models.CharField(max_length=10, choices=SEMESTER, blank=True)
    is_current_semester = models.BooleanField(default=False, blank=True, null=True)
    session = models.ForeignKey(Session, on_delete=models.CASCADE, blank=True, null=True)
    next_semester_begins = models.DateField(null=True,blank=True)

    def __str__ (self):
        return self.semester


class Course(models.Model):
    course_name = models.CharField(max_length=150)
    course_unit = models.CharField(max_length=150)
    description = models.CharField(max_length=250)
    semester = models.CharField(choices=SEMESTER, max_length=200)
    is_elective = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.course_name

    def get_absolute_url(self):
        return reverse('course_list', kwargs={'pk': self.pk})

    def get_total_unit(self):
        t = 0
        total = Course.objects.all()
        for unit in total:
            t += unit
        return unit


    def __str__(self):
        return self.course_name
