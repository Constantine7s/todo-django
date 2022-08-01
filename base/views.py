from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from base.models import Task

class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'

class SingleTask(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/single_task.html'
    
class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    template_name = 'base/task_create.html'
    success_url = reverse_lazy('tasks')

    
