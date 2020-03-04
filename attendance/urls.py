from django.urls import path
from . import views

urlpatterns = [

    path('courses/<int:pk>/', views.AttendanceCourseDetailView.as_view(), name='attendance-detail-page'),
]