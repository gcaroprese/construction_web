from django.contrib.sites.models import Site
from .email import send_email_from_template

def send_email(sender, instance, signal, *args, **kwargs):
    from .models import Recipient

    recipients = [recipient.email for recipient in Recipient.objects.active()]
    headers = {'Reply-To': u'%s <%s>' % (instance.full_name, instance.email)}
    context = {
        'contact': instance,
        'domain': Site.objects.get_current().domain
    }
    send_email_from_template('emails/contact/', recipients, context)
