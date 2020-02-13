from django.urls import path
from . import views

urlpatterns = [
        path('', views.home, name="home"),
        path('profile/', views.profile, name="profile"),
        path('courses/', views.CourseListView.as_view(), name="course-list"),

]
