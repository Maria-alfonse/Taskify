

from django.urls import path
from myapp import views as myapp_views
from tasks import views as tasks_views
from availableTasks import views as availableTask_views

urlpatterns = [
  path('', myapp_views.home_view, name='home'),  # Home view from myapp
path('availableTasks/', myapp_views.teacher_home, name='teacherhome'),  # Teacher home view from myapp
path('login/', myapp_views.auth, name='auth'),  # Auth view from myapp
path('login/', myapp_views.login, name='login'),  # Login view from myapp
path('signup/', myapp_views.signup, name='signup'),  # Signup view from myapp
path('availableTasks/', availableTask_views.availableTasks, name='teacherhome'),  # Teacher home with name from myapp
path('Home/AdminHome', tasks_views.showTask, name='showTask'),
]