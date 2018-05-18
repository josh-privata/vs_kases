"""
Case Forms.
"""

from django import forms
from case.models import Case
from django.utils.translation import ugettext_lazy as _
from django.forms import ModelForm, CharField
from django.utils.text import slugify
import itertools


class CaseForm(forms.ModelForm):

    title = CharField(max_length=200, required=False, label='Title',)
    reference = CharField(max_length=200, required=False, label='Reference',)
    background = CharField(required=False, label='Background',)
    location = CharField(max_length=200, required=False, label='Location',)
    description = CharField(required=False, label='Description',)
    brief = CharField(required=False, label='Brief',)
    comment = CharField(required=False, label='Comment',)
   
    class Meta:
        model = Case
        fields = ['title', 'reference', 'background', 'location', 'description', 'brief', 'comment', 'private', 'type', 'status',
                 'classification', 'priority', 'authorisation', 'image_upload']
        labels = {'type': _('Case Type'),}
        error_messages = {
            'case': {'max_length': _("The Case Type is Invalid"),},
        }

    def save(self):
        instance = super(CaseForm, self).save(commit=False)
        instance.slug = orig = slugify(instance.title)
        for x in itertools.count(1):
            if not Case.objects.filter(slug=instance.slug).exists():
                break
            instance.slug = '%s-%d' % (orig, x)
        instance.save()
        return instance



#class MessageForm(forms.Form):
#    recipient = forms.ModelChoiceField(label=_("Recipient"), queryset=User.objects.all(), required=True,)
#    message = forms.CharField(label=_("Message"), widget=forms.Textarea, required=True,)

#    def __init__(self, request, *args, **kwargs):
#        super(MessageForm, self).__init__(*args, **kwargs)
#        self.request = request
#        self.fields["recipient"].queryset = self.fields["recipient"].queryset.exclude(pk=request.user.pk)


#    def save(self):
#        cleaned_data = self.cleaned_data
#        send_mail(subject=ugettext("A message from %s") % self.request.user,
#                  message=cleaned_data["message"],
#                  from_email=self.request.user.email,
#                  recipient_list=[cleaned_data["recipient"].email],
#                  fail_silently=True,)