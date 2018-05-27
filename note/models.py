## Note Models ##

## python imports
from django.db import models
from utils.models import ObjectDescriptionMixin
from django.urls import reverse
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
#import note.managers as managers
from simple_history.models import HistoricalRecords


## Admin Models
class NoteAuthorisationType(ObjectDescriptionMixin):
    # General Fields
    title = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Note Classification")

    class Meta:
        ordering = ('id',)
        verbose_name = _('Note Classification')
        verbose_name_plural = _('Note Classifications')

    #def get_absolute_url(self):
    #    return reverse('Note_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return '%s' % self.title
    

class NoteClassificationType(ObjectDescriptionMixin):
    # General Fields
    title = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Note Classification")
    
    class Meta:
        ordering = ('id',)
        verbose_name = _('Note Classification')
        verbose_name_plural = _('Note Classifications')

    #def get_absolute_url(self):
    #    return reverse('Note_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return '%s' % self.title


class NoteType(ObjectDescriptionMixin):
    # General Fields
    title = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Note Type")
    
    class Meta:
        ordering = ('id',)
        verbose_name = _('Note Type')
        verbose_name_plural = _('Note Types')

    #def get_absolute_url(self):
    #    return reverse('Note_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return '%s' % self.title


class NotePriority(ObjectDescriptionMixin):
    # General Fields
    title = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Note Priority")
    colour = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Colour")
    #action_delta_hours = models.IntegerField(blank=True, null=True, default=None, verbose_name="Action Delta Days")
   
    class Meta:
        ordering = ('id',)
        verbose_name = _('Note Priority')
        verbose_name_plural = _('Note Priorities')

    #def get_absolute_url(self):
    #    return reverse('Note_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return '%s' % self.title


class NoteCategory(ObjectDescriptionMixin):
    # General Fields
    title = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Note Category")
    
    class Meta:
        ordering = ('id',)
        verbose_name = _('Note Category')
        verbose_name_plural = _('Note Categories')

    #def get_absolute_url(self):
    #    return reverse('note_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return '%s' % self.title


class NoteStatusType(ObjectDescriptionMixin):
    # General Fields
    title = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Note Status Type")

    class Meta:
        ordering = ('id',)
        verbose_name = _('Note Status Type')
        verbose_name_plural = _('Note Status Types')

    #def get_absolute_url(self):
    #    return reverse('Note_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return '%s' % self.title


class NoteStatusGroup(ObjectDescriptionMixin):
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
                             verbose_name="Note Status Group")
    # Linked Fields
    Note_status = models.ManyToManyField(NoteStatusType, blank=True, verbose_name="Note Status")

    class Meta:
        ordering = ('id',)
        verbose_name = _('Note Status Group')
        verbose_name_plural = _('Note Status Groups')

    #def get_absolute_url(self):
    #    return reverse('Note_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return '%s' % self.title


## Main Models
class Note(ObjectDescriptionMixin):
    # General Fields
    title = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Note Note Type")
    slug = models.SlugField(blank=True, null=True, unique=True, verbose_name="Note NoteSlug")
    image_upload = models.FileField(blank=True, null=True, verbose_name="Note Note Image")
    private = models.BooleanField(default=False, blank=True, verbose_name="Private")
    # Linked Fields
    type = models.ForeignKey(NoteType, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Note Type")
    status = models.ForeignKey(NoteStatusType, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Note Status")
    classification = models.ForeignKey(NoteClassificationType, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Note Classification")
    priority = models.ForeignKey(NotePriority, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Note Priority")
    category = models.ForeignKey(NoteCategory, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Note Category")
    authorisation = models.ForeignKey(NoteAuthorisationType, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Note Authorisation")
    assigned_to = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='note_assigned_to', blank=True, verbose_name="Assigned To")
    note_manager = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='note_manager', on_delete=models.CASCADE, blank=True, null=True, verbose_name="Note Manager")
    assigned_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='note_assigned_by', on_delete=models.CASCADE, blank=True, null=True, verbose_name="Assigned By")
    
    class Meta:
        ordering = ('id',)
        verbose_name = _('Note')
        verbose_name_plural = _('Notes')

    def get_absolute_url(self):
        return reverse('note_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return '%s' % self.title


## Data Models