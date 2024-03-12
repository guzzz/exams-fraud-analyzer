from django.db import models
from django.utils.translation import gettext_lazy as _


class Person(models.Model):
    name = models.CharField(_("Name"), max_length=50, null=False, blank=False)
    surname = models.CharField(_("Surname"), max_length=50, null=False, blank=False)
    age = models.PositiveIntegerField(_("Age"), null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.name} {self.surname}"
