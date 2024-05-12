from django.urls import path
from . import views

urlpatterns= [
    path('availableTasks/',views.availableTasks)
]