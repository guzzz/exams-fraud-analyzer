from django.contrib import admin
from .models import *


class MonitorAdmin(admin.ModelAdmin):
	list_display = ( '__str__', 'type' )
	list_filter = ['type']
admin.site.register(Monitor, MonitorAdmin)
# admin.site.register(Monitor)
