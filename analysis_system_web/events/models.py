from django.db import models
from django.utils.translation import gettext_lazy as _



class Event(models.Model):
    title = models.CharField(_("Title"), max_length=50, null=False, blank=False)
    base_blood_pressure = models.PositiveIntegerField(_("Base Blood Pressure"), null=False, blank=False)
    base_heart_rate = models.PositiveIntegerField(_("Base Heart Rate"), null=False, blank=False)
    start_date = models.DateTimeField(_("Start Date"))
    end_date = models.DateTimeField(_("End Date"))
    is_fraud = models.BooleanField(_("Is Fraud ?"),  null=True)

    person = models.ForeignKey(to="persons.Person", on_delete=models.CASCADE, null=False)
    blood_pressure_monitor = models.ForeignKey(to="monitors.Monitor", related_name="blood_pressure_monitor", on_delete=models.CASCADE, null=False)
    heart_rate_monitor = models.ForeignKey(to="monitors.Monitor", related_name="heart_rate_monitor", on_delete=models.CASCADE, null=False)

    def __str__(self) -> str:
        fraud = ""
        if self.is_fraud is None:
            fraud = "Still Unknow"
        elif self.is_fraud is False:
            fraud = "No"
        else:
            fraud = "Yes"
        return f"{self.title} - Fraud: {fraud}"
