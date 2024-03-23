from os import path

class MobileAwareTemplateMixin(object):
    def get_template_names(self):
        template_names = super(MobileAwareTemplateMixin, self).get_template_names()
        if self.request.is_mobile:
            template_names = [self.mobile_template_name]
        return template_names
