from django.views.generic import TemplateView, FormView
from tasks.forms import TaskForm
from django.urls import reverse_lazy

class Index(FormView):
    form_class = TaskForm
    template_name = 'index.html'
    success_url = reverse_lazy('index')