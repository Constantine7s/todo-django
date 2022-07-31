from django.urls import path
from .views import TaskList, SingleTask

urlpatterns = [
    path('',TaskList.as_view(), name='tasks'),
    path('task/<int:pk>',SingleTask.as_view(), name='task'),

]

