from django.db import models


class Task(models.Model):
    title=models.CharField(max_length=50)
    priority=models.CharField(max_length=20)
    description=models.TextField()
    status=models.BooleanField(default=False)
    createdby=models.CharField(max_length=100, default='test')
# Create your models here.
