from django.urls import path
from . import views

urlpatterns = [

    path('courses/<int:pk>/', views.AttendanceCourseDetailView.as_view(), name='courseattendance-detail-page'),
    path('<int:pk>/', views.AttendanceDetailView.as_view(), name='attendance-detail-page'),
    path('<int:pk>/edit/', views.AttendanceEditView.as_view(), name="edit-attendance-page"),
]