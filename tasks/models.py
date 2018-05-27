## Task Models ##

## python imports
from django.db import models
from utils.models import ObjectDescriptionMixin
from django.urls import reverse
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
#import task.managers as managers
from simple_history.models import HistoricalRecords


## Admin Models
class TaskAuthorisationType(ObjectDescriptionMixin):
    # General Fields
    title = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Task Classification")

    class Meta:
        ordering = ('id',)
        verbose_name = _('Task Classification')
        verbose_name_plural = _('Task Classifications')

    #def get_absolute_url(self):
    #    return reverse('Task_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return '%s' % self.title
    

class TaskClassificationType(ObjectDescriptionMixin):
    # General Fields
    title = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Task Classification")
    
    class Meta:
        ordering = ('id',)
        verbose_name = _('Task Classification')
        verbose_name_plural = _('Task Classifications')

    #def get_absolute_url(self):
    #    return reverse('Task_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return '%s' % self.title


class TaskType(ObjectDescriptionMixin):
    # General Fields
    title = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Task Type")
    
    class Meta:
        ordering = ('id',)
        verbose_name = _('Task Type')
        verbose_name_plural = _('Task Types')

    #def get_absolute_url(self):
    #    return reverse('Task_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return '%s' % self.title


class TaskPriority(ObjectDescriptionMixin):
    # General Fields
    title = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Task Priority")
    colour = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Colour")
    #action_delta_hours = models.IntegerField(blank=True, null=True, default=None, verbose_name="Action Delta Days")
   
    class Meta:
        ordering = ('id',)
        verbose_name = _('Task Priority')
        verbose_name_plural = _('Task Priorities')

    #def get_absolute_url(self):
    #    return reverse('Task_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return '%s' % self.title


class TaskCategory(ObjectDescriptionMixin):
    # General Fields
    title = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Task Category")
    
    class Meta:
        ordering = ('id',)
        verbose_name = _('Task Category')
        verbose_name_plural = _('Task Categories')

    #def get_absolute_url(self):
    #    return reverse('task_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return '%s' % self.title


class TaskStatusType(ObjectDescriptionMixin):
    # General Fields
    title = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Task Status Type")

    class Meta:
        ordering = ('id',)
        verbose_name = _('Task Status Type')
        verbose_name_plural = _('Task Status Types')

    #def get_absolute_url(self):
    #    return reverse('Task_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return '%s' % self.title


class TaskStatusGroup(ObjectDescriptionMixin):
    ## Choices
    # CREATED = 'Created'
    # PENDING = 'Awaiting Authorisation'
    # REJECTED = 'Rejected'
    # OPEN = 'Open'
    # Active = 'Active'
    # CLOSED = 'Closed'
    # ARCHIVED = 'Archived'
    ## Choice Groups
    # closedStatuses = [CLOSED, ARCHIVED]
    # all_statuses = [CREATED, OPEN, CLOSED, ARCHIVED, PENDING, REJECTED]
    # approved_statuses = [CREATED, OPEN, CLOSED, ARCHIVED]
    # active_statuses = [CREATED, PENDING, REJECTED, OPEN]
    # workable_statuses = [CREATED, OPEN]
    # forensic_statuses = [OPEN]
    
    # General Fields
    title = models.CharField(max_length=250, blank=True, null=True, default=None, 
                             verbose_name="Task Status Group")
    # Linked Fields
    Task_status = models.ManyToManyField(TaskStatusType, blank=True, verbose_name="Task Status")

    class Meta:
        ordering = ('id',)
        verbose_name = _('Task Status Group')
        verbose_name_plural = _('Task Status Groups')

    #def get_absolute_url(self):
    #    return reverse('Task_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return '%s' % self.title


## Main Models
class Task(ObjectDescriptionMixin):
    # General Fields
    title = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Task Title")
    background = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Task Background")
    location = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Task Location")
    creation_date = models.DateTimeField(auto_now=True, null=True, verbose_name="Creation Date")
    deadline = models.DateTimeField(auto_now=True, null=True, verbose_name="Deadline")
    private = models.BooleanField(default=False, blank=True, verbose_name="Private")
    # Linked Fields
    type = models.ForeignKey(TaskType, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Task Type")
    status = models.ForeignKey(TaskStatusType, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Task Status")
    classification = models.ForeignKey(TaskClassificationType, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Task Classification")
    priority = models.ForeignKey(TaskPriority, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Task Priority")
    category = models.ForeignKey(TaskCategory, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Task Category")
    authorisation = models.ForeignKey(TaskAuthorisationType, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Task Authorisation")
    assigned_to = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='task_assigned_to', blank=True, verbose_name="Assigned To")
    task_manager = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='task_manager', on_delete=models.CASCADE, blank=True, null=True, verbose_name="Case Manager")
    assigned_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='task_assigned_by', on_delete=models.CASCADE, blank=True, null=True, verbose_name="Assigned By")
    

## Data Models