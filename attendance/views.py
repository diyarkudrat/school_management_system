from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic import UpdateView
from django.views import View
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.http import HttpResponseRedirect
from .models import CourseAttendance, Attendance
from classes.models import Course
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required



class AttendanceCourseDetailView(View):

    def get(self, request, *args, **kwargs):
        course = get_object_or_404(Course, pk=kwargs['pk'])
        attendances = CourseAttendance.objects.filter(course=course)
        context = {'course': course, 'attendances': attendances}
        return render(request, 'courseattendance_detail.html', context)

class AttendanceDetailView(View):

    def get(self, request, *args, **kwargs):
        course = get_object_or_404(CourseAttendance, pk=kwargs['pk'])
        # attendance = CourseAttendance.objects.filter(course=course)
        students = Attendance.objects.filter(course=course)
        context = {'course': course, 'students': students}
        return render(request, 'attendance_detail.html', context)

@method_decorator([login_required], name='dispatch')
class AttendanceEditView(UpdateView):
    model = Attendance
    fields = ['course','student', 'attendance_status']

    template_name = 'attendance_edit.html'
    success_url = reverse_lazy('course-list')

