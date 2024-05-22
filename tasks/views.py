from django.shortcuts import render
from .models import Task
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def showTask(request):
    task =Task.objects.all()
    return render(request, 'AdminHome/AdminHome.html',{'task':task})
    
def task_detail(request,taskid):
    return render(request, 'task.html', {'Task': get_object_or_404(Task,id=taskid )})

def viewlist(request):
    return render(request, 'viewlist.html')


def delete_task(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, id=task_id)
        task.delete()
        return redirect('showTask')
    return JsonResponse({'success': False, 'error': 'Invalid request method'})