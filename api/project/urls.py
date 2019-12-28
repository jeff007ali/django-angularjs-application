from django.urls import path
from .views import *


urlpatterns = [
    #Project URLs
    path('project/', ProjectsListView.as_view()),
    path('project/<uuid:projectId>/', ProjectDetailView.as_view()),
    path('project/create/', CreateProjectView.as_view()),
    #Task URLs
    path('project/<uuid:projectId>/task/', TasksListView.as_view()),
    path('project/<uuid:projectId>/task/<uuid:taskId>/', TaskDetailView.as_view()),
    path('project/<uuid:projectId>/task/create/', CreateTaskView.as_view()),
    #Subtask URLs
    path('project/<uuid:projectId>/task/<uuid:taskId>/subtask/', SubtasksListView.as_view()),
    path('project/<uuid:projectId>/task/<uuid:taskId>/subtask/<uuid:subtaskId>/', SubtaskDetailView.as_view()),
    path('project/<uuid:projectId>/task/<uuid:taskId>/subtask/create/', CreateSubtaskView.as_view()),
    #Users URLs
    path('user/', UsersListView.as_view()),
]