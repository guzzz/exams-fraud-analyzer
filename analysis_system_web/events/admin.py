from django.contrib import admin
from .models import *


class EventAdmin(admin.ModelAdmin):
	list_display = ( 'title', 'person', 'start_date', 'is_fraud' )
	list_filter = ['is_fraud']

admin.site.register(Event, EventAdmin)
