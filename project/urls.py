
from django.contrib import admin
from django.urls import path,include
from myapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('availableTasks.urls')),
    path('completed/', include('completed.urls')),
    path('addTask/', include('addTask.urls')),
    path('Home/',include('tasks.urls')),
    path('', include('myapp.urls')),
     path('viewlist/',include('viewlist.urls')),
]