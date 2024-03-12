from django.contrib import admin
from .models import *


class BloodPressureEvidenceAdmin(admin.ModelAdmin):
	list_display = ( 'date', 'systolic_bp' )
admin.site.register(BloodPressureEvidence, BloodPressureEvidenceAdmin)

class HeartRateEvidenceAdmin(admin.ModelAdmin):
	list_display = ( 'date', 'pulse' )
admin.site.register(HeartRateEvidence, HeartRateEvidenceAdmin)
