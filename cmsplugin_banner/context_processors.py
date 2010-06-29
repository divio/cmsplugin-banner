from cmsplugin_banner import conf
from cmsplugin_banner import models
def plugin_ad_slots(request):
    slots = list(models.Slot.objects.filter(banners__gt=0))
    print slots
    return {'CMSPLUGIN_BANNER_SLOTS': slots,}
