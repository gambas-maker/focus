from django.db import models
from accounts.models import CustomUser
from django.utils import timezone

# Create your models here.
class Task(models.Model):
    user_email = models.ForeignKey(CustomUser, blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    note = models.TextField(blank=True, null=True)
    rounds = models.IntegerField()
    time = models.DateTimeField(default=timezone.now)
