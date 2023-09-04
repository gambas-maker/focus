from django.shortcuts import render
<<<<<<< HEAD
from django.urls import reverse_lazy
from django.views.generic import CreateView
from . import forms

# Create your views here.
class SignUp(CreateView):

    form_class = forms.CustomUserCreationForm
    success_url = reverse_lazy('index.html')
    template_name = 'accounts/sign_up.html'
=======
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
>>>>>>> 6f35e699ff10e261826416ea7ca6d108e01df272
