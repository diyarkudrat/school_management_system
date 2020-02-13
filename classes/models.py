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

COMMENT = (
    (PASS, 'PASS'),
    (FAIL, 'FAIL')
)

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

Homework = 'Homework'
Quiz = 'Quiz'
Test ='Test'
Midterm ='Midterm'
Final = 'Final'
Participation = 'Participation'


ASSIGNMENT_TYPES = (
        (Homework, 'Homework'),
        (Quiz, 'Quiz'),
        (Test, 'Test'),
        (Midterm, 'Midterm'),
        (Final, 'Final'),
        (Participation, 'Participation')

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

# class Session(models.Model):
#     session = models.CharField(max_length=200, unique=True)
#     is_current_session = models.BooleanField(default=False, blank=True, null=True)
#     next_session_begins = models.DateField(blank=True, null=True)

#     def __str__(self):
#         return self.session

class Semester(models.Model):
    semester = models.CharField(max_length=10, choices=SEMESTER, blank=True)
    is_current_semester = models.BooleanField(default=False, blank=True, null=True)
    # session = models.ForeignKey(Session, on_delete=models.CASCADE, blank=True, null=True)
    next_semester_begins = models.DateField(null=True,blank=True)

    def __str__ (self):
        return self.semester

class Assignment(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    course = models.ForeignKey('Course', on_delete=models.CASCADE, blank=True, null=True)
    assignment_type = models.CharField(max_length=30, choices=ASSIGNMENT_TYPES, blank=True)
    total_points = models.PositiveIntegerField(blank=True, null=True, default=0)
    assigned_date = models.DateField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    course_name = models.CharField(max_length=150)
    description = models.CharField(max_length=250)
    assigments = models.ManyToManyField(Assignment, blank=True, null=True, related_name="course_assignments")

    def __str__(self):
        return self.course_name

    def get_absolute_url(self):
        return reverse('course_list', kwargs={'pk': self.pk})


class TakenCourse(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='taken_courses')
    course_average = models.PositiveIntegerField(blank=True, null=True, default=0)
    exam = models.PositiveIntegerField(blank=True, null=True, default=0)
    total = models.PositiveIntegerField(blank=True, null=True, default=0)
    grade = models.CharField(choices=GRADE, max_length=1, blank=True)
    comment = models.CharField(choices=COMMENT, max_length=200, blank=True)

    def get_absolute_url(self):
        return reverse('update_score', kwargs={'pk': self.pk})


    def get_total(self, course_average, exam):
        return int(course_average) + int(exam)

    def get_grade(self, course_average, exam):
    	total = int(course_average) + int(exam)
    	if total >= 90:
    		grade = A
    	elif total >= 80:
    		grade = B
    	elif total >=70:
    		grade = C
    	elif total >=60:
    		grade = D
    	else:
    	 	grade = F
    	return grade

    def get_comment(self, grade):
        if not grade == "F":
            comment = PASS
        else:
            comment = FAIL
        return comment
