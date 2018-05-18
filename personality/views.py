"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
#from personality.forms import PersonalityForm

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'personality/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

#def new_personality(request):
#    form = PersonalityForm()
#    return render(request, 'personality/new_personality.html', {'form': form})