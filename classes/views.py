from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import User, Course, Session, Semester
from django.views.generic import CreateView, UpdateView, DeleteView




@login_required
def home(request):

    students = Student.objects.all().count()
    staff = User.objects.filter(is_lectue=True).count()
    courses = Course.objects.all()
    current_semester = Semester.objects.get(is_current_semester=True)

    context = {
        'total_students': students,
        'total_staff': staff,
        'total_courses': courses
    }

    return render(request, 'home.html', context)

# @login_required
# def profile(request):
#     current_semester = Semester.objects.get(is_current_semester=True)

#     if request.user.is_lecturer:
#         courses = Course.objects.filter(assigned_course__lecturer__pk=request.user.id).filter(semester=current_semester)
#         return render(request, 'profile.html', {"courses": courses})
#     elif request.user.is_student:
#         student = Student.objects.get(user__pk=request.user.id)
#         courses = 


# Create your views here.
