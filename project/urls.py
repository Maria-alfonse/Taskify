
from django.contrib import admin
from django.urls import path,include
urlpatterns = [
    path('admin/', admin.site.urls),
   
    path('addTask/', include('addTask.urls')),
    path('Home/',include('tasks.urls')),
   
]