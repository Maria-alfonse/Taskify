from django.db import models


class Task(models.Model):
    title=models.CharField(max_length=50)
    priority=models.CharField(max_length=20)
    description=models.TextField()
    status=models.BooleanField(default=False)
# Create your models here.
