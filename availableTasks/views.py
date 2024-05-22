from django.http import HttpResponse
from django.template import loader
from tasks.models import Task
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from tasks.models import Task
from myapp.models import User


def availableTasks(request):
    tasks = Task.objects.filter(completed=False)
    return render(request, 'availableTasks.html', {'tasks': tasks, 'user': request.user})



def available_task_detail(request, task_id):  # Add task_id parameter
    task = get_object_or_404(Task, pk=task_id)  # Filter by primary key (pk)
    return render(request, 'task_detail.html', {'task': task})

# View to mark a task as not done
@require_POST
@csrf_exempt  # Only use csrf_exempt for demonstration purposes; in production, ensure CSRF is handled properly
def mark_as_done(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = True
    task.save()
    return JsonResponse({'status': 'success', 'completed': task.completed})

# View to handle completed task page if different from task_detail
def task_detail(request):
    # Assuming this would list all completed tasks again or a specific logic for completed tasks
    tasks = Task.objects.filter(completed=True)
    return render(request, 'task_detail.html', {'tasks': tasks})