from typing import Any, Dict
from django.views.generic import TemplateView, CreateView, ListView,FormView
from tasks.forms import TaskForm
from tasks.models import Task
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy

class Index(FormView, TemplateView):
    template_name = 'index.html'
    success_url = reverse_lazy('index')

    def get(self, request, *args, **kwargs):
        form = TaskForm()
        return self.render_to_response(self.get_context_data(form=form))

    def post(self, request, *args, **kwargs):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect or handle success as needed
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
        
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.all()
        return context
    
def remove_task(task, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('index')
    # success_url = reverse_lazy('index')



    