from django.contrib import admin
from .models import Session, Semester, Course
# Register your models here.

admin.site.register(Session)
admin.site.register(Semester)
admin.site.register(Course)
