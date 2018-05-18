## Tasks ##

# python imports
from django.db import models
from case.models import Case
from evidence.models import Evidence



class TaskStatus(models.Model):
    # Choices
    CREATED = 'CR'
    QUEUED = 'QU'
    ALLOCATED = 'AL'
    PROGRESS = 'FP'
    QA = 'QA'
    DELIVERY = 'DE'
    COMPLETE = 'CO'
    CLOSED = 'CL'

    CHOICES = ((CREATED, 'Created'),
                (QUEUED, 'Queued'),
                (ALLOCATED, 'Allocated'),
                (PROGRESS, 'Forensics in Process'),
                (QA, 'QA'), (DELIVERY, 'Delivery'),
                (COMPLETE, 'Complete'),
                (CLOSED, 'Closed'),)

    # Choice Groups
    openStatuses = [CREATED, QUEUED, ALLOCATED, PROGRESS, QA, DELIVERY]
    beAssigned = [QUEUED, ALLOCATED, PROGRESS, QA]
    preInvestigation = [QUEUED, ALLOCATED]
    notesAllowed = [ALLOCATED, PROGRESS, QA, DELIVERY, COMPLETE]
    qaComplete = [DELIVERY, COMPLETE, CLOSED]
    closedStatuses = [COMPLETE, CLOSED]
    invRoles = [ALLOCATED, PROGRESS, DELIVERY, COMPLETE]
    qaRoles = [QA]
    workerRoles = [ALLOCATED, PROGRESS, QA, DELIVERY, COMPLETE]
    all_statuses = [CREATED, QUEUED, ALLOCATED, PROGRESS, QA, DELIVERY, COMPLETE, CLOSED]
    
    # General Fields
    date_time = models.DateTimeField(auto_now=True, null=True, verbose_name="Date")
    task_status = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Task Status")
    reason = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Reason For Status")
    # Linked Fields
    #user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="User")


class TaskType(models.Model):
    # General Fields
    task_type = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Task Type")
    # Linked Fields

 
class TaskCategory(models.Model):
    # General Fields
    task_category = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Task Category")


class TaskAuthorisation(models.Model):
    # Choices
    STATUS = {'AUTH': {'description': 'Authorised'},
              'NOAUTH': {'description': 'Rejected'},
              'PENDING': {'description': 'Pending'},}
    
    # General Fields
    task_authorisation = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Authorisation Status")
    reason = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Reason For Authorisation")
    date_time = models.DateTimeField(auto_now=True, null=True, verbose_name="Date")
    # Linked Fields
    #authoriser = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="the")


class TaskPriority(models.Model):
    # General Fields
    task_priority = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Task Priority")
    colour = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Colour")


class TaskNotes(models.Model):
    # General Fields
    date_time = models.DateTimeField(auto_now=True, null=True, verbose_name="Date")
    task_note = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Task Note")
    note_hash = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Note Hash")
    # Linked Fields
    #author = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="the")


class TaskHistory(models.Model):
    # General Fields
    task_title = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Task Title")
    background = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Task Background")
    location = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Task Location")
    creation_date = models.DateTimeField(auto_now=True, null=True, verbose_name="Creation Date")
    deadline = models.DateTimeField(auto_now=True, null=True, verbose_name="Deadline")


class Task(models.Model):
    # General Fields
    task_title = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Task Title")
    background = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Task Background")
    location = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Task Location")
    creation_date = models.DateTimeField(auto_now=True, null=True, verbose_name="Creation Date")
    deadline = models.DateTimeField(auto_now=True, null=True, verbose_name="Deadline")
    # Linked Fields
    type = models.ForeignKey(TaskType, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Task Type")
    status = models.ForeignKey(TaskStatus, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Task Status")
    category = models.ForeignKey(TaskCategory, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Task Category")
    notes = models.ForeignKey(TaskNotes, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Task Notes")
    priority = models.ForeignKey(TaskPriority, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Task Priority")
    authorisation = models.ForeignKey(TaskAuthorisation, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Task Authorisation")
    
class CaseTask(Task):
    # Linked Fields
    case = models.ForeignKey(Case, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Case")

class EvidenceTask(Task):
    # Linked Fields
    evidence = models.ForeignKey(Evidence, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Evidence")

