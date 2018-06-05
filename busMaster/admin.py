from django.contrib import admin
from busMaster.models import *
# Register your models here.


class TxnAdminInline(admin.TabularInline):
    model=routeStop

class RAdmin(admin.ModelAdmin):
	list_display=('rid','pk','rname','created_at','modified_at')
	list_filter=('rid','rname')
	inlines=(TxnAdminInline,)
	
admin.site.register(routeMaster,RAdmin)

def stopName(self,obj):
	return obj.sname
stopName.short_description='stop name selection'
class SAdmin(admin.ModelAdmin):
	list_display=('sid','sname','pk')
	list_filter=('sname','routestop__stopNum','created_at','modified_at')
	inlines=(TxnAdminInline,)
	actions=[stopName]
	#autocomplete_fields = ['routestop__sid']
	
admin.site.register(stopMaster,SAdmin)

class RSAdmin(admin.ModelAdmin):
	list_display = ('rsid', 'route_id', 'stop_id', 'pk', 'stopNum','created_at','modified_at')
	list_filter =('route_id','stop_id')
	
admin.site.register(routeStop, RSAdmin)
admin.site.register(BusMS)