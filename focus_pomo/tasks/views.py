from typing import Any
from django.db import models
from django.shortcuts import render
from django.views.generic import CreateView
from tasks.models import Task
from . import forms
# from tasks.forms import TaskForm
from django.urls import reverse_lazy

# Create your views here.
class TaskCreation(CreateView):
    form_class = forms.TaskForm
    model = Task
    fields = ('title', 'note', 'rounds')
    template_name = 'index.html'
    success_url = reverse_lazy('accounts:login') 

    