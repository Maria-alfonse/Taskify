from django.urls import path
from . import views

urlpatterns= [
    path('availableTasks/',views.availableTasks),
    path('availableTasks/task/<int:task_id>/', views.available_task_detail, name='available_task_detail'),
    
]