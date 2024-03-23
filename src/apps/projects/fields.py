import re
from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _

# --------------------------------------------------------------------------------------------------

class YearField(models.IntegerField):
    def __init__(self, *args, **kwargs):
        year_validator = RegexValidator(r'^\d{4}$', _('Enter a valid year.'), 'invalid')
        kwargs['validators'] = [year_validator]
        super(YearField, self).__init__(*args, **kwargs)
