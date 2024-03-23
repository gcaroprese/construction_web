from os import path
from django.conf import settings
from django.template import loader
from django.core.mail import EmailMultiAlternatives
from django.db.models.query import QuerySet


def send_email_from_template(template_base_name, recipients, context={}, headers={}):
    subject_template = path.join(template_base_name, 'subject.txt')
    body_txt_template = path.join(template_base_name, 'body.txt')
    body_html_template = path.join(template_base_name, 'body.html')

    subject = loader.render_to_string(subject_template, context).strip()
    body_txt = loader.render_to_string(body_txt_template, context).strip()
    body_html = loader.render_to_string(body_html_template, context).strip()

    if isinstance(recipients, QuerySet):
        recipients = list(recipients)
    elif not isinstance(recipients, list):
        recipients = [recipients]

    recipients = [recipient if isinstance(recipient, basestring) else recipient.email
                  for recipient in recipients]

    msg = EmailMultiAlternatives(subject, body_txt, to=recipients, headers=headers)
    msg.attach_alternative(body_html, 'text/html')

    msg.send()

