from django.urls import path
from .views import TaskCreate, TaskList, SingleTask

urlpatterns = [
    path('',TaskList.as_view(), name='tasks'),
    path('task/<int:pk>',SingleTask.as_view(), name='task'),
    path('task/create/',TaskCreate.as_view(), name='task-create'),
]

