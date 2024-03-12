
from django import forms
from monitors.models import Monitor

from persons.models import Person
from events.models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['blood_pressure_monitor']=forms.ModelChoiceField(queryset=Monitor.objects.filter(type='BLOOD_PRESSURE'))
        self.fields['heart_rate_monitor']=forms.ModelChoiceField(queryset=Monitor.objects.filter(type='HEART_RATE'))
        self.fields['person']=forms.ModelChoiceField(queryset=Person.objects.all())
