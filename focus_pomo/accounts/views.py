from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth import get_user_model
from . import models
from . import forms
from django.urls import reverse_lazy

# Create your views here.
User = get_user_model()

class SignUp(CreateView):
    form_class = forms.CustomUserCreationForm
    model = User
    template_name = 'accounts/sign_up.html'
    success_url = reverse_lazy('accounts:login') 
