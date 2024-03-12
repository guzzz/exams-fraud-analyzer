from django.db import models
from django.utils.translation import gettext_lazy as _


class BloodPressureEvidence(models.Model):
    systolic_bp = models.PositiveIntegerField(_("Systolic Blood Pressure"), null=False, blank=False)
    event = models.ForeignKey(to="events.Event", on_delete=models.CASCADE, null=False, blank=False)
    date = models.DateTimeField()

class HeartRateEvidence(models.Model):
    pulse = models.PositiveIntegerField(_("Pulse"), null=False, blank=False)
    event = models.ForeignKey(to="events.Event", on_delete=models.CASCADE, null=False, blank=False)
    date = models.DateTimeField()
