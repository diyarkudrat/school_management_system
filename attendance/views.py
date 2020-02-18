from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic import UpdateView
from django.views import View
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.http import HttpResponseRedirect
from classes.models import Course, Student



class CourseAttendanceView(View):

   model = Course

    def get(self, request):
         course = self.get_queryset()
        return render(request, 'attendance_list.html', {
            'course': course
        })


class AttendanceView(View):

    def get(self, request, *args, **kwargs):
        course = get_object_or_404(Course, pk=kwargs['pk'])
        students = Player.objects.all()
        context = {'course': course, 'students': students}
        return render(request, 'course_detail.html', context)
