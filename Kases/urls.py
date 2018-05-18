"""
Definition of urls for Kases.
"""

from datetime import datetime
from django.conf.urls import url
from django.urls import path
import django.contrib.auth.views
import base.forms
import base.views
import case.views
import personality.views
import evidence.views
import tasks.views
import debug_toolbar
from case.views import CaseList, CaseCreate, CaseUpdate, CaseTable, CaseDelete, CaseHome, CaseDetail

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    
    # Base
    url(r'^$', base.views.home, name='home'),
    path('contact', base.views.contact, name='contact'),

    # Cases
    path('case/edit/<int:pk>', CaseUpdate.as_view(), name='case_update'),
    path('case/detail/<int:pk>', CaseDetail.as_view(), name='case_detail'),
    path('case/delete/<int:pk>', CaseDelete.as_view(), name='case_delete'),
    path('case/list', CaseList.as_view(), name='case_list'),
    path('case/table', CaseTable.as_view(), name='case_table'),
    path('case/create', CaseCreate.as_view(), name='case_create'),
    path('case', CaseHome.as_view(), name='cases'), 

    # Evidence
    path('evidence/', evidence.views.home, name='evidence'),
    #path('new/evidence/', evidence.views.new_evidence, name='new_evidence'),

    # Tasks
    path('tasks', tasks.views.home, name='tasks'),
    #path('new/task', tasks.views.new_task, name='new_task'),

    # Personality
    path('personality', personality.views.home, name='personality'),
    #path('new/personality', personality.views.new_personality, name='new_personality'),
    
    # Debug Toolbar
    path('__debug__/', include(debug_toolbar.urls)),
    
    # Needed for Django Authentication
    path('accounts/', include('django.contrib.auth.urls')),
    # Login
    path('login',
        django.contrib.auth.views.login,
        {
            'template_name': 'registration/login.html',
            'authentication_form': base.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    # Logout
    path('logout',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),
  
    # Uncomment the admin/doc line below to enable admin documentation:
    path('admin/doc', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    path('admin', admin.site.urls),
]
