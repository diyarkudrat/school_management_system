from django.db import models
from classes.models import Course, Student

attendance_choices = (
    ('absent', 'Absent'),
    ('present', 'Present'),
    ('excused', 'Excused'),
    ('tardy', 'Tardy')
)

class Attendance(models.Model):

    course = models.ForeignKey(Course, on_delete = models.CASCADE)
    student = models.ForeignKey(Student, on_delete = models.CASCADE)

    attendance_status = models.CharField(max_length=20, choices=attendance_choices, blank=True)

    def __str__(self):
        return self.student.user.first_name + ' ' + self.student.user.last_name
