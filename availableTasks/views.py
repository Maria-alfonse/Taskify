from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Task
from django.shortcuts import render, get_object_or_404


def availableTasks(request):
    task=Task.objects.all()
    return render(request,'availableTasks.html',{'task':task})

def task_detail(request):
    task=get_object_or_404(Task)
    return render(request, 'task_detail.html', {'task': task})