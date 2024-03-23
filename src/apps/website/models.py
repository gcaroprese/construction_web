import os
from django.db import models
from django.db.models.query import QuerySet
from django.utils.translation import ugettext_lazy as _

from model_utils import Choices
from easy_thumbnails.fields import ThumbnailerImageField

# --------------------------------------------------------------------------------------------------

class SlideshowQuerySet(QuerySet):
    def active(self):
        return self.filter(is_active=True)

class Slideshow(models.Model):
    name = models.CharField(_('Name'), max_length=255)
    is_active = models.BooleanField(_('Is active'), default=True)

    objects = SlideshowQuerySet.as_manager()

    class Meta:
        verbose_name = _('Slideshow')
        verbose_name_plural = _('Slideshows')

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.is_active:
            Slideshow.objects.exclude(id=self.id).update(is_active=False)
        return super(Slideshow, self).save(*args, **kwargs)

# --------------------------------------------------------------------------------------------------

class SlideshowImage(models.Model):
    CROPPING_SETTINGS = Choices(
        ('center_center_contain', _('Center Center - No Crop')),
        ('left_top_cover', _('Left Top - Crop')),
        ('left_center_cover', _('Left Center - Crop')),
        ('left_bottom_cover', _('Left Bottom - Crop')),
        ('right_top_cover', _('Right Top - Crop')),
        ('right_center_cover', _('Right Center - Crop')),
        ('right_bottom_cover', _('Right Bottom - Crop')),
        ('center_top_cover', _('Center Top - Crop')),
        ('center_center_cover', _('Center Center - Crop')),
        ('center_bottom_cover', _('Center Bottom - Crop'))
    )

    slideshow = models.ForeignKey(Slideshow, related_name='images', verbose_name=_('Slideshow'))
    file = ThumbnailerImageField(_('File'), upload_to='slideshows/')
    position = models.PositiveSmallIntegerField(_('Position'), default=0)
    cropping_settings = models.CharField(
        _('Cropping Settings'),
        max_length=50,
        choices=CROPPING_SETTINGS,
        default=CROPPING_SETTINGS.center_center_cover
    )

    class Meta:
        verbose_name = _('Image')
        verbose_name_plural = _('Images')
        ordering = ['position']

    def __unicode__(self):
        return os.path.basename(self.file.name)

    def get_cropping_styles(self):
        horizontal, vertical, size = self.cropping_settings.split('_')
        return 'background-position: %s %s; background-size: %s;' % (horizontal, vertical, size)

    def get_image_styles(self):
        return 'background-image: url(%s);' % (self.file.url)
