from typing import Any
from django.db import models
from django.shortcuts import render
from django.views.generic import CreateView
from tasks.models import Task
from tasks.forms import TaskForm

# Create your views here.
class TaskCreation(CreateView):
    model = Task
    form_class = TaskForm
    fields = ('title', 'note', 'rounds')
    template_name = 'index.html'

    