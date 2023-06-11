from typing import Any
from django.db import models
from django.shortcuts import render
from django.views.generic import CreateView
from tasks.models import Task

# Create your views here.
class TaskCreation(CreateView):
    model = Task
    fields = ('title', 'note', 'rounds', 'time')
    template_name = 'index.html'

    # def get_queryset(self) -> QuerySet[Any]:
    #     return super().get_queryset()