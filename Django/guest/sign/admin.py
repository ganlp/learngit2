from django.contrib import admin
from sign.models import Event,Guest


# Register your models here.

class EventAdmin(admin.ModelAdmin):
	list_display=['name','status','start_time','id']
	search_fields=['name']
	list_filter=['status']


class GuestAdmin(admin.ModelAdmin):
	list_display=['realname','event','phone','email','sign','create_time']
	search_fields=['realname','phone']
	list_filter=['sign']

admin.site.register(Event,EventAdmin)
admin.site.register(Guest,GuestAdmin)