"""models.py"""

from django.db import models
from assignment.models import Student, Grade


A = "A"
B = "B"
C = "C"
D = "D"
F = "F"
PASS = "PASS"
Fail = "FAIL"

GRADE = (
    (A, 'A'),
    (B, 'B'),
    (C, 'C'),
    (D, 'D'),
    (F, 'F'),
)

LEVEL = (

        ("100", 100),
        ("200", 200),
        ("300", 300),
        ("400", 400),
        ("500", 500),
)
FIRST = "First"
SECOND = "Second"

SEMESTER = (
        (FIRST, "First"),
        (SECOND, "Second"),
)


class User(User):
    student = models.BooleanField(default=False)
    teacher = models.BooleanField(default=False)
    email = models.EmailField(blank=True,null=True)

    def get_full_name(self):
        full_name = self.username
        if self.first_name and self.last_name:
            full_name = self.first_name + " " + self.last_name
        return full_name

class Session(models.Model):
    session = models.CharField(max_length=200, unique=True)
    is_current_session = models.BooleanField(default=False, blank=true, null=True)
    next_session_begins = models.DataField(black=true, null=True)

    def __str__(self):
        return self.session


class Course(models.Model):
    name = models.CharField(max_length=150)
    students = models.ManyToManyField(Student)


    def __str__(self):
        return self.name
