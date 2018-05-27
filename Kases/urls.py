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
import entity.views
import evidence.views
import tasks.views
import debug_toolbar
from case.views import CaseList, CaseCreate, CaseUpdate, CaseTable, CaseDelete, CaseHome, CaseDetail, CaseNoteCreate

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [

    # Case
    path('case/<int:pk>/edit', CaseUpdate.as_view(), name='case_edit'),
    path('case/<int:pk>/detail', CaseDetail.as_view(), name='case_detail'),
    path('case/<int:pk>/delete', CaseDelete.as_view(), name='case_delete'),
    path('case/create', CaseCreate.as_view(), name='case_create'),
    # Case Notes
    path('case/<int:casepk>/note/create', CaseNoteCreate.as_view(), name='casenote_create'),
    #path('case/<int:casepk>/note/<int:notepk>/edit', CaseNoteUpdate.as_view(), name='casenote_update'),
    #path('case/<int:pk>/note/<int:pk>/detail', CaseDetail.as_view(), name='case_detail'),
    #path('case/<int:pk>/note/<int:pk>/delete', CaseDelete.as_view(), name='case_delete'),
    #path('case/<int:pk>/note/list', CaseList.as_view(), name='case_list'),
    #Case Display
    path('case/list', CaseList.as_view(), name='case_list'),
    path('case/table', CaseTable.as_view(), name='case_table'),

    path('case', CaseHome.as_view(), name='cases'), 

    # Evidence
    path('evidence/', evidence.views.home, name='evidence'),
    #path('new/evidence/', evidence.views.new_evidence, name='new_evidence'),

    # Task
    path('tasks', tasks.views.home, name='tasks'),
    #path('new/task', tasks.views.new_task, name='new_task'),

    # Personality
    path('entity', entity.views.home, name='entity'),
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

    # Base CatchAll
    url(r'^$', CaseHome.as_view(), name='home'),
]
