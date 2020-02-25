from django.contrib import admin
from .models import Attendance, CourseAttendance

admin.site.register(Attendance)
admin.site.register(CourseAttendance)
