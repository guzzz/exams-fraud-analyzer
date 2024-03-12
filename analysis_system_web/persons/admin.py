from django.contrib import admin
from .models import *


class PersonAdmin(admin.ModelAdmin):
	list_display = ( '__str__', 'age' )
	list_filter = ['age']
admin.site.register(Person, PersonAdmin)
