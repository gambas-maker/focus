from django.db import models
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


