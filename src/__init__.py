
#---------------------------------------------------------------------------------------------------
# EasyThumbnails | ImageClearableFileInput | Monkey Patching
#---------------------------------------------------------------------------------------------------

from easy_thumbnails.widgets import ImageClearableFileInput

ImageClearableFileInput.template_with_thumbnail = (
    u'<a href="%(source_url)s" target="_blank" style="display: inline-block; margin-bottom: 5px;">%(thumb)s</a>'
    u'%(template)s'
)

ImageClearableFileInput.template_with_clear = (
    u'<div style="display: block; margin-bottom: 5px;">'
    u'%(clear)s <label for="%(clear_checkbox_id)s">%(clear_checkbox_label)s</label>'
    u'</div>'
)

ImageClearableFileInput.template_with_initial = (
    u'%(clear_template)s'
    u'<span style="display: block;">%(input)s</span>'
)
