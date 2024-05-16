# forms.py
from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['Taskiid','title','teacher','choose','Description','admin','completed']

        def __init__(self, *args, **kwargs):
           super().__init__(*args, **kwargs)
    # Disable the 'admin' field
           self.fields['admin'].disabled = True

