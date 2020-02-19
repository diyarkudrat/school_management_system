from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import User, Course, Semester, Student, Assignment, TakenCourse
from django.views.generic import CreateView, UpdateView, DeleteView, View
from django.views.generic.list import ListView
from .decorators import student_required
from django.utils.decorators import method_decorator
from .decorators import lecturer_required, student_required
from .forms import CourseForm, AssignmentForm




def landing_page(request):
    return render(request, 'landing.html')

def about_page(request):
    return render(request, 'about.html')

def contact_page(request):
    return render(request, 'contact.html')

@login_required
def home(request):

    students = Student.objects.all().count()
    staff = User.objects.filter(teacher_access=True).count()
    courses = Course.objects.all()
    # current_semester = Semester.objects.get(is_current_semester=True)

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
    
    model = TakenCourse

    def get(self, request):
        courses = self.get_queryset()
        return render(request, 'grades.html', {
          'courses': courses,
        })

@method_decorator([login_required], name='dispatch')
class CourseCreateView(CreateView):

    model = Course

    def get(self, request, *args, **kwargs):
        context = {'form': CourseForm()}
        return render(request, 'add-course.html', context)

    def post(self, request, *args, **kwargs):
        form = CourseForm(request.POST)
        if form.is_valid():
            player = form.save()
            return HttpResponseRedirect('course-list-page')

        return render(request, 'add-course.html', {'form': form})
        
@method_decorator([login_required], name='dispatch')
class CourseDetailView(View):

    def get(self, request, *args, **kwargs):
        course = get_object_or_404(Course, pk=kwargs['pk'])
        specific_assignments = Assignment.objects.filter(course=course)
        context = {'course': course, 'specific_assignments': specific_assignments}
        return render(request, 'course_detail.html', context)

@method_decorator([login_required], name='dispatch')
class CourseEditView(UpdateView):
    model = Course 
    fields = ['course_name', 'description']

    template_name = 'course_edit.html'
    success_url = reverse_lazy('course-list-page')

@method_decorator([login_required], name='dispatch')
class CourseDeleteView(DeleteView):

    model = Course
    template_name = 'course_delete.html'
    success_url = reverse_lazy('course-list-page')

@method_decorator([login_required], name='dispatch')
class AssignmentListView(ListView):

    def get(self, request, *args, **kwargs):
        course = get_object_or_404(Course, pk=kwargs['pk'])
        assignments = Assignment.objects.filter(assignment__in=assignments, course=course)
        context = {'course': course, 'assignments': assignments}
        return render(request, 'assignments_list.html', context)

@method_decorator([login_required], name='dispatch')
class AssignmentCreateView(CreateView):

    model = Assignment

    def get(self, request, *args, **kwargs):
        context = {'form': AssignmentForm()}
        return render(request, 'assignment_new.html', context)

    def post(self, request, *args, **kwargs):
        form = AssignmentForm(request.POST)
        if form.is_valid():
            assignment = form.save()
            return HttpResponseRedirect(reverse_lazy('assignment-list-page'))

        return render(request, 'assignment_new.html', {'form': form})

@method_decorator([login_required], name='dispatch')
class AssignmentDetailView(View):

    def get(self, request, *args, **kwargs):
        assignment = get_object_or_404(Assignment, pk=kwargs['pk'])
        context = {'assignment': assignment}
        return render(request, 'assignment_detail.html', context)

@method_decorator([login_required], name='dispatch')
class AssignmentEditView(UpdateView):

    model = Assignment 
    fields = ['name', 'description', 'course', 'assignment_type', 'total_points', 'assigned_date', 'due_date']

    template_name = 'assignment_edit.html'
    success_url = reverse_lazy('assignment-list-page')


@method_decorator([login_required], name='dispatch')
class AssignmentDeleteView(DeleteView):

    model = Assignment 
    template_name = 'assignment_delete.html'
    success_url = reverse_lazy('assignment-list-page')

@login_required
@lecturer_required
def student_list(request):
    
    students = Student.objects.all()
    user_type = "Student"

    context = {
        'students': students,
        'user_type': user_type,
    }
    return render(request, 'student_list.html', context)

@login_required
@lecturer_required
def staff_list(request):

    staff = User.objects.filter(teacher_access=True)
    user_type = 'Staff'

    context = {
        'staff': staff,
        'user_type': user_type,
    }
    return render(request, 'staff_list.html', context)

