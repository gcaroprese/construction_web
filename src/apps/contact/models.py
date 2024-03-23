from django.db import models
from django.db.models.query import QuerySet
from django.db.models.signals import post_save
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _

from model_utils.choices import Choices
from model_utils.fields import AutoCreatedField

from .signals import send_email

# --------------------------------------------------------------------------------------------------

class RecipientQuerySet(QuerySet):
    def active(self):
        return self.filter(is_active=True)

class Recipient(models.Model):
    name = models.CharField(_('Name'), max_length=255)
    email = models.EmailField(_('Email'))
    is_active = models.BooleanField(_('Is active'), default=True)

    objects = RecipientQuerySet.as_manager()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('Recipient')
        verbose_name_plural = _('Recipients')

# --------------------------------------------------------------------------------------------------

class Contact(models.Model):
    STATUS = Choices(
        (0, 'pending', _('Pending')),
        (1, 'answered', _('Answered'))
    )

    full_name = models.CharField(_('Full Name'), max_length=255)
    email = models.EmailField('Email')
    message = models.TextField(_('Message'))
    cv = models.FileField(_('CV'), upload_to='cvs/', null=True, blank=True)

    status = models.PositiveSmallIntegerField(_('Status'), choices=STATUS, default=STATUS.pending)
    date = AutoCreatedField(_('Date'))

    class Meta:
        verbose_name = _('Contact')
        verbose_name_plural = _('Contacts')
        ordering = ['-date']

    def __unicode__(self):
        return u'%s | %s | %s' %(self.full_name, self.email, self.date.strftime('%d/%m/%Y'))

    def get_admin_url(self):
        admin_url = "admin:%s_%s_change" % (self._meta.app_label, self._meta.module_name)
        return reverse_lazy(admin_url, args=(self.id))

# --------------------------------------------------------------------------------------------------

post_save.connect(send_email, Contact)

