from django import forms
from .models import Task
#Incharge of creating the form for the task model.
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date']