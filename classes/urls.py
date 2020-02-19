from django.urls import path
from . import views

urlpatterns = [
        path('', views.landing_page, name="landing-page"),
        path('about/', views.about_page, name="about"),
        path('contact/', views.contact_page, name="contact"),
        path('home/', views.home, name="home"),
        path('profile/', views.profile, name="profile"),
        path('courses/', views.CourseListView.as_view(), name="course-list"),
        path('courses/new/', views.CourseCreateView.as_view(), name='course-create-page'),
        path('courses/<int:pk>/', views.CourseDetailView.as_view(), name='course-detail-page'),
        path('courses/<int:pk>/delete/', views.CourseDeleteView.as_view(),name='course-delete-page'),
        path('courses/<int:pk>/edit/', views.CourseEditView.as_view(), name="edit-course-page"),
        path('assignments/', views.AssignmentListView.as_view(), name="assignment-list"),
        path('assignments/new/', views.AssignmentCreateView.as_view(), name='assignment-create-page'),
        path('assignments/<int:pk>/', views.AssignmentDetailView.as_view(), name='assignment-detail-page'),
        path('assignments/<int:pk>/delete/', views.AssignmentDeleteView.as_view(),name='assignment-delete-page'),
        path('assignments/<int:pk>/edit/', views.AssignmentEditView.as_view(), name="edit-assignment-page"),

]
