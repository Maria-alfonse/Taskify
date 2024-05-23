from django.urls import path
from . import views

urlpatterns = [

    # path('addTask/',views.showPage,name='showPage'),
    path('',views.SaveData,name='SaveData')
    
]
