from django.db import models
from django.utils.translation import gettext_lazy as _

from monitors.choices import MONITOR_TYPE_CHOICES


class Monitor(models.Model):
    device = models.CharField(_("Device"), max_length=50, null=False, blank=False)
    version = models.CharField(_("Version"), max_length=50, null=False, blank=False)
    type = models.CharField(_("Version"), max_length=20, choices=MONITOR_TYPE_CHOICES)

    def __str__(self) -> str:
        return f"{self.device} / {self.version}"
