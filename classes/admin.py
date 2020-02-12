from django.contrib import admin
from classes.models import User, Student, Semester, Assignment, Course, TakenCourse

admin.site.register(User)
admin.site.register(Student)
admin.site.register(Semester)
admin.site.register(Assignment)
admin.site.register(Course)
admin.site.register(TakenCourse)