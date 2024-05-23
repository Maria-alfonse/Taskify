from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from tasks.models import Task
from myapp.models import User

def availableTasks(request):
    task=Task.objects.filter(completed=False)
    return render(request,'availableTasks.html',{'task':task})


def available_task_detail(request, task_id):  # Add task_id parameter
    task = get_object_or_404(Task, pk=task_id)  # Filter by primary key (pk)
    return render(request, 'task_detail.html', {'task': task})

@require_POST
@csrf_exempt
def mark_as_done(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = True
    task.save()
    return JsonResponse({'status': 'success', 'completed': task.completed})

def task_detail(request):
    tasks = Task.objects.filter(completed=True)
    return render(request, 'task_detail.html', {'tasks': tasks})

