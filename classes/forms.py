from django import forms 
from classes.models import Course, Assignment

class CourseForm(forms.ModelForm):

    class Meta:
        model = Course 
        fields = ('name', 'description')

class AssignmentForm(models.ModelForm):

    class Meta:
        model = Assignment 
        fields = ('name', 'description', 'course', 'assignment_type', 'total_points', 'assigned_date', 'due_date')