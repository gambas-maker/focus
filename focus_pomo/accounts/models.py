from django.db import models
<<<<<<< HEAD
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    
=======
from django.contrib.auth.models import AbstractUser#
# 
from django.utils.translation import gettext_lazy
# Create your models here.

from .managers import CustomUserManager

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(gettext_lazy('Email'), unique=True)

    # defines the unique identifier for the user model to email
    USERNAME_FIELD = 'email'
    # list of fields prompted while creating a super user
    REQUIRED_FIELDS = []
 
    objects = CustomUserManager()

    def __str__(self) -> str:
        return self.email


>>>>>>> 6f35e699ff10e261826416ea7ca6d108e01df272
