"""
Evidence Forms
"""

from django import forms
from evidence.models import Evidence


class EvidenceForm(forms.ModelForm):

    class Meta:
        model = Evidence
        fields = ['title', 'reference', 'comment', 'evidence_bag_number', 'location', 'uri', 'qr_code_text', 'qr_code', 'retention_reminder_sent', 'type', 'status', 'chain_of_custody']
