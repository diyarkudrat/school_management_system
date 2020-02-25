from django.db import models
from classes.models import Course, Student, User

attendance_choices = (
    ('absent', 'Absent'),
    ('present', 'Present'),
    ('excused', 'Excused'),
    ('tardy', 'Tardy')
)


class CourseAttendance(models.Model):

    course = models.ForeignKey(Course, on_delete = models.CASCADE)
    date = models.DateField(null=True)
    students = models.ManyToManyField(Student, through='Attendance', null=True)
    # students = models.ManyToManyField(
    #     'classes.Student',
    #     through='Attendance',
    #     through_fields=('course', 'student'),
    # )

class Attendance(models.Model):

    course = models.ForeignKey(CourseAttendance, on_delete = models.CASCADE, null=True)
    student = models.ForeignKey(Student, on_delete = models.CASCADE)

    attendance_status = models.CharField(max_length=20, choices=attendance_choices, blank=True)

    def __str__(self):
        return self.student.user.first_name + ' ' + self.student.user.last_name