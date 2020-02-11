from django.contrib import admin
from .models import User, Semester, Course, Assignment, Student
# Register your models here.

admin.site.register(User)
# admin.site.register(Session)
admin.site.register(Semester)
admin.site.register(Course)
admin.site.register(Assignment)
admin.site.register(Student)
