from django.shortcuts import render
from .models import Task
from django.shortcuts import render, get_object_or_404
from django.template import loader

def showTask(request):
    task =Task.objects.all()
    return render(request, 'AdminHome/AdminHome.html',{'task':task})
    
def task_detail(request,taskid):
    return render(request, 'task.html', {'Task': get_object_or_404(Task,id=taskid )})

