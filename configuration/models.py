from django.db import models

# Configuration Models

class Options(models.Model):

    CASE_NAME_OPTIONS = ['NumericIncrement', 'DateNumericIncrement', 'FromList']
    TASK_NAME_OPTIONS = ['NumericIncrement', 'FromList', 'TaskTypeNumericIncrement']
    ACCOUNT_LOCKOUT = [("No lockout", "None"), ("1 attempt", "1"), ("2 attempts", "2"), ("3 attempts", "3"),
                       ("4 attempts", "4"), ("5 attempts", "5")]


    date_format = models.CharField(max_length=250, blank=True, null=True, default=None)
    default_location = models.CharField(max_length=250, blank=True, null=True, default=None)
    case_names = models.CharField(max_length=250, blank=True, null=True, default=None)
    #c_increment = Column(Integer)
    #c_leading_zeros = Column(Integer)
    c_leading_date = models.CharField(max_length=250, blank=True, null=True, default=None)
    c_list_name = models.CharField(max_length=250, blank=True, null=True, default=None)
    task_names = models.CharField(max_length=250, blank=True, null=True, default=None)
    #t_increment = Column(Integer)
    #t_leading_zeros = Column(Integer)
    t_list_name = models.CharField(max_length=250, blank=True, null=True, default=None)
    company = models.CharField(max_length=250, blank=True, null=True, default=None)
    department = models.CharField(max_length=250, blank=True, null=True, default=None)
    date_created = models.DateTimeField(auto_now=True, null=True)
    over_limit_case = models.BooleanField(default=False, blank=True)
    over_limit_task = models.BooleanField(default=False, blank=True)
    auth_view_tasks = models.BooleanField(default=False, blank=True)
    auth_view_evidence = models.BooleanField(default=False, blank=True)
    manager_inherit = models.BooleanField(default=False, blank=True)
    #evidence_retention_period = Column(Integer)
    evidence_retention = models.BooleanField(default=False, blank=True)
    email_alert_all_inv_task_queued = models.BooleanField(default=False, blank=True)
    email_alert_inv_assigned_task = models.BooleanField(default=False, blank=True)
    email_alert_qa_assigned_task = models.BooleanField(default=False, blank=True)
    email_alert_caseman_inv_self_assigned = models.BooleanField(default=False, blank=True)
    email_alert_caseman_qa_self_assigned = models.BooleanField(default=False, blank=True)
    email_alert_req_task_completed = models.BooleanField(default=False, blank=True)
    email_alert_case_man_task_completed = models.BooleanField(default=False, blank=True)
    email_alert_all_caseman_new_case = models.BooleanField(default=False, blank=True)
    email_alert_all_caseman_case_auth = models.BooleanField(default=False, blank=True)
    email_alert_req_case_caseman_assigned = models.BooleanField(default=False, blank=True)
    email_alert_req_case_opened = models.BooleanField(default=False, blank=True)
    email_alert_req_case_closed = models.BooleanField(default=False, blank=True)
    email_alert_req_case_archived = models.BooleanField(default=False, blank=True)
    email_alert_caseman_requester_add_task = models.BooleanField(default=False, blank=True)
    #number_logins_before_account_lockout = Column(Integer)
