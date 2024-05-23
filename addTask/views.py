from django.shortcuts import render
from myapp.models import User
from tasks.models import Task
# def showPage(request):
#     admin_username = request.GET.get('admin')
#     admin = User.objects.get(username=admin_username)
    
#     # Assuming you want to retrieve the latest task created by the admin user
#     task = Task.objects.filter(admin=admin).order_by('-id').first()
    
#     return render(request, 'addTask/addTask.html', {'task': task}) 

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from myapp.models import User  # Import the custom User model from myapp
from tasks.models import Task

@login_required
def SaveData(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        teacher = request.POST.get('teacher')
        choose = request.POST.get('choose')
        Description = request.POST.get('Description')
        admin = request.user  # Get the currently logged-in user

        # Create and save the Task object if it doesn't already exist
        if not Task.objects.filter(title=title, teacher=teacher, choose=choose, Description=Description, admin=admin).exists():
            data = Task(title=title, teacher=teacher, choose=choose, Description=Description, admin=admin)
            data.save()
            return render(request, 'addTask/addTask.html', {'task': data})  # Pass the task to the template for confirmation

    return render(request, 'addTask/addTask.html')



