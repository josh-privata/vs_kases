from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from tasks.models import CaseTask, TaskHistory, EvidenceTask, TaskNotes, TaskPriority, TaskAuthorisation, TaskCategory, TaskType, TaskStatus
from case.models import Case, CaseAuthorisation, CaseClassification, CaseType, CasePriority, CaseStatus, CaseStatusGroup, CaseStatusType
from evidence.models import Evidence, EvidenceType, ChainOfCustody, EvidenceStatus
from user.models import Profile
from configuration.models import Options

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Options)
admin.site.register(EvidenceType)
admin.site.register(ChainOfCustody)
admin.site.register(EvidenceStatus)
admin.site.register(Evidence)
admin.site.register(CaseAuthorisation)
admin.site.register(CaseClassification)
admin.site.register(CaseType)
admin.site.register(CasePriority)
admin.site.register(CaseStatus)
admin.site.register(CaseStatusGroup)
admin.site.register(CaseStatusType)
admin.site.register(Case)
admin.site.register(CaseTask)
admin.site.register(EvidenceTask)
admin.site.register(TaskNotes)
admin.site.register(TaskPriority)
admin.site.register(TaskAuthorisation)
admin.site.register(TaskCategory)
admin.site.register(TaskType)
admin.site.register(TaskStatus)
