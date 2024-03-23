from django.contrib import admin
from django import forms

from easy_thumbnails.fields import ThumbnailerImageField
from easy_thumbnails.widgets import ImageClearableFileInput

from .models import Slideshow, SlideshowImage

# --------------------------------------------------------------------------------------------------

class SlideshowImageInline(admin.StackedInline):
    extra = 0
    model = SlideshowImage
    sortable_field_name = 'position'
    inline_classes = ('grp-collapse grp-open')
    formfield_overrides = {
        ThumbnailerImageField: {'widget': ImageClearableFileInput}
    }


class SlideshowAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']
    list_filter = ['is_active']
    inlines = [
        SlideshowImageInline
    ]

# --------------------------------------------------------------------------------------------------

admin.site.register(Slideshow, SlideshowAdmin)
