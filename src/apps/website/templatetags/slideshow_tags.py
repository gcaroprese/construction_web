from django import template
from django.core.urlresolvers import reverse
from classytags.helpers import InclusionTag

from ..models import Slideshow

# --------------------------------------------------------------------------------------------------

register = template.Library()

# --------------------------------------------------------------------------------------------------

class IncludeActiveSlideshow(InclusionTag):
    name = 'active_slideshow'
    template = 'website/slideshow.html'

    def get_context(self, context, **kwargs):
        try:
            slideshow = Slideshow.objects.active().first()
        except Slideshow.DoesNotExist:
            slideshow = None
        return {'slideshow': slideshow}

# --------------------------------------------------------------------------------------------------

register.tag(IncludeActiveSlideshow)
