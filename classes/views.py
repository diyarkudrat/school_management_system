from django.shortcuts import render

# Create your views here.
def course_view(request):
    return render(request, 'classes/course.html')

def add_course(request):
    return render(request,'classes/add-course.html')

def attendance(request):
    return render(request, 'classes/attendance.html')