"""
Case Forms.
"""

from django import forms
from case.models import Case, CaseNote, CaseTask
from django.utils.translation import ugettext_lazy as _
from django.forms import ModelForm, CharField
from django.utils.text import slugify
import itertools
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms import layout, bootstrap
from simple_history.utils import update_change_reason


class CaseCreateForm(forms.ModelForm):

    title = CharField(max_length=200, required=False, label='Title',)
    reference = CharField(max_length=200, required=False, label='Reference',)
    background = CharField(required=False, label='Background',)
    location = CharField(max_length=200, required=False, label='Location',)
    description = CharField(required=False, label='Description',)
    brief = CharField(required=False, label='Brief',)
    comment = CharField(required=False, label='Comment',)
   
    class Meta:
        model = Case
        fields = ['title', 'reference', 'background', 'purpose', 'location',
                 'description', 'brief', 'comment', 'private', 'type', 'status',
                 'classification', 'priority', 'authorisation', 'image_upload', 'assigned_to',
                 'case_manager', 'assigned_by']
        labels = {'type': _('Case Type'),}
        error_messages = {
            'case': {'max_length': _("The Case Type is Invalid"),},
        }

    def save(self):
        instance = super(CaseCreateForm, self).save(commit=False)
        instance.slug = orig = slugify(instance.title)
        for x in itertools.count(1):
            if not Case.objects.filter(slug=instance.slug).exists():
                break
            instance.slug = '%s-%d' % (orig, x)
        instance.save()
        update_change_reason(instance, 'Initial Case Creation')
        return instance


class CaseEditForm(forms.ModelForm):

    title = CharField(max_length=200, required=False, label='Title',)
    reference = CharField(max_length=200, required=False, label='Reference',)
    background = CharField(required=False, label='Background',)
    location = CharField(max_length=200, required=False, label='Location',)
    description = CharField(required=False, label='Description',)
    brief = CharField(required=False, label='Brief',)
    comment = CharField(required=False, label='Comment',)
    change_reason = CharField(required=False, label='Reason For Change',)
   
    class Meta:
        model = Case
        fields = ['title', 'reference', 'background', 'location', 'description',
                  'brief', 'comment', 'private', 'type', 'status',
                  'classification', 'priority', 'authorisation', 'image_upload']
        labels = {'type': _('Case Type'),}
        error_messages = {
            'case': {'max_length': _("The Case Type is Invalid"),},
        }

    def save(self):
        instance = super(CaseEditForm, self).save(commit=False)
        instance.slug = orig = slugify(instance.title)
        for x in itertools.count(1):
            if not Case.objects.filter(slug=instance.slug).exists():
                break
            instance.slug = '%s-%d' % (orig, x)
        changereason = self.cleaned_data['change_reason']
        instance.save()
        update_change_reason(instance, changereason)
        return instance


class CaseNoteCreateForm(forms.ModelForm):

    title = CharField(max_length=200, required=False, label='Title',)
        
    class Meta:
        model = CaseNote
        fields = ['title', 'private', 'image_upload', 'description']

    def save(self):
        instance = super(CaseNoteForm, self).save(commit=False)
        instance.slug = orig = slugify(instance.title)
        for x in itertools.count(1):
            if not CaseNote.objects.filter(slug=instance.slug).exists():
                break
            instance.slug = '%s-%d' % (orig, x)
        changereason = self.cleaned_data['change_reason']
        instance.save()
        update_change_reason(instance, changereason)
        return instance


class CaseTaskCreateForm(forms.ModelForm):

    title = CharField(max_length=200, required=False, label='Title',)
    background = CharField(required=False, label='Background',)
    location = CharField(max_length=200, required=False, label='Location',)
    description = CharField(required=False, label='Description',)
    change_reason = CharField(required=False, label='Reason For Change',)

    class Meta:
        model = CaseTask
        fields = ['title', 'background', 'location', 'description', 'private', 'type', 'status', 'priority', 'authorisation',]

    def save(self):
        instance = super(CaseTaskForm, self).save(commit=False)
        instance.slug = orig = slugify(instance.title)
        for x in itertools.count(1):
            if not CaseTask.objects.filter(slug=instance.slug).exists():
                break
            instance.slug = '%s-%d' % (orig, x)
        changereason = self.cleaned_data['change_reason']
        instance.save()
        update_change_reason(instance, changereason)
        return instance


class CrispyCaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = ['title', 'reference', 'background', 'location', 'description', 'brief', 'private', 'type', 'status',
                 'classification', 'priority', 'authorisation', 'image_upload']
    
    def __init__(self, *args, **kwargs):
        super(CrispyCaseForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_action = ""
        self.helper.form_method = "POST"
        self.fields["private"].widget = forms.RadioSelect()
        self.fields["type"].widget = forms.Select()
        self.fields["status"].widget = forms.Select()
        self.fields["classification"].widget = forms.Select()
        self.fields["priority"].widget = forms.Select()
        self.fields["authorisation"].widget = forms.Select()
    
        # delete empty choice for the type
        #del self.fields["private"].choices[0]
        self.helper.layout = layout.Layout(layout.Fieldset(_("Main data"),
                          layout.Field("background", css_class="input-block-level"),
                          layout.Field("location", css_class="input-block-level"),
                          layout.Field("brief", css_class="input-block-level"),
                          layout.Field("comment", css_class="input-block-level"),
                          layout.Field("description", css_class="input-blocklevel", rows="3"),
                          layout.Field("private"),
                          layout.Field("type"),
                          layout.Field("private"),
                          layout.Field("status"),
                          layout.Field("classification"),
                          layout.Field("authorisation"),
                          layout.Div(bootstrap.PrependedText("title","""<span class="glyphicon glyphicon earphone"></span>""", css_class="inputblock-level"),
                                     bootstrap.PrependedText("reference", "@", css_class="input-block-level", placeholder="contact@example.com"), css_id="contact_info",),),

            layout.Fieldset(_("Image"),
                          layout.Field("image_upload", css_class="input-block-level"),
                          layout.HTML(u"""{% load i18n %}
                            <p class="help-block">
                                {% trans "Available formats are JPG, GIF, and PNG. Minimal size is 800 × 800 px." %}
                            </p>"""),
                          title=_("Image upload"), css_id="image_fieldset",),

            layout.Fieldset(_("Contact"), 
                          layout.Field("contact_person", css_class="input-blocklevel"), 
                          layout.Div(bootstrap.PrependedText("title","""<span class="glyphicon glyphicon earphone"></span>""", css_class="inputblock-level"),
                                     bootstrap.PrependedText("reference", "@", css_class="input-block-level", placeholder="contact@example.com"), css_id="contact_info",),),

            bootstrap.FormActions(layout.Submit("submit", _("Save")),))

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