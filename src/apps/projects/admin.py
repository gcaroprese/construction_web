from django.contrib import admin
from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import (Project, ProjectImage)

# --------------------------------------------------------------------------------------------------

class NameHandler(object):
    def normalized_name(self, instance):
        return instance.normalized_name
    normalized_name.short_description = _('Name')
    normalized_name.admin_order_field = 'name'

# --------------------------------------------------------------------------------------------------

class ProjectImageInline(admin.StackedInline):
    model = ProjectImage
    sortable_field_name = 'position'
    extra = 0

# --------------------------------------------------------------------------------------------------

class ProjectAdmin(NameHandler, admin.ModelAdmin):
    list_display = [
        'normalized_name',
        'program',
        'work',
        'grid_x',
        'grid_y',
        'grid_w',
        'grid_h',
        'grid_badge_position'
    ]
    list_editable = ['grid_x', 'grid_y', 'grid_w', 'grid_h', 'grid_badge_position']
    list_filter = ['is_active']
    search_fields = ['name', 'work', 'program']

    prepopulated_fields = {'slug': ['name']}
    inlines = [ProjectImageInline]
    fieldsets = [
        [None, {
            'fields': [
                'name',
                'slug',
                'program',
                'work',
                'authors',
                'location',
                'year',
                'surface',
                'is_active'
            ]
        }],
        [_('Grid'), {
            'fields': [
                'grid_x',
                'grid_y',
                'grid_w',
                'grid_h',
                'grid_image',
                'grid_mobile_image',
                'grid_badge_position'
            ]
        }]
    ]

    def changelist_view(self, request, extra_context=None):
        response = super(ProjectAdmin, self).changelist_view(request, extra_context)
        extra_context = {'grid_projects': Project.objects.active()}
        if hasattr(response, 'context_data'):
            response.context_data.update(extra_context)
        return response

# --------------------------------------------------------------------------------------------------
admin.site.register(Project, ProjectAdmin)
