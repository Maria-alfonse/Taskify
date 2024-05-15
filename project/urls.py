

from django.contrib import admin
from django.urls import path,include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('availableTasks.urls')),
    path('AdminHome/', include('addTask.urls')),
    path('',include('tasks.urls'))
]
