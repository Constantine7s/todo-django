from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from base.models import Task

class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'

class SingleTask(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/single_task.html'