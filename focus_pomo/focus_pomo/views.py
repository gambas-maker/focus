from django.views.generic import TemplateView, FormView, ListView
from tasks.forms import TaskForm
from tasks.views import TaskCreation
from tasks.models import Task
from django.urls import reverse_lazy
from django.utils import timezone

class Index(FormView, ListView):
    form_class = TaskForm
    template_name = 'index.html'
    success_url = reverse_lazy('index')

    model = Task

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context[""] = timezone.now()
        return context