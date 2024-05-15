from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage, name = 'completed'),
    path('completed/taskdetails/', views.ctask, name = 'completed_task'),

]



