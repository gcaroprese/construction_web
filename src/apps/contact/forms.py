from django import forms
from django.utils.translation import ugettext_lazy as _

from .fields import RestrictedFileField
from .models import Contact

# --------------------------------------------------------------------------------------------------

class ContactForm(forms.ModelForm):
    cv = RestrictedFileField(
        label = _('CV'),
        required = False,
        content_types = [
            'application/pdf',
            'application/msword',
            'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
            'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        ],
        max_upload_size = 5242880
    )

    class Meta:
        model = Contact
        fields = ['full_name', 'email', 'message', 'cv']

