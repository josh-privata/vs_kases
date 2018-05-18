## Case ##

# python imports
from django.db import models
from base.models import UploadModel
from django.urls import reverse
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
#import case.managers as managers


class CaseAuthorisationTypes(models.Model):
    # General Fields
    title = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Case Classification")

    class Meta:
        ordering = ('id',)
        verbose_name = _('Case Classification')
        verbose_name_plural = _('Case Classifications')

    #def get_absolute_url(self):
    #    return reverse('case_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return '%s' % self.title


class CaseAuthorisation(models.Model):
    # Choices
    STATUS = {'AUTH': {'description': 'Authorised'},
              'NOAUTH': {'description': 'Rejected'},
              'PENDING': {'description': 'Pending'},}
    
    # General Fields
    title = models.ForeignKey(CaseAuthorisationTypes, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Case Authorisation")
    reason = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Reason For Authorisation")
    date_time = models.DateTimeField(auto_now=True, null=True, verbose_name="Date")
    # Linked Fields
    authorised_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Authorised By")

    class Meta:
        ordering = ('id',)
        verbose_name = _('Case Authorisation')
        verbose_name_plural = _('Case Authorisations')

    #def get_absolute_url(self):
    #    return reverse('case_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return '%s' % self.title
    

class CaseClassification(models.Model):
    # General Fields
    title = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Case Classification")
    # Linked Fields
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Modified By")

    class Meta:
        ordering = ('id',)
        verbose_name = _('Case Classification')
        verbose_name_plural = _('Case Classifications')

    #def get_absolute_url(self):
    #    return reverse('case_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return '%s' % self.title


class CaseType(models.Model):
    # General Fields
    title = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Case Type")
    # Linked Fields
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Modified By")

    class Meta:
        ordering = ('id',)
        verbose_name = _('Case Type')
        verbose_name_plural = _('Case Types')

    #def get_absolute_url(self):
    #    return reverse('case_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return '%s' % self.title


class CasePriority(models.Model):
    # General Fields
    title = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Case Priority")
    colour = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Colour")
    # Linked Fields
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Modified By")

    class Meta:
        ordering = ('id',)
        verbose_name = _('Case Priority')
        verbose_name_plural = _('Case Priorities')

    #def get_absolute_url(self):
    #    return reverse('case_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return '%s' % self.title


class CaseStatusType(models.Model):
    # General Fields
    title = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Case Status Type")
    description = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Description")

    class Meta:
        ordering = ('id',)
        verbose_name = _('Case Status Type')
        verbose_name_plural = _('Case Status Types')

    #def get_absolute_url(self):
    #    return reverse('case_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return '%s' % self.title


class CaseStatus(models.Model):
    
    # General Fields
    date_time = models.DateTimeField(auto_now=True, null=True, verbose_name="Date")
    reason = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Reason For Status")
    # Linked Fields
    title = models.ForeignKey(CaseStatusType, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Case Status")
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="User")

    class Meta:
        ordering = ('id',)
        verbose_name = _('Case Status')
        verbose_name_plural = _('Case Status')

    #def get_absolute_url(self):
    #    return reverse('case_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return '%s' % self.title.title


class CaseStatusGroup(models.Model):
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
    title = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Case Status Group")
    description = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Description")
    # Linked Fields
    case_status = models.ManyToManyField(CaseStatusType, blank=True, verbose_name="Case Status")

    class Meta:
        ordering = ('id',)
        verbose_name = _('Case Status Group')
        verbose_name_plural = _('Case Status Groups')

    #def get_absolute_url(self):
    #    return reverse('case_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return '%s' % self.title


class CaseHistory(models.Model):
    # General Fields
    title = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Case Title")
    reference = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Case Reference")
    background = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Case Background")
    location = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Case Location")
    description = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Case Description")
    brief = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Case Brief")
    comment = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Comment")
    private = models.BooleanField(default=False, blank=True, verbose_name="Private")
    creation_date = models.DateTimeField(auto_now=True, null=True, verbose_name="Creation Date")
    deadline = models.DateTimeField(auto_now=True, null=True, verbose_name="Case Deadline")

    class Meta:
        ordering = ('id',)
        verbose_name = _('Case History')
        verbose_name_plural = _('Case Histories')

    #def get_absolute_url(self):
    #    return reverse('case_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return '%s' % self.title


class CaseImageUpload(UploadModel):
    # General Fields
    # Linked Fields
    location = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Location")
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Uploaded By")

    class Meta:
        ordering = ('id',)
        verbose_name = _('Case Image Upload')
        verbose_name_plural = _('Case Image Uploads')

    #def get_absolute_url(self):
    #    return reverse('case_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return '%s' % self.location
    

class Case(models.Model):
    # General Fields
    title = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Case Title")
    reference = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Case Reference")
    background = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Case Background")
    location = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Case Location")
    description = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Case Description")
    brief = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Case Brief")
    comment = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Comment")
    private = models.BooleanField(default=False, blank=True, verbose_name="Private")
    creation_date = models.DateTimeField(auto_now=True, null=True, verbose_name="Creation Date")
    deadline = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Case Deadline")
    slug = models.SlugField(blank=True, null=True, unique=True, verbose_name="Case Slug")
    # Linked Fields
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Assigned To")
    type = models.ForeignKey(CaseType, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Case Type")
    status = models.ForeignKey(CaseStatus, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Case Status")
    classification = models.ForeignKey(CaseClassification, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Case Classification")
    priority = models.ForeignKey(CasePriority, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Case Priority")
    authorisation = models.ForeignKey(CaseAuthorisation, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Case Authorisation")
    image_upload = models.ForeignKey(CaseImageUpload, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Case Image Upload")

    #manager = managers.CaseManager()

    class Meta:
        ordering = ('id',)
        verbose_name = _('Case')
        verbose_name_plural = _('Cases')

    def get_absolute_url(self):
        return reverse('case_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return '%s' % self.title
    
    
    # Property Methods
    def _get_case(self):
        """ A user-friendly Case ID, which is a combination of Case ID
        and queue slug. This is generally used in e-mail subjects. """

        return u"[%s]" % self.case_for_url
    case = property(_get_case)

    def _get_case_for_url(self):
        """ A URL-friendly Case ID, used in links. """
        return u"%s-%s" % (self.queue.slug, self.id)
    case_for_url = property(_get_case_for_url)  
    
    def _get_assigned_to(self):
        """ Custom property to allow us to easily print 'Unassigned' if a
        Case has no owner, or the users name if it's assigned. If the user
        has a full name configured, we use that, otherwise their username. """
        if not self.assigned_to:
            return _('Unassigned')
        else:
            if self.assigned_to.get_full_name():
                return self.assigned_to.get_full_name()
            else:
                return self.assigned_to.get_username()
    get_assigned_to = property(_get_assigned_to)

    #def _get_case_url(self):
    #    """
    #    Returns a publicly-viewable URL for this Case, used when giving
    #    a URL to the submitter of a Case.
    #    """
    #    from django.contrib.sites.models import Site
    #    from django.core.exceptions import ImproperlyConfigured
    #    from django.urls import reverse
    #    try:
    #        site = Site.objects.get_current()
    #    except ImproperlyConfigured:
    #        site = Site(domain='configure-django-sites.com')
    #    return u"http://%s%s/%s" % (
    #        site.domain,
    #        reverse('case:case_detail'),
    #        self.case_for_url,
    #    )
    #case_url = property(_get_case_url)


class LinkedCase(models.Model):
    # General Fields
    reason = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Reason For Link")
    date_time = models.DateTimeField(auto_now=True, null=True, verbose_name="Date")
    # Linked Fields
    linked_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="the")
    case = models.ManyToManyField(Case, blank=True, verbose_name="Case")