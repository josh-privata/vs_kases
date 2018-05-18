"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from tasks.forms import TaskForm

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'tasks/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )


def new_task(request):
    form = TaskForm()
    return render(request, 'tasks/new_task.html', {'form': form})