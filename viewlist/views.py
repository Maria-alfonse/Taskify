from django.shortcuts import render,get_object_or_404
from .models import Task 
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
# Create your views here.


def viewlist(request):
    task=Task.objects.all()
    return render(request,'viewlist.html',{'task':task})

from django.shortcuts import render, get_object_or_404
from tasks.models import Task

def task_detail(request,taskid):
    return render(request, 'task.html', {'Task': get_object_or_404(Task,id=taskid )})