# myproject/urls.py


from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('availableTasks/',views.teacher_home, name='teacherhome'),
    path('login/', views.auth, name='auth'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('adminpage/', views.admin_home, name='admin_home'),
]