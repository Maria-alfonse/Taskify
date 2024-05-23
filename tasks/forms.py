
# forms.py
from django import forms
from .models import Task
from tasks.models import (Task, x)


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['Taskiid', 'title', 'teacher', 'choose', 'Description', 'admin', 'completed']
        choose = forms.ChoiceField(choices=x, widget=forms.Select(attrs={'class': 'form-control'}))
        widgets = {
            'admin': forms.TextInput(attrs={'readonly': True}),
        }

