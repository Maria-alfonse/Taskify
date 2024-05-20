from django.urls import path
from . import views

urlpatterns = [
    path('AdminHome/', views.showTask,name='showTask'),
    path('tasks/<int:taskid>/', views.task_detail, name='task_detail')

  

]