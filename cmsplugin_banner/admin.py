from django.contrib import admin
from cmsplugin_banner.models import Slot

class SlotAdmin(admin.ModelAdmin):
    search_fields = ('name', )
    list_display = ('id', 'name','banners_count')
    list_editable = ('name',)
    
    def banners_count(self, obj):
        return len( obj.banners.all() )
        
    
admin.site.register(Slot, SlotAdmin)