from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import User, Course, Semester, Student
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .decorators import student_required
from django.utils.decorators import method_decorator




@login_required
def home(request):

    students = Student.objects.all().count()
    staff = User.objects.filter(teacher_access=True).count()
    courses = Course.objects.all()
    current_semester = Semester.objects.get(is_current_semester=True)

    context = {
        'total_students': students,
        'total_staff': staff,
        'total_courses': courses
    }

    return render(request, 'home.html', context)

@login_required
def profile(request):
     
    current_semester = Semester.objects.get(is_current_semester=True)

    if request.user.is_lecturer:
        courses = Course.objects.filter(assigned_course__lecturer__pk=request.user.id).filter(semester=current_semester)
        return render(request, 'profile.html', {"courses": courses})
    elif request.user.is_student:
        student_info = Student.objects.get(user__pk=request.user.id)
        courses = TakenCourse.objects.filter(student__user__id=request.user.id)
        context = {
            'courses': courses,
            'student_info': student_info,
        }
        return render(request, 'profile.html', context)
    else:
        staff = User.objects.filter(teacher_access=True)
        return render(request, 'profile.html', { 'staff': staff })

@login_required
def user_profile(request, id):
    if request.user.id == id:
        return redirect('/profile/')

    current_semester = Semester.objects.get(is_current_semester=True)
    user = User.objects.get(pk=id)
    if user.teacher_access:
        courses = Course.objects.filter(allocated_course__lecturer__pk=id).filter(semester=current_semester)
        context = {
            'user': user,
            'courses': courses,
        }
        return render(request, 'user_profile.html', context)
    elif user.student_access:
        level = Student.objects.get(user__pk=id)
        courses = TakenCourse.objects.filter(student__user__id=id, course__level=level.level)
        context = {
            "user_type": "student",
            'courses': courses,
            'user':user,
        }
        return render(request, 'user_profile.html', context)
    else:
        context = {
            "user": user,
            "user_type": "superuser"
            }
        return render(request, 'user_profile.html', context)

@login_required
def profile_update(request):

    user = request.user.id
    user = User.objects.get(pk=user)
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.email = form.cleaned_data.get('email')
            user.phone = form.cleaned_data.get('phone')
            user.address = form.cleaned_data.get('address')
            if request.FILES:
                user.picture = request.FILES['picture']
            user.save()
            messages.success(request, 'profile successfully edited.')
            return redirect("/profile/")
    else:
        form = ProfileForm(instance=user, initial={
            'firstname': user.first_name,
            'lastname': user.last_name,
            'email': user.email,
            'phone': user.phone,
            'picture': user.picture,
            })

    return render(request, 'profile_update.html', {'form': form})


@method_decorator([login_required], name='dispatch')
class CourseListView(ListView):
    
    model = Course

    def get(self, request):
        courses = self.get_queryset()
        return render(request, 'course_list.html', {
          'courses': courses,
        })


@login_required
# @lecturer_required
def student_list(request):
    
    students = Student.objects.all()
    user_type = "Student"

    context = {
        'students': students,
        'user_type': user_type,
    }
    return render(request, 'student_list.html', context)

@login_required
# @lecturer_required
def staff_list(request):

    staff = User.objects.filter(teacher_access=True)
    user_type = 'Staff'

    context = {
        'staff': staff,
        'user_type': user_type,
    }
    return render(request, 'staff_list.html', context)





