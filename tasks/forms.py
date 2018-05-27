"""
Task Forms
"""

from django import forms
from tasks.models import Task


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['title', 'background', 'location', 'type', 'status', 'priority']
