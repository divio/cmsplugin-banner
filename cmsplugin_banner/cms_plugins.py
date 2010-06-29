from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from models import Banner
from django.utils.translation import ugettext as _

class BannerPlugin(CMSPluginBase):
    model = Banner
    name = _("banner")
    render_template = "cmsplugin_banner/banner.html"
    
    def render(self, context, instance, placeholder):
        context.update({'instance':instance,
                        'banner':instance,
                        'placeholder':placeholder})
        return context

plugin_pool.register_plugin(BannerPlugin)