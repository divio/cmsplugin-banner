from django.db import models
from cms.models import CMSPlugin
from django.utils.translation import ugettext_lazy as _

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
