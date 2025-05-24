from django.urls import path
from .views import ProgressListCreateView, CourseProgressView

urlpatterns = [
    path('', ProgressListCreateView.as_view(), name='progress'),
    path('course/<int:course_id>/', CourseProgressView.as_view(), name='course-progress'),
]