"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from evidence.forms import EvidenceForm

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'evidence/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )


def new_evidence(request):
    form = EvidenceForm()
    return render(request, 'evidence/new_evidence.html', {'form': form})