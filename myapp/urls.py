# myproject/urls.py


from django.urls import path
from myapp import views

urlpatterns = [
  
    path('', views.home_view, name='home'),
      path('signup/teacher_home.html',views.teacher_home, name='teacherhome'),
    path('TeacherHome/', views.teacher_home, name='teacher_home'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),  # Corrected view name
    path('adminpage/', views.admin_home, name='admin_home'),
    path('login/teacher_home.html/',views.teacher_home,name='teacherhome')
]
