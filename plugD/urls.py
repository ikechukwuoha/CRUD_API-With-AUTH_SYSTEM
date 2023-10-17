from django.urls import path
from plugD.views import ProjectView





urlpatterns = [
    path('projects/', ProjectView.as_view(), name='project-list'),
    path('project/<int:pk>/', ProjectView.as_view(), name='project-detail'),
]