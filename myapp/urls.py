

from django.urls import path
from myapp import views as myapp_views
from tasks import views as tasks_views
from availableTasks import views as availableTask_views

urlpatterns = [
<<<<<<< HEAD
  path('', myapp_views.home_view, name='home'),  # Home view from myapp
path('availableTasks/', myapp_views.teacher_home, name='teacherhome'),  # Teacher home view from myapp
path('login/', myapp_views.auth, name='auth'),  # Auth view from myapp
path('login/', myapp_views.login, name='login'),  # Login view from myapp
path('signup/', myapp_views.signup, name='signup'),  # Signup view from myapp
path('availableTasks/', availableTask_views.availableTasks, name='teacherhome'),  # Teacher home with name from myapp
path('Home/AdminHome', tasks_views.showTask, name='showTask'),
=======
    path('', views.home_view, name='home'),
    path('availableTasks/',views.teacher_home, name='teacherhome'),
    path('auth/', views.auth, name='auth'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('adminpage/', views.admin_home, name='admin_home'),
>>>>>>> d5ae8f8d412cb020e54d33e70f3fc863a2f8569c
]