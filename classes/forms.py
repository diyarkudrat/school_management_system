from django import forms 
from classes.models import Course, Assignment

class CourseForm(forms.ModelForm):

    class Meta:
        model = Course 
        fields = ('course_name', 'description', 'course_teacher' )

class AssignmentForm(forms.ModelForm):

    class Meta:
        model = Assignment 
        fields = ('name', 'description', 'course', 'assignment_type', 'total_points', 'assigned_date', 'due_date')