from django.shortcuts import render
from django.http import HttpResponse
from tasks.models import Task
# Create your views here.

   
def SaveData(request):
   if all(request.GET.get(param) for param in ['Taskiid', 'title', 'teacher', 'choose', 'admin']):
        Taskiid = request.GET.get('Taskiid')
        title = request.GET.get('title')
        teacher = request.GET.get('teacher')
        choose = request.GET.get('choose')
        Description = request.GET.get('Description')
        admin = request.GET.get('admin')
        data = Task(Taskiid=Taskiid, title=title, teacher=teacher, choose=choose, Description=Description, admin=admin)
        if not Task.objects.filter(Taskiid=Taskiid, title=title, teacher=teacher, choose=choose, Description=Description, admin=admin).exists():
            data = Task(Taskiid=Taskiid, title=title, teacher=teacher, choose=choose, Description=Description, admin=admin)
            data.save()
       

   return render(request, 'addTask/addTask.html')