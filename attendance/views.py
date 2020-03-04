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



class AttendanceCourseDetailView(View):

    def get(self, request, *args, **kwargs):
        course = get_object_or_404(CourseAttendance, pk=kwargs['pk'])
        students = Attendance.objects.filter(course=course)
        context = {'course': course, 'students': students}
        return render(request, 'attendance_detail.html', context)
