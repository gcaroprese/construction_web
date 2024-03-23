import os
from django.db import models
from django.db.models.query import QuerySet
from django.conf import settings
from django.core.urlresolvers import reverse_lazy

from django.utils.translation import ugettext_lazy as _
from django.utils.functional import cached_property

from easy_thumbnails.fields import ThumbnailerImageField
from model_utils import Choices

from .fields import YearField

# --------------------------------------------------------------------------------------------------

class NameHandler(object):
    @cached_property
    def normalized_name(self):
        return ' '.join(self.name.split())

    def __unicode__(self):
        return self.normalized_name

# --------------------------------------------------------------------------------------------------

class ProjectQuerySet(QuerySet):
    def active(self):
        return self.filter(is_active=True)

class Project(NameHandler, models.Model):

    GRID_BADGES = Choices(
        ('bottom_left', _('Bottom Left')),
        ('bottom_right', _('Bottom Right')),
        ('top_left', _('Top Left')),
        ('top_right', _('Top Right')),
    )
    SIZES = Choices(
        ('1x1','1x1'),
        ('1x2','1x2'),
        ('2x1','2x1'),
        ('2x2','2x2'),
    )

    name = models.TextField(_('Name'), max_length=512)
    slug = models.SlugField(_('Slug'), unique=True, max_length=512)
    program = models.TextField(_('Program'), blank=True)
    work = models.TextField(_('Work'), blank=True)
    authors = models.TextField(_('Authors'), default=_('Aulet Abiega Arquitectos'), blank=True)
    location = models.TextField(_('Location'), blank=True)
    year = YearField(_('Year'), blank=True, null=True)
    surface = models.PositiveIntegerField(_('Surface'), blank=True, null=True)

    grid_x = models.PositiveIntegerField(_('Grid X'), max_length=512, default=0)
    grid_y = models.PositiveIntegerField(_('Grid Y'), max_length=512, default=0)
    grid_w = models.PositiveIntegerField(_('Grid W'), max_length=512, default=0)
    grid_h = models.PositiveIntegerField(_('Grid H'), max_length=512, default=0)

    grid_image = ThumbnailerImageField(_('Grid Image'))
    grid_mobile_image = ThumbnailerImageField(_('Grid Mobile Image'), blank=True, null=True)
    grid_badge_position = models.CharField(
        _('Badge Position'),
        max_length=12,
        choices=GRID_BADGES,
        default=GRID_BADGES['bottom_left']
    )

    is_active = models.BooleanField(_('Is Active'), default=True)

    objects = ProjectQuerySet.as_manager()

    class Meta:
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')
        ordering = ['grid_x', 'grid_y']

    def get_absolute_url(self):
        return reverse_lazy('projects:detail', kwargs={'slug': self.slug})

    @property
    def size(self):
        return '%dx%d' % (self.grid_w, self.grid_h)

# --------------------------------------------------------------------------------------------------

class ProjectImage(models.Model):
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

    project = models.ForeignKey(Project, related_name='images', verbose_name=_('Project'))
    file = ThumbnailerImageField(_('File'), upload_to='projects/')
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
