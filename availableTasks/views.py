from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from tasks.models import Task
from django.shortcuts import render, get_object_or_404


def availableTasks(request):
    task=Task.objects.all()
    return render(request,'availableTasks.html',{'task':task})

from django.shortcuts import render, get_object_or_404
from tasks.models import Task

def available_task_detail(request, task_id):  # Add task_id parameter
    task = get_object_or_404(Task, pk=task_id)  # Filter by primary key (pk)
    return render(request, 'task_detail.html', {'task': task})

