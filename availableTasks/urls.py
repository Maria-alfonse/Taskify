from django.urls import path
from . import views

urlpatterns= [
    path('availableTasks/',views.availableTasks),
    path('task/', views.task_detail, name='task_detail'),
]