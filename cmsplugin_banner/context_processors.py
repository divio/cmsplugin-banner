from cmsplugin_banner import conf
from cmsplugin_banner import models
def plugin_ad_slots(request):
    # TODO: this should be cached
    slots = list(models.Slot.objects.filter(banners__gt=0))
    return {'CMSPLUGIN_BANNER_SLOTS': slots,}
