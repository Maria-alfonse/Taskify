from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage, name='completed'),
    path('taskdetails/task/<int:task_id>/', views.comptask, name='completed_task'),
    path('task/<int:task_id>/', views.ctask, name='ctask'),
    path('task/<int:task_id>/mark_as_not_done/', views.mark_as_not_done, name='mark_as_not_done'),
    path('comptask/<int:task_id>/', views.comptask, name='comptask'),
]
