from django.contrib import admin
from .models import User, Session, Semester, Course
# Register your models here.

admin.site.register(User)
admin.site.register(Session)
admin.site.register(Semester)
admin.site.register(Course)
