from django.db import models
from cms.models import CMSPlugin
from cms.models.fields import PageField
from django.utils.translation import ugettext_lazy as _
from filer.fields.file import FilerFileField

from cmsplugin_banner import conf

class Slot(models.Model):
    name = models.CharField(_("name"), max_length=255)
    
    def __unicode__(self):
        return u"%s" % self.name

class Banner(CMSPlugin):
    title = models.CharField(max_length=255, null=True, blank=True)
    slot = models.ForeignKey(Slot, related_name="banners")
    style = models.CharField(_("banner style"), max_length=255, null=True, blank=True, choices=conf.STYLE_CHOICES)
    
    def __unicode__(self):
        return u"%s" % (self.title or self.id, )

CLICK_TARGET_CHOICES = (
    ('_blank', _('open in new window')),
    ('_self', _('open in same window')),
)

class LocalBanner(CMSPlugin):
    file = FilerFileField(help_text=_('use swf file'))
    width = models.CharField(_('width'), max_length=6)
    height = models.CharField(_('height'), max_length=6)
    
    click_tag_free = models.CharField(_('click tag'), max_length=255, blank=True, default='')
    click_tag_page = PageField(null=True, blank=True)
    click_target = models.CharField(_('click target'), choices=CLICK_TARGET_CHOICES, max_length=32, null=True, blank=True)
    
    bgcolor = models.CharField(_('background color'), default="#000000", max_length=7, blank=True)

    def click_tag(self):
        if self.click_tag_free:
            return self.click_tag_free
        elif self.click_tag_page:
            return self.click_tag_page.get_absolute_url()
        else:
            return ''