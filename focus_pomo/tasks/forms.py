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
                "class": "note-control",
                "placeholder": "Some notes...",
            }),
            'rounds': TextInput(attrs={
                'class': "round-control",
            }),
        }
        labels = {
            'title': "",
            'note': "",
            'rounds': "Est Pomodoros"
        }

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['rounds'].initial = 1