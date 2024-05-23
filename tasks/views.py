from django.shortcuts import render
from .models import Task
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Task
from myapp.models import User
@login_required
def showTask(request):
    try:
        # Fetch tasks associated with the currently logged-in admin user
        tasks = Task.objects.filter(admin=request.user)
    except Exception as e:
        tasks = None
        print('Exception:', e)
        # You may want to log the error or display a more user-friendly message

    context = {
        'task': tasks,  # Pass tasks to the template context
    }
    
    return render(request, 'AdminHome/AdminHome.html', context)

    
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

def edit(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            if request.is_ajax():
                return JsonResponse({'success': True, 'message': 'Task updated successfully!'})
            messages.success(request, 'Task updated successfully!')
            return redirect('task_detail', taskid=task_id)
        else:
            if request.is_ajax():
                return JsonResponse({'success': False, 'errors': form.errors})
            messages.error(request, 'Form validation failed. Please check the input fields.')
    else:
        form = TaskForm(instance=task)

    context = {
        'form': form,
        'task': task
    }
    return render(request, 'Edit.html', context)

