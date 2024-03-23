import json
from django import template

from classytags.core import Tag, Options
from classytags.arguments import Argument

register = template.Library()

# --------------------------------------------------------------------------------------------------

class ExtractSize(Tag):
    name = 'extract_size'
    options = Options(
        Argument('human_readable_size'),
    )

    def render_tag(self, context, **kwargs):
        size = kwargs.get('human_readable_size').split('x')
        return 'data-w="%s" data-h="%s"' % (size[0], size[1])

# --------------------------------------------------------------------------------------------------

class IsProjectSize(Tag):
    name = 'is_project_size'
    options = Options(
        Argument('human_readable_size'),
        Argument('project'),
    )

    def render_tag(self, context, **kwargs):
        if kwargs.get('project').size == kwargs.get('human_readable_size'):
            return 'selected'
        return ''

# --------------------------------------------------------------------------------------------------

register.tag(ExtractSize)
register.tag(IsProjectSize)
