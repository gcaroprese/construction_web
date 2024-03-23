from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import Contact, Recipient

# --------------------------------------------------------------------------------------------------

class ContactAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'formated_date', 'status']
    list_filter = ['date', 'status']
    search_fields = ['full_name', 'email']

    def formated_date(self, instance):
        return instance.date.strftime('%d/%m/%Y - %H:%m')
    formated_date.short_description = _('Date')

# --------------------------------------------------------------------------------------------------

class RecipientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'is_active']
    list_filter = ['is_active']
    search_fields = ['name', 'email']

# --------------------------------------------------------------------------------------------------

admin.site.register(Contact, ContactAdmin)
admin.site.register(Recipient, RecipientAdmin)
