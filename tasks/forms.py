# forms.py
from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['Taskiid', 'title', 'teacher', 'choose', 'Description', 'admin', 'completed']
        widgets = {
            'admin': forms.TextInput(attrs={'readonly': True}),
        }
