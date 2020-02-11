"""Urls.py"""
from django.urls import path
from . import views
urlpatterns = [
    path('', views.assignments_view, name='assignment_view'),
]
