from django.db import models
from accounts.models import CustomUser

# Create your models here.
class Task(models.Model):
    user_email = models.ForeignKey(CustomUser, blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    note = models.TextField()
    rounds = models.IntegerField()
    time = models.TimeField(blank=True, null=True)
