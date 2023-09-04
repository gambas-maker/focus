from typing import Any, Optional
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.base_user import AbstractBaseUser
from django.http.request import HttpRequest

class EmailBackend(ModelBackend):
    def authenticate(self, request: HttpRequest, username, password, **kwargs):
        usermodel = get_user_model()
        try:
            user = usermodel.objects.get(email=username)
        except usermodel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None