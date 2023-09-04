from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from . import forms

# Create your views here.
class SignUp(CreateView):

    form_class = forms.CustomUserCreationForm
    success_url = reverse_lazy('index.html')
    template_name = 'accounts/sign_up.html'