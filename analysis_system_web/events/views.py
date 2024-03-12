
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.urls import reverse
from structlog import get_logger

from events.services import EventService
from events.forms import EventForm
from events.models import Event

event_service = EventService()
log = get_logger()


class EventCreateView(LoginRequiredMixin, CreateView):
    template_name = 'events/event_form.html'
    form_class = EventForm

    def form_valid(self, form):
        try:
            log.info("[Event View] Form valid...")
            record = form.save(commit=True)
            record.is_fraud, graph_data = event_service.process_integration(record)
            self.kwargs["new_id"] = record.id
            self.request.session["graph_data"] = graph_data
            return super().form_valid(record)
        except:
            log.info("[Event View] Redirecting to Error Page...")
            return HttpResponseRedirect(reverse('error'))

    def get_success_url(self, **kwargs):        
        return reverse('processed-page', kwargs={'pk': self.kwargs["new_id"]})


class ProcessedTemplateView(LoginRequiredMixin, DetailView):
    template_name = 'events/result.html'
    model = Event
    context_object_name = 'event'

    def get_context_data(self, **kwargs):
        log.info("[Event View] Puting graph data into context...")
        context = super().get_context_data(**kwargs)
        graph_data = self.request.session.pop("graph_data", {})
        context['bp_x'] = graph_data.get('bp_x', [])
        context['bp_y'] = graph_data.get('bp_y', [])
        context['hr_x'] = graph_data.get('hr_x', [])
        context['hr_y'] = graph_data.get('hr_y', [])
        return context

class ErrorTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'events/error.html'
