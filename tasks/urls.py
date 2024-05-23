from django.urls import path
from . import views

urlpatterns = [
    path('AdminHome/', views.showTask,name='showTask'),
    path('tasks/<int:id>/', views.task_detail, name='task_detail'),
    path('viewist/',views.viewlist, name='list'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
  
]