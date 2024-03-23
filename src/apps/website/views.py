from django.views.generic import TemplateView
from utils.views import MobileAwareTemplateMixin


# --------------------------------------------------------------------------------------------------

class LandingView(MobileAwareTemplateMixin, TemplateView):
    template_name = 'website/landing.html'
    mobile_template_name = 'website/mobile-landing.html'

# --------------------------------------------------------------------------------------------------

class HomeView(MobileAwareTemplateMixin, TemplateView):
    template_name = 'website/home.html'
    mobile_template_name = 'website/mobile-home.html'

# --------------------------------------------------------------------------------------------------

class AboutUsView(MobileAwareTemplateMixin, TemplateView):
    template_name = 'website/about-us.html'
    mobile_template_name = 'website/mobile-about-us.html'


