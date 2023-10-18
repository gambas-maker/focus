from tasks.models import Task
from django import forms
from django.forms import TextInput

class TaskForm(forms.ModelForm):
    class Meta():
        model = Task
        fields = ('title', 'rounds', 'note')
        widgets = {
            'title': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'What are you working on?',
            }),
            'note': TextInput(attrs={
                "class": "form-control",
                "placeholder": "Some notes...",
            })
        }
        labels = {
            'title': "",
            'note': "",
            'rounds': "Est Pomodoros"
        }