from django import template
from django.core.urlresolvers import resolve

from classytags.core import Tag, Options
from classytags.arguments import Argument

register = template.Library()

# --------------------------------------------------------------------------------------------------

class IsActiveURL(Tag):
    name = 'is_active_url'
    options = Options(
        Argument('name'),
        Argument('class_name', required=False, resolve=False)
    )

    def matches(self, context, **kwargs):
        matches = False

        path = context.get('request').path
        resolved_url = resolve(path)

        namespace, url_name = kwargs.get('name').split(':')
        if namespace and url_name:
            matches =  namespace == resolved_url.namespace and url_name == resolved_url.url_name
        elif namespace and not url_name:
            matches =  namespace == resolved_url.namespace
        elif not namespace and url_name:
            matches =  url_name == resolved_url.url_name

        return matches

    def render_tag(self, context, **kwargs):
        if self.matches(context, **kwargs):
            return kwargs.get('class_name') or 'active'
        return ''

# --------------------------------------------------------------------------------------------------

register.tag(IsActiveURL)
