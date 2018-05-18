## Evidence ##

# python imports
from django.db import models
from base.models import UploadModel
from case.models import Case



class EvidenceType(models.Model):
    # General Fields
    evidence_type = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Evidence Type")


class ChainOfCustody(models.Model):
    # General Fields
    date_recorded = models.DateTimeField(auto_now=True, null=True, verbose_name="Date Recorded")
    date_of_custody = models.DateTimeField(auto_now=True, null=True, verbose_name="Date of Custody")
    check_in = models.BooleanField(default=False, blank=True, verbose_name="Checked-In")
    comment = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Comment")
    custody_receipt = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Custody Receipt Number")
    custody_receipt_label = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Custody Receipt Label")
    # Linked Fields
    #user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="User")
    #custodian = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Custodian")


class EvidenceStatus(models.Model):
    # Choices
    INACTIVE = 'Inactive'
    ACTIVE = 'Active'
    ARCHIVED = 'Archived'
    DESTROYED = 'Destroyed'
    # Choice Groups
    statuses = [INACTIVE, ACTIVE, ARCHIVED, DESTROYED]
    
    # General Fields
    date_time = models.DateTimeField(auto_now=True, null=True, verbose_name="Date")
    evidence_status = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Status")
    comment = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Comment")
    # Linked Fields
    #user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="the")


class EvidenceHistory(models.Model):
    # General Fields
    title = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Evidence Title")
    reference = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Evidence Reference")
    comment = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Comment")
    evidence_bag_number = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Bag Number")
    location = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Physical Location")
    uri = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="File Location")
    current_status = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Current Status")
    qr_code_text = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="QR Code Text")
    qr_code = models.BooleanField(default=False, blank=True, verbose_name="QR Code")
    retention_reminder_sent = models.BooleanField(default=False, blank=True, verbose_name="Retention Reminder")
    retention_date = models.DateTimeField(auto_now=True, null=True, verbose_name="Retention Date")
    date_added = models.DateTimeField(auto_now=True, null=True, verbose_name="Date Added")
    retention_start_date = models.DateTimeField(auto_now=True, null=True, verbose_name="Retention Start Date")
    # Linked Fields
    #user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="the")
    #type = models.ForeignKey(EvidenceType, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Evidence Type")
    #status = models.ForeignKey(EvidenceStatus, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Evidence Status")
    #chain_of_custody = models.ForeignKey(ChainOfCustody, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Chain Of Custody")
    #case = models.ForeignKey(Case, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Case")


class EvidenceImageUpload(UploadModel):
    # General Fields
    # Linked Fields
    location = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Location")
    #uploader = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="the")
    #deleter = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="the")


class Evidence(models.Model):
    # General Fields
    title = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Evidence Title")
    reference = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Evidence Reference")
    comment = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Comment")
    evidence_bag_number = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Bag Number")
    location = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Physical Location")
    uri = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="File Location")
    current_status = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Current Status")
    qr_code_text = models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="QR Code Text")
    qr_code = models.BooleanField(default=False, blank=True, verbose_name="QR Code")
    retention_reminder_sent = models.BooleanField(default=False, blank=True, verbose_name="Retention Reminder")
    retention_date = models.DateTimeField(auto_now=True, null=True, verbose_name="Retention Date")
    date_added = models.DateTimeField(auto_now=True, null=True, verbose_name="Date Added")
    retention_start_date = models.DateTimeField(auto_now=True, null=True, verbose_name="Retention Start Date")
    # Linked Fields
    #user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="the")
    type = models.ForeignKey(EvidenceType, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Evidence Type")
    status = models.ForeignKey(EvidenceStatus, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Evidence Status")
    image_upload = models.ForeignKey(EvidenceImageUpload, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Evidence Image Upload")
    chain_of_custody = models.ForeignKey(ChainOfCustody, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Chain Of Custody")
    case = models.ForeignKey(Case, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Case")
