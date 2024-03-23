from django.views.generic import View, CreateView, TemplateView
from django.core.urlresolvers import reverse_lazy

from utils.views import MobileAwareTemplateMixin

from .models import Contact
from .forms import ContactForm

# --------------------------------------------------------------------------------------------------

class ContactCreateView(MobileAwareTemplateMixin, CreateView):
    model = Contact
    form_class = ContactForm
    success_url = reverse_lazy('contact:success')
    template_name = 'contact/contact.html'
    mobile_template_name = 'contact/mobile-contact.html'

# --------------------------------------------------------------------------------------------------

class ContactSuccessView(MobileAwareTemplateMixin, TemplateView):
    template_name = 'contact/success.html'
    mobile_template_name = 'contact/mobile-success.html'

