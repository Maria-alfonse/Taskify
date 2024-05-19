from django.apps import AppConfig

class MyAppConfig(AppConfig):  # Correct the class name here
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'
